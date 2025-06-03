## Search engine 

The project is part of Hexlet course assignments. It implements a simple search engine that can perform searches on a collection of documents. The search engine supports text preprocessing to handle punctuation and case insensitivity and uses the TF-IDF metric to rank search results by relevance.


### Hexlet tests and linter status:
[![Actions Status](https://github.com/vmi98/algorithms-project-69/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/vmi98/algorithms-project-69/actions)

## Features

- Exact Search: Search for documents containing a specific term.
- Fuzzy Search: Search for documents containing any of the terms in the query.
- Text Preprocessing: Convert text to lowercase and remove punctuation to ensure accurate search results.
- Relevance Ranking: Use TF-IDF (Term Frequency-Inverse Document Frequency) to rank documents by relevance.

## Tech Stack

- Python
- Ruff (linting)
- pytest (testing)
- uv (package management)

## Installation
```
git clone https://github.com/vmi98/algorithms-project-69.git
cd python-oop-project-101

make install
```

## Run tests
```
make test
```

## Usage

You can use the search engine by importing the search function and passing a list of documents and a query string. Each document should be represented as a dictionary with id and text keys.

```
  from search_engine.search_engine import search

  doc1 = "I can't shoot straight unless I've had a pint!"
  doc2 = "Don't shoot shoot shoot that thing at me."
  doc3 = "I'm your shooter."

  docs = [
      {'id': 'doc1', 'text': doc1},
      {'id': 'doc2', 'text': doc2},
      {'id': 'doc3', 'text': doc3},
  ]

  result = search(docs, 'shoot at me')
  print(result)  # ['doc2', 'doc1']
```
