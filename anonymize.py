import re
def scrub(log_text: str) -> str:
    log_text = re.sub(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', '[REDACTED_EMAIL]', log_text)
    log_text = re.sub(r'\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})\b', '[REDACTED_CC]', log_text)
    return log_text
