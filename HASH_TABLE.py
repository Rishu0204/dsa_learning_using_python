# HASH MAPPING

# defing class HashTable

class HashTable:
    def __init__(self):
        self.size=20        # size of the table
        self.table=[0]* self.size    #initially none in all the indexes

    def hash_function(self,key):        # for generating hash functions
        h=0
        for char in key:        # using the ASCII values
            h+=ord(char)
        return h% self.size     # generating hash key

    def __setitem__(self,key,val):      # adding into hash table 
        h=self.hash_function(key)
        self.table[h]=val
    
    def __getitem__(self,key):      #retriving from the hash table
        h=self.hash_function(key)
        return self.table[h]
    
    def __delitem__(self,key):      # deleting from hash table
        h=self.hash_function(key)
        self.table[h]=0
ht=HashTable()
ht["1"]=1200
ht["5"]=5656
ht["march 2"]=873458
ht["7373"]=874538
print(ht["1"])
print(ht.table)

print("Removing ",ht["5"])
del ht['5']
print(ht.table)

