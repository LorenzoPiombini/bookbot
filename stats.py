
def get_word_count(book_content):
    return len(book_content.split());


def get_char_count(book_content):
    chars = {};
    for i in range(0,len(book_content)):

        if book_content[i].lower() in chars:
            chars[book_content[i].lower()] += 1;
        else:
            chars[book_content[i].lower()] = 1;

    return chars;

def sort_on(chars):
    return chars['num']

def sort_data(char_count):
    sorted_list = [];
    for char in char_count:
        sorted_list.append({"char": char, "num": char_count[char]});

    sorted_list.sort(reverse = True, key=sort_on);
    return sorted_list;


