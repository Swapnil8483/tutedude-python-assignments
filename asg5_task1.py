#Dictionary of student marks
std_marks = {
    "sagar" : 97,
    "tushar" : 80,
    "kishor" : 60,
    "pravin" : 75,
    "navin" : 68
}

name = (input("Enter student's name:"))
if name in std_marks:
    print(f"{name}'s marks : {std_marks[name]}")
else:
    print(f"{name} not found.")
