# @ Hridoy Rahman

import os

# input from file...
hex_characters = "ïÃÂËÞÍØÙÀÍØÅÃÂß¡¦¡¦ÿÉÞÅÃÙßÀÕÁÍÂÕÏÃÂËÞÍØßéÚÉÂØÄÃÙËÄØÄÅßÅßÂØÏÃÁÜÙØÍØÅÃÂÍÀÀÕÈÅÊÊÅÏÙÀØ¡¦ÅØßÏÉÞØÍÅÂÀÕÍØÀÉßÍØÍÀÅØØÀÉÃÙØßÅÈÉÃÙÞÂÃÞÁÍÀÏÃÁÊÃÞØÖÃÂÉßÞÅËÄØ¡¦¡¦çÿÃÂÃÛÕÃÙÄÍÚÉØÛÃØÄÅÂËßØÃÈÃ¡¦õÃÙÂÉÉÈØÃÍÏØÙÍÀÀÕÏÞÉÍØÉÕÃÙÞÜÞÃÃÊÃÊÄÍÚÅÂËßÃÀÚÉÈØÄÅßØÍßÇ¡¦õÃÙÂÉÉÈØÃÁÃÚÉÃÂØÃØÄÉßÉÏÃÂÈÄÍÀÊÜÍÞØî¡¦¡¦øÃÏÞÉÍØÉÕÃÙÞÜÞÃÃÊÃÊÄÍÚÅÂËßÃÀÚÉÈØÄÅßØÍßÇÆÙßØÙßÉØÄÉßÍÁÉÎÍßÅÏ¡¦ÜÞÃÏÉßßÕÃÙÙßÉÈØÃÈÉÏÞÕÜØØÄÅßÁÉßßÍËÉØÃÉÂÏÞÕÜØÍÂÉÛßÜÉÏÅÊÅÏÃÂÉ¡¦åÂÍÊÅÀÉßØÃÞÉÕÃÙÞÂÍÁÉÙßÉÞÂÍÁÉÍÂÈßØÙÈÉÂØÂÙÁÎÉÞéÂÏÞÕÜØØÄÅßÊÅÀÉ¡¦ÛÅØÄÍÇÉÕÃÊÜÀÙßØÄÉÀÍßØØÛÃÈÅËÅØßÃÊÕÃÙÞßØÙÈÉÂØÂÙÁÎÉÞ¡¦¡¦ÉËÅÊÕÃÙÞÙßÉÞÂÍÁÉÛÍßÉÊÍÎÛÅØÄÍßØÙÈÉÂØÂÙÁÎÉÞÃÊÕÃÙÈÄÍÚÉ¡¦ÍÊÅÀÉÏÃÂØÍÅÂÅÂË¡¦éÍÞÀÊÞÉÈêÃÔØÃÂÉÊÍÎ¡¦¡¦ÍÂÈÉÂÏÞÕÜØÅØÛÅØÄÍÇÉÕÃÊ¡¦âÍÁÉØÄÉÊÅÀÉÍßÙßÉÞÂÍÁÉÍÂßÛÉÞíÉÂÏ¡¦ÿÃÅÂØÄÅßÏÍßÉ¡¦ÉÊÍÎÍÂßÛÉÞíÉÂÏ¡¦¡¦õÉßÍÎÅØÁÙÏÄåÞÉÍÀÅÖÉîÙØÉÍßÅÉÞËÞÍÈÅÂËÅßÝÙÅÏÇÉÞËÞÍÈÅÂË¡¦¡¦íÀßÃÅÂÏÀÙÈÉÛÄÍØÉÚÉÞÏÃÈÉÃÞßÏÞÅÜØÕÃÙÁÍÈÉØÃËÉÂÉÞÍØÉØÄÅßÊÅÀÉ¡¦ÍßÛÉÀÀÍßØÃßÃÀÚÉÊÃÞØÄÉÇÉÕÊÃÞÚÉÞÅÊÅÏÍØÅÃÂÞÉÍÈÍÚÃÅÈÅÂËØÄÉ¡¦ÂÉÉÈÊÃÞÜÍÜÉÞÛÃÞÇÜÙÞÜÃßÉß¡¦¡¦åÂÏÀÙÈÉÕÃÙÞßØÙÈÉÂØÂÙÁÎÉÞÅÂÍÏÃÁÁÉÂØÍØØÄÉØÃÜÃÊØÄÉßÏÞÅÜØ¡¦ßÃÕÃÙÞÁÍÞÇÉÞÈÃÉßÂØÂÉÉÈØÃËÃÄÙÂØÅÂËÍÞÃÙÂÈÊÃÞÅØ¡¦¡¦¡¦ãÇÍÕØÄÉÂØÄÍØÆÙßØÀÉÍÚÉßÙßÛÅØÄØÄÉßÉÏÃÂÈÜÍÞØÞÅËÄØ¡¦øÄÅßÃÂÉßÈÉÏÅÈÉÈÀÕØÞÅÏÇÅÉÞÎÙØÅÊÕÃÙßÃÀÚÉÈØÄÅßÃÂÉÕÃÙßÄÃÙÀÈÎÉ¡¦ÊÅÂÉÛÅØÄØÄÉÂÉÔØÃÂÉÍßÛÉÀÀ¡¦¡¦øÄÉßÉÏÃÂÈíÿïååÁÉßßÍËÉÄÍßÍÀßÃÎÉÉÂÉÂÏÞÕÜØÉÈÛÅØÄÍÇÉÕßØÞÉÍÁÎÙØØÄÉ¡¦ÇÉÕÅßÂØÉÔÍÏØÀÕÎÅØßåÂßØÉÍÈÅØßÎÅØß¡¦äÃÛÈÃÉßØÄÍØÛÃÞÇéÍßÕ¡¦øÄÉÇÉÕÅßÉÊÊÉÏØÅÚÉÀÕÍÂÙÁÎÉÞÂÃØÊÞÃÁØÃÎÙØÊÞÃÁØÃ¡¦ÿØÍÞØÅÂËÊÞÃÁØÄÉÊÞÃÂØÃÊØÄÉÇÉÕÅØËÞÍÎßÎÅØßÍÂÈØÄÉÂØÄÉÂÉÔØÎÅØß¡¦ÍÂÈØÄÉÂØÄÉÂÉÔØÎÅØßäÃÛîÕÀÃÃÜÅÂË¡¦øÄÍØÅßØÄÉÊÅÞßØÎÅØßÍÞÉÆÙßØÀÅÇÉÛÅØÄØÄÅßÚÉÞßÅÃÂîÙØØÄÉÂÉÔØ¡¦ØÍÇÉØÄÉÞÉÁÍÅÂÅÂËÎÅØßÊÃÀÀÃÛÉÈÎÕØÄÉÊÅÞßØÎÅØÃÊØÄÉÇÉÕøÄÉØÄÅÞÈ¡¦ÇÉÕÎÕØÉßØÍÞØßÍØØÄÉßÉÏÃÂÈÎÅØÃÊØÄÉÇÉÕÉØÏ¡¦¡¦íÂÈÏÀÉÍÞÀÕÄÍÚÅÂËÍÜÃßßÅÎÀÉÇÉÕßÜÍÏÉÃÊÃÂÀÕØÅÁÉßØÄÉßÅÖÉÃÊØÄÅß¡¦ÀÍßØÚÉÞßÅÃÂÛÃÂØÁÍÇÉÅØÄÍÞÈÉÞÍØÍÀÀÞÅËÄØ¡¦¡¦ûÉÀÀÄÉÞÉßÛÄÍØåÏÍÂßÍÕÊÃÞÄÅÂØß¡¦åØßÍÂíÿïååÊÅÀÉ¡¦åÛÃÂØØÉÀÀÕÃÙÛÄÍØÀÅÂÉÉÂÈÅÂËßÅØÙßÉß¡¦øÄÉÞÉÅßÚÍßØÀÕÁÃÞÉØÄÍÂÉÂÃÙËÄÁÍØÉÞÅÍÀÛÅØÄÅÂØÄÉÊÅÀÉØÃßÃÀÚÉÅØ¡¦äÃÛÉÚÉÞÕÃÙßÃÀÚÉÊÃÞØÄÉÇÉÕÕÃÙÀÀßØÅÀÀÂÉÉÈØÃÉÔÜÀÅÏÅØÀÕÈÉÏÞÕÜØ¡¦ØÄÉÁÉßßÍËÉØÃËÉØØÄÉßÙÎÁÅßßÅÃÂÅÂßØÞÙÏØÅÃÂß¡¦øÄÃÙËÄØÄÉÇÉÕßØÞÉÍÁËÉÂÉÞÍØÅÃÂÅßßÀÅËÄØÀÕÁÃÞÉÏÃÁÜÀÅÏÍØÉÈÍÏØÙÍÀÀÕ¡¦ßÃÀÚÅÂËÅØÁÅËÄØÎÉÉÚÉÂÉÍßÅÉÞØÄÍÂØÄÅßÀÍßØÃÂÉ¡¦¡¦íÂÈÊÃÞØÄÉÀÍßØÄÅÂØÏÃÂßÅÈÉÞÛÄÍØÕÃÙÇÂÃÛíÂÈåÁÉÍÂéúéþõøäåâëÕÃÙÇÂÃÛ¡¦¡¦êÃÞÉÔÍÁÜÀÉØÄÃÙËÄÕÃÙÁÅËÄØÄÍÚÉÊÃÙÂÈßÃÁÉÏÀÉÚÉÞÍÀØÉÞÂÍØÅÚÉÅØÛÍßÁÕ¡¦ÄÃÜÉØÄÍØÕÃÙÈßÃÀÚÉØÄÅßÀÍßØÚÉÞßÅÃÂÎÕßÅÁÜÀÕÅØÉÞÍØÅÂËÃÚÉÞÍÀÀ¡¦ÜÃßßÅÎÀÉÇÉÕßÍÂÈßÉÉÅÂËÛÄÅÏÄÃÂÉËÉÂÉÞÍØÉÈØÄÉÁÃßØÅÂßØÍÂÏÉßÃÊÎÕØÉ¡¦ÚÍÀÙÉßÃÊÊÃÀÀÃÛÉÈÎÕÏÃÞÞÉßÜÃÂÈÅÂËØÃïþàê¡¦øÄÍØÛÃÂØÄÉÀÜÕÃÙØÄÅßØÅÁÉÎÙØÛÄÍØÉÀßÉÈÃÕÃÙÇÂÃÛ¡¦¡¦õÃÙÏÍÂÈÃØÄÅß¡¦"
result = ""

