# Run the file in cmd to decrypt.
# the following takes an encrypted file, a key, and output_file_name as inputs
# ________________________________________________________________________________
# 
# @ Hridoy Rahman
# ________________________________________________________________________________
# encrypts a file using a key 
def xor_encrypt(input_text, key):
    encrypted_text = ""
    for char in input_text:
        encrypted_char = ord(char) ^ key # xors char with a key.
        encrypted_text += chr(encrypted_char) # stores the result and concatenates with previous results
    return encrypted_text

# file input.
print("To Decrypt: ")
encrypted_file = input("Input Encrypted File: ")
decrypt_key = int(input("Enter Key To Decrypt: "))
file_output = input("Enter Decrypted File Name(anything.answer.A.Decrypted):")

# reads from a encrypted file.
with open(encrypted_file, "r", encoding="utf-8") as eFile:
    data = eFile.read()
    deciphered_text = xor_encrypt(data, decrypt_key) # stores decrypted result in deciphered_text
    with open(file_output, "w", encoding="utf-8") as answer: # writes in a file.
        answer.writelines(deciphered_text)