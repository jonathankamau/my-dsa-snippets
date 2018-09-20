def insertion_sort(unsorted_list):
    sorted_list = []
    for index in range(0, len(unsorted_list)):
        number = unsorted_list[index]

        position = index - 1

        while position >= 0 and number < unsorted_list[position]:
            unsorted_list[position + 1] = unsorted_list[position]
            position -= 1
            sorted_list.append(number)

        unsorted_list[position+1] = number


unsorted_list = [90, 10, 20, 56, 800, 89]
insertion_sort(unsorted_list)
print('sorted list = %s' % unsorted_list)
