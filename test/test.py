class MyClass:
    def __init__(self):
        self.name = "John"
        self.age = 30
        self.is_student = True
        self.address = {
            "street": "123 Main St",
            "city": "Anytown"
        }
        self.hobbies = ["reading", "sports"]

def class_to_json(obj):
    if not isinstance(obj, MyClass):
        raise TypeError("Input object must be an instance of MyClass")

    description = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            description[attr] = value

    return description

# Example usage:
obj = MyClass()
result = class_to_json(obj)
print(result)
