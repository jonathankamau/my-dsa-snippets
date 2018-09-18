def binary_search_implementation(number_list, search_item):
    
    list_size = len(number_list) - 1
    
    first_index = 0
    last_index = list_size
    
    while first_index <= last_index:
        midpoint = (first_index + last_index)//2
        
        if number_list[midpoint] == search_item:
            return str(search_item)+' Found at position '+str(midpoint)
        if number_list[midpoint] < search_item:
            first_index = midpoint + 1
        else:
            last_index = midpoint - 1
            
list = [2,4,9,20,40,60,80]
number = int(input('Enter the number you would like to search for: '))
print(binary_search_implementation(list, number))
