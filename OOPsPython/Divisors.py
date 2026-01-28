divisor = int(input("Enter a number "))
List = []
for i in range(1, 1000):
    if divisor % i == 0:
        List.append(i)
    
print(List)