import re
from urllib.parse import urljoin

from ..base import BaseConnector
from ..common import company_from_url, fetch, html_jobs, html_text, json_payload, require_jobs
from ..errors import FetchError
from ..models import NormalizedJob


class WPJobManagerConnector(BaseConnector):
    """Fetch WordPress Job Manager REST listings with JSON-LD fallback."""

    def fetch_jobs(self, target_url: str) -> list[NormalizedJob]:
        api_url = target_url if "/wp-json/" in target_url else urljoin(
            target_url.rstrip("/") + "/", "wp-json/wp/v2/job-listings"
        )
        body = fetch(api_url, "application/json")
        try:
            records = json_payload(body, api_url)
        except FetchError:
            records = None
        jobs = []
        if isinstance(records, list):
            for record in records:
                title = record.get("title", {}).get("rendered")
                if title:
                    description = record.get("content", {}).get("rendered")
                    jobs.append(NormalizedJob(
                        re.sub("<[^>]+>", "", title).strip(), company_from_url(target_url),
                        None, description, record.get("link", target_url),
                    ))
        if jobs:
            return jobs
        html = html_text(fetch(target_url, "text/html"), target_url)
        return require_jobs(html_jobs(html, target_url, company_from_url(target_url)), target_url)
