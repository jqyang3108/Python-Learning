def get_ngrams(words,n):
    b=[]
    for index,word in enumerate(words):
        b.append(word)
        if index >= n-1:
            count =n
            index2 = index-(n-1)
            c=[]
            while count !=0:
                c.append(b[index2])
                index2 += 1
                count -= 1
            yield tuple(c)
def get_distinct_ngrams(words,n):
    b=[]
    d=[]
    for index,word in enumerate(words):
        b.append(word)
        if index >= n-1:
            count =n
            index2 = index-(n-1)
            c=[]
            while count !=0:
                c.append(b[index2])
                index2 += 1
                count -= 1
            if c not in d:
                d.append(c)
                yield tuple(c)
def get_distinct_unordered_ngrams(words,n):
    b=[]
    d=[]
    for index,word in enumerate(words):
        b.append(word)
        if index >= n-1:
            count =n
            index2 = index-(n-1)
            c=[]
            while count !=0:
                c.append(b[index2])
                index2 += 1
                count -= 1
            if set(c) not in d:
                d.append(set(c))
                yield tuple(c)
def get_ith_ngram(words,n,i):
    b=[]
    d=[]
    for index,word in enumerate(words):
        b.append(word)
        if index >= n-1:
            count =n
            index2 = index-(n-1)
            c=[]
            while count !=0:
                c.append(b[index2])
                index2 += 1
                count -= 1
            d.append(tuple(c))
    if (d==[]):
        return tuple()
    else:
        return d[i]
if __name__ == "__main__":
    n = 9
    test_list1 = ['a','b','c','d','a','b','c','d']

    n = 3


    #=================test1==================
    n = 4
    test_list1 = ['a','b','c','d','a','b','c','d']
    print("\n\nproblem1\n",get_ngrams(test_list1,n))
    print(list(get_ngrams(test_list1,n)))


 #=================test2==================
    n = 3
    test_list1 = ['a','b','c','b','a','b','c','d']
    print("\n\nproblem2\n",get_distinct_ngrams(test_list1,n))
    print(list(get_distinct_ngrams(test_list1,n)))

    n=3
    test_list1 = ['a','b','c','b','a','b','c','d']
    print("\n\nproblem3\n",get_distinct_unordered_ngrams(test_list1,n))
    print(list(get_distinct_unordered_ngrams(test_list1,n)))


    n=3
    i=2
    test_list1 = ['a','b','c','d','a']

    print("\n\nproblem4\n",get_ith_ngram(test_list1,n,i))
