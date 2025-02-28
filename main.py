import sys
from pathlib import Path
from stats import (
    get_book_text, 
    count_words, 
    count_characters, 
    sort_character_count,
    get_books_path
)

def analyze_book(path):
    text = get_book_text(path)
    word_count = count_words(text)
    char_counts = count_characters(text)
    sorted_chars = sort_character_count(char_counts)
    
    print(f"\nAnalyzing book: {path.name}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in sorted_chars:
        print(f"{char}: {count}")
    print("---------------------------------")

def main():
    if len(sys.argv) > 1:
        # If a specific book is provided as argument
        book_path = Path(sys.argv[1])
        if book_path.exists():
            analyze_book(book_path)
        else:
            print(f"Error: Book file '{book_path}' not found")
    else:
        # If no argument, process all books in the directory
        books_path = get_books_path()
        book_files = [f for f in books_path.glob("*.txt")]
        
        print("============ BOOKBOT ============")
        for book_path in book_files:
            analyze_book(book_path)
        print("============= END ===============")

if __name__ == "__main__":
    main()