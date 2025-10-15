import sys

sys.path.insert(0, "c:/Users/Asus/Documents/ogcz/_DEV/ivy")

from lib.math.calculator import word_to_number

tests = ["ten", "fifteen", "twenty", "half", "product", "percent", "three fourths"]

for test in tests:
    try:
        result = word_to_number(test)
        print(f"'{test}' -> {result}")
    except Exception as e:
        print(f"'{test}' -> ERROR: {e}")
