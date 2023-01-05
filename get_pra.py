# for close book project 
# the purpose of this script is extract the pragrphs from any given pdf file
# and save them in a text file

import PyPDF2
import os
import sys
import re

# read the pdf file using its path
def read_pdf(path):
    pdfFileObj = open(path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
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

# main function
def main():
    # get the path of the pdf file
    path = 'test.pdf'
    # get the pdf file
    pdfReader = PyPDF2.PdfReader(path)
    # extract the paragraphs
    pra = extract_pra(pdfReader)
    # save the paragraphs
    save_pra(pra, 'test.txt')

if __name__ == '__main__':
    main()