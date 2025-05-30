from search_engine.search_engine import search


def test_no_doc():
    result = search([], 'shoot')
    assert result == []


def test_correct_doc_search():
    doc1 = "I can't shoot straight unless I've had a pint!"
    doc2 = "Don't shoot shoot shoot that thing at me."
    doc3 = "I'm your shooter."

    docs = [
      {'id': 'doc1', 'text': doc1},
      {'id': 'doc2', 'text': doc2},
      {'id': 'doc3', 'text': doc3},
    ]

    result = search(docs, 'shoot')
    assert result == ['doc1', 'doc2']


def test_case_insentive_search():
    doc1 = "I can't shoot straight unless I've had a pint!"
    doc2 = "Don't shoot shoot shoot that thing at me."
    doc3 = "I'm your shooter."

    docs = [
      {'id': 'doc1', 'text': doc1},
      {'id': 'doc2', 'text': doc2},
      {'id': 'doc3', 'text': doc3},
    ]

    result = search(docs, 'Shoot')
    assert result == ['doc1', 'doc2']


def test_punctuation_insentive_search():
    doc1 = {'id': 'doc1', 'text': "I can't shoot straight unless I've had a pint!"}
    docs = [doc1]

    assert search(docs, 'pint') == ['doc1']
    assert search(docs, 'pint!') == ['doc1']
