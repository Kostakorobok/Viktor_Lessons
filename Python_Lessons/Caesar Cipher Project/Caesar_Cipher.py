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

# Homework 1:
# [x] Task 1 
#   choicAe decrypt or encrypt:
#   decrypt (multi -1) : -factor 
#   encrypt (multi 1) : +factor 
# [x] Task 2
#   while -> to repeat cypher

app_on = True

print(logo)
print(f"Welcome to the caesar Cipher encryptor.\nThis software will encrypt a word by a randomised encryption factor\nRules:\n-You may enter any number of words separated by space\n-Only letters or space to be used\n")

while(app_on):
    encryption_factor:int = random.randint(1,10)
    # print(encryption_factor)
    alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    secrete_word = input("Enter the word to be encrypted:\n").lower()
    encrypted_word_list = []

    for i in range(0, len(secrete_word)):
        alphabet_index = alphabet.index(secrete_word[i]) + encryption_factor
        encrypted_word_list.append(alphabet[alphabet_index])

    encrypted_word_str = "".join(encrypted_word_list)
    print(f"Encrypted version: {encrypted_word_str}")
    user_input = input("Would you like to decrypt the word?\n(Y) Yes\n(N) No\n").lower()
    if user_input == "y":
        encrypted_word_list = []
        encryption_factor *= -1
        for i in range(0, len(encrypted_word_str)):
            alphabet_index = alphabet.index(encrypted_word_str[i]) + encryption_factor
            encrypted_word_list.append(alphabet[alphabet_index])
        
        encrypted_word_str = "".join(encrypted_word_list)
        print(f"Original word is: {encrypted_word_str}")

    elif user_input == "n":
        pass
    else:
        print("Wrong input, try again.\n")
        
    user_input = input("Encrypt another word or exit?\n(1) Encrypt\n(2) Exit \n").lower()
    if user_input == "1":
        continue
    elif user_input == "2":
        print("Thank you for using Caesar Cipher, good bye\n")
        break
    else:
        print("Wrong input, try again.\n")



