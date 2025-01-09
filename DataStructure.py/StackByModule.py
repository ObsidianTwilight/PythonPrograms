import collections
stack = collections.deque()

def Push():
    item = input("Enter the element")
    stack.append(item)
    print(stack)

def Pop():
    if stack is None:
        print("Stack is empty")
    else:
        i = stack.pop()
        print("Removed element from stack is: ", i)
        print(stack)

while True:
    print("Select the operation: 1.Push, 2.Pop, 3.Quit")
    choice = int(input("Enter the choice"))
    if choice == 1:
        Push()
    elif choice == 2:
        Pop()
    elif choice == 3:
        break
    else:
        print("Enter correct operation!")