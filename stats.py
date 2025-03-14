def get_num_words(text):
    word_count = len(text.split())
    return word_count

def get_char_count(text):
    count_dict = {}
    text = text.lower()
    for char in text:
        if char not in count_dict:
            count_dict[char] = 1
        else:
            count_dict[char] += 1
    return count_dict