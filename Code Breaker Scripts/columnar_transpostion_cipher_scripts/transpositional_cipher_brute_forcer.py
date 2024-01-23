import math

def get_user_text () :
    encrypted_text = input("Please enter encrypted text here: \n")
    encrypted_text = ''.join(char for char in encrypted_text if char.isalpha())
    decrypted_text = (decrypt(encrypted_text))
    

def decrypt(encrypted_text) :
    file = open("transpositional_cipher.txt", "w")
    key = 1
    while key <= len(encrypted_text) :
        num_of_columns = int(math.ceil(len(encrypted_text) / float(key)))
        num_of_rows = int(key)
        num_of_blocked_boxes = (num_of_columns * num_of_rows) - len(encrypted_text)
        key += 1

        
        decrypted_text = [''] * num_of_columns
        row = 0
        column = 0

        for char in encrypted_text :
            decrypted_text[column] += char
            column += 1

            if (column == num_of_columns) or (column == num_of_columns - 1 and row >= num_of_rows - num_of_blocked_boxes) :
                column = 0
                row += 1
        decrypted_text = "".join(char for char in decrypted_text if char.isalpha())
        file.write( "Key of " + str(key - 1) + ":" + str(decrypted_text) + "\n")
        

get_user_text()