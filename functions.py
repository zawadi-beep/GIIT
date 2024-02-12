# in-built functions
# max function
number = max(87, 56, 23, 45, 6, 12)
print(number)

# min function
x = min(34, 67, 45, 12, 48, 90, 11)
print(x)

# power function
z = pow(2, 3)
print(z)


# user defined functions
def details():
    print("Zawadi")


# call a function for it to run
details()


def student():
    name = "Zawadi"
    age = 18
    course = "MIT"
    print(name, age, course)


student()


# parameters
def student(name, age, course):
    print(name, age, course)


student("Zawadi", 18, "MIT")
student("Shantel", 17, "Cybersecurity")
student("Kassim", 19, "MIT")
student("Natasha", 16, "Cybersecurity")
student("Prudence", 20, "MIT")


# create a user defined function called employees that displays details of five employee.
# parameters are; full name,age,gender,position,salary

def employee(Fullname, Age, Gender, Position, Salary):
    print(Fullname, Age, Gender, Position, Salary)


employee("Prudence Zawadi", 28, "Female", "CEO", 500000)
employee("Shantel Neem", 23, "Female", "Human Resource Manager", 450000)
employee("Liam Styles", 32, "Male", "Office Supervisor", 230000)
employee("Kenzie Bell", 18, "Female", "Receptionist", 56000)
employee("Simon Peter", 43, "Male", "Video Editor", 190000)
