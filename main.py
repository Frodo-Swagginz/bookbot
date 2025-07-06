import sys
from stats import word_count, character_counts, sort_character_counts

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    text = get_book_text(book_path)
    count = word_count(text)
    print("----------- Word Count ----------")
    print(f"Found {count} total words")

    print("--------- Character Count -------")
    ch_dict = character_counts(text)
    ch_sort = sort_character_counts(ch_dict)

    for item in ch_sort:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
