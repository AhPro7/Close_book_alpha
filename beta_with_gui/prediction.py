import transformers
from transformers import pipeline
import os
from pdf_pre import *
# Replace this with your own checkpoint
model_checkpoint = "Ahmed007/close-book"
question_answerer = pipeline("question-answering", model=model_checkpoint)
os.system('clear')
name = input('Enter book name in books folder: ')
path = 'book/'+name+'.pdf'
pdf = pdf_pre(path)
pdf.save_pra('beta_with_gui/test.txt')
print(path)
print('\n')
top_class3 = top_3('beta_with_gui/test.txt')
def predict_answer(top_class=top_class3):
    # print('\n__________________________________________________________________________\n\n')
    que = input('Enter your question: ')
    # que='what is loss function?'
    # q = '' +que+''
    top_3 = top_class3.save_top_3(question= que,path='beta_with_gui/top3.txt')
    print('__________________________________________________________________________')
    print(question_answerer(question=que,
                      context=top_3[0])['answer'])
    print('__________________________________________________________________________')
    print(question_answerer(question=que,
                      context=top_3[1])['answer'])
    print('__________________________________________________________________________')
    print(question_answerer(question=que,
                      context=top_3[2])['answer'])

new_question = 'y'
while True or new_question in ['y','n','c']:
    if new_question == 'y':
        predict_answer(path)
        new_question = input('Do you want to ask another question? (y/n): ')
    elif new_question == 'n':
        os.system('clear')
        print('Thank you for using our app!')
        break
    elif new_question =='c':
        os.system('clear')
        predict_answer(path)
        new_question = input('Do you want to ask another question? (y/n): ')
