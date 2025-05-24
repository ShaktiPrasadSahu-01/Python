#Sort Lists

# Sort List Alphanumericaly , sort()
''' it will sort the list alphanumerically , ascending, by default. '''
thislist = ["Orange", "mango", "Kiwi", "Pineaple", "banana"]
thislist.sort()
print(thislist)

number = [100, 50, 65, 82, 23]
number.sort()
print(number)
# note: sort(reverse = True), sort in descending order

number.sort(reverse = True)
print(number)

# reverse()
''' reverses the current sorting order of the elements.'''
num = [1, 3, 4 , 2, 3, 90, 7 , 6]
num.reverse()
print(num)
