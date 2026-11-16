import xml.etree.ElementTree as ET

from ..base import BaseConnector
from ..common import company_from_url, fetch, html_jobs, html_text, json_jobs, json_payload, require_jobs
from ..errors import FetchError
from ..models import NormalizedJob


class ZohoRecruitConnector(BaseConnector):
    """Fetch Zoho Recruit JSON, XML, or public careers HTML."""

    def fetch_jobs(self, target_url: str) -> list[NormalizedJob]:
        body = fetch(target_url, "application/json, application/xml, text/html")
        company = company_from_url(target_url)
        try:
            jobs = json_jobs(json_payload(body, target_url), target_url, company)
        except FetchError:
            jobs = []
        if jobs:
            return jobs
        try:
            root = ET.fromstring(body)
        except ET.ParseError:
            return require_jobs(html_jobs(html_text(body, target_url), target_url, company), target_url)
        jobs = []
        for node in root.iter():
            fields = {child.tag.rsplit("}", 1)[-1]: " ".join(child.itertext()).strip()
                      for child in node}
            title = fields.get("title") or fields.get("name")
            if title:
                jobs.append(NormalizedJob(title, company, fields.get("location"),
                                          fields.get("description"), fields.get("url", target_url)))
        return require_jobs(jobs, target_url)
