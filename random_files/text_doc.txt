# Caesar Cipher Incryptor

import random

logo = """
   ______                              _______       __             
  / ____/___ ____  _________ ______   / ____(_)___  / /_  ___  _____
 / /   / __ `/ _ \/ ___/ __ `/ ___/  / /   / / __ \/ __ \/ _ \/ ___/
/ /___/ /_/ /  __(__  ) /_/ / /     / /___/ / /_/ / / / /  __/ /    
\____/\__,_/\___/____/\__,_/_/      \____/_/ .___/_/ /_/\___/_/     
                                          /_/                                                                                                                                                                                                                                                                                                                                               
"""
encryption_factor:int = random.randint(1,10)
# print(encryption_factor)
print(logo)
print(f"Welcome to the caesar Cipher encryptor.\nThis software will encrypt a word by a factor of: {encryption_factor}\nRules:\n-You may enter any number of words separated by space\n-Only letters or space to be used\n")

alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

secrete_word = input("Enter the word to be encrypted:\n").lower()
encrypted_word_list = []

for i in range(0, len(secrete_word)):
    alphabet_index = alphabet.index(secrete_word[i]) + encryption_factor
    encrypted_word_list.append(alphabet[alphabet_index])

encrypted_word_str = "".join(encrypted_word_list)
print(f"Original version: {secrete_word}\nEncrypted version: {encrypted_word_str}")
# input("Press Enter to exit")


###ciepher -> decepher
# encryption_factor
# a -> f
  # 
decrypted_word_str = ""

for i in range(0, len(encrypted_word_str)):
  alphabet_index = alphabet.index(encrypted_word_str[i]) - encryption_factor
  decrypted_word_str += alphabet[alphabet_index]
  # decrypted_word_list.append(alphabet[alphabet_index])

print(decrypted_word_str)

# Homework 1:
# 1 
# choicAe decrypt or encrypt:
# decrypt (multi -1) : -factor 
# encrypt (multi 1) : +factor 
# 2
# while -> to repeat cypher
