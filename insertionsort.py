def insertion_sort(arr):
    n = len(arr)
    
    # We start from 1 since the first element is trivally sorted
    for i in range(1,n):
        target = arr[i]
        j = i - 1

        #compare key with each element on the left of it until an element smaller than it is found  
        #For descending order, change arr[j] . target to arr[j] < target.
        while j >= 0 and arr[j] > target:
            arr[j + 1] = arr[j]
            j = j - 1

            #Place key at the element just smaller than it
            arr[j + 1] = target
    
    return arr
            

