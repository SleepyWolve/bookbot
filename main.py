__name__ == '__main__'
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def word_count(book):
    words = book.split()
    return len(words)

print(main())
print(word_count(main()))