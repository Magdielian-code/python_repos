import json

""" Encodig  cusstom object """
class User1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

Mark = User1("Mark", 24)

# custom function for encoding(python to json)
def encode_user (user_name):
    if isinstance(user_name, User1):
        return {"name": user_name.name, "age": user_name.age, user_name.__class__.__name__: True}
    else:
        raise TypeError("Object of type user is not JSON serialiazable.")
    

userJSON = json.dumps(Mark, default=encode_user)
print(userJSON)