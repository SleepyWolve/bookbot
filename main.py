import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_words_count(text)
    letters_count = get_characters_count(text)
    print(f"{text} \nword count: {word_count}\nLetters count: {letters_count}")
    

def get_words_count(book):
    words = book.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_characters_count(text):
    letter_dict = {c: 0 for c in string.ascii_lowercase}
    lowercase = text.lower()
    letter_dict[" "] = 0
    for i in lowercase:
        if i in letter_dict:
            letter_dict[i] += 1
            
    return letter_dict

if __name__ == '__main__':
    main()