#1
t= tuple(map(int,input("Enter tuple").split()))

maximum =t[0]
minimum=t[0]

for i in t:
    if i>maximum:
        maximum=i
    if i<minimum:
        minimum=i

print(maximum,minimum)

#2
lst =[(1,'a'), (2,'b'),(3,'c')]
d={}

for key,value in lst:
    d[key]=value

print("Dictionary",d)

#3

t=tuple(map(int,input("Enter tuple").split()))
element = int(input("Enter element"))

count=0

for i in t:
    if i==element:
        count+=1

print("Occurrence",count)

#4
t=(1,2,[3,4,5])

print("Before modification",t)

t[2][0]=100
t[2].append(6)

print("After modification",t)

#5
t1=(1,2,3)
t2=(4,5,6)

print ("before swap")
print("t1=",t1)
print("t2=",t2)

t1,t2 = t2,t1

print("t1=",t1)
print("t2=",t2)

