#1

s= input("Enter a string:")

vowels = 0
consonants = 0
digits = 0
special = 0

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1


print("vowels:",vowels)
print("consonants:",consonants)
print("digits:",digits)
print("special:",special)


#2

s= input("Enter a string:")

words=s.split()
reversed_words=[]

for word in words:
    reversed_words.append(word[::-1])

result=" ".join(reversed_words)
print(result)

#3
# using slicing

s= input("Enter a string:")

if s == s[::-1]:
    print("Palindrome")
else:
    print("not Palindrome")

#using indexing

s= input("Enter a string:")

is_palindrome=True
n= len(s)

for i in range(n//2):
    if s[i] != s[n//2-i]:
        is_palindrome=False
        break
if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")

#4

s= input("Enter a string:")

freq={}

for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print("Character freqeuncies")
for key , value in freq.items():
    print(key,":",value)


#5
s="hello"

try:
    s[0]='H'
except TypeError as e:
    print("Error occured",e)

print("Original String",s)
