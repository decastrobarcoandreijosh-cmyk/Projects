from datetime import datetime


def wrong_option():
    while True:
        option = (input("Exit or Continue?: ")).lower()
        if option == "exit":
            return True
        elif option== "continue":
            return False
        else:
            print("Invalid option")

def borrow_book(book_manage: dict, log_manage: dict, borrow_manage: dict):
    while True:
        if not borrow_manage:
            print("No books to borrow yet")
            
        print("===LIST OF AVAILABLE BOOKS TO BORROW===")
        for key, value in book_manage.items():
            if value['status'] == "Available":
                print("BOOK ID: " + key)
                print("TITLE: " + value['title'])
                print("AUTHOR: " + value['author'])
                print("DATE PUBLISHED: " + value['date_published'])
                if value['list_of_borrowers']:
                    print("LIST OF PREVIOUS BORROWERS")
                    for borrow_id in value['list_of_borrowers']:
                        print("    " + borrow_id + ": ", end="")
                        for key, value in borrow_manage.items():
                            if key == borrow_id:
                                log_id = value['log_id']
                        
                        for key, value in log_manage.items():
                            if key == log_id:
                                print(value['name'])

        title = input("Enter title of book you wish to borrow: ")
        author = input("Enter author of book you wish to borrow: ")
        list_of_books = []

        for key, value in book_manage.items():
            if value['title'] == title and value['author'] == author:
                list_of_books.append(key)
        
        if not list_of_books:
            print("No such book in the library")
            if wrong_option(): 
                break
            else:
                continue

        borrow_id = (input("Please input Borrow ID (Format: BL1, BL2, BL100): ")).upper()
        if borrow_id[0] != 'B' and borrow_id[1] != 'L':
            print("Error: Invalid format")
            if wrong_option(): 
                break
            else:
                continue

        try:
            borrow_id[2]
        except IndexError:
            print("Error: Invalid format")
            if wrong_option(): 
                break
            else:
                continue

        for i in range(2, len(borrow_id)):
            try:
                int(borrow_id[i])
            except ValueError:
                print("Error: Invalid format")
                if wrong_option(): 
                    break
                else:
                    continue

        if borrow_id in borrow_manage:
            print("Error: Duplicate Borrow ID")
            if wrong_option(): 
                break
            else:
                continue 

        if len(list_of_books) == 1:
            book_id = list_of_books[0]
        else:
            print("MULTIPLE BOOKS WITH SAME TITLE AND AUTHOR NAME")
            for books in book_id:
                for key, value in book_manage.items():
                    if key == books:
                        print("BOOK ID: " + key)
                        print("DATE PUBLISHED: " + value['date_of_'])


        break

        


def borrow_manage(book_manage: dict, log_manage: dict, borrow_manage: dict):
    while True:
        print()
        print("===BORROW MANAGEMENT MENU===")
        print("[1] BORROW BOOK")
        print("[0] EXIT")
        select = input("Enter your input: ")

        if select == '1':
            borrow_book(book_manage, log_manage, borrow_manage)
        elif select == '0':
            break
        else:
            print("Error: Invalid input")