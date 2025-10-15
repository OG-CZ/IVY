import sys
import re

sys.path.insert(0, "c:/Users/Asus/Documents/ogcz/_DEV/ivy")

text = "add together one hundred and one and one hundred and two"
print(f"Original: '{text}'")

sum_match = re.search(r"(?:the\s+)?sum\s+of\s+(.+)", text)
print(f"Sum pattern match: {sum_match}")

add_and_match = re.search(
    r"\badd\s+(.+?)\s+and\s+(.+?)(?=\s+(?:plus|minus|times|$)|\s*$)", text
)
print(f"Add X and Y match: {add_and_match}")
if add_and_match:
    print(f"  X: '{add_and_match.group(1)}'")
    print(f"  Y: '{add_and_match.group(2)}'")

text2 = re.sub(r"\btogether\b", " ", text)
text2 = re.sub(r"\s+", " ", text2).strip()
print(f"\nAfter removing 'together': '{text2}'")

add_and_match2 = re.search(
    r"\badd\s+(.+?)\s+and\s+(.+?)(?=\s+(?:plus|minus|times|$)|\s*$)", text2
)
if add_and_match2:
    print(f"Add X and Y match: YES")
    print(f"  X: '{add_and_match2.group(1)}'")
    print(f"  Y: '{add_and_match2.group(2)}'")
