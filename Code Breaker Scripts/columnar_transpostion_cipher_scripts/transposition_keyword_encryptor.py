import math

def get_user_text() :
    plain_text = input("Please enter string to be encoded here: \n")
    plain_text = ''.join(char for char in plain_text if char.isalpha())
    key = input("Please enter keyword translated to numbers seperated by spaces here: \n" +
                "i.e: Subtract -> abcrsttu -> 1 2 3 4 5 6 7 8 -> 5 8 2 6 4 1 3 7\n")
    key = list(key.split())
    key_array = []
    for char in key : # turn list(key) into array(int(key_array))
        char = int(char)
        key_array.append(char)
    encrypted_message = encrypt_message(plain_text, key_array) # func call to encryptor function
    encrypted_message = ''.join(char for char in encrypted_message if char.isalpha())
    print(encrypted_message)

def encrypt_message(msg,key): 
    encoded_text = "" # this empty string will be encrypted code
  
    index = 0 # used to control key_array index to know what letter of the keyword the script is on
  
    msg_len = float(len(msg)) # numbers needed to figure out grid size
    msg_list = list(msg) 
    key_list = sorted(list(key)) # turn keyword into sorted list for alphabetical-ish order
  
    col = len(key) # keyword length determins how many columns are needed in the grid
    row = int(math.ceil(msg_len / col))  # (number of characters to be encrypted / num of characters in keyword) rounded up
  
    # add the padding character '_' for empty cells
    padding = int((row * col) - msg_len) # pad empty cells to avoid index out of reach errors, i've learned from my mistakes with the decryptor
    msg_list.extend('_' * padding) # easier way of putting padding characters on the end of str(plain_text)

    # really ugly math boils down to: "make a 2d array with dimensions that meet the requirements from above"
    # and also fill positions with respective letters from list(msg_list) which used to be str(plain_text) 
    matrix = [msg_list[i: i + col]  for i in range(0, len(msg_list), col)] 
  
    for _ in range(col): # for loop takes strips off of the matrix and puts them in the str from before
        curr_idx = key.index(key_list[index]) #curr_idx denotes what letter of the keyword the script is on
        encoded_text += ''.join([row[curr_idx]  for row in matrix]) 
        index += 1
  
    return encoded_text

get_user_text()
