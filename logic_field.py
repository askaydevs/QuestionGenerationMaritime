'''
import pdftotext
from infant_pipe import process
with open('Solverminds_Data/Sample/004.pdf', 'rb') as f:
    text = pdftotext.PDF(f)

text = '\n\n'.join(text)
print(process(text))
'''

'''
import slate
def extract_text_from_pdf(pdf_path):
    with open(pdf_path) as fh:
        document = slate.PDF(fh, password='', just_text=0)
    for page in document:
        print(page)

extract_text_from_pdf('Solverminds_Data/Sample/004.pdf')
'''


import PyPDF2
from os import listdir
from os.path import isfile, join

path = '/home/askaydevs/Documents/Merged'
onlyfiles = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('.pdf')]
def pdf_to_text(file_path):
    input = PyPDF2.PdfFileReader(open(file_path, 'rb'))
    if input.isEncrypted:
        pass
    else:
        text = ""
        for _ in range (0, input.getNumPages()):
            text += input.getPage(_).extractText()
    return len(text)

print(pdf_to_text('Solverminds_Data/Sample/004.pdf'))
#def get_len_of_docs()
'''
lengths = []
n = 0
for file in onlyfiles:
    lengths.append(pdf_to_text(join(path, file)))
    per = n/2291*100
    n += 1
    print(str(int(per)) + '%')

print(len(lengths))
'''
