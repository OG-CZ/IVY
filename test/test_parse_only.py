import sys

sys.path.insert(0, "c:/Users/Asus/Documents/ogcz/_DEV/ivy")

from lib.math.calculator import parse_text_to_expression

tests = [
    "increase 200 by 10 percent",
    "tell me what 999 times 2 is",
]

for test in tests:
    expr = parse_text_to_expression(test)
    print(f"'{test}'")
    print(f"  -> '{expr}'")
    print()
