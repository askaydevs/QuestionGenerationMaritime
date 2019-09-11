'''
import pdftotext
from infant_pipe import process
with open('Solverminds_Data/Sample/004.pdf', 'rb') as f:
    text = pdftotext.PDF(f)

text = '\n\n'.join(text)
print(process(text))
'''


import slate
def extract_text_from_pdf(pdf_path):
    with open(pdf_path) as fh:
        document = slate.PDF(fh, password='', just_text=0)
    for page in document:
        print(page)

extract_text_from_pdf('Solverminds_Data/Sample/004.pdf')
