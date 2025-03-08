marks = {
 "harshit" : 100,
 "harry" : 87,
 "larry" : 48
}

# print(marks.keys())
# print(marks.values())

marks.update({"harshit":99})

print(marks.get("harry"))
print(marks["harry"])