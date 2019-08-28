'''
Merge sort is termed as a divide and conquer algorithm which divides the list 
into equal halves, sorts them then combines them. It keeps dividing the list 
into equal halves then it combines the smaller sorted lists while keeping then 
in a sorted order. The efficiency is O(n log(n))
'''


def split(unsorted_list):
    unsorted_list_length = len(unsorted_list)
    midpoint = unsorted_list_length // 2
    return unsorted_list[:midpoint], unsorted_list[midpoint:]


def merge_sorted_lists(left_list, right_list):
    if len(left_list) == 0:
        return right_list
    elif len(right_list) == 0:
        return left_list
    
    left_index = right_index = 0
    merged_list = []
    final_list_length = len(left_list) + len(right_list)
    
    while len(merged_list) < final_list_length:
        if left_list[left_index] <= right_list[right_index]:
            merged_list.append(left_list[left_index])
            left_index += 1
        else:
            merged_list.append(right_list[right_index])
            right_index += 1
        
        if right_index == len(right_list):
            merged_list += left_list[left_index:]
            break
        elif left_index == len(left_list):
            merged_list += right_list[right_index:]
            break
    
    return merged_list


def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    else:
        left, right = split(unsorted_list)
        return merge_sorted_lists(merge_sort(left), merge_sort(right))


unsorted_list = [90, 10, 20, 56, 800, 89]
print('sorted list = %s' % merge_sort(unsorted_list))
