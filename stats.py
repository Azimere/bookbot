import sys
from pathlib import Path

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_books_path():
    return Path(sys.path[0]) / "books"

def count_words(text):
    word_count = len(text.split())
    return word_count

def count_characters(text):
    lower_text = text.lower()
    character_count = {}
    for character in lower_text:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def sort_character_count(character_count):
    sorted_character = []
    for char, count in character_count.items():
        if char.isalpha():
            sorted_character.append((char, count))
    sorted_character.sort(key=lambda x: x[1], reverse=True)
    return sorted_character