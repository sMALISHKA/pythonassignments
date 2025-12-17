fruits=("apple","orange","banana","kiwi","papaya")
vegs=("tomoto","brinjal")
print(fruits[0])
print(fruits[1:4])
print(fruits*3)
print(fruits+vegs)
print(fruits.index("orange"))

for i in fruits:
    print(i)

t=1,2,3
a,b,c=t
print(a)
print(b)
print(c)

l1=[50,60,70]
t1=tuple(l1)
print(t1)

x=10
y=20
x,y=y,x
print("x:",x)
print("x:",y)

def calc(a,b):
    return a+b,a-b,a*b
result=calc(30,50)

print(result)