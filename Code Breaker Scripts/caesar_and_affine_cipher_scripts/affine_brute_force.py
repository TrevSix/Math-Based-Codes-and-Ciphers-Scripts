DECRYPTED_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def brute_force() :
    MODULO_INVERSE_PAIRS = [3,5,7,9,11,15,17,19,21,23,25]#[3,9,5,21,7,15,11,19,17,23,25]
    encrypted_text = input('Please enter encrypted text: \n')
    encrypted_text = (''.join(char for char in encrypted_text if char.isalpha())).lower()
    file = open('affine.txt', 'w')
    add_key = 0
    
    while add_key < 26:
        for indexi in MODULO_INVERSE_PAIRS :
            encrypted_alphabet = ''
            decrypted_text = ''
            for indexs, _ in enumerate(DECRYPTED_ALPHABET) :
                encrypted_char_index = ((indexs * indexi) + add_key) % 26
                encrypted_alphabet = encrypted_alphabet + DECRYPTED_ALPHABET[encrypted_char_index]
            file.write(f'Multiplicative Key: {indexi},   Additive Key: {add_key},   Encrypted Alphabet: {encrypted_alphabet}\n')

            for indexa, char in enumerate(encrypted_text) :
                encrypted_char_index = list(encrypted_alphabet).index(char)
                decrypted_text = decrypted_text + DECRYPTED_ALPHABET[encrypted_char_index]
            file.write(f'Decrypted Text: {decrypted_text}\n')
        add_key += 1

brute_force()
#Q IMUVOFAN GMOLR RAWANXA FM ZA IQLLAR KDFALLKSADF KJ KF IMOLR RAIAKXA Q BOUQD KDFM ZALKAXKDS FBQF KF GQW BOUQD. QLQD FONKDS. 