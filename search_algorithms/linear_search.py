class LinearSearch:
    def __init__(self, numbers, search_item):
        self.number_list = number_list
        self.number = search_item
        self.output = self.linear_search_implementation(numbers)

    def create_number_list(self, numbers):
        number_list = list(map(int, self.number_list.split(',')))
        return number_list

    def linear_search_implementation(self, numbers):
        number_list = self.create_number_list(numbers)
        result = ''

        for position in range(0, len(number_list)):
            
            if self.number == number_list[position]:
               
                result += str(self.number)+" Found in position "+str(position)
                break
    
            else:
                result = "Number not Found! Please try again!"
          
        return result


number_list = input('Enter the numbers for the list seperated by a comma: ')
search_item = int(input('Enter the number you would like to search for: '))
result = LinearSearch(number_list, search_item)
print(result.output)
