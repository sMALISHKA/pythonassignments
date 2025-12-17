num={1,2,3,4,"python","java",1,2}
print(num)
num.add("c#")
print(num)

num.update(["java","php"])
print(num)
num.remove(1)
print(num)

A={1,2,3}
B={1,2}
print("union:", A|B)
print("Intersection:", A&B)
print("difference:",A-B)
print("difference:",B-A)
print("Symmetric difference:",A^B)

print(200 not in A)

print(B.issubset(A))

squares={x*x for x in range(1,6)}
print(squares)

fs=frozenset([1,2,3])
print(fs)