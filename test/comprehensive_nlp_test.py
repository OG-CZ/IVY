"""
Comprehensive Natural Language Arithmetic Test Suite
Tests fuzzy NLP calculator capabilities with real-world queries
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.math.calculator import calculate


def run_test(category, test_num, query, expected, tolerance=0.01):
    """Run a single test case"""
    result = calculate(query)

    if result["success"]:
        actual = result["result"]

        if isinstance(expected, (float, int)) and isinstance(actual, (float, int)):
            if isinstance(expected, float) or isinstance(actual, float):
                passed = abs(float(actual) - float(expected)) < tolerance
            else:
                passed = actual == expected
        else:
            passed = False

        status = "PASS" if passed else "FAIL"
        if passed:
            print(f"  OK  Test {test_num:2d}: {query:55s} = {actual}")
        else:
            print(
                f"  FAIL Test {test_num:2d}: {query:55s} = {actual} (expected {expected})"
            )
        return passed
    else:
        print(f"  ERR  Test {test_num:2d}: {query:55s} - {result['error']}")
        return False


def main():
    """Run all comprehensive NLP test cases"""

    print("=" * 100)
    print(" COMPREHENSIVE NATURAL LANGUAGE CALCULATOR TEST SUITE")
    print("=" * 100)

    total_passed = 0
    total_failed = 0
    category_stats = {}

    category = "Basic Arithmetic"
    print(f"\n[BASIC ARITHMETIC]")
    print("-" * 100)

    tests = [
        ("what is 1 + 1", 2),
        ("two plus two", 4),
        ("five minus three", 2),
        ("10 times 2", 20),
        ("20 divided by 4", 5),
        ("subtract 8 from 15", 7),
        ("add 10 and 5", 15),
        ("multiply 7 by 3", 21),
        ("divide 9 by 3", 3),
    ]

    passed = sum(run_test(category, i + 1, q, e) for i, (q, e) in enumerate(tests))
    failed = len(tests) - passed
    category_stats[category] = (passed, failed)
    total_passed += passed
    total_failed += failed

    category = "Natural Word Variants"
    print(f"\n[NATURAL WORD VARIANTS]")
    print("-" * 100)

    tests = [
        ("what's the sum of ten and fifteen", 25),
        ("how much is twelve multiplied by three", 36),
        ("the result of forty divided by eight", 5),
        ("calculate six times five", 30),
        ("difference between one hundred and ninety", 10),
        ("add twenty two to thirty", 52),
        ("product of nine and eleven", 99),
        ("half of twenty", 10),
    ]

    passed = sum(run_test(category, i + 1, q, e) for i, (q, e) in enumerate(tests))
    failed = len(tests) - passed
    category_stats[category] = (passed, failed)
    total_passed += passed
    total_failed += failed

    category = "Large Numbers"
    print(f"\n[LARGE NUMBERS]")
    print("-" * 100)

    tests = [
        ("what is one hundred thousand plus fifty", 100050),
        ("two million minus ten thousand", 1990000),
        ("one million and five hundred fifty three plus two hundred", 1000753),
        ("what is 100 thousand plus 205", 100205),
        ("calculate 10 million divided by 5", 2000000),
        ("add 3.5 million and 200 thousand", 3700000),
        (
            "nine hundred ninety nine thousand nine hundred ninety nine plus one",
            1000000,
        ),
    ]

    passed = sum(run_test(category, i + 1, q, e) for i, (q, e) in enumerate(tests))
    failed = len(tests) - passed
    category_stats[category] = (passed, failed)
    total_passed += passed
    total_failed += failed

    category = "Complex/Multi-Operation"
    print(f"\n[COMPLEX/MULTI-OPERATION]")
    print("-" * 100)

    tests = [
        ("what is 10 plus 5 times 2", 20),
        ("two plus two times three minus one", 7),
        ("(10 + 5) * 2", 30),
        ("twenty divided by five plus six", 10),
        ("one hundred minus fifty times two", 0),
        ("calculate 20% of 400", 80),
        ("square of twelve", 144),
        ("cube of three", 27),
    ]

    passed = sum(run_test(category, i + 1, q, e) for i, (q, e) in enumerate(tests))
    failed = len(tests) - passed
    category_stats[category] = (passed, failed)
    total_passed += passed
    total_failed += failed

    category = "Fuzzy/Natural Sentences"
    print(f"\n[FUZZY/NATURAL SENTENCES]")
    print("-" * 100)

    tests = [
        ("hey can you add 50 and 70 for me", 120),
        ("how much do I get if I take 200 minus 55", 145),
        ("please calculate the total of 100 plus 23", 123),
        ("tell me what 999 times 2 is", 1998),
        ("if I have 10 apples and get 5 more how many do I have", 15),
        ("split 100 into 4 equal parts", 25),
    ]

    passed = sum(run_test(category, i + 1, q, e) for i, (q, e) in enumerate(tests))
    failed = len(tests) - passed
    category_stats[category] = (passed, failed)
    total_passed += passed
    total_failed += failed

    category = "Decimals/Percentages"
    print(f"\n[DECIMALS/PERCENTAGES]")
    print("-" * 100)

    tests = [
        ("what is half of 90", 45),
        ("three fourths of 200", 150),
        ("what is 1.5 plus 2.25", 3.75),
        ("ten percent of 500", 50),
        ("increase 200 by 10 percent", 220),
        ("0.5 times 8", 4.0),
    ]

    passed = sum(run_test(category, i + 1, q, e) for i, (q, e) in enumerate(tests))
    failed = len(tests) - passed
    category_stats[category] = (passed, failed)
    total_passed += passed
    total_failed += failed

    category = "Ambiguous/Human-like"
    print(f"\n[AMBIGUOUS/HUMAN-LIKE]")
    print("-" * 100)

    tests = [
        ("what's two plus two again", 4),
        ("add together one hundred and one and one hundred and two", 203),
        ("give me the sum of twenty, thirty, and fifty", 100),
        ("how much is 7 more than 12", 19),
        ("reduce 50 by 10 percent", 45),
        ("what's double of 24", 48),
        ("what's triple of 7", 21),
    ]

    passed = sum(run_test(category, i + 1, q, e) for i, (q, e) in enumerate(tests))
    failed = len(tests) - passed
    category_stats[category] = (passed, failed)
    total_passed += passed
    total_failed += failed

    print("\n" + "=" * 100)
    print(" CATEGORY BREAKDOWN")
    print("=" * 100)

    for cat, (p, f) in category_stats.items():
        total = p + f
        percentage = (p / total * 100) if total > 0 else 0
        print(f"{cat:30s}: {p:2d}/{total:2d} passed ({percentage:5.1f}%)")

    print("\n" + "=" * 100)
    total = total_passed + total_failed
    percentage = (total_passed / total * 100) if total > 0 else 0
    print(f"OVERALL RESULTS: {total_passed}/{total} tests passed ({percentage:.1f}%)")
    print("=" * 100)

    if percentage >= 95:
        print("*** EXCELLENT - Production ready!")
    elif percentage >= 85:
        print("*** VERY GOOD - Minor improvements needed")
    elif percentage >= 70:
        print("*** GOOD - Some gaps to address")
    else:
        print("*** NEEDS WORK - Significant improvements required")


if __name__ == "__main__":
    main()
