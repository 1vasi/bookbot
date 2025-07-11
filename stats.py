def get_num_words(str1): 
    num_words = 0
    lst= str1.split()
    for word in lst:
        num_words += 1
    return num_words

def get_num_letter(str1):
    dict_letter = {}
    list_of_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                        "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        
    for i in list_of_letters:
        correct_str = str1.lower()
        each_letter_counted = correct_str.count(i)
        dict_letter[i] = each_letter_counted
        
    return dict_letter
    
def sort_dict(lst_dict):
    lst = []

    for k,v in lst_dict.items():
        new_dict = {"char": k, "num": v}
        lst.append(new_dict)  
    lst.sort(reverse=True, key=lambda x: x['num'])

    return lst

