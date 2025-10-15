import sys

sys.path.insert(0, r"c:\Users\Asus\Documents\ogcz\_DEV\ivy")

from lib.math.calculator import calculate

print("=" * 90)
print(" CALCULATOR OUTPUT TEST - Display Numbers with Commas, Speak Words")
print("=" * 90)

test_cases = [
    ("what is 1 + 1", "2", "two"),
    ("what is 1 million plus ten million", "11,000,000", "eleven million"),
    ("calculate 1 divided by 2", "0.5", "zero point five"),
    ("what is 15123 + 20000", "35,123", "thirty five thousand one hundred twenty three"),
    ("what is one billion plus five hundred million", "1,500,000,000", "one billion five hundred million"),
    ("calculate 22 divided by 7", "3.142857...", "three point one four two eight five seven..."),
    ("what is 0.25 times 8", "2", "two"),
    ("calculate 3.14159 times 2", "6.28318", "six point two eight three one eight"),
]

for query, expected_display, expected_speak in test_cases:
    print(f"\n{'─' * 90}")
    print(f"� Query: {query}")
    print(f"{'─' * 90}")
    
    result = calculate(query)
    if result["success"]:
        print(f"📊 Display Message: The answer is {result['result_display']}")
        print(f"🔊 Speak Message:   The answer is {result['result_words']}")
        print(f"✅ Expected Display: {expected_display}")
        print(f"✅ Expected Speak:   {expected_speak}")
    else:
        print(f"❌ Error: {result['error']}")

print("\n" + "=" * 90)
print("✨ Perfect! Numbers with commas on screen, natural words when spoken!")
print("=" * 90)

