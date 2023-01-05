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

#print the top 3 paragraphs
def print_top_3(top_3):
	print('The first paragraph is: ')
	print('------------------------')
	print(top_3['first'])
	print('------------------------')
	print('------------------------')
	print('The second paragraph is: ')
	print('------------------------')
	print(top_3['second'])
	print('------------------------')
	print('------------------------')
	print('The third paragraph is: ')
	print('------------------------')
	print(top_3['third'])
	print('------------------------')
	print('------------------------')