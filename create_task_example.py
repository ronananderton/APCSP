books = []
print("Welcome to the digital library!")

response = input("Do you want to add a book, find a book, or quit? Select A/F/Q \n")

if response == "A":
    book = input("What book do I want to add")
    books.append(book)

elif response == "F":
    search = input("What book do you want to find? \n")
    found = False
    for book in books:
        if book == search:
            found = True
            print("This book was found! \n")
            break
    if found == False:
            print("We do not have this book \n")