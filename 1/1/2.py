import re

text = """
2025-09-26 12:34:56 Connection from 192.168.0.1
2025-09-26 12:35:01 ERROR User JOHN logged in
admin@site.com tried to connect
"""

print("IP адреса:", re.findall(r"\d+\.\d+\.\d+\.\d+", text))
print("Временные метки:", re.findall(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", text))
print("Слова UPPERCASE:", re.findall(r"\b[A-Z]+\b", text))
print("Текст с заменой email:\n", re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "[EMAIL PROTECTED]", text))
