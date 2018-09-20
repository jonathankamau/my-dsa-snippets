personal_details = {'Name':'John'}
print('Original Dictionary', personal_details)
personal_details['Phone'] = '0712321564'
personal_details['Location'] = 'Mombasa'

print('Updated dictionary with new key/value pairs', personal_details)

personal_details['Name'] = 'Mary'

print('Updated an existing key with a new value', personal_details)
print('Retrieved a specific value from a key in the dictionary', personal_details['Location'])
