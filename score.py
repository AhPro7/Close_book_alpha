# gave a pareagraph a score by question

import sys
import re
import os
import PyPDF2
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
    # get the intersection of the question words and the paragraph words
    intersection = set(question_words).intersection(set(pra_words))
    # get the score
    score = len(intersection)/len(question_words)
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
    return top_3

# main function
def main():
    # get the path of the text file
    path = 'test.txt'
    # get the question
    question = input('Please enter your question: ')
    print('------------------------')
    print('------------------------')
    # get the list of paragraphs
    pra_list = read_text_file(path)
    # get the top 3 paragraphs
    top_3 = get_top_3(pra_list, question)
    # print the top 3 paragraphs
    for pra in top_3:
        print(pra)
        print('------------------------')
        print('------------------------')

    #save the top 3 paragraphs
    with open('top_3.txt', 'w') as f:
        for pra in top_3:
            f.write(pra +'\n\n\n'+ '------------------------' +'\n\n\n')

if __name__ == '__main__':
    main()

