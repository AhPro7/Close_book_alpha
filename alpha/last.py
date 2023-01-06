import transformers
from transformers import pipeline

model_checkpoint = "Ahmed007/close-book"
question_answerer = pipeline("question-answering", model=model_checkpoint)
print(question_answerer(question='1',
                      context='''
The histogram is the most basic graph type for visualizing a distribution. It is a specific kind of bar chart that presents the tabulated frequency of data over distinct intervals, “called bins”
The entire sample is divided into these bins, and the height of each bar shows the number of observations within each interval. Histograms can show where values are concentrated within a distribution, where extreme values are, and whether there are any gaps or unusual values.
					  '''))
