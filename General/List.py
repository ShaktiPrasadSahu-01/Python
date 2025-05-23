#Change Lists 
"""
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrent"
print(thislist) 

"""

#change a range of item Values
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

"""
""" 

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

"""

#Insert Items
""" 
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
"""

#Add List items:-
#append()
thislist = ["a", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#insert()
thislist.insert(1, "hello world")
print(thislist)

#extend() , it will append elements from another list to the current list, use the extend(). This method does not have to appendlist, we can add any iterable object(tuples, sets, dictionaries etc.)

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

summer = ("kiwi", "Orange")
thislist.extend(summer)
print(thislist)


#Remove List Items:-
'''
remove():- removes the specified item
pop():- removes the specified index. If does not specfie index , removes the last elements
del :- also delete the specified index. If index does not specified , it delete the list completely

clear():- empties the list


'''
'''
thislist.remove("banana")
print(thislist)
thislist.pop(1)
print(thislist)
thislist.pop()
print(thislist)
del thislist[0]
print(thislist)
thislist01 = thislist
del  thislist01
#print(thislist01)
thislist02 = thislist
thislist02.clear()
print(thislist02)
'''

#Looping using List comprehensi
[print(x) for x in thislist]

