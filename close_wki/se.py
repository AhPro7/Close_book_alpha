import transformers
from transformers import pipeline
from selenium import webdriver

import requests

import os

from googlesearch import search
os.system('clear')
query = input("Enter your query: ")
res = list(search(query))
# print()

# get all paragraphs in web page using beautiful soup and store them in a list from web site url

url = res[0]
# add important headers to the request
page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
par = soup.find_all('p')
paragraphs = [i.text for i in par]
# print(paragraphs[0])
# print(url)

# get top3 



model_checkpoint = "Ahmed007/close-book"
question_answerer = pipeline("question-answering", model=model_checkpoint)
for i in [paragraphs[0],paragraphs[1],paragraphs[2]]:
    print(question_answerer(question=query, context=i))
    print('_________________________________________________________')