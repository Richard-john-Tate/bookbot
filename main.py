def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    print_report(book_path, word_count, letter_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(string):
    words = string.split()
    return len(words)

def count_letters(string):
    string = string.lower()
    letter_count = {}
    for char in string:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return letter_count

def print_report(book_path, word_count, letter_count):
    sorted_letters = sorted(letter_count.items(), key=lambda item: item[1], reverse=True)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for char, count in sorted_letters:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

if __name__ == '__main__':
    main()
