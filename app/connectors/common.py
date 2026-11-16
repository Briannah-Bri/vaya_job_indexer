import json
import re
from html import unescape
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, urlopen

from .errors import FetchError
from .json_ld import extract_json_ld_jobs
from .models import NormalizedJob


USER_AGENT = "Mozilla/5.0 (compatible; VayaJobIndexer/1.0; +public-job-indexing)"


def fetch(url: str, accept: str = "*/*") -> bytes:
    request = Request(url, headers={"Accept": accept, "User-Agent": USER_AGENT})
    try:
        with urlopen(request, timeout=20) as response:
            if response.status != 200:
                raise FetchError(response.status, f"unexpected response for {url}")
            return response.read()
    except HTTPError as exc:
        raise FetchError(exc.code, f"request failed for {url}") from exc
    except (URLError, TimeoutError, OSError) as exc:
        raise FetchError(None, f"request failed for {url}: {exc}") from exc


def json_payload(body: bytes, url: str) -> Any:
    try:
        return json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise FetchError(200, f"invalid JSON from {url}") from exc


def html_text(body: bytes, url: str) -> str:
    try:
        return body.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise FetchError(200, f"invalid UTF-8 from {url}") from exc


def company_from_url(url: str) -> str:
    host = urlsplit(url).hostname or "Unknown"
    parts = host.split(".")
    return parts[0].replace("-", " ").title() if parts else "Unknown"


def json_jobs(payload: Any, source_url: str, company: str | None = None) -> list[NormalizedJob]:
    records: list[dict[str, Any]] = []

    def visit(value: Any) -> None:
        if isinstance(value, list):
            for item in value:
                visit(item)
        elif isinstance(value, dict):
            if any(key in value for key in (
                "title", "name", "jobTitle", "position_name", "jobOpeningName"
            )):
                records.append(value)
            for key, child in value.items():
                if key not in {
                    "description", "content", "html", "location", "company",
                    "hiringOrganization", "department", "atsLocation",
                }:
                    visit(child)

    visit(payload)
    jobs = []
    seen: set[str] = set()
    for record in records:
        title = _first(record, "title", "jobTitle", "position_name", "jobOpeningName", "name")
        if not title or title in seen:
            continue
        seen.add(title)
        url = _first(record, "url", "jobUrl", "absolute_url", "apply_url", "link") or source_url
        location = _location(record)
        jobs.append(
            NormalizedJob(
                title=str(title).strip(),
                company=str(company or _nested_name(record, "company", "hiringOrganization") or "Unknown"),
                location=location,
                description=_first(record, "description", "jobDescription", "content"),
                url=urljoin(source_url, str(url)),
                employment_type=_first(record, "employmentType", "employment_type", "type"),
            )
        )
    return jobs


def html_jobs(html: str, source_url: str, company: str | None = None) -> list[NormalizedJob]:
    jobs = extract_json_ld_jobs(html, source_url)
    if jobs:
        return jobs
    scripts = re.findall(
        r"<script(?=[^>]*(?:type=[\"']application/json[\"']|id=[\"']__NEXT_DATA__[\"']))[^>]*>(.*?)</script>",
        html,
        flags=re.IGNORECASE | re.DOTALL,
    )
    for raw in scripts:
        try:
            jobs = json_jobs(json.loads(unescape(raw)), source_url, company)
        except json.JSONDecodeError:
            continue
        if jobs:
            return jobs
    page_data = re.search(
        r"window\.pageData\s*=\s*(\{.*?\})\s*;",
        html,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if page_data:
        try:
            return json_jobs(json.loads(page_data.group(1)), source_url, company)
        except json.JSONDecodeError as exc:
            raise FetchError(200, f"invalid window.pageData JSON at {source_url}") from exc
    return []


def require_jobs(jobs: list[NormalizedJob], url: str) -> list[NormalizedJob]:
    if not jobs:
        raise FetchError(200, f"no job listings found at {url}")
    return jobs


def _first(record: dict[str, Any], *keys: str) -> Any:
    return next((record[key] for key in keys if record.get(key)), None)


def _nested_name(record: dict[str, Any], *keys: str) -> Any:
    for key in keys:
        value = record.get(key)
        if isinstance(value, dict) and value.get("name"):
            return value["name"]
        if isinstance(value, str):
            return value
    return None


def _location(record: dict[str, Any]) -> str | None:
    value = _first(record, "location", "jobLocation", "city")
    if isinstance(value, dict):
        return ", ".join(str(value[key]) for key in ("city", "state", "country")
                         if value.get(key)) or None
    return str(value) if value else None
