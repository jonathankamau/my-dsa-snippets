'''
The selection sort algorithm is also a comparison based algorithm in the list
is divided into two sub-lists, sorted and unsorted sub-lists. The sorted list
appears at the left end of the larger list. It then picks the smallest element
in the list and places it at the beginning of the sorted sub-list. It then
checks for the next smallest element and places it also in the sorted sub-list.
'''


def selection_sort(unsorted_list):
    for index in range(len(unsorted_list)):
        smallest_index = index

        for position in range(index+1, len(unsorted_list)):
            if unsorted_list[smallest_index] > unsorted_list[position]:
                smallest_index = position

        unsorted_list[index], unsorted_list[smallest_index] = (
            unsorted_list[smallest_index], unsorted_list[index])


unsorted_list = [20, 12, 78, 20, 34, 30]
selection_sort(unsorted_list)
print('Sorted list = %s' % unsorted_list)
