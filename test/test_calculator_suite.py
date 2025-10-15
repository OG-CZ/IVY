"""
Comprehensive Test Suite for Natural Language Calculator
Tests all 45 cases from the specification
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.math.calculator import calculate


def run_test(test_num, input_text, expected):
    """Run a single test case"""
    result = calculate(input_text)

    if result["success"]:
        actual = result["result"]
        if isinstance(expected, float) or isinstance(actual, float):
            passed = abs(actual - expected) < 0.001
        else:
            passed = actual == expected

        status = "✓ PASS" if passed else "✗ FAIL"
        symbol = "✓" if passed else "✗"

        print(
            f"{symbol} Test {test_num:2d}: {input_text:50s} => {actual:15} (expected: {expected})"
        )
        return passed
    else:
        print(f"✗ Test {test_num:2d}: {input_text:50s} => ERROR: {result['error']}")
        return False


def main():
    """Run all test cases"""

    print("=" * 100)
    print(" NATURAL LANGUAGE CALCULATOR - COMPREHENSIVE TEST SUITE")
    print("=" * 100)

    tests = [
        ("what is 1 + 1", 2),
        ("what is one plus one", 2),
        ("2 divided by 2", 1),
        ("what is 100000 plus 20241", 120241),
        (
            "one million and five hundred fifty three plus 200",
            1000753,
        ),
        ("five plus ten", 15),
        ("100 minus 45", 55),
        ("what is one hundred twenty five plus fifty five", 180),
        (
            "one thousand and two minus 2",
            1000,
        ),
        ("subtract five from ten", 5),
        ("add two hundred to fifty", 250),
        ("six times seven", 42),
        ("multiply ten by five", 50),
        ("three multiplied by four plus two", 14),
        ("ten times one hundred", 1000),
        ("divide ten by two", 5),
        ("forty divided by eight", 5),
        ("one hundred divided by twenty", 5),
        ("divide five thousand by ten", 500),
        ("two hundred plus fifty divided by ten", 205),
        ("ten plus twenty times three", 70),
        (
            "one thousand minus five hundred divided by ten",
            950,
        ),
        ("five plus six times two minus four", 13),
        ("what is 2 plus 2 times 2", 6),
        ("one million plus one", 1000001),
        ("three million five hundred thousand plus two thousand", 3502000),
        ("ten thousand minus fifty", 9950),
        ("one hundred thousand times two", 200000),
        ("one million and five hundred fifty three plus 200", 1000753),
        ("what is five point five plus two point five", 8.0),
        ("three and a half plus one and a half", 5.0),
        ("half of one hundred", 50),
        ("twenty percent of 500", 100),
        ("two to the power of three", 8),
        ("what is 10 squared", 100),
        ("the square root of 49", 7),
        ("three cubed", 27),
        ("five raised to the power of four", 625),
        ("twenty divided by five times two", 8),
        ("what is 100 million plus 50 thousand and 53", 100050053),
        ("add fifty to ten times five", 100),
        ("take away two from eight", 6),
        ("give me the result of two hundred divided by four", 50),
        ("please calculate five times five plus one", 26),
        ("how much is three million and ten", 3000010),
    ]

    passed = 0
    failed = 0

    print("\n🧪 CORE TEST CASES (Basic Arithmetic)")
    print("-" * 100)
    for i in range(5):
        if run_test(i + 1, tests[i][0], tests[i][1]):
            passed += 1
        else:
            failed += 1

    print("\n➕ ADDITION & SUBTRACTION VARIANTS")
    print("-" * 100)
    for i in range(5, 11):
        if run_test(i + 1, tests[i][0], tests[i][1]):
            passed += 1
        else:
            failed += 1

    print("\n✖️  MULTIPLICATION")
    print("-" * 100)
    for i in range(11, 15):
        if run_test(i + 1, tests[i][0], tests[i][1]):
            passed += 1
        else:
            failed += 1

    print("\n➗ DIVISION")
    print("-" * 100)
    for i in range(15, 19):
        if run_test(i + 1, tests[i][0], tests[i][1]):
            passed += 1
        else:
            failed += 1

    print("\n🧮 MIXED EXPRESSIONS")
    print("-" * 100)
    for i in range(19, 24):
        if run_test(i + 1, tests[i][0], tests[i][1]):
            passed += 1
        else:
            failed += 1

    print("\n🧠 LARGE NUMBERS & WORDS")
    print("-" * 100)
    for i in range(24, 29):
        if run_test(i + 1, tests[i][0], tests[i][1]):
            passed += 1
        else:
            failed += 1

    print("\n⚡ EDGE & COMPLEX PHRASES")
    print("-" * 100)
    for i in range(29, 40):
        if run_test(i + 1, tests[i][0], tests[i][1]):
            passed += 1
        else:
            failed += 1

    print("\n🧩 OPTIONAL NATURAL VARIANTS")
    print("-" * 100)
    for i in range(40, 45):
        if run_test(i + 1, tests[i][0], tests[i][1]):
            passed += 1
        else:
            failed += 1

    print("\n" + "=" * 100)
    print(f"RESULTS: {passed} passed, {failed} failed out of {passed + failed} tests")
    print(f"Success Rate: {(passed / (passed + failed) * 100):.1f}%")
    print("=" * 100)


if __name__ == "__main__":
    main()
