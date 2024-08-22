from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
import os

# Define schema
schema = Schema(id=ID(stored=True), content=TEXT)

# Create index
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")
ix = create_in("indexdir", schema)
writer = ix.writer()

# Add documents
my_dict = {
    "1": "This is the first sentence.",
    "2": "This is the second sentence with more words.",
    "3": "Another example of a sentence in the dictionary."
}

for key, value in my_dict.items():
    writer.add_document(id=key, content=value)
writer.commit()

# Search the index
with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("sentence")
    results = searcher.search(query)
    for result in results:
        print(result['id'], result['content'])
