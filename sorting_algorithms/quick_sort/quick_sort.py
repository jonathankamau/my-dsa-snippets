'''
Quick sort algorithm is a divide and conquer algorithm that partitions a list 
into two smaller lists then calls itself recursively to sort the resulting 
lists.
'''


def quick_sort_helper(unsorted_list, first_index, last_index):
    if first_index < last_index:
        split_point = partition(unsorted_list, first_index, last_index)

        quick_sort_helper(unsorted_list, first_index, split_point - 1)
        quick_sort_helper(unsorted_list, split_point + 1, last_index)


def partition(unsorted_list, first_index, last_index):
    pivot = unsorted_list[first_index]
    left_item_position = first_index + 1
    right_item_position = last_index

    done = False
    while not done:
        while (left_item_position <= right_item_position and
               unsorted_list[left_item_position] <= pivot):
            left_item_position = left_item_position + 1

        while (unsorted_list[right_item_position] >= pivot and
               right_item_position >= left_item_position):
            right_item_position = right_item_position - 1

        if right_item_position < left_item_position:
            done = True
        else:
            temp = unsorted_list[left_item_position]
            unsorted_list[
                left_item_position] = unsorted_list[right_item_position]
            unsorted_list[right_item_position] = temp

    temp = unsorted_list[first_index]
    unsorted_list[first_index] = unsorted_list[right_item_position]
    unsorted_list[right_item_position] = temp

    return right_item_position


def quick_sort(unsorted_list):
    quick_sort_helper(unsorted_list, 0, len(unsorted_list)-1)


unsorted_list = [90, 10, 20, 56, 800, 89]
quick_sort(unsorted_list)
print('sorted list = %s' % unsorted_list)
