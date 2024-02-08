courses = ["MIT", "Cybersecurity", "Datascience"]
print(courses)
# accessing an element in an array
print(courses[1])
# looping through an array
for course in courses:
    print(course)

# adding an element into an array
courses.append("Android development")
print(courses)

# deleting an element from an array
courses.remove("Datascience")
print(courses)