from dataclasses import dataclass


@dataclass(frozen=True)
class NormalizedJob:
    """Canonical representation of a public job posting."""

    title: str
    company: str
    location: str | None
    description: str | None
    url: str
    employment_type: str | None = None
