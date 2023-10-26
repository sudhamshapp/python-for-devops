import re

text = "quick brown fox"
pattern = r"quick"

catch = re.match(pattern, text)
if catch:
    print("Match found:", catch.group())
else:
    print("No match")
