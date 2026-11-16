class FetchError(RuntimeError):
    """Raised when a connector cannot fetch or parse a target."""

    def __init__(self, http_status: int | None, message: str) -> None:
        self.http_status = http_status
        self.message = message
        status = f"HTTP {http_status}: " if http_status is not None else ""
        super().__init__(f"{status}{message}")
