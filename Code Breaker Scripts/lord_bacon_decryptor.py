decryption_dict = {
    '00000' : 'a',
    '00001' : 'b',
    '00010' : 'c',
    '00011' : 'd',
    '00100' : 'e',
    '00101' : 'f',
    '00110' : 'g',
    '00111' : 'h',
    '01000' : 'i/j',
    '01001' : 'k',
    '01010' : 'l',
    '01011' : 'm',
    '01100' : 'n',
    '01101' : 'o',
    '01110' : 'p',
    '01111' : 'q',
    '10000' : 'r',
    '10001' : 's',
    '10010' : 't',
    '10011' : 'u/v',
    '10100' : 'w',
    '10101' : 'x',
    '10110' : 'y',
    '10111' : 'z'
}

def get_user_text () :
    user_text = input("Please input encrypted text: ")
    translate_to_binary(user_text.replace(" ", ""))

def translate_to_binary (user_text) :
    binary_str = []
    user_text = "".join(char for char in user_text if char.isalpha())
    print(user_text)
    index = 0
    for character in user_text :
        if str(user_text[index]).isupper() :
            binary_str.append("1")
        elif str(user_text[index]).isupper() == False:
            binary_str.append("0")
        index = index + 1
    decrypt(binary_str)

def decrypt (binary_str) :
    index = 0
    decrypted_str = []
    binary_list = []
    for character in binary_str :
        binary_list.append(binary_str[index])
        if str(len(binary_list)) == '5' :
            binary_list = "".join(char for char in binary_list if char.isalnum())
            decrypted_str.append(decryption_dict[str(binary_list)])
            binary_list = []
        index = index + 1
    print(decrypted_str)

get_user_text()