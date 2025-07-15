def bubble_sort(lst: list):
    for i in range(len(lst)):
        counter = 1
        for j in range(len(lst) - counter):
            print(i,  j, lst)
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
                counter += 1
            counter += 1
    return lst

int_list = [2,1 ,3,32,4,2,3,42,3,2232323,2323,23232324523532,5454]
print(bubble_sort(int_list))
#what if its not a function
#write a tracetable

