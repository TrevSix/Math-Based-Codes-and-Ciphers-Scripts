def decrypt(encrypted_text, modulus, exponent):
    decrypted_text = ""
    num = int(encrypted_text, 16)
    key = pow(num, exponent, modulus)
    decrypted_text = hex(key)[2:].rstrip("L")
    if len(decrypted_text) % 2 != 0:
        decrypted_text = "0" + decrypted_text
    return decrypted_text.decode("hex")

encrypted_text = input('Enter encrypted text to be decrypted: \n')
bit_length, modulus, exponent = input('Enter Private key in format "modulus, exponent": \n').split(',')

print("Decrypted text: ", decrypt(encrypted_text, modulus, exponent))