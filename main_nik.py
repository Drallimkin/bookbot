def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_contents(book_path)
    letters = letter_count(book_contents)
    num_words = number_of_words(book_contents)
    print_report = report(book_path, num_words, letters)
    print(print_report)

def number_of_words(book_contents):
    words = book_contents.split()
    return len(words)

def letter_count(book_contents):
    chars = {}
    for char in book_contents:
        char_lower = char.lower()
        if char_lower not in chars:
            chars[char_lower] = 1
        else:
            chars[char_lower] += 1
    return chars

def report(book_path, num_words, letters):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for letter in letters:
        if letter.isalpha():
            print(f"The {letter} character was found {letters[letter]} times")
    print("--- End report ---")

def get_contents(path):
    with open(path) as f:
        return f.read()
    
main()
