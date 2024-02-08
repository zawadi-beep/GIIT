# datatypes
number = 45  # int
bun = 56.89  # float
greeting = "hello there"  # string
isPythonIntresing = True  # bool
# variable storing multiple values
languages = ["Python", "Php", "JavaScript"]  # list
fruits = ("apple", "banana", "grapes")  # tuple

countries = {"Kenya", "Korea", "China"}  # set
# dictionary
details = {
    "First Name": "Grace",
    "Age": "17",
    "Course": "MIT",
    "Nationality": "North America",
}

print(number)
print(greeting)
print(countries)
print(isPythonIntresing)
print(details)
print(details["Course"])
print(details["Nationality"])

# DETERMINING THE DATATYPE
print(type(details))
print(type(countries))

# typecasting-converting one data type to another
print(float(number))
print(int(bun))

# deleting an element from a list
del languages[0]
print(languages)