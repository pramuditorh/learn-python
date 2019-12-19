from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(self): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def display(self):
        print(f'Title: {title}\nAuthor: {author}\nPrice: {price}')

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()