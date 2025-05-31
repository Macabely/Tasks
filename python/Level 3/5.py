list1 = [-20, 50, 100, -56, -4, 2, 15, 23]
list2 = []
while list1:
    t = list1[0]
    for x in list1:
        if x < t:
            t = x
    list2.append(t)
    list1.remove(t)
print(list2)            