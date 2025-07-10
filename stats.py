def get_num_words(str1): 
    num_words = 0
    lst= str1.split()
    for word in lst:
        num_words += 1
    return f"{num_words} words found in the document"