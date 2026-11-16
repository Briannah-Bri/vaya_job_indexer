import json
import re
from html import unescape
from typing import Any
from urllib.parse import urljoin

from .models import NormalizedJob


def _objects(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, dict):
        if "@graph" in value:
            return _objects(value["@graph"])
        return [value]
    if isinstance(value, list):
        return [item for item in value if isinstance(item, dict)]
    return []


def extract_json_ld_jobs(html: str, source_url: str) -> list[NormalizedJob]:
    jobs: list[NormalizedJob] = []
    scripts = re.findall(
        r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        html,
        flags=re.IGNORECASE | re.DOTALL,
    )
    for raw in scripts:
        try:
            payload = json.loads(unescape(raw).strip())
        except json.JSONDecodeError:
            continue
        for item in _objects(payload):
            item_type = item.get("@type")
            if item_type != "JobPosting" and (
                not isinstance(item_type, list) or "JobPosting" not in item_type
            ):
                continue
            if not item.get("title"):
                continue
            location = item.get("jobLocation")
            if isinstance(location, list):
                location = location[0] if location else None
            if isinstance(location, dict):
                address = location.get("address", location)
                location = ", ".join(
                    str(address.get(key))
                    for key in ("addressLocality", "addressRegion", "addressCountry")
                    if isinstance(address, dict) and address.get(key)
                )
            jobs.append(
                NormalizedJob(
                    title=str(item["title"]).strip(),
                    company=str(item.get("hiringOrganization", {}).get("name", "Unknown")).strip(),
                    location=location or None,
                    description=item.get("description"),
                    url=urljoin(source_url, str(item.get("url", source_url))),
                    employment_type=item.get("employmentType"),
                )
            )
    return jobs
