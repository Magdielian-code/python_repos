import json

"""Serialization - From python dict to json object"""

person = {"name": "John", "age": 30, "city": "Lagos", "hasChildren": True, "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=4, sort_keys=True) 
# print(personJSON)

"""Deserialization - Json object to python"""
with open("person.json", "r", encoding="utf-8") as file:
    person = json.load(file)
    print(person)