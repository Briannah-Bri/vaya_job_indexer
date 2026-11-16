from ..base import BaseConnector
from ..common import company_from_url, fetch, html_jobs, html_text, require_jobs
from ..models import NormalizedJob


class BrassRingConnector(BaseConnector):
    """Extract BrassRing search-page JSON-LD or embedded XHR data."""

    def fetch_jobs(self, target_url: str) -> list[NormalizedJob]:
        html = html_text(fetch(target_url, "text/html, application/json"), target_url)
        return require_jobs(html_jobs(html, target_url, company_from_url(target_url)), target_url)
