"""
Author: Nattapong Sindhu
Course: CS101 Introduction to Computer Science

Chapter 4: Programming Excercise 4-2
Program: decrypt.py
Instructions: Decrypt an entire file of text using a Caesar cipher.

1. Significant constants
        none
2. The inputs are
        an input file name
        an output file name
        a distance value
3. Computations:
        each character in the file is shifted back by the distance value
4. The outputs are
        the decrypted file
"""
# Request the inputs
input_file_name = input("Enter the input file name: ")
output_file_name = input("Enter the output file name: ")
distance = int(input("Enter the distance value: "))

# Open the input file and read the text
input_file = open(input_file_name, "r")
message = input_file.read()
input_file.close()

# Decrypt the text
decrypted_text = ""
for ch in message:
    if ord(ch) >= 32 and ord(ch) <= 126:
        code = ord(ch) - 32
        code = (code - distance) % 95
        ch = chr(code + 32)
    decrypted_text += ch

# Write the decrypted text to the output file
output_file = open(output_file_name, "w")
output_file.write(decrypted_text)
output_file.close()

# Display the result
print("The file has been decrypted.")
