from abc import ABC, abstractmethod

from .models import NormalizedJob


class BaseConnector(ABC):
    """Base interface for public job-board connectors."""

    @abstractmethod
    def fetch_jobs(self, target_url: str) -> list[NormalizedJob]:
        """Fetch and normalize jobs from a public target URL."""
