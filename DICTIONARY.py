# DICTIONARY

#Dictionary creation
dict={'name':'Rishu', 'age':19}
print(dict,"\n")

#accessing keys
print(dict.keys(),"\n")

#accessing values
print(dict.values(),"\n")

#items in dictionary
print(dict.items(),"\n")

#get function: checks whether key is present in dictionary or not if not present gives desired message
print(dict.get('email','not found!!!'),"\n") 

#adding elements in dictionary
dict['dob']='2004/02/22'
print(dict,"\n")

#pop in dictionary
print("pop element: ",dict.pop('dob'),"\n")

#iterating in dictionary
for i in dict.items():
    print(i)

#storing multiple data,i.e. dictionary inside dictionary
dict1={1:{'name':'abc', 'age':20},
       2:{'name':'def', 'age':19},
       3:{'name':'qwe', 'age':22}}
print("")
for i in dict1.items():
    print(i)

#asking user for n input
myDict={}
while True:
    key=input("Enter a key: ")
    value = input("Enter the value for key: ")
    myDict[key]=value
    choice=input("Do you want to enter another key-value pair (yes or no): ")
    if choice.lower()!='yes' or choice.lower()!='y':
        break
print(myDict)