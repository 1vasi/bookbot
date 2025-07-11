import sys
from stats import get_num_words
from stats import get_num_letter
from stats import sort_dict


import sys

try:
    text_file = sys.argv[1]  # Try to access the argument
except IndexError:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():

    

    get_book_text(text_file)
    
    get_num_words(get_book_text(text_file))

    get_num_letter(get_book_text(text_file))

    sort_dict(get_num_letter(get_book_text(text_file)))

def get_book_text(filepath):
    with open(filepath) as f:
        output_str = f.read()
        return output_str

def print_report():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{text_file}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text(text_file))} total words")
    print("--------- Character Count -------")
    for i in sort_dict(get_num_letter(get_book_text(text_file))):
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

print_report()


main() 


    


