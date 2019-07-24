array = [3,5,1,2,9,8]

def linear_search(num):
    
    for index in range(0, len(array)):
        if array[index] == num:
            number = array[index]

    return number

print(linear_search(8))

