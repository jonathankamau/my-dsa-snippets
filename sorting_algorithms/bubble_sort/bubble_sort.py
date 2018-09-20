def bubble_sort(list):
    for iterated_numbers in range(len(list)-1, 0, -1):
        for index in range(iterated_numbers):
            if list[index] > list[index+1]:
                temp = list[index]
                list[index] = list[index+1]
                list[iindex+1] = temp


list = [100, 20, 34, 10, 89, 90, 40, 30, 120]
bubble_sort(list)
print(list)