'''
This script calls the OpenLibrary search api with the user-provided keyword and returns the results in the format
"Book 1" by Author 1
"Book 2" by Author 1, Author 2
....
'''

import requests
import json


'''
The response format from the API call:-
{
    "numFound": 629,
    "docs": [
        {...},
        {...},
        {...},
        ...
        {...}]
}
'''
books_json = requests.get('http://openlibrary.org/search.json?q=calcutta+chromosome')

# Representing the JSON response as a Python data structure so that it is easier to manipulate using language primitives.
# 'docs' is the JSON elemnet we are interested in
books_data = json.loads(books_json.text)
docs = books_data['docs']

'''
Each document in "docs" is of the format
Each document specified listed in "docs" will be of the following format: 

{
    cover_i: 258027,
    has_fulltext: true,
    edition_count: 120,
    title: "The Lord of the Rings",
    author_name: [
        "J. R. R. Tolkien"
    ],
    first_publish_year: 1954,
    key: "OL27448W",
    ia: [
        "returnofking00tolk_1",
        "lordofrings00tolk_1",
        "lordofrings00tolk_0",
        "lordofrings00tolk_3",
        "lordofrings00tolk_2",
        "lordofrings00tolk",
        "twotowersbeingse1970tolk",
        "lordofring00tolk",
        "lordofrings56tolk",
        "lordofringstolk00tolk",
        "fellowshipofring00tolk_0"
    ],
    author_key: [
        "OL26320A"
    ],
    public_scan_b: true
}
'''
for doc in docs:
	print('"%s" by %s' %(doc['title'], ", ".join(doc['author_name'])))



'''
References:-
https://openlibrary.org/dev/docs/api/search
http://www.pythonforbeginners.com/requests/using-requests-in-python
http://www.pythonforbeginners.com/python-on-the-web/parsingjson/
'''