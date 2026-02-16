lst = [2, 3, 4, 2, 5, 6, 7, 2, 9, 10, 11, 45, 23, 87, 2, 3, 5, 6]

def bubble_sort(reyna):
    is_sorted = False 
    indexing_length = len(reyna) - 1

    while not is_sorted: 
        is_sorted = True 

        for i in range(0, indexing_length): 
            if reyna[i] > reyna[i+1]: 
                is_sorted = False 
                reyna[i], reyna[i+1] = reyna[i+1], reyna[i]

    return reyna

print(bubble_sort(lst))