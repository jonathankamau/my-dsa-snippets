def make_heap(list_of_values, n, index):
    largest = index
    left_child_index = 2 * index + 1
    right_child_index = 2 * index + 2

    if (left_child_index < n and list_of_values[index]      
            < list_of_values[left_child_index]):

        largest = left_child_index

    if (right_child_index < n and list_of_values[largest] 
            < list_of_values[right_child_index]):

        largest = right_child_index

    if largest != index:
        list_of_values[index], list_of_values[largest] = (
            list_of_values[largest], list_of_values[index])

        make_heap(list_of_values, n, largest)


def heap_sort(list_of_values):
    n = len(list_of_values)

    for index in range(n, -1, -1):
        make_heap(list_of_values, n, index)

    for index in range(n-1, 0, -1):
        list_of_values[index], list_of_values[0] = (
            list_of_values[0], list_of_values[index])

        make_heap(list_of_values, index, 0)


list_of_values = [400, 1, 29, 90, 12, 4, 78, 100, 90]
heap_sort(list_of_values)
print('Sorted array is %s' % list_of_values)
