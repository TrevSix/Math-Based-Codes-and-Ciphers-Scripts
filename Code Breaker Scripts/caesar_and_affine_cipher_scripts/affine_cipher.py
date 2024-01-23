import math
import sys

DECRYPTED_ALPHABET = 'abcdefghijklmnopqrstuvwxyz' #change this if special chars are needed or to change alphabet

def user_input() :
    user_answer = input('Please enter -e for encrypt or -d for decrypt\n') # self explanetory menu. minamal error handling
    encrypted_alphabet = get_encrypted_alphabet()
    if user_answer == '-e' :
        encrypt(encrypted_alphabet)
    elif user_answer == '-d':
        decrypt(encrypted_alphabet)
    else :
        print(f'Bad menu selection: {user_answer}')
        sys.exit()

def get_encrypted_alphabet() :
    encrypted_alphabet = '' #temp string to build encrypted alphabet 
    multiplicative_key = 0 # these two integer variables must be set to a default value so they both exist for the try catch statement below
    additave_key = 0
    MODULO_INVERSE_PAIRS = [3,9,5,21,7,15,11,19,17,23,25,25]
    key = input('Please enter key or -o to enter multiplicative and additive keys manually: \n') #submenu that gives option to enter raw int or enter both end values
    if key == '-o' :
        multiplicative_key = input('Please enter multiplicative key: ')
        additave_key = input('Please enter additave key: ')
    else:
        key = int(key) 
        if key < 26 :
            additave_key = key % 26
            multiplicative_key = 1
        else:
            multiplicative_key = int((key) / 26) #math. gross! basically boils down to key / 26 without decimal = mult key
            additave_key = math.ceil(((key / 26) - multiplicative_key) * 26) # (key / 26) - whole number * 26 = add key

    try:
        multiplicative_key = int(multiplicative_key) # makes sure user hasnt entered any funcky values
        additave_key = int(additave_key) #also, only useful for manual key entry option. algorithmic math already turns both variables into integers
    except:
        print('Bad key format.') # some error handling because im feeling nice.
        sys.exit() #heh, goofy. kills script so user can try again. somewhere along the way user failed to read instructions.

    if multiplicative_key in MODULO_INVERSE_PAIRS:
        print(f'multiplicative key: {multiplicative_key}\nadditave key: {additave_key}') #WEEEEEE!!!!! Mult and Add keys.
        for index, _ in enumerate(DECRYPTED_ALPHABET) : # im pretty sure using enumerate here is useless, but i just learned it and wanted to use it.
            encrypted_char_index = ((int(index) * int(multiplicative_key)) + int(additave_key)) % 26 #math. still gross. basically get index of encrypted char
            encrypted_alphabet = encrypted_alphabet + DECRYPTED_ALPHABET[encrypted_char_index] 
        print(f'Decrypted Alphabet: {DECRYPTED_ALPHABET} \nEncrypted Alphabet: {encrypted_alphabet}') #WEEEEE!!! Plain text and cipher text table
        return encrypted_alphabet
    else:
        print(f'Multiplicative key not in modulo inverse pair: {multiplicative_key}')
        sys.exit()


def encrypt(encrypted_alphabet) :
    decrypted_text = input('Please enter text to be encrypted here: \n').lower()
    encrypted_text = ''
    for index, char in enumerate(decrypted_text) : #enumerate function is actually useful here, but i think it might just be list() in another form. a weed by any other name and all that jazz.
        if decrypted_text[index][0] in DECRYPTED_ALPHABET : #decrypted_text[index][0] = current char of decrypted text. if char in decrypted text is in alphabet...
            decrypted_char_index = list(DECRYPTED_ALPHABET).index(char) # ...do this, lol. turn const(DECRYPTED_ALPHABET) into list and find the index that char is at.
            encrypted_text = encrypted_text + encrypted_alphabet[decrypted_char_index] #add the encrypted char at the index of the decrypted char to our string. yay
    print(f'Encrypted text: {encrypted_text}') # Voila, final product.

def decrypt(encrypted_alphabet) : # do everything in the function above, but in reverse. kek dub.
    encrypted_text = input('Please enter text to be decrypted here: \n').lower()
    decrypted_text = ''
    for index, char in enumerate(encrypted_text) :
        if encrypted_text[index][0] in DECRYPTED_ALPHABET :
            encrypted_char_index = list(encrypted_alphabet).index(char)
            decrypted_text = decrypted_text + DECRYPTED_ALPHABET[encrypted_char_index]
    print(f'Decrypted text: {decrypted_text}')

user_input()
#had to put something on this line for obvious reasons.
#Q IMUVOFAN GMOLR RAWANXA FM ZA IQLLAR KDFALLKSADF KJ KF IMOLR RAIAKXA Q BOUQD KDFM ZALKAXKDS FBQF KF GQW BOUQD. QLQD FONKDS. 