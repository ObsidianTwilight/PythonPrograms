numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
userNumber = int(input("Enter the number please: "))
lessNums = []

for nums in numbers:
    if nums < userNumber:
        lessNums.append(nums)
print(lessNums)
print("------------------(❁´◡`❁)-------------------------")

print("List comprehetion:")
[print(num) for num in numbers if num < 8]

print("------------------(❁´◡`❁)-------------------------")





            

