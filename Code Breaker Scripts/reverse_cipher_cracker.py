def decode_user_text () :
    user_text = input("Please enter encoded text: ")
    print(user_text[::-1].replace(" ", ""))

decode_user_text()