'''
1. get encrypted text
2. get count of each letter
3. rearrange by relative frequency
'''
ENGLISH_LETTER_FREQUENCY = {"E": 12.02, "T": 9.10, "A": 8.12, "O": 7.68, "I": 7.31, "N": 6.95, "S": 6.28, "R": 6.02, "H": 5.92, "D": 4.32, "L": 3.98, "U": 2.88, "C": 2.71, "M": 2.61, "F": 2.30, "Y": 2.11, "W": 2.09, "G": 2.03, "P": 1.82, "B": 1.49, "V": 1.11, "K": 0.69, "X": 0.17, "Q": 0.11, "J": 0.10, "Z": 0.07}

def decrypt(text):
    altered_text = text
    key_of_letters = []
    while_loop_controller = True
    while while_loop_controller:
        menu_option = input("Please enter 'c' to replace a letter or 'r' to revert a letter: \n")
        if menu_option == 'r':
            letter_to_revert = input("Please enter the letter you want to revert: I.E. P -> E, to revert, 'e' \n")
            if letter_to_revert == '' :
                continue
            else:
                for i in range(len(key_of_letters)):
                    if letter_to_revert == key_of_letters[i][1]:
                        original_letter = key_of_letters[i][0]
                        altered_text = altered_text.replace(letter_to_revert, original_letter)
                        key_of_letters.pop(i)
                        print(f'Altered Text: {altered_text}\nKey of Changed Letters: {key_of_letters}')
                        break
                else:
                    print("Letter not found in key.")
        else:
            replacement_letter = input('Please enter letter to replace and replacement letter separated by space: \n')
            if replacement_letter == '':
                continue
            else:
                letter_to_replace, replacement_letter = replacement_letter.capitalize().split()
                altered_text = altered_text.replace(letter_to_replace, replacement_letter.lower())
                key_of_letters.append((letter_to_replace, replacement_letter))
            print(f'Altered Text: {altered_text}\nKey of Changed Letters: {key_of_letters}')



def letter_frequency(text):
    letter_freq = {}
    for letter in text:
        if letter.isalpha() :
            if letter in letter_freq : #if letter is already in our dictionary, increment it's count by one. else, add it to the dict with a count of 1
                letter_freq[letter] += 1
            else:
                letter_freq[letter] = 1
        else :
            continue
    letter_freq = letter_freq
    total_letters = len(text)
    letter_percentage = {}
    for letter, count in letter_freq.items():
        percentage = (count / total_letters) * 100
        percentage = round(percentage, 2)
        letter_percentage[letter] = percentage
    sorted_letter_percentage = dict(sorted(letter_percentage.items(), key=lambda item: item[1], reverse=True)) # gross way to sort letters by highest percentage
    return sorted_letter_percentage 
    # Sort the items of the 'letter_percentage' dictionary by value in descending order, then create a new dictionary from the sorted items. New comment ^^

def main():
    # Get the text to encrypt/decrypt
    text = input("Enter the encrypted text: \n")
    letter_freq = letter_frequency(text)
    print('Relative Frequency Analysis of each letter: %s\n' %(str(letter_freq).replace("\'", "")))
    print('Frequency of Letters in English: %s\n' %(str(ENGLISH_LETTER_FREQUENCY).replace("\'", "")))
    decrypt(text)


main()

'''
NLCCP NUTT IJ U WUAP KRUK IJ ETUXPO SIKR PIWRK TUFWP NUTTJ UBO LBP JAUTTPF KUFWPK LF LNGPCK NUTT CUTTPO U EUTTIBU. KRPFP UFP YLMF NUTTJ EPF KPUA UBO KRPX UFP AUOP LY U OIYYPFPBK CLTLF LF EUKKPFB KL OIJKIBWMIJR KRP NUTTJ LY LBP KPUA YFLA KRLJP LY KRP LKRPF KPUA.
'''