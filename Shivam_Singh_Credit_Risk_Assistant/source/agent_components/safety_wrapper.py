def safe_input(text: str):
    lowered = text.lower()
    blocked_terms = ["ignore policy", "hack", "exploit"]
    blocked = any(term in lowered for term in blocked_terms)
    return {"allowed": not blocked, "reason": "blocked content" if blocked else "safe"}
