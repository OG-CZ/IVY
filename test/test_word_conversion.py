import sys

sys.path.insert(0, "c:/Users/Asus/Documents/ogcz/_DEV/ivy")

from lib.math.calculator import word_to_number

tests = ["10 million", "forty", "twenty"]

for test in tests:
    try:
        result = word_to_number(test)
        print(f"'{test}' -> {result}")
    except Exception as e:
        print(f"'{test}' -> ERROR: {e}")
