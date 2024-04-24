class Author:
    def __init__(self,name):
        self.name = name

    def contracts(self):
        return [ c for c in Contract.all if c.author==self]
    
    def books(self):
        return [ c.book for c in Contract.all if c.author==self]
    
    def total_royalties(self):
        return sum([ c.royalties for c in Contract.all if c.author==self])
    
    def sign_contract(self,book,date,royalties):
        return Contract(self,book,date,royalties)


class Book:
    def __init__(self,title):
        self.title = title

    def contracts(self):
        return [ c for c in Contract.all if c.book==self]
    
    def authors(self):
        return [ c.author for c in Contract.all if c.book==self]


class Contract:
    all=[]

    def __init__(self,author,book,date,royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls,date):
        return [ c for c in Contract.all if c.date==date]

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self,author):
        if not isinstance(author,Author):
            raise TypeError
        self._author=author

    @property
    def book(self):
        return self._book
    @book.setter
    def book(self,book):
        if not isinstance(book,Book):
            raise TypeError
        self._book=book

    @property
    def date(self):
        return self._date
    @date.setter
    def date(self,date):
        if not type(date)==str:
            raise TypeError
        self._date=date

    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self,royalties):
        if not type(royalties)==int:
            raise TypeError
        self._royalties=royalties