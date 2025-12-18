#1
from assignmenttuple import count


def get_even_numbers(numbers):
    return [num for num in numbers if num%2 == 0]

print(get_even_numbers([23,56,43,89,22,44,66]))

#2
def character_count(s):
    count={}
    for ch in s:
        count[ch]=count.get(ch,0)+1
    return count

print(character_count("Malishka"))

#3
def is_palindrome(num):
    return str(num) == str(num)[::-1]

print(is_palindrome(123))
print(is_palindrome(666))

#4
def average(*args):
    if len(args)==0:
        return 0
    return sum(args)/len(args)
print(average(1,2,3,4,5,6,7,8,9))

#5
def common_elements(list1,list2):
    result=[]
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result

l1=[1,2,3,4,5,6,7,8,9]
l2=[2,4,6,8,0]

print(common_elements(l1,l2))