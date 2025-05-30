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
            docs_found.append(
                {'doc_id': doc['id'],
                 'word_repeat': tokens.count(term_word)}
            )
    sorted_docs_found = sorted(
        docs_found,
        key=lambda x: x['word_repeat'],
        reverse=True
    )
    relevant_docs = list(map(lambda doc: doc['doc_id'], sorted_docs_found))
    return relevant_docs

