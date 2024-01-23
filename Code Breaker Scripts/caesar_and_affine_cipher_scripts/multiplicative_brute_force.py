DECRYPTED_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
MODULO_INVERSE_PAIRS = [3,9,5,21,7,15,11,19,17,23,25,25]

def brute_force():
    file = open('affine.txt', 'w')
    encrypted_alphabet = ''
    decrypted_text = ''
    while_loop_controller = 0
    decrypted_alphabet_index = 0
    encrypted_text = (input('Please enter encrypted text: \n')).lower()
    encrypted_text = ''.join(char for char in encrypted_text if char.isalpha())
    while while_loop_controller < len(MODULO_INVERSE_PAIRS):
        decrypted_text = ''
        encrypted_alphabet = ''
        for index, char in enumerate(DECRYPTED_ALPHABET): 
            encrypted_char_index = index * MODULO_INVERSE_PAIRS[while_loop_controller]
            if encrypted_char_index > 25 :
                encrypted_char_index = (encrypted_char_index % 26)
            encrypted_alphabet = encrypted_alphabet + (DECRYPTED_ALPHABET[encrypted_char_index])
        file.write(f'Mult Key: {MODULO_INVERSE_PAIRS[while_loop_controller]}, Encrypted Alphabet: {encrypted_alphabet}\n')
        for index, char in enumerate(encrypted_text) :
            encrypted_char_index = list(encrypted_alphabet).index(char)
            decrypted_text = decrypted_text + DECRYPTED_ALPHABET[encrypted_char_index]
        file.write(f'Decrypted Text: {decrypted_text}\n')
        while_loop_controller += 1

brute_force()
#FKWFVK QLW PLUNM PLKI MNWQ KHKXIPLUNC AXK A CXKAP ANNWIANSK PW PLWGK WT YG QLW BW.