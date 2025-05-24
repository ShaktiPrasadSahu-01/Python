#Copy Lists
'''
list2 = list1 , it is wrong, for copying list1 to list2
beacuse it will only be a reference to list1, and changes made in list1 will automatically also be made in list2
'''

#copy(), we can use this built in method to copy a list

num = [1, 2 , 3 , 5 ,6 ,7 , 9]
num01 = num.copy()
print(num01)

#list()

num02 = list(num)
print(num02)

#using : (slice) operator
num03 = num[:]
print(num)
