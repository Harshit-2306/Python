
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# print(my_dict["name"])


my_dict["job"] = "Engineer"


my_dict["age"] = 26
del my_dict["city"]
# print(my_dict["job"])


# for key, value in my_dict.items():
    # print(f"{key}: {value}")

# my_dict.clear()
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.fromkeys(my_dict,"34"))

my_dict.setdefault("profession","artist")
print(my_dict.setdefault("age",))