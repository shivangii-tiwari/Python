books = []
issued_book = []

def add_book():
    book = input('Enter the tital of book: ')
    books.append(book)
    print('Book is added')

def show_books():
    if len(books) == 0:
        print('not Avilable')
    else:
        print('Avilable')
        for s in books:
            print(s)

def issue_book():
    book = input('Enter the title of book: ')
    if book in books:
        issued_books.append(book)
        books.remove(book)
        print('book is issued')
    else:
        print('book is not avilable')

        def return_book():
            book = input('enter the title of book: ')
            if book in issued_books:
                issued_books.remove(book)
                books.append(book)
                print('The book is returned')
            else:
                print('book is not issued')
            
def library():
    while True:
        print("lib managment system")
        print('1. add book')
        print('2. show book')
        print('3. issue book')
        print('4. return book')
        print('5. exit')
        coco = int (input('enter your choice: '))
        if coco == 1:
            add_book()
        elif coco == 2:
            show_books()
        elif coco == 3:
            issue_book()
        elif coco == 4:
            return_book()
        elif coco == 5:
            print('Thank you for visiting our library')
            break
        else:
            print('invalid choice')

library()