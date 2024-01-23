
def vigenere_cipher_encoder(plain_text, key):
    plain_text = plain_text.upper()
    key = key.upper()
    ciphertext = ""
    index = 0
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            shift = ord(key[index % len(key)]) - 65 #gets ascii value of char to shift by
            char = chr((ord(char) - 65 + shift) % 26 + 65) #add ^^ to ascii value of decrypted char to encrypt <- Old Comment
            index += 1                               #add the value of decrypted character to the encryption value to get encrypted charachter value <- New Comment
        ciphertext += char
    return ciphertext

def vigenere_cipher_decrypter(cipher_text, key):
    cipher_text = cipher_text.upper()
    key = key.upper()
    plaintext = ""
    index = 0
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        if char.isalpha():
            shift = ord(key[index % len(key)]) - 65 #get ascii value of char to shift by
            char = chr((ord(char) - 65 - shift + 26) % 26 + 65) #subtract ^^ from ascii value of encrypted char to get decrypted char
            index += 1
        plaintext += char
    return plaintext

def main() :
    menu_opt = input("Enter 'e' to encrypt or 'd' to decrypt: \n")
    if menu_opt == 'e' :
        plain_text = input('Enter Plain Text Here: \n')
        key = input('Enter key here: \n')
        print('Encrypted Text: ' + vigenere_cipher_encoder(plain_text, key))
    elif menu_opt == 'd' :
        cipher_text = input('Enter cipher text here: \n')
        key = input('Enter key here: \n')
        print('Decrypted Text: ' + vigenere_cipher_decrypter(cipher_text, key))
    else: 
        print(f'Bad Menu Option: {menu_opt}')

main()
'''
A polyalphabetic substitution is a cipher in which the alphabet changes from letter to letter during encryption
'''