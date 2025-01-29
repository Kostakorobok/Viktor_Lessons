# #8-1. Message.
# def display_message():
#     """Information about chapter 8."""
#     print("In the Chatper 8, we will be learning about the fucntions in the python")

# display_message()

#8-2. Favorite book.

def favorite_book(title):
    print(f"One of my favorite books is {title.title()}!")

fav_book = input("Enter name of your favorite book: \n")
favorite_book(fav_book)