import math
import re
from collections import defaultdict


def clean_word(w):
    return ''.join(re.findall(r'\w+', w)).lower()


def clean_multiple_words(words):
    return [clean_word(t) for t in re.findall(r'\w+', words.lower())]


def create_index(docs, words):
    index = defaultdict(list)

    words_set = set(words)
    doc_words_map = {doc['id']: set(doc['text']) for doc in docs}

    for word in words_set:
        for key, value in doc_words_map.items():
            if word in value:
                index[word].append(key)
    return index


def TF_IDF(index, docs, words):
    result = []
    for doc in docs:

        doc_text = doc['text']
        if not any(word in doc_text for word in words):
            continue

        acc = []
        for word in words:
            tf = doc_text.count(word) / len(doc_text)

            numerator = len(docs) - len(index[word]) + 1
            denominator = len(index[word]) + 0.5
            fraction = numerator / denominator

            idf = math.log2(1 + fraction)
            tf_idf = tf * idf
            acc.append(tf_idf)
        result.append({'id': doc['id'], 'weight': sum(acc)})
    return result


def search(docs, words):
    if not docs or not words:
        return []

    if len(words) < 2:
        term_words = {clean_word(words)}
    else:
        term_words = clean_multiple_words(words)

    term_docs = [
        {'id': doc['id'], 'text': clean_multiple_words(doc['text'])}
        for doc in docs
    ]
    index = create_index(term_docs, term_words)

    weighted_docs = TF_IDF(index, term_docs, term_words)
    sorted_docs = sorted(
        weighted_docs,
        key=lambda x: x['weight'],
        reverse=True
    )
    relevant_docs = list(map(lambda doc: doc['id'], sorted_docs))
    return relevant_docs
