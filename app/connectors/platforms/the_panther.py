import re
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlsplit, urlunsplit
from urllib.request import Request, urlopen

from ..base import BaseConnector
from ..errors import FetchError
from ..json_ld import extract_json_ld_jobs
from ..models import NormalizedJob


class ThePantherConnector(BaseConnector):
    """Extract public The Panther postings from JSON-LD JobPosting markup."""

    user_agent = "Mozilla/5.0 (compatible; VayaJobIndexer/1.0; +public-job-indexing)"
    timeout_seconds = 20

    def fetch_jobs(self, target_url: str) -> list[NormalizedJob]:
        html = self._request(target_url, "text/html")
        jobs = extract_json_ld_jobs(html.decode("utf-8"), target_url)
        if jobs:
            return jobs
        parts = urlsplit(target_url)
        rss_url = urlunsplit(
            (parts.scheme, parts.netloc, "/rss/rss.smpl",
             "", ""),
        ) + "?arg=list_posts&pp=100&pid=gwt&view=0"
        payload = self._request(rss_url, "application/rss+xml")
        try:
            rss = payload.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise FetchError(200, f"could not decode RSS from {target_url}") from exc
        jobs = []
        items = re.findall(r"<item\b[^>]*>(.*?)</item>", rss, flags=re.IGNORECASE | re.DOTALL)
        if not items:
            raise FetchError(200, f"could not parse RSS from {target_url}")
        for item in items:
            title = _rss_value(item, "title")
            link = _rss_value(item, "link")
            description = _rss_value(item, "description")
            if not title or not link:
                raise FetchError(200, f"invalid RSS job item from {target_url}")
            location = _location_from_description(description or "")
            jobs.append(
                NormalizedJob(
                    title=title.strip(),
                    company="The Panther Group",
                    location=location,
                    description=description,
                    url=urljoin(target_url, link.strip()),
                )
            )
        if not jobs:
            raise FetchError(200, f"no jobs found at {target_url}")
        return jobs

    def _request(self, url: str, accept: str) -> bytes:
        request = Request(url, headers={"Accept": accept, "User-Agent": self.user_agent})
        try:
            with urlopen(request, timeout=self.timeout_seconds) as response:
                if response.status != 200:
                    raise FetchError(response.status, f"unexpected response for {url}")
                return response.read()
        except HTTPError as exc:
            raise FetchError(exc.code, f"request failed for {url}") from exc
        except (URLError, TimeoutError, OSError) as exc:
            raise FetchError(None, f"request failed for {url}: {exc}") from exc


def _location_from_description(description: str) -> str | None:
    match = re.search(r"\|\s*(?:Remote\s*[–-]\s*)?([^<\n]+)", description)
    return match.group(1).strip() if match else None


def _rss_value(item: str, tag: str) -> str | None:
    match = re.search(
        rf"<{tag}\b[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</{tag}>",
        item,
        flags=re.IGNORECASE | re.DOTALL,
    )
    return re.sub(r"<[^>]+>", "", match.group(1)).strip() if match else None
