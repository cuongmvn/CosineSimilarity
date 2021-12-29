# comparing sentences
import re
import string
import numpy as np


def pre_process(s):
    res = re.sub('[' + string.punctuation + ']', '', s.lower()).split()
    return res


def make_dictionary(list_of_words):
    sentence_dict = {}
    k = 0
    for word in list_of_words:
        if word not in sentence_dict:
            sentence_dict[word] = k
            k = k + 1
    return sentence_dict


def make_vector(dictionary, sentence_words):
    vector = np.zeros(len(dictionary))
    for word in sentence_words:
        vector[dictionary.get(word)] += 1
    return vector


def cosine_similarity(s1, s2):
    w1 = pre_process(s1)
    w2 = pre_process(s2)

    total_words = np.concatenate((w1, w2))
    dictionary = make_dictionary(total_words)

    v1 = make_vector(dictionary, w1)
    v2 = make_vector(dictionary, w2)

    cos_sim = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

    return cos_sim


def main():
    print("Please enter first sentence:")
    s1 = input()
    print("Please enter second sentence:")
    s2 = input()
    # s1 = "I am, happy!!!"
    # s2 = "I am not sad, I really do!"
    # sample value: 0.5773502691896257
    print("How similar these 2 sentence is: ", cosine_similarity(s1, s2))


if __name__ == '__main__':
    main()
