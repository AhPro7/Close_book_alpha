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


# ____________________________________________________________________________
# make the module 
class pdf_pre:
    def __init__(self, path):
        self.path = path
        self.pdfReader = read_pdf(self.path)
        self.pra = extract_pra(self.pdfReader)
        self.pra_re = extract_pra_re(self.pdfReader)
    
    def save_pra(self, path):
        save_pra(self.pra, path)
# ____________________________________________________________________________

import nltk
nltk.download('punkt')

# read the paragraph and the question
#check if the question answer may be in the paragraph
#return the score
def score(pra, question):
    # get the question words
    question_words = nltk.word_tokenize(question)
    # get the paragraph words
    pra_words = nltk.word_tokenize(pra)
    # get the number of question words in the paragraph
    count = 0
    for word in question_words:
        if word in pra_words:
            count += 1
    # get the score
    score = count/len(question_words)
    return score

# read the text file with all paragraphs with "'\n\n\n'+ '------------------------' +'\n\n\n'" as the separator
# return a list of paragraphs
def read_text_file(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
    return text.split('\n\n\n'+ '------------------------' +'\n\n\n')

# get top 3 paragraphs
def get_top_3(pra_list, question):
    # get the score of each paragraph
    score_list = []
    for pra in pra_list:
        score_list.append(score(pra, question))
    # get the top 3 paragraphs
    top_3 = []
    for i in range(3):
        top_3.append(pra_list[score_list.index(max(score_list))])
        score_list[score_list.index(max(score_list))] = 0

    # replace the new line with space in the top 3 paragraphs only
    for i in range(len(top_3)):
        top_3[i] = top_3[i].replace('\n', '')
    return top_3


class top_3:
    def __init__(self, path):
        self.path = path
        self.pra_list = read_text_file(self.path)

    def get_top_3(self, question):
        return get_top_3(self.pra_list, question)
    #  save the top 3 paragraphs in a text file
    def save_top_3(self, question, path):
        top_3 = self.get_top_3(question)
        with open(path, 'w') as f:
            for pra in top_3:
                f.write(pra +'\n\n\n'+ '------------------------' +'\n\n\n')
        return top_3


