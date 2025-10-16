import re


if x := re.search(r"search\s+(.+?)\s+on\s+google", "search dogs on google"):
    print(x.group(2))
