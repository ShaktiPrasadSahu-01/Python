#List Comprehension
''' It provides a shorter syntax when you want to create a new list based on the values of an existing list'''
#witthout list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "Mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

#with list comprehension
newlist = [x for x in fruits if "a" in x]
print(newlist)

#The syntax:-
''' 
newlist = [expression for item in iterable if condition == True] 
'''
# the iterable can be any iterable object, like a list, tuple, set etc.
#the condition can be omitted
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list.

newlist = [x.upper() for x in fruits]
print(newlist)
newlist = ['Hello' for x in fruits]
print(newlist)
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
