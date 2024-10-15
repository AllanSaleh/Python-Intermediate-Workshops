# Python Dictionary Lesson
# A dictionary in Python is a collection of key-value pairs. Each key is associated with a value, and both the keys and values can be of any data type. (By convention, keys are usually strings)

#1. Creating a Dictionary: Create a dictionary by enclosing key-value pairs in curly braces {}, separated by colons :
# Empty Dictionary

my_dictionary = {}

# Dictionary with values
# student1 = ["Adam", 99, "San Diego"]
# grocery_list = ["apple", "pineapple", "grapes"]

# print(student1[1])

person = {
    "name": "Allan",
    "age": 99,
    "city": "Toronto",
    "hasCar": False
}

#2. Accessing Values: You can access values in a dictionary by using their keys inside square brackets []
# NOTE: If the key doesn't exist, python will raise a "KeyError". To avoid this, you can use the .get() method which returns "None"(or a default value).
# Accessing values by key
print(person["name"])
print(person["city"])

print(person.get("nameeee"))


#3. Adding and Modifying Values: You can add a new key-value pair or modify an existing one by assigning a value to a key.
# Adding a new key-value pair
person["isInstructor"] = True

# Modifying an existing key-value pair
person["age"] = 101


#4. Removing Values: You can remove key-value pairs using the del statement(), .pop(), or .popitem()
# Remove a specific key-value pair
del person["city"]


# Using .pop() to remove and return the value
deleted_key = person.pop("hasCar")
print(f"The key with the value {deleted_key} has been deleted.")

print(person)

#5. Dictionary Methods:
# .keys(): returns all keys in the dictionary
# .values(): returns all values
# .items(): returns all key-value pairs as tuples
print(person.keys())
print(person.values())
print(person.items())

#6. Iterating through a dictionary: looping with for loop
# looping through keys
for key in person.keys():
    print(key)

for values in person.values():
    print(values)   

# looping through key-value pairs
for key, value in person.items():
    print(key, value)


#7. Nesting Dictionaries
people = {
    "student1": {
        "name":"Adam",
        "age":99
    },
    "student2":{
        "name":"Silas",
        "age":100,
        "favTeam":{
            "name":"Steelers",
            "city":"Pittsburgh",
            "players":["Ben","John","Mike"]
        }
    }
}

print(people)
# accessing values in a nested dictionary
print(people["student1"]["name"])
print(people["student2"]["favTeam"]["city"])
print(people["student2"]["favTeam"]["players"][1])
#8. Common Operations with Dictionaries
# Checking if a key exists: use the "in" keyword
if "student12" in people:
    print("Students 1 exists")
else:
    print("student 1 doesnt exist")

if "favTeam" in people["student2"]:
    print("favTeam exists")
else:
    print("favTeam doesnt exist")  
# Dictionary Length: Use len() to get the number of key-value pairs
print(len(people["student2"]))



# Python Tuples Lesson
# A tuple is a collection of items that is ORDERED and IMMUTABLE. Tuples are similar to lists, but with immutability and faster performance.

#1. Creating a Tuple
my_tuple = (1,2,3)
print(my_tuple)

# Tuples can contain elements of different data types
mixed_tuple = (12, 3 ,"apples",False)
print(mixed_tuple)

# Single Element Tuple: You need to add a comma after the element, otherwise Python will treat it as a simple value.

# without comma, its not a tuple
single_element_tuple = (2,)
print(single_element_tuple)


#2. Accessing Tuple Elements: Tuples are indexed, just like lists.
print(mixed_tuple[3])



#3. Slicing a Tuple: Slice a tuple to access a range of elements
grocery_list = ("apple", "pineapple", "grapes", "bread", "milk")
print(grocery_list[1:4])

print(type(9))
print(isinstance(grocery_list, tuple))