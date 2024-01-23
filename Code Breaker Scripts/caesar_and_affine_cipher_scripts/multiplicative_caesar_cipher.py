import sys

DECRYPTED_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def user_input() :
    user_input = input("Please enter -e to encrypt or -d to decrypt: \n")
    encrypted_alphabet = get_encrypted_alphabet()
    print(f'Decrypted Alphabet: {DECRYPTED_ALPHABET} \nEncrypted Alphabet: {encrypted_alphabet}')
    if user_input == '-e' :
        encrypt(encrypted_alphabet) 
    elif user_input == '-d' :
        decrypt(encrypted_alphabet)
    else:
        print(f'Bad menu selection: {user_input}')
        sys.exit()


def get_encrypted_alphabet() :
    key = input('Please enter key here: \n')
    encrypted_alphabet = ''
    MODULO_INVERSE_PAIRS = [3,9,5,21,7,15,11,19,17,23,25,25] #3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25
    try :
        key = int(key)
    except:
        print(f'Key is not an integer: {key}')
        sys.exit()
    if MODULO_INVERSE_PAIRS.index(key) :   
        for index, char in enumerate(DECRYPTED_ALPHABET) :
            encrypted_char_index = index * (key % 26)
            if encrypted_char_index > 25 :
                encrypted_char_index = (encrypted_char_index % 26)
            encrypted_alphabet = encrypted_alphabet + (DECRYPTED_ALPHABET[encrypted_char_index])
        return encrypted_alphabet
    else:
        print(f'Key is not a modulo inverse pair: {key}')
        sys.exit()

def encrypt(encrypted_alphabet) :
    decrypted_text = input('Please enter text to be encrypted here: \n').lower()
    encrypted_text = ''
    for index, char in enumerate(decrypted_text) : 
        if decrypted_text[index][0] in DECRYPTED_ALPHABET : 
            decrypted_char_index = list(DECRYPTED_ALPHABET).index(char)
            encrypted_text = encrypted_text + encrypted_alphabet[decrypted_char_index] 
    print(f'Encrypted text: {encrypted_text}')

def decrypt(encrypted_alphabet) :
    encrypted_text = input('Please enter text to be decrypted here: \n').lower()
    decrypted_text = ''
    for index, char in enumerate(encrypted_text) :
        if encrypted_text[index][0] in DECRYPTED_ALPHABET :
            encrypted_char_index = list(encrypted_alphabet).index(char)
            decrypted_text = decrypted_text + DECRYPTED_ALPHABET[encrypted_char_index]
    print(f'Decrypted text: {decrypted_text}')

user_input()