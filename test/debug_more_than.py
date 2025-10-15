import sys
import re

sys.path.insert(0, "c:/Users/Asus/Documents/ogcz/_DEV/ivy")

text = "how much is 7 more than 12"
text = text.lower().strip()

text = text.replace("what's", "what is")

fillers = [
    r"\bhey\b",
    r"\bcan you\b",
    r"\bplease\b",
    r"\bfor me\b",
    r"\btell me\b",
    r"\bagain\b",
    r"\btogether\b",
    r"\bif i\b",
    r"\bhave\b",
    r"\bapples?\b",
    r"\bget\b",
    r"\bhow many do i have\b",
    r"\bwhat is\b",
    r"\bhow much\b",
    r"\bdo i get\b",
    r"\bdo i\b",
    r"\bcalculate\b",
    r"\bthe total of\b",
    r"\btake\b",
    r"\bthan\b(?! )",
]

for filler in fillers:
    text = re.sub(filler, " ", text)

text = re.sub(r"\s+", " ", text).strip()
print(f"After filler removal: '{text}'")

more_than_match = re.search(r"(\S+(?:\s+\S+)*?)\s+more\s+than\s+(.+)", text)
if more_than_match:
    print(f"More than match found!")
    print(f"  X: '{more_than_match.group(1)}'")
    print(f"  Y: '{more_than_match.group(2)}'")
