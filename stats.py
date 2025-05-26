def get_num_words(text_off_book):
    list_of_words = text_off_book.split()
    return len(list_of_words)

def get_num_chars(text_off_book):
    convert_low = text_off_book.lower()
    list_of_chars = [*convert_low]
    char_dict = {}
    temp_int = 0
    for char in list_of_chars:
        if char in char_dict:
            temp_int = char_dict[char]
            temp_int += 1
            char_dict[char] = temp_int
        else:
            char_dict[char] = 1
    return char_dict


def get_sorted_list(num_chars):
    def sort_on(dict):
        return dict["char"]
    new_list = []
    temp_dict = {}
    for char in num_chars:
        temp_dict = {"char" : f"{char}", "num" : num_chars[char]}
        new_list.append(temp_dict)
        temp_dict = {}
    new_list.sort(key=sort_on)
    return new_list
        

