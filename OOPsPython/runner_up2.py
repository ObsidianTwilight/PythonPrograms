if __name__ == '__main__':
    n = int(input("Enter the value of n: "))
    arr = list(map(int, input().split()))

    arr.sort()
    arr2 = set(arr)
    arr3 = list(arr2)
    arr3.sort()
    
    
    

print("sorted list: ",arr)
print("Unique + sorted: ", arr3[-2])