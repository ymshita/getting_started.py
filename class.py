from operator import attrgetter

class Page:
    book_title = 'Python Practice Book'
    def __init__(self, num, content):
        self.num = num
        self.content = content
    def output(self):
        return f'{self.content}'
    @classmethod
    def print_pages(cls, *pages):
        print(cls.book_title)
        pages = list(pages)
        for page in sorted(pages, key=attrgetter('num')):
            print(page.output())
    @staticmethod
    def is_blank(page):
        return not bool(page.content)

title_page = Page(0, 'Python Practice Book')
print(f'type: {type(title_page)}')
print(f'title_page is Page: {isinstance(title_page, Page)}')
print(f'title_page attributes: {dir(title_page)}')
print(f'title_page.output(): {title_page.output()}')
print('Page.book_title: ', Page.book_title)
Page.book_title = 'No title'
print('Page.book_title: ', Page.book_title)

first = Page(1, 'first page')
second = Page(2, 'second page')
third = Page(3, 'third page')
Page.print_pages(first, second, third)

page = Page(1, '')
print('blank: ',Page.is_blank(page))

def some_function(self):
    print('function')


# instance method
class Klass:
    def some_method(self):
        print('method')
kls = Klass()
Klass.some_function = some_function
print(f'kls.some_function(): {kls.some_function()}')

# instance variable
title_page.section = 0
print(f'title_page.section: {title_page.section}')

first_page = Page(1, 'first page')
#print(f'first_page.section: {first_page.section}') # error

# instance initialization
class Page2:
    def __init__(self, num, content, section=None):
        self.num = num
        self.content = content
        self.section = section
    
    def output(self):
        return f'{self.content}'

second_page = Page2(1, 'second page')
print(f'second_page.section: {second_page.section}')

# constructor
class Klass: 
    def __new__(cls, *args):
        print(f'cls= {cls}')
        print('Klass new', args)
        return super().__new__(cls)

    def __init__(self, *args):
        print('Klass init', args)

kls = Klass(1, 2, 3)

# properties

class Book: 
    def __init__(self, raw_price):
        if raw_price < 0:
            raise ValueError('price must be positive')
        self.raw_price = raw_price
        self._discounts = 0

    @property
    def discounts(self):
        return self.discounts
    @discounts.setter
    def discounts(self, value):
        if value < 0 or 100 < value:
            raise ValueError('discounts must be between 0 and 100')
        self._discounts = value
    @property
    def price(self):
        multi = 100 - self._discounts
        return int(self.raw_price * multi / 100)

book = Book(2000)
print("price: ", book.price)
book.discounts = 20
print("price discounted: ", book.price)
# book.discounts = 120 #error


# override methods
class TitlePage(Page):
    def output(self):
        title = super().output()
        return title.upper()

title = TitlePage(0, 'Python Practice Book')
print("title.output", title.output())


# subclass of built-in types
class Length(float):
    def to_cm(self):
        return super().__str__() + 'cm'
pencil_length = Length(16)
print('cm: ', pencil_length.to_cm())


# Multiple inheritance
class HTMLPageMixin:
    def to_html(self):
        return f'<html><body>{self.output()}</body></html>'

class WebPage(Page, HTMLPageMixin):
    pass

webPage = WebPage(0, 'web content')
print('html: ', webPage.to_html())

# diamond problem
class A:
    def hello(self):
        print('Hello')

class B(A):
    def hello(self):
        print('Hola')
        super().hello()

class C(A):
    def hello(self):
        print('Bonjour')
        super().hello()

class D(B, C):
    def hello(self):
        print('こんにちは')
        super().hello()

d = D()
d.hello()
print('mro', D.__mro__)