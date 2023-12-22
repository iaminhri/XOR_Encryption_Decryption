# @ Hridoy Rahman
import binascii

# reads fifteen bytes from the text file
def read_15_bytes(input_file):
    with open(input_file, 'rb') as file:
        content = file.read(15)
        return content

# input file
input_file = 'secretmessageB.txt.enc' 
read_bytes = read_15_bytes(input_file)

print(f"First 15 bytes from the file: {read_bytes}")

# converts to binary from bytes of data
binary_data = bin(int(binascii.hexlify(read_bytes), 16))[2:]

str_value = binary_data
print(f"Binary representation: {str_value}")
print(f"Length of Text: {len(str_value)}")


# Finding Key 
# takes every 8 bits from str_value variable 
# and xors first bit from it and stores the result in a key variable
key = [""]*15
for k in range(0, len(str_value), 8):
    xor_result = int(str_value[k], 2) ^ 0 # xors kth string with 0 and stores the result in xor_result
    key[k%15] += str(xor_result) # converts to string and puts it in the corresponding index
    k += 8 # skips 8 characters

key = ''.join(key) # joins the key to a single string
print(f"Key: {key}") # prints the key

# decryption
# reads the input_file defined at the top of the program
# outputs the result in a file
# xors every 15 bit with the key and converts to ascii by reading each 8 bit of the binary string,
# and converts it to decimal first then ascii characters.
with open(input_file, 'rb') as file_input, open("secretMessageB.txt", "w") as output_file:
    ciphered_text = file_input.read() # reads the whole input file
    ciphered_text_binary = bin(int(binascii.hexlify(ciphered_text), 16))[2:] # converts to binary string

    xorred_text = ""

    # Xors each 15 bit of the ciphered_text with the key.
    for i in range(len(ciphered_text_binary)):
        xorred_text += str(int(ciphered_text_binary[i]) ^ int(key[i % len(key)]))

    ascii_chars = ""
    # Takes each 8 bit from the xorred result and converts it to ascii value and outputs in a file.
    for j in range(0, len(xorred_text), 8):
        ascii_chars += chr(int(xorred_text[j:j+8], 2))
        j += 8
    output_file.writelines(ascii_chars)
