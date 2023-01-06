import wikipedia as wp
import wikipediaapi

import os
from transformers import pipeline


wp.set_lang("en")
os.system('clear')

query = input("Enter your query: ")
print("\n")
title = wp.search(query, results = 10)
# print tiltes with index to make user choose between the results
for i in range(len(title)):
    print(i, title[i])

# get the index of the result user wants
index = int(input("\nEnter the index of the result you want: "))
title = str(title[index])
print('the title is: ' + title + '\n')

wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
)

page_py = wiki_wiki.page(title)
# print(page_py.text)
wiki_html = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.HTML
)
p_html = wiki_html.page(title)
# get all paragraphs between <p> and </p> and store them in a list
paragraphs = []
start = 0
end = 0
while True:
    start = p_html.text.find('<p>', end)
    end = p_html.text.find('</p>', start)
    if start == -1 or end == -1:
        break
    paragraphs.append(p_html.text[start+3:end])


# get top3 paragraphs that have the most keywords with the query in them
keywords = query.split()
top3 = []
for i in range(3):
    max = 0
    max_index = 0
    for j in range(len(paragraphs)):
        count = 0
        for k in keywords:
            if k in paragraphs[j]:
                count += 1
        if count > max:
            max = count
            max_index = j
    top3.append(paragraphs[max_index])
    paragraphs.pop(max_index)

# get the summary of the page
summary = page_py.summary
summary2=paragraphs[0]
# add the summary to the first of top3 paragraphs
top3.insert(0, summary)
top3.insert(0, summary2)

# get answer from the top3 paragraphs

model_checkpoint = "Ahmed007/close-book"
question_answerer = pipeline("question-answering", model=model_checkpoint)
os.system('clear')
print('the question is: ' + query + '\n')
print('\n _________________________________________________________ \n')
for i in range(len(top3)):
    print('the answer ' + str(i+1) + ' is: ')
    print(question_answerer(question=query, context=top3[i])['answer'])
    print('\n _________________________________________________________ \n')