# STACK

# Approach : Last in First Out (LIFO)

# STACK FUNCTIONS:
#   1.peek()
#   2.push()
#   3.pop()

class Stack():
    
    def __init__(self):
        self.items=[]   # creating instance variable 'items'
    
    def is_Empty(self): # checking if the stack is empty or not
        return len(self.items)==0   #if empty returns true else false
    
    def push(self,num): # stack push() function
        self.items.append(num)
    
    def pop(self):  # stack pop() function
        if not self.is_Empty(): # checks if list is empty or not
            return self.items.pop()    # if not empty pop element
        else:
            raise IndexError("Stack Empty!!!")  # if empty raises error
    
    def peek(self): # stack peek() function
        if not self.is_Empty(): # checks if list is empty or not
            return self.items[-1]   # returns top-most element
        else:
            raise IndexError("Stack Empty!!!")  # if empty raises error
    
stack=Stack()

print("     STACK       ")
print("\nOperations")
print("\n  1.push()")
print("\n  2.pop()")
print("\n  3.peek()")

loopCondition=True
while loopCondition:
    choice= int(input("\nEnter your choice (1/2/3): "))
    if choice == 1:
        while True:
            element=int(input("Enter element to enter in stack: "))
            stack.push(element)
            do_Again=input("Do you want to enter again (Y/N): ")
            if do_Again.lower()=="y":
                continue
            elif do_Again.lower()=="n":
                break
            else:
                raise ValueError("Invalid input!!!")
        
        print(f" Stack is: {stack.items}")
        
    elif choice==2:
        while True:
            popped_Element=stack.pop()
            print(f"Popped Element: {popped_Element}")
            if stack.is_Empty():
                break
            do_Again=input("Do you want to enter again (Y/N): ")
            if do_Again.lower()=="y":
                continue
            elif do_Again.lower()=="n":
                break
            else:
                raise ValueError("Invalid input!!!")
            
        print(f" Stack is: {stack.items}")

    elif choice == 3:
        top_Element = stack.peek()
        print(f"Top-most Element: {top_Element}")
        

        try_again=input("Do you want to enter again (Y/N): ")
        
        if try_again.lower()=='y':
            loopCondition=True
        elif try_again.lower()=='n':
            loopCondition=False
            break
        else:
            raise ValueError("Invalid input!!!")