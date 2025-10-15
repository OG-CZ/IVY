"""
Fresh batch of realistic natural language test cases
Testing how people casually ask for calculations
"""

import sys

sys.path.insert(0, "c:/Users/Asus/Documents/ogcz/_DEV/ivy")

from lib.math.calculator import calculate


def run_test(category, tests):
    """Run a batch of tests for a category"""
    print(f"\n{'='*80}")
    print(f" {category}")
    print("=" * 80)

    passed = 0
    failed = 0

    for query, expected in tests:
        result = calculate(query)

        if result["success"]:
            actual = float(result["result"])
            is_correct = abs(actual - expected) < 0.01

            if is_correct:
                passed += 1
                print(f"  ✓  {query:60} = {actual}")
            else:
                failed += 1
                print(f"  ✗  {query:60} = {actual} (expected {expected})")
        else:
            failed += 1
            error = result.get("error", "Unknown error")
            print(f"  ✗  {query:60} - ERROR: {error}")

    total = passed + failed
    percentage = (passed / total * 100) if total > 0 else 0
    print(f"\n{category}: {passed}/{total} passed ({percentage:.1f}%)")

    return passed, failed


basic_tests = [
    ("add 4 and 6", 10),
    ("subtract 9 from 12", 3),
    ("multiply 3 by 7", 21),
    ("divide 20 by 5", 4),
    ("what is 15 minus 3", 12),
    ("2 plus 8 equals what", 10),
    ("give me 6 times 4", 24),
    ("what is 100 divided by 25", 4),
]

natural_language_tests = [
    ("how much is ten plus five", 15),
    ("find the result of twenty divided by two", 10),
    ("what's the product of nine and three", 27),
    ("what's the difference between fifty and thirty", 20),
    ("sum of one hundred and two hundred", 300),
    ("half of sixty four", 32),
    ("double of fifteen", 30),
    ("triple of eight", 24),
]

large_numbers_tests = [
    ("add one thousand two hundred and fifty to three thousand", 4250),
    ("what is two hundred thousand plus fifty thousand", 250000),
    ("one million minus ten thousand", 990000),
    ("five hundred thousand divided by ten", 50000),
    ("what is a million plus one", 1000001),
    ("add 10 million and 250 thousand", 10250000),
    ("seven hundred eighty nine thousand times two", 1578000),
]

multi_operation_tests = [
    (
        "add 5 and 3 then multiply by 2",
        16,
    ),
    ("ten plus twenty times three", 70),
    ("(ten plus twenty) times three", 90),
    ("what is 100 divided by 5 plus 10", 30),
    ("two multiplied by five plus ten minus three", 17),
    ("calculate 50 percent of 80", 40),
    ("twenty five percent of 400", 100),
]

conversational_tests = [
    ("can you add 45 and 70 for me", 115),
    ("how much do I get if I multiply 10 and 11", 110),
    ("what's the answer if I divide 40 by 8", 5),
    ("what's 5 less than 30", 25),
    ("I had 200 and I spent 50, how much left", 150),
    ("increase 120 by 10 percent", 132),
    ("reduce 400 by 25 percent", 300),
]

fractions_decimals_tests = [
    ("one half of 80", 40),
    ("three quarters of 100", 75),
    ("1.25 plus 2.75", 4.0),
    ("0.1 times 500", 50),
    ("ten percent of 250", 25),
    ("what is 75% of 40", 30),
    ("increase 50 by 20%", 60),
]

fuzzy_tests = [
    ("what's two plus two again", 4),
    ("how much is one hundred and one added to ninety nine", 200),
    ("if I double 7 and add 3, what's that", 17),
    ("how many is five times three minus two", 13),
    ("give me the total of 100, 200, and 300", 600),
    ("make 40 three times bigger", 120),
    ("divide 99 by three and then add one", 34),
]


if __name__ == "__main__":
    print("\n" + "=" * 80)
    print(" FRESH NATURAL LANGUAGE CALCULATOR TEST SUITE")
    print("=" * 80)

    total_passed = 0
    total_failed = 0

    p, f = run_test("🧮 Basic Expressions", basic_tests)
    total_passed += p
    total_failed += f

    p, f = run_test("💬 Natural-Language Math", natural_language_tests)
    total_passed += p
    total_failed += f

    p, f = run_test("💰 Large & Mixed Numbers", large_numbers_tests)
    total_passed += p
    total_failed += f

    p, f = run_test("⚙️ Multi-Operation & Order", multi_operation_tests)
    total_passed += p
    total_failed += f

    p, f = run_test("💬 Conversational Forms", conversational_tests)
    total_passed += p
    total_failed += f

    p, f = run_test("🔢 Fractions, Decimals, %", fractions_decimals_tests)
    total_passed += p
    total_failed += f

    p, f = run_test("🧩 Fuzzy & Human-Like", fuzzy_tests)
    total_passed += p
    total_failed += f

    total_tests = total_passed + total_failed
    overall_percentage = (total_passed / total_tests * 100) if total_tests > 0 else 0

    print("\n" + "=" * 80)
    print(" OVERALL RESULTS")
    print("=" * 80)
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {total_passed}")
    print(f"Failed: {total_failed}")
    print(f"Success Rate: {overall_percentage:.1f}%")

    if overall_percentage >= 95:
        print("*** EXCELLENT - Production ready!")
    elif overall_percentage >= 90:
        print("*** VERY GOOD - Minor improvements needed")
    elif overall_percentage >= 80:
        print("*** GOOD - Some gaps to address")
    else:
        print("*** NEEDS WORK - Significant improvements required")

    print("=" * 80)
