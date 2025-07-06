def word_count(book_text) :
    words = book_text.split()
    return len(words)

def character_counts(book_text) :
    words = book_text.lower()
    character_dictionary = {}
    for character in words :
        if character in character_dictionary :
            character_dictionary[character] += 1
        else :
            character_dictionary[character] = 1
    return character_dictionary

def sort_on(dict_item):
    return dict_item["num"]

def sort_character_counts(char_dict):
    result = []
    for char in char_dict:
        result.append({"char" : char, "num" : char_dict[char]})
    result.sort(reverse=True, key=sort_on)
    return result