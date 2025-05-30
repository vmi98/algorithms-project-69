import re


def clean_word(w):
    return ''.join(re.findall(r'\w+', w)).lower()


def search(docs, word):
    if not docs or not word:
        return []

    term_word = clean_word(word)
    docs_found = []
    for doc in docs:
        tokens = [
            clean_word(t)
            for t in re.findall(r'\w+', doc['text'].lower())
        ]
        if term_word in tokens:
            docs_found.append(doc['id'])
    return docs_found
