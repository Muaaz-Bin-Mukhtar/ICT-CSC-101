def make_words_list(input_filename):
    """
    Takes a text file, returns a list of words in that file.

    input_filename: text file

    returns: list
    """
    words_list = []
    with open(input_filename) as input_file:
        for line in input_file:
            word = line.split()[0]
            words_list.append(word)
    return words_list


def sorted_word(word):
    """
    Returns a string with characters rearranged in ASCII order.

    word: string

    returns: string
    """
    return ''.join(sorted(word))


def anagram_sets(wordlist):
    """
    Returns a dictionary with letter groups as strings, and anagrams of those
    strings as keys.

    wordlist: list

    returns: dict
    """
    anagram_dict = {}
    for word in wordlist:
        word_family = sorted_word(word)
        if word_family in anagram_dict:
            anagram_dict[word_family].append(word)
        else:
            anagram_dict[word_family] = [word]

    # Pare down dict to keys with more than one word (ie words with an anagram)
    for word_family, anagram_list in list(anagram_dict.items()):
        if len(anagram_list) < 2:
            del anagram_dict[word_family]
    return anagram_dict


def is_metathesis_pair(word1, word2):
    assert word1 != word2, "Words are the same word."
    assert len(word1) == len(word2), "Words are not equal in length."
    assert sorted_word(word1) == sorted_word(word2), (
            f"Words '{word1}', '{word2}' are not anagrams of eachother.")

    letter_pairs = zip(word1, word2)
    count = 0
    for letter_1, letter_2 in letter_pairs:
        if count > 2:
            return False
        if letter_1 != letter_2:
            count += 1
    if count == 2:
        return True
    elif count > 2:
        return False
    else:
        return "Error." 



def find_metathesis_pairs(anagram_dict):
    """
    Takes a dict mapping word families to words, and looks in each to find
    words that are metathesis pairs (ie words that are the same, except for a
    single pair of swapped letters.
    Returns a list of tuples of these pairs.

    anagram_dict: dict

    returns: list
    """
    metathesis_pairs_list = []
    for word_family in anagram_dict.keys():
        # Prevent iterating over a pair more than once by iterating over a word
        # and subsequent words in list.
        for word1_index in range(len(anagram_dict[word_family])):
            word1 = anagram_dict[word_family][word1_index]
            for word2 in anagram_dict[word_family][word1_index+1:]:
                if word1 != word2:
                    if is_metathesis_pair(word1, word2):
                        metathesis_pairs_list.append((word1, word2))
    return metathesis_pairs_list


def metathesis_pairs(input_filename):
    """
    Return list of metathesis pairs from a file (ie all pairs of words that
    differ by swapping two letters).

    input_filename: text file

    returns: list of tuples
    """
    wordlist = make_words_list(input_filename)
    anagram_dict = anagram_sets(wordlist)

    return find_metathesis_pairs(anagram_dict)
