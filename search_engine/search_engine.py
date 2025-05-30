import re


def search(docs, word):
    if not docs or not word:
        return []
    docs_found = [
        doc['id'] for doc in docs
        if word.lower() in re.findall(r'\w+', doc['text'].lower())
    ]
    return docs_found
