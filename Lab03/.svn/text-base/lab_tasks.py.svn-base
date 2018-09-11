#Jiaqi Yang Lab03 09112018


def filter_by_letter(sentence, c):
    #print("task1\n")
    senList = sentence.split()
    output = []
    for word in senList:
        if(word.startswith(c) or word.endswith(c)):
            if(word not in output):
                output.append(word)
    return output


def get_cumulative_sum():
    #print("task2\n")
    i = 1
    output = []
    for count in range(1,101):
        sum2 = 0
        for count2 in range(1,count+1):
            sum2+=count2
        output.append(sum2)
        #print("S({}) = ".format(count), sum2)
    return output



if __name__ == "__main__":

    s = "the power of this engine matches that of the one we had last year"
    print(filter_by_letter(s, "t"))
    print(get_cumulative_sum())
