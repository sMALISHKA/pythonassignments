#1

file=open("sales.txt","w")

n=int(input("enter the number of sales records"))

for i in range(n):
    date=input("enter the date of sale")
    product=input("enter the product name")
    amount=int(input("enter the amount of sale"))
    file.write(date+","+product+","+str(amount)+"\n")

file.close()
print("sales record stored successfully")

#2

file=open("sales.txt","a")

date=input("enter the date of sale")
product=input("enter the product name")
amount=int(input("enter the amount of sale"))

file.write(date+","+product+","+str(amount)+"\n")

file.close()
print("sales record stored successfully")

#3

import csv

txt_file=open("sales.txt","r")
csv_file=open("sales.csv","w", newline='')

writer=csv.writer(csv_file)
writer.writerow(["date","product","amount"])

for line in txt_file:
    data=line.strip().split(",")
    writer.writerow(data)

txt_file.close()
csv_file.close()

print("sales.txt converted to sales.csv successfully")

#4
import csv

file=open("sales.txt","r")
reader=csv.reader(file)

for row in reader:
    print(row)

file.close()

#5

import csv

total =0
file=open("sales.csv","r")
reader=csv.reader(file)

next(reader)

for row in reader:
    total+=int(row[2])

file.close()

print("total sales amount",total)
