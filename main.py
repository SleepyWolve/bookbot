import string

#settings
set_print_entire_book = False
set_count_spaces = False
set_pretty_output = True


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_words_count(text)
    letters_count = get_characters_count(text)
    if set_print_entire_book:
        print(text)
    print(f"Word count: {word_count}\nLetters count:\n{letters_count}")
    

def get_words_count(book):
    words = book.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_characters_count(text):
    letter_dict = {c: 0 for c in string.ascii_lowercase}
    if set_count_spaces:
        letter_dict[" "] = 0
    lowercase = text.lower()
    for i in lowercase:
        if i in letter_dict:
            letter_dict[i] += 1
    if set_pretty_output:
        return prettify(letter_dict)
    else:
        return letter_dict


def prettify(dict):
    pretty_string = ""
    for letter in dict:
        pretty_string += f"the '{letter}' has found {dict[letter]} times\n"

    return pretty_string


if __name__ == '__main__':
    main()
