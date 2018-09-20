def selection_sort(unsorted_list):
    for index in range(len(unsorted_list)):
        smallest_index = index

        for position in range(index+1, len(unsorted_list)):
            if unsorted_list[smallest_index] > unsorted_list[position]:
                smallest_index = position

        unsorted_list[index], unsorted_list[smallest_index] = (unsorted_list[smallest_index], unsorted_list[index])


unsorted_list = [20, 12, 78, 20, 34, 30]
selection_sort(unsorted_list)
print('Sorted list = %s' % unsorted_list)
