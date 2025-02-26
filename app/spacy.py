from spacy_llm.util import assemble

nlp = assemble('/config.cfg')
doc = nlp('You look gorgeous!')
print(doc.cats)

"""
https://github.com/knipknap/receiptparser/blob/master/receiptparser/parser.py
https://github.com/knipknap/receiptparser/blob/master/receiptparser/receipt.py
"""