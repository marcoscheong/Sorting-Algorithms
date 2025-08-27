def bubble_sort(lst: list):
    for iteration in range(len(lst) - 1): #reduce the number of iterations to length - 1 since there isnt a need for the last iteration
        counter = 0
        for j in range(len(lst) - counter): #number of swapping iterations in each interation
            swap_counter = 1 #swap_counter intialised to 1 during the 1st iteration
            # import pdb; pdb.set_trace()
            if j == len(lst) - counter - 1:
                pass
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp

            else:
                swap_counter += 1 
                if swap_counter == len(lst) - counter:
                    return lst
            counter += 1
    return lst

int_list = [2,1 ,3,32,4,2,3,42,3,2232323,2323,23232324523532,5454]
print(bubble_sort(int_list))
#what if its not a function
#write a tracetable

