from collections import Counter
import pickle


def get_labels():
    """
    This method takes the entire word list and assign the word to its most used category
    :return: a list of word labels
    """
    wordlist = get_wordlist()
    word_freq = []
    for w in wordlist:
        word_freq.append([])
    f = open("GoldStandard.txt", 'rb')
    p = pickle.load(f)
    f.close()
    for r in p:
        id, datetime, wl, label = r[0], r[1], r[2], r[3]
        for word in wl:
            word_freq[wordlist.index(word)].append(label)

    labels = []
    for i in range(len(word_freq)):
        t = Counter(word_freq[i]).most_common(3)
        labels.append(t[0][0])

    return labels


def get_numbered_labels():
    """
    This method returns the label list in a numbered format
    With RAT -> 0, Crypter -> 1, and Keylog -> 2
    :return:
    """
    labels = get_labels()
    dict = {"RAT": 0, "Crypter":1, "Keylog": 2}

    return [dict[l] for l in labels]


def get_wordlist():
    """
    This method load the wordlist
    :return: the full word list
    """
    f = open("Wordlist-GoldStandard.pkl", 'rb')
    p = pickle.load(f)
    f.close()
    return p


def get_sentences():
    """
    This method parse the query data and generate one sentence for each thread
    :return: a list of sentences; each sentence is a list of words
    """
    f = open("GoldStandard.txt", 'rb')
    p = pickle.load(f)
    f.close()
    sentences = []
    for r in p:
        id, datetime, wordlist, label = r[0], r[1], r[2], r[3]
        sentences.append(wordlist)

    return sentences