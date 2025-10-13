import re
from lib.main.command import speak


def extract_numbers(query):
    """Extract numbers from a query string"""
    # Find all numbers (including decimals)
    numbers = re.findall(r"-?\d+\.?\d*", query)
    return [float(n) for n in numbers]


def extract_operation(query):
    """Detect the mathematical operation"""
    query_lower = query.lower()

    if any(word in query_lower for word in ["plus", "add", "sum"]):
        return "add"
    elif any(word in query_lower for word in ["minus", "subtract", "less"]):
        return "subtract"
    elif any(word in query_lower for word in ["times", "multiply", "product"]):
        return "multiply"
    elif any(word in query_lower for word in ["divide", "divided"]):
        return "divide"
    elif any(word in query_lower for word in ["power", "to the power"]):
        return "power"
    elif any(word in query_lower for word in ["square root", "sqrt"]):
        return "sqrt"
    elif "percent" in query_lower or "%" in query_lower:
        return "percent"

    # Try to detect from symbols
    if "+" in query:
        return "add"
    elif "-" in query:
        return "subtract"
    elif "*" in query or "×" in query:
        return "multiply"
    elif "/" in query or "÷" in query:
        return "divide"

    return None


def calculate(query):
    """Perform calculation based on query"""
    try:
        numbers = extract_numbers(query)
        operation = extract_operation(query)

        if not numbers:
            speak("I couldn't find any numbers in your request.")
            return

        if not operation:
            speak("I'm not sure what operation you want me to perform.")
            return

        # Perform calculation
        if operation == "add":
            result = sum(numbers)
            speak(f"The sum is {result}")

        elif operation == "subtract":
            if len(numbers) < 2:
                speak("I need at least two numbers to subtract.")
                return
            result = numbers[0] - numbers[1]
            speak(f"{numbers[0]} minus {numbers[1]} equals {result}")

        elif operation == "multiply":
            result = 1
            for num in numbers:
                result *= num
            speak(f"The product is {result}")

        elif operation == "divide":
            if len(numbers) < 2:
                speak("I need two numbers to divide.")
                return
            if numbers[1] == 0:
                speak("I can't divide by zero!")
                return
            result = numbers[0] / numbers[1]
            speak(f"{numbers[0]} divided by {numbers[1]} equals {result}")

        elif operation == "power":
            if len(numbers) < 2:
                speak("I need a base and an exponent.")
                return
            result = numbers[0] ** numbers[1]
            speak(f"{numbers[0]} to the power of {numbers[1]} is {result}")

        elif operation == "sqrt":
            if len(numbers) < 1:
                speak("I need a number to find the square root.")
                return
            if numbers[0] < 0:
                speak("I can't find the square root of a negative number.")
                return
            result = numbers[0] ** 0.5
            speak(f"The square root of {numbers[0]} is {result}")

        elif operation == "percent":
            if len(numbers) < 2:
                # Single number percentage (e.g., "what is 25 percent")
                speak(f"{numbers[0]} percent is {numbers[0] / 100}")
            else:
                # Percentage of a number (e.g., "what is 25 percent of 200")
                result = (numbers[0] / 100) * numbers[1]
                speak(f"{numbers[0]} percent of {numbers[1]} is {result}")

    except Exception as e:
        print(f"Calculation error: {e}")
        speak("Sorry, I had trouble with that calculation.")


def handle_math_request(query):
    """Entry point for math requests"""
    calculate(query)


def quick_add(a, b):
    """Quick addition"""
    result = a + b
    speak(f"{a} plus {b} equals {result}")
    return result


def quick_multiply(a, b):
    """Quick multiplication"""
    result = a * b
    speak(f"{a} times {b} equals {result}")
    return result
