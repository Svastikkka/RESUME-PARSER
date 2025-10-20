def get_spacy_doc(file, data):
  nlp = spacy.blank('en')
  db = DocBin()

  for text, annot in tqdm(data):
    doc = nlp.make_doc(text)
    annot = annot['entities']

    ents = []
    entity_indices = []

    for start, end, label in annot:
      skip_entity = False
      for idx in range(start, end):
        if idx in entity_indices:
          skip_entity=True
          break
      if skip_entity==True:
        continue

      entity_indices = entity_indices + list(range(start, end))

      try:
        span = doc.char_span(start, end, label=label, alignment_mode='strict')
      except:
        continue

      if span is None:
        err_data = str([start, end]) + "    " + str(text) + "\n"
        file.write(err_data)

      else:
        ents.append(span)

    try:
      doc.ents = ents
      db.add(doc)
    except:
      pass

  return db


import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
import json
cv_data = json.load(open('data/train/train_data.json', 'r'))
print(len(cv_data))

from sklearn.model_selection import train_test_split
train, test = train_test_split(cv_data, test_size=0.3)
print(len(train), len(test))

file = open('error.txt', 'w')
db = get_spacy_doc(file, train)
db.to_disk('train_data.spacy')
db = get_spacy_doc(file, test)
db.to_disk('test_data.spacy')
file.close()

print("Token Length: ",len(db.tokens))