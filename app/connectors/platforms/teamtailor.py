from ..base import BaseConnector
from ..common import company_from_url, fetch, html_jobs, html_text, json_jobs, json_payload, require_jobs
from ..models import NormalizedJob


class TeamtailorConnector(BaseConnector):
    """Fetch Teamtailor career-site JSON-LD or public JSON listings."""

    def fetch_jobs(self, target_url: str) -> list[NormalizedJob]:
        body = fetch(target_url, "text/html, application/json")
        company = company_from_url(target_url)
        html = html_text(body, target_url)
        jobs = html_jobs(html, target_url, company)
        if not jobs:
            jobs = json_jobs(json_payload(body, target_url), target_url, company)
        return require_jobs(jobs, target_url)
