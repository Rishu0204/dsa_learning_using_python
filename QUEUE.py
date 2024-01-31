#       QUEUE
# Queue operations:
#   1. enqueue(): Adding element
#   2. dequeue(): Removing element

class Queue:
    def __init__(self):
        self.items=[]
    
    def is_Empty(self):
        return len(self.items)==0
    
    def enqueue(self,num):
        self.items.append(num)
    
    def dequeue(self):
        if not self.is_Empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue Empty!!!")

queue=Queue()

print("\t   QUEUE")
print("\n 1. enqueue()")
print("\n 2. dequeue()")

loopCondition=True

while loopCondition:
    choice=int(input("\nEnter your choice (1/2): "))

    if choice==1:
        while True:
            inputQueue=input("\nEnter element you want to enter: ")
            queue.enqueue(inputQueue)
            do_Again=input("\nDo you want to try again (Y/N): ")
            if do_Again.lower() == 'y':
                continue
            elif do_Again.lower()== 'n':
                break
            else:
                raise ValueError("Invalid input!!!")
        print(f" Queue is: {queue.items}")
    
    elif choice ==2:
        while True:
            popped_Element=queue.dequeue()
            print(f"Popped Element: {popped_Element}")
            if queue.is_Empty():
                break
            do_Again=input("\nDo you want to enter again (Y/N): ")
            if do_Again.lower()=="y":
                continue
            elif do_Again.lower()=="n":
                break
            else:
                raise ValueError("Invalid input!!!")
            
        print(f" Queue is: {queue.items}")
        try_again=input("\nDo you want to try again (Y/N): ")
        
        if try_again.lower()=='y':
            loopCondition=True
        elif try_again.lower()=='n':
            loopCondition=False
            break
        else:
            raise ValueError("Invalid input!!!")
    
    else:
        raise ValueError("Invalid input!!!")