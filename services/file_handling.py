import os
import sys


BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    data = ['.', ',', '!', ':', ';', '?']
    index = 0

    while True:
        t = text[start: start + size + 1]
        if t[-1] == ' ' or len(text) == (start + size):
            break
        size -= 1

    for value in data:
        char = text[start: start + size].rfind(value)
        if char > index:
            index = char
    result = text[start: start + index + 1]
    return result, len(result)


def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as file:
        start, key = 0, 1
        text = file.read()

        while start != len(text):
            value, index = _get_part_text(text, start, PAGE_SIZE)
            start += index
            book[key] = value.lstrip()
            key += 1


prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
