'''
This is a sorting algorithm that repeatedly checks adjacent elements and if 
they are not in order it swaps them. 
This is done through multiple passes on a list. For each iteration, the 
largest element in the array will "bubble" to the top. 
The efficiency or worst case  of this algorithm is O(nˆ2). This is however 
considered not to be a practical sorting algorithm.
'''


def bubble_sort(list):
    for iterated_numbers in range(len(list)-1, 0, -1):
        for index in range(iterated_numbers):
            if list[index] > list[index+1]:
                temp = list[index]
                list[index] = list[index+1]
                list[index+1] = temp


list = [100, 20, 34, 10, 89, 90, 40, 30, 120]
bubble_sort(list)
print('sorted list =%s' % list)
