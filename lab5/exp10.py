#Experiment-10: Create a dictionary to represent key-value pairs and perform operations like adding, updating, and accessing values.

my_dict = {
    "apple" : 2,
    "banana" : 3,
    "orange" : 4
}

print("Number of apples:", my_dict["apple"])
print("Number of bananas:", my_dict.get("banana"))

my_dict["grape"] = 6
print("Upadated dictionary after adding grape:", my_dict)

my_dict["apple"] = 5
print("Upadated dictionary:", my_dict)
print("Number of apples:", my_dict["apple"])
print("Number of bananas:", my_dict.get("banana"))

del my_dict["orange"]
print("Updated after removing orange:", my_dict)