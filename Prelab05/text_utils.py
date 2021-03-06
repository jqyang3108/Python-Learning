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

