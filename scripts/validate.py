# Build: 29edbb20784148a9ada9e8216ffc1b67

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
