import random

a = [1, 2, 3, 4, 5, 6, 16, 12, 11]
b = [2, 4, 6, 8, 9, 11, 13, 14, 16, 18]
c = []
for i in a:
    for j in b:
        if i == j:
            c.append(i)
print("Result: ",c)
print()
print("--------------------------------------------------")
print()

print("comparing random integers")
list1 = []
list2 = []
list3 = []

for i in range(10):
    R = random.randint(1, 50)
    list1.append(R)

for j in range(15):
    L = random.randint(1, 50)
    list2.append(L)

for num1 in list1:
    for num2 in list2:
        if num1 == num2:
            list3.append(num2)

list1.sort()
list2.sort()
list3.sort()
print(list1)
print(list2)
print("Common elements between list1 and list2: ",list3)
print()
print("---------------------------------------------------------------")
print()
print("Printing in one line")

[print(i) for i in a for j in b if i == j]

