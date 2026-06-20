def add_book(catalog,book_id,title,author,year):
    catalog[book_id]=(title,author,year)

def borrow_book(catalog,borrowed_books,book_id):
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)
        
def return_book(borrowed_books,book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)

def register_member(members,member_id):
    members.add(member_id)

def show_available(catalog,borrowed_books):
    print("Available Books:")
    for book_id,details in catalog.items():
        if book_id not in borrowed_books:
            print(f"ID:{book_id}|{details[0]} by {details[1]}({details[2]})")

def main():
    catalog={}
    borrowed_books=[]
    members=set()

    add_book(catalog,101,"The Great Gatsby","F.Scott Fitzgerald",1925)
    add_book(catalog,102,"Thirukkural","Thiruvalluvar",1900)
    add_book(catalog,103,"The Hobbit","J.R.R.Tolkien",1937)
    add_book(catalog,104,"Python Crash Course","Eric Mattes",2019)

    register_member(members,"M01")
    register_member(members,"M02")
    register_member(members,"M01")
   
    borrow_book(catalog,borrowed_books,101)
    borrow_book(catalog,borrowed_books,102)

    return_book(borrowed_books,101)

    show_available(catalog,borrowed_books)
    print(f"\nRegistered Members:{members}")

if __name__=="__main__":
    main()
