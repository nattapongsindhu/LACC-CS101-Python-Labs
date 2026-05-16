"""
File: encrypt.py
Project 4.3

Encrypts a text file. The inputs are the names of
the input file and the output file and the distance value.
The encrypted code is written to a new file.
"""

# Take the inputs
inName = input("Enter the input file name: ")
outName = input("Enter the output file name: ")
distance = int(input("Enter the distance value: "))

# Open the input file and read the plain text
inputFile = open(inName, "r")
plainText = inputFile.read()

# Open the output file and write the encrypted text
outFile = open(outName, "w")
code = ""
for ch in plainText:
    ordValue = ord(ch)
    cipherValue = ordValue + distance
    if cipherValue > 127:
        cipherValue = distance - (127 - ordValue + 1)
    code += chr(cipherValue)
outFile.write(code)

inputFile.close()
outFile.close()
