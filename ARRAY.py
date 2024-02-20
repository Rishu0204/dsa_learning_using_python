# Array or list in python is a list of any data type stored within '[]'

# Array declaration
#Method 1 
a=[]
a.append("apple")
a.append(2)
a.append("orange")
print(a)

#Method 2
b=["apple",2,"orange"]
print(b)

# Retriving data from a array
# we can use indexing to retrive data from array
# In arrays index starts from 0

print(a[0])
print(b[1])

# inserting element in list
# We use two functions for this:
#   1. insert(): inserts element of the desired index
#   2. append(): inserts element of the last of list

a.insert(0,1)
b.append("yellow")
print(a,b)

# for removing or deleting elements from the list
#   1. remove(): remeove element from the desired index
#   2. pop(): remove the last element of the list

a.pop()
b.pop()
print(a,b)