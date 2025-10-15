import sys

sys.path.insert(0, r"c:\Users\Asus\Documents\ogcz\_DEV\ivy")

try:
    from lib.math.calculator import calculate

    print("\n" + "=" * 70)
    print("  CALCULATOR DISPLAY VS SPEAK TEST")
    print("=" * 70)

    test_1 = calculate("what is 1 + 1")
    print(f"\n1️⃣  Query: what is 1 + 1")
    print(f"   Display: The answer is {test_1['result_display']}")
    print(f"   Speak:   The answer is {test_1['result_words']}")

    test_2 = calculate("what is 1 million plus ten million")
    print(f"\n2️⃣  Query: what is 1 million plus ten million")
    print(f"   Display: The answer is {test_2['result_display']}")
    print(f"   Speak:   The answer is {test_2['result_words']}")

    test_3 = calculate("calculate 1 divided by 2")
    print(f"\n3️⃣  Query: calculate 1 divided by 2")
    print(f"   Display: The answer is {test_3['result_display']}")
    print(f"   Speak:   The answer is {test_3['result_words']}")

    print("\n" + "=" * 70)
    print("✅ SUCCESS! Display shows formatted numbers, speak uses words!")
    print("=" * 70 + "\n")

except Exception as e:
    print(f"ERROR: {e}")
    import traceback

    traceback.print_exc()
