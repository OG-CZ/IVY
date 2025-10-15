from asteval import Interpreter
import re
import math

aeval = Interpreter()

aeval.symtable["pi"] = math.pi
aeval.symtable["e"] = math.e
aeval.symtable["sqrt"] = math.sqrt
aeval.symtable["sin"] = math.sin
aeval.symtable["cos"] = math.cos
aeval.symtable["tan"] = math.tan
aeval.symtable["log"] = math.log
aeval.symtable["log10"] = math.log10
aeval.symtable["exp"] = math.exp
aeval.symtable["factorial"] = math.factorial
aeval.symtable["abs"] = abs
aeval.symtable["round"] = round
aeval.symtable["pow"] = pow


def word_to_number(text):
    text = text.lower().strip()

    if re.match(r"^-?\d+\.?\d*$", text):
        return float(text) if "." in text else int(text)

    fraction_map = {
        "half": 0.5,
        "third": 1 / 3,
        "fourth": 0.25,
        "quarter": 0.25,
        "fifth": 0.2,
        "sixth": 1 / 6,
        "seventh": 1 / 7,
        "eighth": 0.125,
        "ninth": 1 / 9,
        "tenth": 0.1,
    }

    fraction_pattern = r"(\w+)\s+(half|third|fourths?|quarters?|fifths?|sixths?|sevenths?|eighths?|ninths?|tenths?)"
    match = re.match(fraction_pattern, text)
    if match:
        numerator_word = match.group(1)
        denominator_word = match.group(2).rstrip("s")

        if numerator_word in {"one", "a", "an"}:
            numerator = 1
        elif numerator_word == "two":
            numerator = 2
        elif numerator_word == "three":
            numerator = 3
        else:
            try:
                numerator = word_to_number(numerator_word)
            except:
                numerator = 1

        if denominator_word in fraction_map:
            return numerator * fraction_map[denominator_word]

    word_to_num = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
        "half": 0.5,
        "third": 1 / 3,
        "quarter": 0.25,
        "fourth": 0.25,
        "fifth": 0.2,
        "sixth": 1 / 6,
        "seventh": 1 / 7,
        "eighth": 0.125,
        "ninth": 1 / 9,
        "tenth": 0.1,
    }

    multipliers = {
        "hundred": 100,
        "thousand": 1000,
        "million": 1000000,
        "billion": 1000000000,
    }

    words = text.split()
    current = 0
    total = 0

    for word in words:
        word = word.strip()
        if not word or word == "and":
            continue

        if word in word_to_num:
            current += word_to_num[word]
        elif word in multipliers:
            if word == "hundred":
                current = (current or 1) * 100
            else:
                current = (current or 1) * multipliers[word]
                total += current
                current = 0
        elif word.replace(".", "").replace("-", "").isdigit():
            num = float(word) if "." in word else int(word)
            current += num
        else:
            raise ValueError(f"Invalid number word: {word}")

    return total + current


