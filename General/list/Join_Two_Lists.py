#Join two Lists
list1 = [1,2,3,4,5,6,7,8]
list2 = [1,2,3]
list3 = list1 + list2
print(list3)

#another one way to do so is
list1 = ["a", "b", "c"]
list2 = [1,2,3]
for x in list2:
    list1.append(x)
print(list1)

#extend() method
list1 = ["A", "B", "C"]
list2 = [1,2,3]

list1.extend(list2)
print(list1)
