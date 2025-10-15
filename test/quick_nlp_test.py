"""Quick NLP test to verify new features"""

from lib.math.calculator import calculate

test_cases = [
    ("what is the sum of twenty and thirty", 50),
    ("what is the product of four and five", 20),
    ("what is the difference between fifty and twenty", 30),
    ("ten more than five", 15),
    ("what is the square of seven", 49),
    ("double of fifteen", 30),
    ("triple of six", 18),
    ("three fourths of 200", 150),
    ("increase 100 by 20 percent", 120),
    ("reduce 100 by 25 percent", 75),
    ("split 100 into 4 equal parts", 25),
    ("hey can you add five and three", 8),
    ("tell me what is ten times two", 20),
]

passed = 0
failed = 0

for query, expected in test_cases:
    result = calculate(query)
    if result["success"]:
        actual = float(result["result"])
        is_correct = abs(actual - expected) < 0.01
        status = "✓ PASS" if is_correct else "✗ FAIL"
        if is_correct:
            passed += 1
        else:
            failed += 1
        print(f"{status}: '{query}' -> {actual} (expected {expected})")
    else:
        failed += 1
        print(f"✗ FAIL: '{query}' -> ERROR: {result.get('error', 'Unknown error')}")

print(f"\nPassed: {passed}/{len(test_cases)} ({100*passed//len(test_cases)}%)")
