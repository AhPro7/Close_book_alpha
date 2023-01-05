# test the moedule
from pdf_pre import *
# path = 'book/test.pdf'
# pdf = pdf_pre(path)
# pdf.save_pra('beta_with_gui/test.txt')
# test the module top_3
path = 'beta_with_gui/test.txt'
top = top_3(path)
top.get_top_3('what is an image classification?')
top_33=top.save_top_3('what is an image classification?','beta_with_gui/top.txt')
print(top_33[0])