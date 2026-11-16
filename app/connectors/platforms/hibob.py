from ..base import BaseConnector
from ..common import company_from_url, fetch, json_jobs, json_payload, require_jobs
from ..models import NormalizedJob


class HiBobConnector(BaseConnector):
    """Fetch HiBob's public career jobs API."""

    def fetch_jobs(self, target_url: str) -> list[NormalizedJob]:
        payload = json_payload(fetch(target_url, "application/json"), target_url)
        return require_jobs(json_jobs(payload, target_url, company_from_url(target_url)), target_url)
