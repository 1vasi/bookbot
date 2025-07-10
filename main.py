from stats import get_num_words

def main():
    get_book_text("/Users/yungvasi/projects/github.com/1vasi/bookbot/books/frankenstein.txt")

    print(get_num_words(get_book_text("/Users/yungvasi/projects/github.com/1vasi/bookbot/books/frankenstein.txt")))

def get_book_text(filepath):
    with open(filepath) as f:
        output_str = f.read()
        return output_str
    
main()

