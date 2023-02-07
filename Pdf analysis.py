from PyPDF2 import PdfReader
import os

def absoluteFilePaths(directory):
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))
pdf_paths = absoluteFilePaths(r'C:\Users\kianv\Desktop\Python\crypto\PDFS')

def get_text(pathfile)
    reader = PdfReader(pathfile)
    # getting a specific page from the pdf file
    page = reader.pages[0]
    # extracting text from page
    text = page.extract_text()
    return(text)

def onlyname(pathfile):
    return(os.path.splitext(pathfile)[0])

for file in pdf_paths:
    with open(str(onlyname(file)), 'w') as f:
        f.write(get_text(file))
 