# test the moedule
from pdf_pre import *
path = '../alpha/test.pdf'
pdf = pdf_pre(path)
pdf.save_pra('beta_with_gui/test.txt')