def bubblesort(arr: list) -> list:
    """sorts an array in-place using bubble sort algorithm"""
    n = len(arr)

    #in the event that there is 0/1 element in an array, there is no necessity to sort
    #and we can simply return the array as is. (BASE CASE)

    if n <= 1:
        return arr
    
    #Optimisation 1: we can skip the final (outer) loop by reducing n to n - 1
    for i in range(n - 1):
        swapped = False

        #Optimisation 2: Skip sorted elements (the ones on the right)
        for j in range(n - i - 1):
            #traverse the array from 0 to n - 2
            #swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

                swapped = True

        #OPTIMISATION 3
        if not swapped:
            return arr
    
    return arr

print(bubblesort([3,2,1]))

    