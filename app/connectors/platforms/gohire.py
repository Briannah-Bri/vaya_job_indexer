from ..base import BaseConnector
from ..common import company_from_url, fetch, html_jobs, html_text, json_jobs, json_payload, require_jobs
from ..errors import FetchError
from ..models import NormalizedJob


class GoHireConnector(BaseConnector):
    """Fetch GoHire's public jobs API or career-page JSON."""

    def fetch_jobs(self, target_url: str) -> list[NormalizedJob]:
        body = fetch(target_url, "application/json, text/html")
        company = company_from_url(target_url)
        try:
            jobs = json_jobs(json_payload(body, target_url), target_url, company)
        except FetchError:
            jobs = html_jobs(html_text(body, target_url), target_url, company)
        return require_jobs(jobs, target_url)