def parse_text_to_expression(text):
    original_text = text
    text = text.lower().strip()

    text = text.replace("what's", "what is")
    text = text.replace("how's", "how is")
    text = text.replace("that's", "that is")

    fillers_to_remove = [
        r"\bhey\b",
        r"\bcan you\b",
        r"\bplease\b",
        r"\bfor me\b",
        r"\btell me\b",
        r"\bagain\b",
        r"\btogether\b",
        r"\bif i\b",
        r"\bhave\b",
        r"\bapples?\b",
        r"\bget\b",
        r"\bhow many do i have\b",
        r"\bwhat is\b",
        r"\bhow much is\b",
        r"\bhow much\b",
        r"\bis\b",
        r"\bdo i get\b",
        r"\bdo i\b",
        r"\bcalculate\b",
        r"\bthe total of\b",
        r"\btake\b",
        r"\bthan\b(?! )",
    ]

    for filler in fillers_to_remove:
        text = re.sub(filler, " ", text)

    text = re.sub(r"\s+", " ", text).strip()

    sum_match = re.search(r"(?:the\s+)?sum\s+of\s+(.+)", text)
    if sum_match:
        nums_text = sum_match.group(1)
        parts = re.split(r",|\s+and\s+", nums_text)
        text = " __PLUS__ ".join(parts)

    product_match = re.search(r"(?:the\s+)?product\s+of\s+(.+?)\s+and\s+(.+)", text)
    if product_match:
        x = product_match.group(1).strip()
        y = product_match.group(2).strip()
        text = f"{x} __MULT__ {y}"

    text = re.sub(r"the\s+result\s+of\s+", "", text)

    text = re.sub(r"the\s+total\s+of\s+", "", text)

    diff_match = re.search(r"difference\s+between\s+(.+?)\s+and\s+(.+)", text)
    if diff_match:
        x = diff_match.group(1).strip()
        y = diff_match.group(2).strip()
        text = f"{x} __MINUS__ {y}"

    more_than_match = re.search(r"(\S+(?:\s+\S+)*?)\s+more\s+than\s+(.+)", text)
    if more_than_match:
        x = more_than_match.group(1).strip()
        y = more_than_match.group(2).strip()
        text = f"{y} __PLUS__ {x}"

    square_of_match = re.search(r"square\s+of\s+(.+)", text)
    if square_of_match:
        x = square_of_match.group(1).strip()
        text = f"{x} __POW__ 2"

    cube_of_match = re.search(r"cube\s+of\s+(.+)", text)
    if cube_of_match:
        x = cube_of_match.group(1).strip()
        text = f"{x} __POW__ 3"

    double_match = re.search(r"double\s+of\s+(.+)", text)
    if double_match:
        x = double_match.group(1).strip()
        text = f"{x} __MULT__ 2"

    triple_match = re.search(r"triple\s+of\s+(.+)", text)
    if triple_match:
        x = triple_match.group(1).strip()
        text = f"{x} __MULT__ 3"

    increase_match = re.search(r"increase\s+(.+?)\s+by\s+(.+?)\s+percent", text)
    if increase_match:
        x = increase_match.group(1).strip()
        y = increase_match.group(2).strip()
        text = f"( {x} ) __MULT__ ( 1 __PLUS__ ( {y} ) __DIV__ 100 )"

    reduce_match = re.search(r"reduce\s+(.+?)\s+by\s+(.+?)\s+percent", text)
    if reduce_match:
        x = reduce_match.group(1).strip()
        y = reduce_match.group(2).strip()
        text = f"( {x} ) __MULT__ ( 1 __MINUS__ ( {y} ) __DIV__ 100 )"

    split_match = re.search(r"split\s+(.+?)\s+into\s+(.+?)\s+equal\s+parts", text)
    if split_match:
        x = split_match.group(1).strip()
        y = split_match.group(2).strip()
        text = f"{x} __DIV__ {y}"

    percent_of_match = re.search(r"(.+?)\s+percent\s+of\s+(.+)", text)
    if percent_of_match:
        x_part = percent_of_match.group(1).strip()
        y_part = percent_of_match.group(2).strip()
        text = f"{x_part} __DIV__ 100 __MULT__ {y_part}"

    text = re.sub(r"(\d+(?:\.\d+)?)\s*%\s+of\s+", r"\1 __DIV__ 100 __MULT__ ", text)

    text = re.sub(r"\bdivided\s+by\b", " __DIV__ ", text)

    text = re.sub(r"\bof\b", " __MULT__ ", text)

    multiply_by_match = re.search(
        r"multiply\s+(.+?)\s+by\s+(.+?)(?=\s+(?:plus|minus|times|divide|$)|\s*$)", text
    )
    if multiply_by_match:
        x_part = multiply_by_match.group(1).strip()
        y_part = multiply_by_match.group(2).strip()
        text = text.replace(multiply_by_match.group(0), f"{x_part} __MULT__ {y_part}")

    divide_by_match = re.search(
        r"divide\s+(.+?)\s+by\s+(.+?)(?=\s+(?:plus|minus|times|multiply|$)|\s*$)", text
    )
    if divide_by_match:
        x_part = divide_by_match.group(1).strip()
        y_part = divide_by_match.group(2).strip()
        text = text.replace(divide_by_match.group(0), f"{x_part} __DIV__ {y_part}")

    text = re.sub(r"\bmultiplied\s+by\b", "multiplied", text)

    subtract_from_match = re.search(r"subtract\s+(.+?)\s+from\s+(.+)", text)
    if subtract_from_match:
        x_part = subtract_from_match.group(1)
        y_part = subtract_from_match.group(2)
        text = f"{y_part} minus {x_part}"

    add_and_match = re.search(
        r"\badd\s+(.+?)\s+and\s+(.+?)(?=\s+(?:plus|minus|times|$)|\s*$)", text
    )
    if add_and_match:
        x = add_and_match.group(1).strip()
        y = add_and_match.group(2).strip()
        text = text.replace(add_and_match.group(0), f"{x} __PLUS__ {y}")
    else:
        add_to_match = re.search(r"add\s+(.+?)\s+to\s+(.+)", text)
        if add_to_match:
            x_part = add_to_match.group(1)
            y_part = add_to_match.group(2)
            text = f"{y_part} plus {x_part}"

    take_away_match = re.search(r"take\s+(.+?)\s+from\s+(.+)", text)
    if take_away_match:
        x_part = take_away_match.group(1)
        y_part = take_away_match.group(2)
        text = f"{y_part} minus {x_part}"

    text = re.sub(
        r"half\s+of\s+(.+?)(?=\s+(?:plus|minus|times|$)|\s*$)", r"\1 __DIV__ 2", text
    )

    def convert_and_half(match):
        word = match.group(1)
        try:
            num = word_to_number(word)
            return f"{num}.5"
        except:
            return match.group(0)

    while re.search(r"(\w+(?:\s+\w+)*?)\s+and\s+a\s+half", text):
        text = re.sub(
            r"(\w+(?:\s+\w+)*?)\s+and\s+a\s+half", convert_and_half, text, count=1
        )

    text = re.sub(r"(\S+(?:\s+\S+)*?)\s+squared(?=\s|$)", r"\1 __POW__ 2", text)

    text = re.sub(r"(\S+(?:\s+\S+)*?)\s+cubed(?=\s|$)", r"\1 __POW__ 3", text)

    text = re.sub(r"the\s+square\s+root\s+of\s+(.+)", r"sqrt( \1 )", text)

    text = re.sub(r"\braised\s+to\s+the\s+power\s+of\b", " __POW__ ", text)

    def convert_decimal_words(match):
        whole = match.group(1).strip()
        decimal = match.group(2).strip()
        try:
            if whole.replace(".", "").replace("-", "").isdigit():
                whole_num = whole
            else:
                whole_num = str(word_to_number(whole))

            if decimal.replace(".", "").replace("-", "").isdigit():
                decimal_num = decimal
            else:
                decimal_num = str(word_to_number(decimal))

            return f"{whole_num}.{decimal_num}"
        except:
            return match.group(0)

    while re.search(
        r"(\S+(?:\s+(?!point)\S+)*)\s+point\s+(\S+(?:\s+(?!plus|minus|times|multiply|divide|divided)\S+)*)",
        text,
    ):
        text = re.sub(
            r"(\S+(?:\s+(?!point)\S+)*)\s+point\s+(\S+(?:\s+(?!plus|minus|times|multiply|divide|divided)\S+)*)",
            convert_decimal_words,
            text,
            count=1,
        )

    operation_placeholders = {
        r"\bplus\b": " __PLUS__ ",
        r"\badd\b": " __PLUS__ ",
        r"\bminus\b": " __MINUS__ ",
        r"\bsubtract\b": " __MINUS__ ",
        r"\btimes\b": " __MULT__ ",
        r"\bmultiply\b": " __MULT__ ",
        r"\bmultiplied\b": " __MULT__ ",
        r"\bdivide\b": " __DIV__ ",
        r"\bdivided\b": " __DIV__ ",
        r"\bover\b": " __DIV__ ",
        r"\bto the power of\b": " __POW__ ",
        r"\bmod\b": " __MOD__ ",
        r"\bmodulo\b": " __MOD__ ",
    }

    for pattern, placeholder in operation_placeholders.items():
        text = re.sub(pattern, placeholder, text)

    function_patterns = {
        r"\bsquare root of\b": " sqrt( ",
        r"\bsqrt of\b": " sqrt( ",
        r"\bsine of\b": " sin( ",
        r"\bsin of\b": " sin( ",
        r"\bcosine of\b": " cos( ",
        r"\bcos of\b": " cos( ",
        r"\btangent of\b": " tan( ",
        r"\btan of\b": " tan( ",
        r"\bnatural log of\b": " log( ",
        r"\bln of\b": " log( ",
        r"\blog of\b": " log10( ",
        r"\bfactorial of\b": " factorial( ",
        r"\babsolute value of\b": " abs( ",
    }

    for pattern, func in function_patterns.items():
        text = re.sub(pattern, func, text)

    text = re.sub(r"\bis\b(?!\s*\d)", " ", text)
    text = re.sub(r"\bwhat\b", " ", text)
    text = re.sub(r"\bhow\b", " ", text)
    text = re.sub(r"\bmany\b", " ", text)
    text = re.sub(r"\bmore\b(?!\s+than)", " ", text)

    text = re.sub(r"\s+", " ", text).strip()

    parts = re.split(
        r"(__PLUS__|__MINUS__|__MULT__|__DIV__|__POW__|__MOD__|\(|\))", text
    )

    converted_parts = []

    for part in parts:
        part = part.strip()
        if not part:
            continue

        if part in [
            "__PLUS__",
            "__MINUS__",
            "__MULT__",
            "__DIV__",
            "__POW__",
            "__MOD__",
        ]:
            placeholder_to_op = {
                "__PLUS__": "+",
                "__MINUS__": "-",
                "__MULT__": "*",
                "__DIV__": "/",
                "__POW__": "**",
                "__MOD__": "%",
            }
            converted_parts.append(placeholder_to_op[part])
        elif part in ["(", ")"]:
            converted_parts.append(part)
        elif part in ["+", "-", "*", "/", "**", "%"]:
            converted_parts.append(part)
        else:
            try:
                num = word_to_number(part)
                converted_parts.append(str(num))
            except (ValueError, Exception):
                if re.match(r"^-?\d+\.?\d*$", part):
                    converted_parts.append(part)
                else:
                    converted_parts.append(part)

    expression = " ".join(converted_parts)
    expression = re.sub(r"\s+", " ", expression).strip()

    return expression


