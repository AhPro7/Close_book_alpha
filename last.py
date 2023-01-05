# final

# read the top_3.txt file with all paragraphs with "'\n\n\n'+ '------------------------' +'\n\n\n'" as the separator
# and return a dic of paragraphs
# like this: {'first': 'paragraph 1', 'second': 'paragraph 2', 'third': 'paragraph 3'}
def read_top_3(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
    pra_list = text.split('\n\n\n'+ '------------------------' +'\n\n\n')
    di = {}
    di['first'] = pra_list[0]
    di['second'] = pra_list[1]
    di['third'] = pra_list[2]
    return di

import requests



API_URL = "https://api-inference.huggingface.co/models/Ahmed007/close-book"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
di = read_top_3('top_3.txt')
output = query({
	"inputs": {
		"question": "what is an image classification?",
		"context": di['first']
	},
})

output1 = query({
	"inputs": {
		"question": "what is an image classification?",
		"context": di['second']
	},
})

output2 = query({
	"inputs": {
		"question": "what is an image classification?",
		"context": di['third']
	},
})


print(output)
print(output1)
print(output2)