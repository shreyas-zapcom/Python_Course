import re

text = "The rain in Spain"
match = re.search("rain", text)
print(match.group() if match else "No match")
