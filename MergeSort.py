def mergesort(arr: list):
    """sorts an array using merge sort algorithm"""

    #handle base case

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_arr = mergesort(left)
    right_arr = mergesort(right)

    sorted_arr = merge(left_arr, right_arr)

    return sorted_arr

def merge(left_arr, right_arr):
    sorted_arr = []
    
    while len(left_arr) > 0 and len(right_arr) > 0:
        if left_arr[0] < right_arr[0]:
            sorted_arr.append(left_arr.pop(0))
        else:
            sorted_arr.append(right_arr.pop(0))

    return sorted_arr + left_arr + right_arr

print(mergesort([3,2,1]))

