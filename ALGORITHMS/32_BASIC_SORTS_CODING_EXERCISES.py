def bubble_sort(my_list):
    for i in range(len(my_list) -1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp

    return my_list


def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        # compare all elements after i 
        # to find another smallest element
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:        
            # swap the items
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp

    return my_list 


def insertion_sort(my_list):
    # start from 2nd item in the list
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1

        # j = -1 means we reached the beginning of array, stop
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1

    return my_list



