def merge_sort(arr):

    #Handle the base case.
    if len(arr) <= 1:
        return arr

    #Split the array into left and right subarrays
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]    #WHY DOES PSEUDOCODE SAY MID + 1
    # print(left,right) 
    
    #Recursively sort each subarray.
    left = merge_sort(left)
    right = merge_sort(right)
    # print(left,right)
    
    # Merge the subarrays into a sorted array.
    sorted_array = merge(left, right)

    return sorted_array

def merge(left: list, right: list):
    p1 = 0 #pointer 1 (left)
    p2 = 0 #pointer 2 (right)
    sorted_array = []

    while p1 < len(left) and p2 < len(right):

        if left[p1] <= right[p2]:
            sorted_array.append(left[p1])
            p1 += 1

        else:
            sorted_array.append(right[p2])
            p2 += 1
    
    return sorted_array




print(merge_sort([13,244,24,89]))