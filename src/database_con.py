import spacy
from pyresparser import ResumeParser

# Load custom spaCy model if available
nlp = spacy.load('en_core_web_sm')

# Resume parsing
data = ResumeParser("C://Users//DanukaDilshanRathnay//Desktop//Head - Data Analyst.pdf" , spacy_model=nlp).get_extracted_data()
print(data)