# This portion of the code,
# takes a input string hex_characters, which is the input file, i just copied it here.
# Brute forces from 0-255 and tries to decode for the key.
# the output1.txt holds all the key along with their corresponding decrypted messages.
with open("output1.txt", "w") as output_file:
    for j in range(256):
        for char in hex_characters:
            xor_result = ord(char) ^ j # xor each characters of hex_characters for a given key.
            decoded_char = chr(xor_result) # converts it to character
            result += repr(decoded_char)[1:-1] # appends the char to the result and removes double quotation from individual characters
        output_file.write(f"key: {j} {result}\n") # prints in a file.
        result = ""


with open("output1.txt", "r") as inputFile: # reads the output1.txt file to extract the actual english text out of garbage.
    output = inputFile.readlines() # reads line by line
    store = ""
    for line in output:
        if "the" in line and "in" in line and "to" in line: # tries to find the words, "the", "in", "to"
            store = line # stores in a string

    # prints the key.
    decimal_number = int(store[5:8]) 
    key = hex(decimal_number)
    print(f"key: {key}")

    store = store[9:] # deletes the key from text_file.

    # takes the stored message and makes it a readable content by breaking lines and outputing in a file.
    with open("secretMessageA_Decrypted.txt", "w") as dFile:
        for line in store.split('\\r\\n'):
            dFile.write(line + '\n')

file_path = "output1.txt"

# omit this, just removing a file after working with it.
try:
    os.remove(file_path)
    print(f"File '{file_path}' has been deleted successfully.")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except PermissionError:
    print(f"Error: Permission denied. Unable to delete '{file_path}'.")
except Exception as e:
    print(f"An error occurred: {e}")