#-- takes text, converts to string, splits into list --
def get_word_count(path_to_file):
    with open(path_to_file) as f:
        book_str = f.read()
    ind_words = book_str.split()
    return len(ind_words), book_str

#-- takes book_str, splits into characters, outputs count --
def get_char_count(book_str):
    char_list = list(book_str.lower())
    char_dict = {}
    temp_list = []
    for char in char_list:
        if char in temp_list:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
            temp_list.append(char)
    return char_dict

#-- sort key for create_list()--
def sort_on(temp_dict):
    return temp_dict["num"]

#-- create list of dictionaries --
def create_list(char_dict):
    dict_list = []
    for char in char_dict:
        temp_dict = {}
        temp_dict["char"] = char
        temp_dict["num"] = char_dict[char]
        dict_list.append(temp_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
    





    