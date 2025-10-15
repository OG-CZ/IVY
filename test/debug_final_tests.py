import sys

sys.path.insert(0, "c:/Users/Asus/Documents/ogcz/_DEV/ivy")

from lib.math.calculator import parse_text_to_expression

tests = [
    "the result of forty divided by eight",
    "calculate 10 million divided by 5",
    "twenty divided by five plus six",
    "how much is 7 more than 12",
    "add together one hundred and one and one hundred and two",
]

for test in tests:
    expr = parse_text_to_expression(test)
    print(f"'{test}'")
    print(f"  -> '{expr}'")
    print()
