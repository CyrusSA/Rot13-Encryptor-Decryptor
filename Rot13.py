def rotted_elem(element): #getting the alphabet 13 places down
    val = ord(element)
    rotted_val = val+13
    if element.isupper() == True and rotted_val>90:
        rotted_val = 65+(rotted_val-91)
    elif element.islower() == True and rotted_val>122:
        rotted_val = 97+(rotted_val-123)
    rotted_elem = chr(rotted_val)
    return rotted_elem
    
def rot(input_string): #replacing each alphabet with the rotted one
    list_char=[]
    rotted_list_char=[]
    output_string=''
    for element in input_string:
        list_char.append(element)
    for element in list_char:
        if element.isalpha()==True:
            rotted_list_char.append(rotted_elem(element))
        else:
            rotted_list_char.append(element)
    for element in rotted_list_char:
        output_string+=element
    return output_string

print('Welcome to the Rotter')

while True:
    input_string = input('Please enter the string to be encoded: ')
    print("Rotted string: " + rot(input_string))
    print()
    
    
