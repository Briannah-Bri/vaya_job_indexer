from dataclasses import dataclass


@dataclass(frozen=True)
class SeedTarget:
    platform_slug: str
    platform_type: str
    employer_or_board_name: str
    target_url: str


SEED_TARGETS = [
    SeedTarget(
        platform_slug="the-panther",
        platform_type="job_board",
        employer_or_board_name="The Panther",
        target_url="https://jobs.thepanthergrp.com/",
    ),
    SeedTarget(
        platform_slug="the-panther",
        platform_type="job_board",
        employer_or_board_name="The Panther",
        target_url="https://jobs.thepanthergrp.com/index.smpl?arg=jb_search_results&view=0",
    ),
    SeedTarget("teamtailor", "ats", "Teamtailor", "https://career.teamtailor.com/"),
    SeedTarget("teamtailor", "ats", "Teamtailor", "https://career.teamtailor.com/jobs"),
    SeedTarget("personio", "ats", "Personio", "https://personio.jobs.personio.de/xml"),
    SeedTarget("personio", "ats", "Personio", "https://personio.jobs.personio.de/xml?language=en"),
    SeedTarget("bamboohr", "ats", "Euna Solutions", "https://euna.bamboohr.com/careers/list"),
    SeedTarget("bamboohr", "ats", "Userpilot", "https://userpilot.bamboohr.com/careers/list"),
    SeedTarget("jazzhr", "ats", "JazzHR Enablement", "https://jazzhrenablement.applytojob.com/apply"),
    SeedTarget("jazzhr", "ats", "JPR", "https://jpr.applytojob.com/apply/jobs/"),
    SeedTarget("jobvite", "ats", "Jobvite", "https://jobs.jobvite.com/jobvite"),
    SeedTarget("jobvite", "ats", "Jobvite", "https://jobs.jobvite.com/jobvite/jobs/feed"),
    SeedTarget("freshteam", "ats", "Locale", "https://locale.freshteam.com/jobs"),
    SeedTarget("freshteam", "ats", "23M", "https://23m.freshteam.com/jobs"),
    SeedTarget("comeet", "ats", "Comeet", "https://www.comeet.co/careers"),
    SeedTarget("comeet", "ats", "Comeet", "https://www.comeet.co/careers-api/2.0/company/comeet/positions"),
    SeedTarget("hirehive", "ats", "HireHive", "https://www.hirehive.com/jobs/"),
    SeedTarget("hirehive", "ats", "HireHive", "https://hirehive-dev.hirehive.com/"),
    SeedTarget("gohire", "ats", "GoHire", "https://gohire.io/jobs"),
    SeedTarget("gohire", "ats", "GoHire", "https://api.gohire.io/v1/jobs"),
    SeedTarget("manatal", "ats", "Manatal", "https://www.manatal.com/careers"),
    SeedTarget("manatal", "ats", "Manatal", "https://api.manatal.com/open/v3/career-page/manatal/jobs/"),
]
