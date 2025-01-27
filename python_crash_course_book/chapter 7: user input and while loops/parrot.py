prompt = "Tell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end\n"
# message = ""
# while message != "quit":
#     message = input(prompt)
#     if message != "quit":
#         print(message)
#     else:
#         print('Good bye.')

active = True

while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(message)

