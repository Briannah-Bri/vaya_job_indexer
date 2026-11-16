from ..base import BaseConnector
from ..common import company_from_url, fetch, html_jobs, html_text, json_jobs, json_payload, require_jobs
from ..errors import FetchError
from ..models import NormalizedJob


class JazzHRConnector(BaseConnector):
    """Fetch JazzHR widget listings or JSON-LD from an apply page."""

    def fetch_jobs(self, target_url: str) -> list[NormalizedJob]:
        body = fetch(target_url, "text/html, application/json, application/xml")
        html = html_text(body, target_url)
        company = company_from_url(target_url)
        jobs = html_jobs(html, target_url, company)
        if not jobs:
            try:
                jobs = json_jobs(json_payload(body, target_url), target_url, company)
            except FetchError:
                jobs = []
        return require_jobs(jobs, target_url)
