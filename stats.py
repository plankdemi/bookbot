def get_number_of_words(text):
    split_text = text.split()
    return len(split_text)   

def get_char_repetition(text):
    chars = {}
    for character in text.lower():
        if character not in chars:
            chars[character] = 1
        else:
            chars[character] = chars[character] + 1   
    return chars         

def sorted_list(char_dict):
    nested_dict = []
    for value in char_dict:
        nested_dict.append({"char" : value, "num" : char_dict[value]})

    nested_dict.sort(reverse=True, key=sort_on)

    return nested_dict


def sort_on(items):
    return items["num"]    