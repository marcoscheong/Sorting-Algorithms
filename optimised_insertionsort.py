def insertion_sort(lst):
    for i in range(2, len(lst)):
        target = lst[i]
        j = i - 1
        while j > 0 and lst[j] > target:
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j + 1] = target
    
    return lst
    

int_list = [1,2323,323,2132332432432,4324,23432432432432,4324,32432,42432432432,234233423422343]
print(insertion_sort(int_list))