def evaluate_expression(expression):
    try:
        result = aeval(expression)

        if aeval.error:
            print(f"Evaluation error: {aeval.error}")
            return None

        return result
    except Exception as e:
        print(f"Exception during evaluation: {e}")
        return None


def format_result(result):
    if result is None:
        return None

    if isinstance(result, (int, float)):
        if isinstance(result, float) and result.is_integer():
            return int(result)
        elif isinstance(result, float):
            return round(result, 10)

    return result


def format_number_for_display(num):
    if not isinstance(num, (int, float)):
        return str(num)

    if isinstance(num, float) and not num.is_integer():
        return f"{num:,}"
    else:
        return f"{int(num):,}"


def number_to_words(num):
    if not isinstance(num, (int, float)):
        return str(num)

    if isinstance(num, float) and not num.is_integer():
        num_str = str(num)
        if "." in num_str:
            whole_part, decimal_part = num_str.split(".")
            if whole_part == "0":
                result = "zero point "
            else:
                whole_num = int(whole_part)
                if whole_num < 0:
                    result = "negative " + number_to_words(abs(whole_num)) + " point "
                else:
                    result = number_to_words(whole_num) + " point "

            digit_names = [
                "zero",
                "one",
                "two",
                "three",
                "four",
                "five",
                "six",
                "seven",
                "eight",
                "nine",
            ]
            decimal_words = " ".join(digit_names[int(d)] for d in decimal_part)
            return result + decimal_words
        return str(num)

    num = int(num)

    if num == 0:
        return "zero"

    if num < 0:
        return "negative " + number_to_words(abs(num))

    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = [
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    tens = [
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]

    def convert_below_thousand(n):
        if n == 0:
            return ""
        elif n < 10:
            return ones[n]
        elif n < 20:
            return teens[n - 10]
        elif n < 100:
            return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
        else:
            return (
                ones[n // 100]
                + " hundred"
                + (" " + convert_below_thousand(n % 100) if n % 100 != 0 else "")
            )

    parts = []

    if num >= 1000000000:
        billions = num // 1000000000
        parts.append(convert_below_thousand(billions) + " billion")
        num %= 1000000000

    if num >= 1000000:
        millions = num // 1000000
        parts.append(convert_below_thousand(millions) + " million")
        num %= 1000000

    if num >= 1000:
        thousands = num // 1000
        parts.append(convert_below_thousand(thousands) + " thousand")
        num %= 1000

    if num > 0:
        parts.append(convert_below_thousand(num))

    return " ".join(parts)


def calculate(query):
    try:
        expression = parse_text_to_expression(query)

        if not expression:
            return {
                "success": False,
                "error": "Could not parse the expression",
                "result": None,
                "result_words": None,
                "expression": None,
            }

        result = evaluate_expression(expression)

        if result is None:
            return {
                "success": False,
                "error": "Could not evaluate the expression",
                "result": None,
                "result_words": None,
                "expression": expression,
            }

        formatted_result = format_result(result)
        result_words = number_to_words(formatted_result)
        result_display = format_number_for_display(formatted_result)

        return {
            "success": True,
            "result": formatted_result,
            "result_display": result_display,
            "result_words": result_words,
            "expression": expression,
            "error": None,
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "result": None,
            "result_words": None,
            "expression": None,
        }


def test_calculator():
    test_cases = [
        "two plus three",
        "five times six",
        "ten minus four",
        "twenty divided by five",
        "two to the power of eight",
        "square root of twenty five",
        "one hundred plus fifty three",
        "one thousand times two",
        "five million plus three thousand",
    ]

    print("Calculator Test Cases:")
    print("=" * 60)

    for query in test_cases:
        result = calculate(query)
        if result["success"]:
            print(f"Query: {query}")
            print(f"Expression: {result['expression']}")
            print(f"Result: {result['result']} ({result['result_words']})")
            print("-" * 60)
        else:
            print(f"Query: {query}")
            print(f"Error: {result['error']}")
            print("-" * 60)
            print("-" * 60)


if __name__ == "__main__":
    ...
