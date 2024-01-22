print(1+2)
print("1" + "2")

print("Operator overloading")

print(int.__add__(1,2))
print(str.__add__('1','2'))

# trying operator overloading with complex numbers using classes

class ComplexNumbers:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    # Now let's overload the '+' operator, by modifying the __add__ method.
    def __add__(self, other):
        selves = self.real + other.real
        others = self.imaginary + other.imaginary
        return f"{selves} + {others}i"


c1 = ComplexNumbers(1,2)
c2 = ComplexNumbers(3,4)

print(c1 + c2)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Overloading the greater than operator
    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False
        
p1 = Person('Dave', 12)
p2 = Person('Sam', 19)

if p1 > p2:
    print(f"{p1.name} pays the bill")
else:
    print(f"{p2.name} pays the bill")



# Method Overloading and Method Overriding

# Method Overloading   
class Demo:
    def add(self, *args):
        total = 0
        for arg in args:
            total += arg
        return total

d = Demo()
d_add = d.add(2,7,9,6,8,4,6,1,4,6)
print(d_add)

# Method Overriding
class Human:
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print(f"{self.name} can sleep for africa")

class Men(Human):
    def sleep(self):
        print(f"{self.name} sleeps only 3 hours everyday.")

Dave = Men('Dave')
Dave = Dave.sleep()

# dunder Method
