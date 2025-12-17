student={
    "Name":"Kavya",
    "Age" : 25,
    "Course":"Python",
    "Marks":{"maths":50,"Science":60,"English":70,"Social":90}
}

print(student.get("Course"))
#student["Marks"]=85
student["Age"]=21
student.pop("Course")
print(student.items())

for key,value in student.items():
    print(key,":",value)
if "Marks" in student:
    print("Marks exists")