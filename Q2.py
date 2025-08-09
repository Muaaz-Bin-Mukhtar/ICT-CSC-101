from bisect import bisect_left

def index(lst, target):
    """If target is in list, returns the index of target; otherwise returns None"""
    i = bisect_left(lst, target)
    if i != len(lst) and lst[i] == target:
        return i
    else:
        return None

def interlock(str1, str2):
    "Takes two strings of equal length and 'interlocks' them."
    if len(str1) == len(str2):
        lst1 = list(str1)
        lst2 = list(str2)
        result = []
        for i in range(len(lst1)):
            result.append(lst1[i])
            result.append(lst2[i])
        return ''.join(result)
    else:
        return None

def interlockings(word_lst):
    """Checks each pair of equal-length words to see if their interlocking is a word; prints each successful pair and the total number of successful pairs."""
    total = 0
    for i in range(1, 12):  # 12 because max word length is 22
        # to shorten the loops, get a sublist of words of equal length
        sub_lst = filter(lambda x: len(x) == i, word_lst)
        for word1 in sub_lst[:-1]:
            for word2 in sub_lst[sub_lst.index(word1)+1:]: # pair word1 only with words that come after word1
                word1word2 = interlock(word1, word2) # interlock word1 with word2
                word2word1 = interlock(word2, word1) # interlock word2 with word1
                if index(lst, word1word2): # check to see if word1word2 is actually a word
                    total += 1
                    print ("Word 1: %s, Word 2: %s, Interlock: %s" % (word1, word2, word1word2))
                if index(lst, word2word1): # check to see if word2word1 is actually a word
                    total += 1
                    print ("Word 2, %s, Word 1: %s, Interlock: %s" % (word2, word1, word2word1))
    print ("Total interlockings: ", total)
