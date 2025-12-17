num=int(input("Enter the number:"))
if num%2==0:
    print("Even Number")
else:
    print("Odd Number")

marks=85

if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
else:
    print("Fail")

n1=-9
if n1>0:
    if n1%2==0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Negative Number")

for i in range(1,6):
    print(i)
j=1
while j<=5:
    print(j)
    j+=1
for i in range(1,6):
    if i==3:
        break
    for k in range(1,4):
     print(i,k)