import csv

file=open("attendance.csv.csv","w", newline="")
writer = csv.writer(file)

writer.writerow(["EmpID","Name","Status"])

n=int(input("enter no. of employees:"))

for i in range(n):
    emp_id=input("enter employee id:")
    name=input("enter employee name:")
    status=input("enter employee status:")
    writer.writerow([emp_id,name,status])

file.close()
print("Attendance data written successfulyy")

#2
import csv

file=open("attendance.csv.csv","r")
reader=csv.reader(file)

for row in reader:
    print(row)
file.close()

#3
import csv

file=open("attendance.csv.csv","a",newline="")
writer=csv.writer(file)

emo_id=int(input("enter employee id:"))
name=input("enter employee name:")
status=input("enter employee status:")

writer.writerow([emo_id,name,status])

file.close()
print("Record appended successfully")

#4
import csv

file=open("attendance.csv.csv","r")
reader=csv.reader(file)

count=0
next(reader)

for row in reader:
    if row[2].lower()=="absent":
        count+=1

file.close()
print("number of absent employees",count)

#5
import csv

file=open("attendance.csv.csv","r")
reader=csv.reader(file)

search_id=int(input("enter employee id:"))
found=False

next(reader)

for row in reader:
    if row[0]==search_id:
        print("employee found",row)
        found=True
        break

if not found:
    print("employee not found")

file.close()


