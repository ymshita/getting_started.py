def print_page(content= 'nothing'):
    print('content: '+content)

print_page('hello world')

def increment(page_num, last=10):
    next_num = page_num + 1
    if next_num <= last:
        return next_num
    # else : return None

increment(2, 10)
increment(last=10, page_num=2)
increment(2, last=10)
increment(2)

def print_pages(content, *args):
    print(content)
    for more in args:
        print('more: ', more)
print_pages('my content')
print_pages('my content', 'content2', 'content3')

def print_page(content, **kwargs):
    print(content)
    for key, value in kwargs.items():
        print(f'{key}: {value}')
print_page('my content', published=2019, author="rei suyama")

def print_pages_unpack_list_and_map(*args, **kwargs):
    for content in args:
        print(content)
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_pages_unpack_list_and_map('my content', 'content2', 'content3', published=2019, author="rei suyama")

def increment_require_keyword(page_num, last, *, ignore_error=False):
    next_page = page_num + 1
    if next_page <= last:
        return next_page
    if ignore_error:
        return None
    raise ValueError('Invalid arguments')

increment_require_keyword(2, 2, ignore_error=True)

def increment_positional_only(page_num, last, /, ignore_error=False):
    next_page = page_num + 1
    if next_page <= last:
        return next_page
    if ignore_error:
        return None
    raise ValueError('Invalid arguments')

increment_positional_only(2, 2, True)

def print_page_with_unpack(one, two, three):
    print(one)
    print(two)
    print(three)

contents = ['content1', 'content2', 'content3']

print_page_with_unpack(*contents)

def print_page_with_unpack2(content, published, author):
    print(content)
    print('published: ', published)
    print('author: ', author)

footer = {'published': 2019, 'author': 'rei suyama'}
print_page_with_unpack2('my content', **footer)

def increment_with_docstring(page_num, last, *, ignore_error=False):
    """次のページの番号を返す
    :param page_num: もとのページ番号
    :type page_num: int
    :param last:　最終ページの番号
    :type last: int
    :param ignore_error: Trueの場合ページのオーバーで例外を送出しない
    :type ignore_error: bool
    :rtype int:
    """

    next_page = page_num + 1
    if next_page <= last:
        return next_page
    if ignore_error:
        return None
    raise ValueError('Invalid arguments')

#lambda
increment = lambda num: num +1

nums = ['one', 'two', 'three']
filtered = filter(lambda x: len(x) == 3, nums)
print(filtered)

# type hints
from typing import Optional

def increment_with_type_hints(
    page_num: int,
    last: int,
    *,
    ignore_error: bool = False) -> Optional[int]:
    next_page =page_num =1
    if next_page <= last:
        return next_page
    if ignore_error:
        return None
    raise ValueError('Invalid arguments')

print(increment_with_type_hints.__annotations__)

def decrement(page_num: int) -> int:
    prev_page: int
    prev_page = page_num -1
    return prev_page

#実行時に型チェックは行われないためエラーにならない
decrement(2.0)
