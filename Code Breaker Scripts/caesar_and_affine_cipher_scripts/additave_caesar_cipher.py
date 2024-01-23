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
    encrypted_alphabet = ''
    key = input('Please enter key integer here: \n')
    try:
        key = int(key)
    except:
        print(f'Bad key: {key}')
    for index, char in enumerate(DECRYPTED_ALPHABET) :
        encrypted_char_index = index + key
        if encrypted_char_index > 25 :
            encrypted_char_index = (encrypted_char_index % 26)
        encrypted_alphabet = encrypted_alphabet + (DECRYPTED_ALPHABET[encrypted_char_index])
    return encrypted_alphabet


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