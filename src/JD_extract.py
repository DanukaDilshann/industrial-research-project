
# from pdf_reader import pdf_text
import pdfplumber
from pyresparser import ResumeParser
import os
import pandas as pd
# import nltk
# nltk.download()
import spacy
custom_nlp = spacy.load("en_core_web_sm")




# Function to extract text from PDF
def extract_pdf_text(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "/n"
    return text

# # File path to job description PDF
pdf_file = "jd's//Head of Data Analyst.pdf" # Update with your PDF path
pdf_text = extract_pdf_text(pdf_file)
if not pdf_text.strip():
    print("Error: No text extracted from PDF.")
else:
    print("Extracted PDF Text Preview (First 500 chars):")
    print(pdf_text[:500])

# Intelligent skill extraction with pyresparser
def extract_skills_with_pyresparser(file_path):
    if os.path.exists(file_path):
        data = ResumeParser(file_path).get_extracted_data()
        skills = data.get('skills', [])
        exp=data.get("experience",[])
        print("//nSkills extracted by pyresparser:")
        print(pd.DataFrame(skills))
        print(data)
        print(exp)

    else:
        print("File not found for pyresparser skill extraction.")

extract_skills_with_pyresparser(pdf_file)






