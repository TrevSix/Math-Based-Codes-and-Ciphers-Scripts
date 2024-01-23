

def get_user_text () : #gets user text and removes all special characters including spaces excluding nums
    user_text = input("Please enter entextd text: ")
    user_text = "".join(char for char in user_text if char.isalnum())
    shift_printer(user_text)

def shift_printer (user_text) :
    index = 0
    key = 0
    file = open("skip_cipher.txt", "w")
    decrypted_text = "Nth letter where n = " + str(key + 1) + " is: " + "\n"

    while key < len(user_text) - 1 :
        if key == 0 :
            decrypted_text += user_text
        file.write("" + decrypted_text + "\n")
        key += 1
        index = 0
        decrypted_text = "Nth letter where n = " + str(key + 1) + " is: " + "\n"
        while index < len(user_text) - key:
            index += key 
            decrypted_text += user_text[index]
            index += 1


get_user_text()