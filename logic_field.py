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

def pdf_to_text(filepath):
    print('Getting text content for {}...'.format(filepath))
    process = subprocess.Popen(['pdf2txt.py', filepath], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = process.communicate()

    if process.returncode != 0 or stderr:
        raise OSError('Executing the command for {} caused an error:\nCode: {}\nOutput: {}\nError: {}'.format(filepath, process.returncode, stdout, stderr))

    return stdout.decode('utf-8')
