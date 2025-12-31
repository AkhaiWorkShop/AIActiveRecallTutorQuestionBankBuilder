import re

def normalize_text(text: str) -> str:
    text = text.replace('\r', '\n')
    text = re.sub(r'[ ]{2,}', ' ', text)
    text = re.sub(r'\n{2,}', '\n', text)
    return text.strip()
