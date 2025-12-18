from operator import truediv

file = open("students.txt","w")

n= int(input("enter no. of students:"))

for i in range(n):
    name=input("enter name:")
    marks=int(input("enter marks:"))
    file.write(name +" "+ str(marks) +"\n")

file.close()
print("Students records written successfully")

#2
file =open("students.txt","r")

content=file.read()
print(content)

file.close()

#3

file=open("students.txt","a")

name=input("enter name:")
marks=int(input("enter marks:"))
file.write(name +" "+ str(marks) +"\n")

file.close()
print("Students records appended successfully")

#4
file=open("students.txt","r")

count=0
for line in file:
    count+=1

file.close()
print("Total students records",count)

#5
file=open("students.txt","r")

search_name=input("enter name:")
found=False

for line in file:
    if search_name in line:
        print("Student found",line)
        found=True
        break

if not found:
    print("Student not found")

file.close()
