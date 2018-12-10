from collections import namedtuple,OrderedDict
WordPosition = namedtuple('WordPosition','word idx')
def get_distinct_words(words):
    a = []
    for b in words:
        if b not in a:
            a.append(b)
            yield b
def get_first_appearances(words):
    b = []
    i=0
    for word in words:
        if word not in b:
            yield WordPosition(word,i)
        b.append(word)
        i+=1
def get_word_to_first_idx(words):
    output = {}
    for b in get_first_appearances(words):
        output[b.word] = b.idx
    return output
def get_word_to_frequency(words):
    a = []
    dic = {}
    for index, word in enumerate(words):
        if word not in a:
            a.append(word)
            dic[word] = 0
        dic[word] += 1
    return dic
def get_word_to_frequency_ordered_by_first_idx(words):
    a = []
    dic = OrderedDict()
    for index, word in enumerate(words):
        if word not in a:
            a.append(word)
            dic[word] = 0
        dic[word] += 1
    return dic

if __name__ == "__main__":
    print("Test Prelab05")
    print("---------------------q1 test ---------------------\n")
    words = ("au", "bu", "cu", "cu", "cu", "du", "du", "du", "du", "du", "eu", "eu", "eu")
    words_gen = (s for s in words)
    print(get_distinct_words(words_gen))
    print(list(get_distinct_words(words_gen)))
    print("\n---------------------end of test q1------------------\n")

    print("---------------------q3 test ---------------------\n")
    words = ("au", "bu", "cu", "cu", "cu", "du", "du", "du", "du", "du", "eu", "eu", "eu")
    words_gen = (s for s in words)
    print(get_first_appearances(words_gen))
    print(list(get_first_appearances(words_gen)))
    print("\n---------------------end of test q3------------------\n")

    print("---------------------q4 test ---------------------\n")
    words = ("au", "bu", "cu", "cu", "cu", "du", "du", "du", "du", "du", "eu", "eu", "eu")
    words_gen = (s for s in words)
    print(get_word_to_first_idx(words_gen))

    print("\n---------------------end of test q4------------------\n")

    print("---------------------q5 test ---------------------\n")
    words = ("au", "bu", "cu", "cu", "cu", "du", "du", "du", "du", "du", "eu", "eu", "eu")
    words_gen = (s for s in words)
    print(get_word_to_frequency(words_gen))
    print("\n---------------------end of test q5------------------\n")



    print("---------------------q6 test ---------------------\n")
    words = ("au", "bu", "cu", "cu", "cu", "du", "du", "du", "du", "du", "eu", "eu", "eu")
    words_gen = (s for s in words)
    print(get_word_to_frequency_ordered_by_first_idx(words_gen))

    print("\nend of test q6------------------")



