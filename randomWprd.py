# import random
#
#
# def randomWord(str_list):
#
#     elem = random.choice(str_list)
#     str_list.remove(elem)
#     yield random.choice(str_list)
#
#
# a_list =  ['book', 'apple', 'word']
# print(randomWord(a_list))
#
#
#
import random

def random_word(words):
    global word_container
    try:
        word_container
    except NameError:
        word_container = list(words)
    else:
        if len(word_container) == 0:
            word_container = list(words)
    r_word = random.choice(word_container)
    word_container.remove(r_word)
    yield r_word




