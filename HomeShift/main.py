# # Importing modules and packages
# import ShiftItem_Ozi.books
# import ShiftItem_Ozi.Clothes.jeans

# ShiftItem_Ozi.Clothes.jeans.display()
# print()

# # How to call a mclass and class module in a package
# b = ShiftItem_Ozi.books.MyClass()
# b.bookType()

from ShiftItem_Ozi import books
from ShiftItem_Ozi.Footwears import shoes, boots

books.display()


print(__name__)
