# LINKED LIST
# It is a type of data structure which uses pointers which points to the next node

# class to make a node
class Node:

    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

# Linked list class
class LinkedList:
    def __init__(self):     # constructor
        self.head=None
    
    def print(self):        # to print the linked list in string format
        if self.head is None:   # checks if the linked list is empty or not
            print("Linked list is empty")
            return
        itr=self.head   #iterator pointing to the head i.e NULL
        llstr=''    #empty string
        while itr:  # iterating through linked list
            llstr += str(itr.data) + '-->'  if itr.next else str(itr.data)      # append the string with the value of the pointer that it is pointing to
            itr =itr.next       
        print(llstr)
    
    def insert_at_begining(self,data):      #inserting at the begining
        node=Node(data,self.head)       #creating a node 
        self.head=node
    
    def get_length(self):       # for getting the length of the linked list
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    
    def insert_at_end(self,data):   #inserting at the end of linked list
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    
    def insert_at(self,index,data):     # inserting the given node
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index==0:
            self.insert_at_begining(data)
            return
        
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count +=1
    
    def remove_at(self,index):      # removing element at a given index
        if index < 0 or index >= self.get_length():
            raise Exception ("Invalid Index")
        
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count== index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
    
    def insert_values(self,data_list):      #inserting a list of values in linked list
        # self.head=None
        for data in data_list:
            self.insert_at_end(data)


l1=LinkedList()
l1.insert_at_begining(5)
l1.insert_at_begining(10)
l1.insert_at_end(20)
l1.insert_at(1,7)
l1.insert_values([1,4,2,7])
l1.print()
l1.remove_at(2)
l1.print()
