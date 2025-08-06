def word_count(book_contents:str) -> int:
    word_count = len(book_contents.split())
    return word_count

def char_count(book_contents:str) -> int:
    lowercase_text = book_contents.lower()
    count_dict = {}
    
    for char in lowercase_text:
        if char.isalpha():
            count_dict[char] = count_dict.get(char, 0) + 1
    
    return count_dict

def sorted_char_count(char_count:dict) -> dict:
    sort_char_count = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    final_dict = []
    for key, value in sort_char_count.items():
        final_dict.append({"char":key, "num":value})
    return final_dict
