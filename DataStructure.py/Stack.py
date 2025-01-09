# Staoc is last in first out
# Stack operations: Push, pop, top, base, empty
# Use case:
# Stack used for reversing string
# Expression evaluation: prefix to postfix and vise versa, infix to prefix
# used for forward and backward features in web browsers
# Used in tower of hanoi algorithm
# Stack implemented by list or module
stack = []
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
