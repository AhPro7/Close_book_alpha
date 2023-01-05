# make a module for the pdf_pre.py file
import PyPDF2
import re

# for close book project 
# the purpose of this script is extract the pragrphs from any given pdf file
# and save them in a text file

import PyPDF2
import re

# read the pdf file using its path
def read_pdf(path):
    pdfFileObj = open(path, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    return pdfReader

# extract the paragraphs from the pdf file
def extract_pra(pdfReader):
    pra = []
    for i in range(len(pdfReader.pages)):
        pageObj = pdfReader.pages[i]
        pra.append(pageObj.extract_text())
    return pra

# extract the paragraphs from the pdf file using regular expression
def extract_pra_re(pdfReader):
    pra = []
    for i in range(len(pdfReader.pages)):
        pageObj = pdfReader.pages[i]
        pra.append(re.findall(r'(?<=\n\n).*?(?=\n\n)', pageObj.extract_text()))
    return pra

# save the paragraphs in a text file
def save_pra(pra, path):
    with open(path, 'w') as f:
        for i in pra:
            f.write(i +'\n\n\n'+ '------------------------' +'\n\n\n')

# make the module 
class pdf_pre:
    def __init__(self, path):
        self.path = path
        self.pdfReader = read_pdf(self.path)
        self.pra = extract_pra(self.pdfReader)
        self.pra_re = extract_pra_re(self.pdfReader)
    
    def save_pra(self, path):
        save_pra(self.pra, path)
