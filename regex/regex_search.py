import re

# Search the string to see if it starts with "The" and ends with "Spain"
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("Yes we have a match!")
else:
    print("No match!")
