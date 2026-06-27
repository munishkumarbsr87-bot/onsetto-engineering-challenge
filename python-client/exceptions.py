class ApiError(Exception):
    """Base API exception."""
    pass


class AuthenticationError(ApiError):
    """Authentication failed."""
    pass


class ValidationError(ApiError):
    """Request validation failed."""
    pass


class RateLimitError(ApiError):
    """API rate limit exceeded."""
    pass