

#ППараметри книги
class Book:
    def __init__(Slf, author, Date, genre):
        Slf.author=author
        Slf.Date=Date
        Slf.genre=genre


#Бібліотека
class Library:
    books = []
    
    
    #Додавання книги
    def addBook(Slf, book):
        Slf.books.append(book)
    
    
    #Видалення книги
    def removeBook(Slf, book):
        Slf.books.remove(book)
    
    
    #Пошук за автором
    def searchByAuthor(Slf, author):
        books = []
        for book in Slf.books:
            if book.author == author:
                books.append(book)
        return books
    
    
    #Пошук по даті
    def searchByDate(Slf, Date):
        books = []
        for book in Slf.books:
            if book.Date == Date:
                books.append(book)
        return books
    
    
    #Пошук за жанром
    def searchByGenre(Slf, genre):
        books = []
        for book in Slf.books:
            if book.genre == genre:
                books.append(book)
        return books


#Книги
def main():
    library = Library()

    library.addBook(Book('Іва́н Нечу́й-Леви́цький', 'Кайдашева сімя', 1878, 'повість'))
    library.addBook(Book('Артур Чарльз Кларк', '2001: Космічна Одіссея', 1968, 'Научная фантастика'))
    library.addBook(Book('Михайло Коцюбинський', 'Тіні забутих предків', 1912, 'драма'))
    library.addBook(Book('Артур Чарльз Кларк', '2010: Одіссея Два', 1982, 'Научная фантастика'))
    library.addBook(Book('Артур Чарльз Кларк', 'Око Часу', 2003, 'Научная Фантастика'))

    
    #Сортування по автору
    author = 'Артур Чарльз Кларк'
    books = library.searchByAuthor(author)
    if len(books) == 0:
        return
    book = books[0]
    print('Кількість книг автора ' + author, len(books))
    print('Автор книги', author)
    library.removeBook(book)
    books = library.searchByAuthor(author)
    print('Нова кількість книг автора ' + author, len(books))


#Кінець
if __name__ == '__main__':
    main()