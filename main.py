from stats import word_count, letter_count, sort_results
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]
    text = get_book_text(path_to_book)
    count = word_count(text)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")

    char_count = letter_count(text)
    results = sort_results(char_count)

    for char_dict in results:
        char = char_dict["char"]
        num = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {num}")


    print("============= END ===============")

    


main()