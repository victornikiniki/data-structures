lst = [2, 3, 4, 2, 5, 6, 7, 2, 9, 10, 11, 45, 23, 87, 2, 3, 5, 6]

def bubble_sort(unsorted_list): 
    is_sorted = False

    while not is_sorted: 
        is_sorted = True 

        for i in range(0, len(unsorted_list) - 1):
            if unsorted_list[i] > unsorted_list[i+1]:
                is_sorted = False
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]

    return unsorted_list

print(bubble_sort(lst))