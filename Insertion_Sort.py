list1 = [3, 41, 12, 9, 74, 15]

for iterav in range(1, len(list1)):
    key = list1[iterav]
    j = iterav - 1

    while j >= 0 and key < list1[j]:
        list1[j+1] = list1[j]
        j = j-1
    
    list1[j+1] = key

print(list1)

# for ine in range(1, len(list1)):
#     print(ine)