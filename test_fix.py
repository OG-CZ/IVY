import sys

sys.path.insert(0, r"c:\Users\Asus\Documents\ogcz\_DEV\ivy")

from lib.math.calculator import calculate

print("=" * 80)
print(" TESTING CALCULATOR - DISPLAY VS SPEAK")
print("=" * 80)

test_cases = [
    "100234 plus 12343",
    "calculate 100 and 20",
    "what is 1 million plus 500 thousand",
]

for query in test_cases:
    result = calculate(query)
    if result["success"]:
        print(f"\n🔍 Query: {query}")
        print(f"   Result (raw): {result['result']}")
        print(f"   📊 Display: The answer is {result['result_display']}")
        print(f"   🔊 Speak:   The answer is {result['result_words']}")
        print(f"   ✅ Words length: {len(result['result_words'])} characters")
        print("-" * 80)
    else:
        print(f"\n❌ Query: {query}")
        print(f"   Error: {result['error']}")

print("\n" + "=" * 80)
print("Now the display won't be overwritten by speak()!")
print("=" * 80)
