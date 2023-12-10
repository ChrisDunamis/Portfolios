from random import shuffle
from string import printable as preferred_chars


MY_COURSE = "Project - Basic Encryption and Decryption Program"
MY_SUBJECT = "BASIC ENCRYPTION & DECRYPTION PROGRAM"

print("\n" + "Course:  " + MY_COURSE)
print("Subject: " + MY_SUBJECT + "\n")

string_characters = preferred_chars[:-5]
string_characters = list(string_characters)
keys = string_characters.copy()

shuffle(keys)
# print("\n" + "My String Characters:", string_characters)
# print("My Keys:".rjust(21, ' '), keys)

# ---------------------------------------------------- ENCRYPTION ---------------------------------------------------- #
print("TEXT CIPHERED".center(100, '-'))

plain_text = input("Plain Text:    ")
cipher_text = ""

for every_letter in plain_text:
    index = string_characters.index(every_letter)
    cipher_text = cipher_text + keys[index]

print("Ciphered Text:", cipher_text)
print('-' * 100)
# -------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------- DECRYPTION ---------------------------------------------------- #
print("TEXT DECIPHERED".center(100, '-'))

cipher_text = input("Deciphered Text:   ")
plain_text = ""

for every_letter in cipher_text:
    index = keys.index(every_letter)
    plain_text = plain_text + string_characters[index]

print("Plain Text:       ", plain_text)
print('-' * 100)
# -------------------------------------------------------------------------------------------------------------------- #
