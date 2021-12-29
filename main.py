import re
import string
import numpy as np
def pre_process(s):
    res = re.sub('['+string.punctuation+']', '', s.lower()).split()
    return res

def make_dictionary(list_of_words):
    sentence_dict = {}
    k = 0
    for word in list_of_words:
        if word not in sentence_dict:
            sentence_dict[word] = k
            k = k+1
    return sentence_dict

def make_vector(dictionary, sentence_words):
    vector = np.zeros(len(dictionary))
    for word in sentence_words:
        vector[dictionary.get(word)] += 1
    return vector

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s1 = "I am, happy!!!"
    s2 = "I am not sad, I really do!"

    w1 = pre_process(s1)
    w2 = pre_process(s2)

    total_words = np.concatenate((w1, w2))
    dictionary = make_dictionary(total_words)

    v1 = make_vector(dictionary, w1)
    v2 = make_vector(dictionary, w2)

    cosine_similarity = np.dot(v1, v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
    print(cosine_similarity)
