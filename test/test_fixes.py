import sys

sys.path.insert(0, "c:/Users/Asus/Documents/ogcz/_DEV/ivy")

from lib.math.calculator import calculate

tests = [
    ("increase 200 by 10 percent", 220),
    ("reduce 50 by 10 percent", 45),
    ("how much is twelve multiplied by three", 36),
    ("tell me what 999 times 2 is", 1998),
]

for query, expected in tests:
    result = calculate(query)
    if result["success"]:
        actual = float(result["result"])
        status = "✓" if abs(actual - expected) < 0.01 else "✗"
        print(f"{status} '{query}' -> {actual} (expected {expected})")
        if status == "✗":
            print(f"   Expression: {result.get('expression', 'N/A')}")
    else:
        print(f"✗ '{query}' -> ERROR: {result.get('error', 'Unknown')}")
        print(f"   Expression: {result.get('expression', 'N/A')}")
