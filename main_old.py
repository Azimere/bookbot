from stats import get_book_text, count_words, count_characters, sort_character_count

def main():
    text = get_book_text()
    word_count = count_words(text)
    char_counts = count_characters(text)
    sort_character = sort_character_count(char_counts)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in sort_character:
        print(f"{char}: {count}")
    print("============= END ===============")





main()