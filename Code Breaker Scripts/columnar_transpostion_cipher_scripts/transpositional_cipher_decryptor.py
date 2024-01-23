import math

def get_user_text () :
    encrypted_text = input("Please enter encrypted text here: \n")
    encrypted_text = ''.join(char for char in encrypted_text if char.isalpha())
    key = input("Please enter key here: \n")
    decrypted_text = (decrypt(key, encrypted_text))
    print(decrypted_text)

def decrypt(key, encrypted_text) :
    num_of_columns = int(math.ceil(len(encrypted_text) / float(key)))
    num_of_rows = int(key)
    num_of_blocked_boxes = (num_of_columns * num_of_rows) - len(encrypted_text)

    decrypted_text = [''] * num_of_columns
    row = 0
    column = 0

    for char in encrypted_text :
        decrypted_text[column] += char
        column += 1

        if (column == num_of_columns) or (column == num_of_columns - 1 and row >= num_of_rows - num_of_blocked_boxes) :
            column = 0
            row += 1
    
    return ''.join(decrypted_text)

get_user_text()