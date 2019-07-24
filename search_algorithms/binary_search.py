'''
This algorithm makes use of the "divide and conquer" principle and for it to work the data collection has to be in sorted form. 
It locates the midpoint of the data collection, then from the index it compares the middle value with the search item to determine the location of the item. 
It ends up returning the position of the item. This search method is much faster than linear search. 

Binary search has a best case eficiency of 0(1) and worst case efficiency of 0(log n).
How the worst case efficiency gets derived is in a case where for instance to search for an element in a sorted list of 16 elements
you would have to divide that list 4 times, so the equation becomes
16 * (1/2)power of 4 = 1
so for n elements it will be n * (1/2)power of k = 1
which equates to n = 2 to the power of k
'''
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
