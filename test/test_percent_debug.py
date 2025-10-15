import re

text = "increase 200 by 10 percent"
text = text.lower().strip()

increase_match = re.search(r"increase\s+(.+?)\s+by\s+(.+?)\s+percent", text)
if increase_match:
    x = increase_match.group(1).strip()
    y = increase_match.group(2).strip()
    text = f"( {x} ) __MULT__ ( 1 __PLUS__ ( {y} ) __DIV__ 100 )"
    print(f"After template: '{text}'")

    text = re.sub(r"\b__PLUS__\b", "+", text)
    text = re.sub(r"\b__MULT__\b", "*", text)
    text = re.sub(r"\b__DIV__\b", "/", text)
    print(f"After placeholder replacement: '{text}'")
