"""
Author: Nattapong Sindhu
Course: CS101 Introduction to Computer Science

Chapter 4: Programming Exercise 4-1
Program: encrypt.py
Instructions: Encrypt an entire file of text using a Caesar cipher.
"""

# Request the inputs
input_file_name = input("Enter the input file name: ")
output_file_name = input("Enter the output file name: ")
distance = int(input("Enter the distance value: "))

# Open the input file and read the text
input_file = open(input_file_name, "r")
message = input_file.read()
input_file.close()

# Encrypt the text
encrypted_text = ""
for ch in message:
    if ord(ch) >= 32 and ord(ch) <= 126:
        code = ord(ch) - 32
        code = (code + distance) % 95
        ch = chr(code + 32)
    encrypted_text += ch

# Write the encrypted text to the output file
output_file = open(output_file_name, "w")
output_file.write(encrypted_text)
output_file.close()

# Display the result
print("The file has been encrypted.")
