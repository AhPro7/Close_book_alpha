import transformers
from transformers import pipeline
import os
from pdf_pre import *
# Replace this with your own checkpoint
model_checkpoint = "Ahmed007/close-book"
question_answerer = pipeline("question-answering", model=model_checkpoint)
os.system('clear')

top = top_3('beta_with_gui/test.txt')
# print('\n__________________________________________________________________________\n\n')
que = input('Enter your question: ')
# que='what is loss function?'
# q = '' +que+''
top_3 = top.get_top_3(que)
print('__________________________________________________________________________')
print(question_answerer(question=que,
                  context=top_3[0])['answer'])
print('__________________________________________________________________________')
print(question_answerer(question=que,
                  context=top_3[1])['answer'])
print('__________________________________________________________________________')
print(question_answerer(question=que,
                  context=top_3[2])['answer'])