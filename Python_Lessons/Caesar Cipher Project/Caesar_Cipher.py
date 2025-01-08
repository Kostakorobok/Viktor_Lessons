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
input("Press Enter to exit")

