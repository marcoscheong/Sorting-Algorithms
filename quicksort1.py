def quicksort(lst):

# def quicksort(lst):
    # Handle the base case.
    if len(lst) <= 1:
        return lst
    
    # Select a pivot.
    pivot = lst.pop() #pop() without any argument removes last element

    # Split remaining elements into less-than-equal and greater-than subarrays by comparing them with the pivot.
    gt_lst = []
    lte_lst = []
    for elem in lst:
        if elem < pivot:
            lte_lst.append(elem)
        else:
            gt_lst.append(elem)
    
    # Recursively sort the subarrays
    left = quicksort(lte_lst)
    right = quicksort(gt_lst)

    # Concatenate the less-than subarray, pivot, and greater-than-or-equal subarrays.
    return left + [pivot] + right

num_list = [6, 7, 3, 4, 2, 1, 5]
print(quicksort(num_list))