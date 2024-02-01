import re

# Search the string to see if it starts with "The" and ends with "Spain"
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("Yes we have a match!")
else:
    print("No match!")


#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

txt2 = "hello planet"
x2 = re.findall("he.{2}o", txt2)

if x2:
    print(x2)
else:
    print("None")


#Find all lower case characters alphabetically between "a" and "m":

txt3 = "The rain in Spain"
x3 = re.findall("[a-m]", txt3)
print(x3)


#Find all digit characters:

txt4 = "That will be 59 dollars"
x4 = re.findall("\d", txt4)
print(x4)


# Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

txt5 = "hello planet"
x5 = re.findall("he..o", txt5)


# #Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

txt6 = "hello planet"
x6 = re.findall("he.*o", txt6)


# search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

txt7 = "hello planet"
x7 = re.findall("he.+o", txt7)
print(x7)


# search for a sequence that starts with "he", followed by 0 or one (any) characters, and an "o":
 
txt8 = "hello planet"
x8 = re.findall("he.?o", txt8)
print(x8)

# search for a sequence that starts with "he", followed by 0 or one (any) characters, and an "o":

txt9 = "hello planet"
x9 = re.findall("he.{2}o", txt9)
print(x9)

#Check if the string contains either "falls" or "stays":

txt = "The rain in Spain falls mainly in the plain!"
x10 = re.findall("falls|stays", txt)

if x10:
  print(f"Yes, there is at least one match!: {x10}")
else:
  print("No match")
