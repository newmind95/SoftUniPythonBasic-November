name_of_book = input()
count_of_books = 0
is_book_found = True

while name_of_book != 'No More Books':
    name_of_book_to_search = input()

    if name_of_book_to_search == 'No More Books':
        is_book_found = False
        break

    if name_of_book == name_of_book_to_search:
        break
    
    count_of_books += 1

if is_book_found:
    print('You checked %d books and found it.' % count_of_books)
else:
    print('The book you search is not here!')
    print('You checked %d books.' % count_of_books)
    
