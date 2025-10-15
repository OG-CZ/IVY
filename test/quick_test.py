import sys

sys.path.insert(0, "c:\\Users\\Asus\\Documents\\ogcz\\_DEV\\ivy")

from lib.math.calculator import calculate

tests = [
    ("what is 1 + 1", 2),
    ("2 divided by 2", 1),
    ("multiply ten by five", 50),
    ("forty divided by eight", 5),
    ("five point five plus two point five", 8.0),
    ("three and a half plus one and a half", 5.0),
    ("100 million plus 50 thousand and 53", 100050053),
]

passed = 0
for query, expected in tests:
    result = calculate(query)
    if result["success"] and result["result"] == expected:
        print(f"OK: {query}")
        passed += 1
    else:
        print(
            f"FAIL: {query} - got {result.get('result', 'ERROR')}, expected {expected}"
        )

print(f"\n{passed}/{len(tests)} passed ({passed*100//len(tests)}%)")
