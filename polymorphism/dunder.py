# Dunder Method

list1 = [1,0,-1]
print(len(list1))
print(list1)
print(type(list1))


class Author:
    def __init__(self, name, book_name, pages):
        self.name = name
        self.book_name = book_name
        self.pages = pages
    
    def __len__(self):
        return self.pages
    
    # To print string mode of an object
    def __str__(self):
        return f"{self.book_name} by {self.name} has {self.pages} pages"
    
    # To make object callable like a fuction
    def __call__(self, *args, **kwargs):
        return f"{self.book_name} was written by {self.name} and it has {self.pages} pages"

    def __del__(self):
        print("Deleted...")

Dave = Author('Dave', 'Come Away', 1500)
print(Dave)

# Call object Dave like a function
"""To make objectscallale use the __call__ dunder method"""
print(Dave())

# Utilize custom __del__ method
del Dave
print(Dave)
