#!/usr/bin/python3

# ASCII value for 'a' is 97, and for 'z' is 122
# We'll iterate from 97 to 122 and print each character without a newline

for letter_code in range(97, 123):
    print(chr(letter_code), end="")
