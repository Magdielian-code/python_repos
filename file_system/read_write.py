import os

with open("mydata.txt", mode='w', encoding="utf-8") as myfile:
    myfile.write("Some random text\nMore random texts\nAnd some more.")

with open("mydata.txt", encoding="utf-8") as myfile:
    """
        read()  - reads everything till it gets to a new line  
        readline()  - reads everything including new lines
        readlines() - reads everything in a list, puts each line into a list.
    """

    print(myfile.read())
"""
    Checks if myfile was closed by with() method: return True if closed.
    Checks file name
    Checks file mode 
""" 

print(myfile.closed)
print(myfile.name)
print(myfile.mode)


# Exploring os modules

os.rename("mydata.txt", "mydata2.txt")
os.remove("mydata2.txt")
os.mkdir("mydir")
os.chdir("mydir")
print("Current directory: ", os.getcwd())