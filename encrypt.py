# @ Hridoy Rahman
# encrypts a file using a key 
def xor_encrypt(input_text, key):
    encrypted_text = ""
    for char in input_text:
        encrypted_char = ord(char) ^ key # xors char with a key.
        encrypted_text += chr(encrypted_char) # stores the result and concatenates with previous results
    return encrypted_text

# input file for encryption
input_file = input("Enter Input File Name For Encryption(anything.txt): ")
out_file = input("Enter Output File Name(file.answer.A.enc):")
key = int(input("Enter Key: "))

# takes an input and reads the text and stores in input_text
with open(input_file, "r", encoding="utf-8") as input_file:
    input_text = input_file.read()

encrypted_text = xor_encrypt(input_text, key) # encrypts the text and stores the result in encrypted_text

# writes the encrypted data to a file.
with open(out_file, "w", encoding="utf-8") as output_file:
    output_file.write(encrypted_text)

print(f"File '{out_file}' has been encrypted with key {key}.") # prints the encrypted key along with file name.


