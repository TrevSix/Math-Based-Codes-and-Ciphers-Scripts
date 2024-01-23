DECRYPTED_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def brute_force():
    file = open('affine.txt', 'w')
    encrypted_alphabet = ''
    decrypted_text = ''
    add_key = 0
    encrypted_text = (input('Please enter encrypted text: \n')).lower()
    encrypted_text = ''.join(char for char in encrypted_text if char.isalpha())
    while add_key < 26:
        decrypted_text = ''
        encrypted_alphabet = ''
        for index, char in enumerate(DECRYPTED_ALPHABET): 
            encrypted_char_index = index + add_key
            if encrypted_char_index > 25 :
                encrypted_char_index = (encrypted_char_index % 26)
            encrypted_alphabet = encrypted_alphabet + (DECRYPTED_ALPHABET[encrypted_char_index])
        file.write(f'Add Key: {add_key}, Encrypted Alphabet: {encrypted_alphabet}\n')
        for index, char in enumerate(encrypted_text) :
            encrypted_char_index = list(encrypted_alphabet).index(char)
            decrypted_text = decrypted_text + DECRYPTED_ALPHABET[encrypted_char_index]
        file.write(f'Decrypted Text: {decrypted_text}\n')
        add_key += 1

brute_force()
#ZWWUUIBM EIVBML. NWCZ-NQNBG I UWVBP XTCA CBQTQBQMA. UCAB IOZMM BW EQXM LWEV BWQTMB AMIB INBMZ CAM.