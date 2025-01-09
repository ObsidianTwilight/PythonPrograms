# Queue is first in first out structure
# Insertion and deletion are from opposite end
# Operations:
# Enqueue: Adding the element in queue -> append method
# Dequeue: Deleting the element from queue-> pop method and  index(delete item)
# Check condition: isfull or not isEmpty or not.
# Appliction: Uploading multiple impages, printing multiple documents etc.
# We can implement queue in Lists
Queue = [5]
def Enqueue():
    item = input("Enter the element\t")
    Queue.append(item)
    print(Queue)

def Dequeue():
    if Queue is None:
        print("Queue is empty")
    else:
        i = Queue.pop(0)
        print("Deleted element from queue is:", i)
        print(Queue)

def display():
    print(Queue)

while True:
    choice = int(input("Enter the choice -> 1.Enqueue, 2.Dequeue, 3.display, 4.Quit\t"))
    if choice == 1:
        Enqueue()
    elif choice == 2:
        Dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Enter correct option!")
