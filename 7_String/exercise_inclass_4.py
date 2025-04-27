## Bỏ dấu câu

import re

text = """
    Maya Angelo said, "If you don't like something, change it. 
    If you can't change it, change your attitude."
"""

cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
print(cleaned_text)

from string import punctuation

def remove_punctuation(text):
    for p in punctuation:
        text = text.replace(p, "")
    return text

print(remove_punctuation(text))