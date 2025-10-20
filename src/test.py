import sys, fitz
import spacy

nlp = spacy.load('output/model-best')
doc = nlp('My name is Manshu Sharma. I worked independent. I have 5+ years of experience')
for ent in doc.ents:
  print(ent.text, " >>>>>> ", ent.label_)
