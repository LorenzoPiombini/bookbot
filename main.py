
import sys
from stats import get_word_count, get_char_count, sort_data


def get_book_text(book_path):
    contents = "";
    try:
        with open(book_path) as f:
            contents = f.read();
    except Exception as e:
        print(e);
        sys.exit(1);
    return contents;
    


def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>");
        sys.exit(1);

    print("============ BOOKBOT ============");

    print(f"Analyzing book found at {sys.argv[1]}");
    print("----------- Word Count ----------");
    print(f"Found {get_word_count(get_book_text(sys.argv[1]))} total words");
    print("--------- Character Count -------");
    test = sort_data(get_char_count(get_book_text(sys.argv[1])));

    for d in test:
            if d['char'].isalpha():
                print(f"{d['char']}: {d['num']}");
    print("============= END ===============");


main();
