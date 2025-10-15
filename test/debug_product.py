import sys

sys.path.insert(0, "c:/Users/Asus/Documents/ogcz/_DEV/ivy")

import re

text = "product of nine and eleven"

product_match = re.search(r"the\s+product\s+of\s+(.+?)\s+and\s+(.+)", text)
print(f"With 'the': {product_match}")

product_match = re.search(r"product\s+of\s+(.+?)\s+and\s+(.+)", text)
if product_match:
    print(f"Without 'the': Match found!")
    print(f"  X: '{product_match.group(1)}'")
    print(f"  Y: '{product_match.group(2)}'")
else:
    print("Without 'the': No match")
