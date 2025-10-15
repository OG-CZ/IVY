import sys

sys.path.insert(0, "c:/Users/Asus/Documents/ogcz/_DEV/ivy")

from lib.math.calculator import word_to_number

tests = [
    "one hundred and one",
    "one hundred and two",
    "one hundred",
    "and one",
]

for test in tests:
    try:
        result = word_to_number(test)
        print(f"'{test}' -> {result}")
    except Exception as e:
        print(f"'{test}' -> ERROR: {e}")
