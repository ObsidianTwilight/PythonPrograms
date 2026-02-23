"""
1. input: Rank of each person.
2. Put it inside list.
3. use of 'for loop' to traverse the list to find max rank number
4. Find a process that will slect sencond place rank of person
5. Return that second place.
"""
L = []
n = int(input("Enter the number of person to be participated: "))
for i in range(n):
    rank = int(input("Enter the rank: "))
    L.append(rank)

print(L)




m = int(input("Enter the arr: "))
arr = list(map(int, input().split()))
