# create an empty dictionary
students = {}
print(type(students))
print("created an empty dictionary:", students)

# add something into dictionary
students["Luffy"] = 3_000_000_000
students["Zoro"] = 1_111_000_000
print("added something:", students)

# modify something in dictionary
students["Luffy"] = 3_500_000_000
print("modified something:", students)

# delete something in dictionary
students.pop("Luffy")
print("deleted something:", students)
