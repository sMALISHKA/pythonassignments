#1
lst = list(map(int,input("Enter a list: ").split()))
unique_list=[]

for item in lst:
    if item not in unique_list:
        unique_list.append(item)

print("list without duplicates",unique_list)

#2

numbers=list(map(int,input("Enter a list: ").split()))

even_numbers=[num for num in numbers if num %2 ==0]
print("Even numbers",even_numbers)

#3

numbers =list(map(int,input("Enter a list: ").split()))

largest=second_largest = float('-inf')
for num in numbers:
    if num>largest:
        second_largest = largest
        largest=num
    elif num> second_largest and num !=largest:
        second_largest = num

if second_largest == float('-inf'):
    print("not found")
else:
    print("second largest",second_largest)

#4
nested_list=[[1,2,3],[4,5,6],[7,8,9]]

for inner_list in nested_list:
    print("sum:",sum(inner_list))

#5

import copy

original =[[1,2],[3,4]]

shallow =copy.copy(original)
deep = copy.copy(original)

original[0][0]=100

print("Original",original)
print("Shallow",shallow)
print("Deep",deep)
