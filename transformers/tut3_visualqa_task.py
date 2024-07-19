from transformers import pipeline

vqa = pipeline(task="document-question-answering", model="impira/layoutlm-document-qa")

output = vqa(image="stock-chart-1.png", question="What is the lowest volume?")

print(output)