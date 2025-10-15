import sys

sys.path.insert(0, "c:/Users/Asus/Documents/ogcz/_DEV/ivy")

from lib.math.calculator import parse_text_to_expression

tests = [
    "what's the sum of ten and fifteen",
    "half of twenty",
    "product of nine and eleven",
    "three fourths of 200",
    "ten percent of 500",
    "increase 200 by 10 percent",
]

for test in tests:
    expr = parse_text_to_expression(test)
    print(f"'{test}'")
    print(f"  -> '{expr}'")
    print()
