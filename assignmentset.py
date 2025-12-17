#1

set1 ={1,2,3,4}
set2 ={5,6,7,8}

print("Union", set1|set2)
print("Intersection", set1&set2)
print("Difference", set1-set2)
print("Symmetric difference", set1-set2)

#2

set1={1,2,3,4}
set2={5,6,7,8}

common=set1&set2

set1 -=common
set2 -=common

print("after removal set1",set1)
print("after removal set2",set2)

#3

set1={1,2}
set2-{1,2,3,4}

if set1.issubset(set2):
    print("set1 is a subset of set2")
else:
    print("set1 is not a subset of set2")

#4

s={10,5,20,15,3}
n=int(input("enter a number"))

for i in s:
    if i>n:
        print(i)


#5

lst =[1,2,3,2,4,1,5]

print("original ist",lst)

unique_list=list(set(lst))
print("unique list",unique_list)
