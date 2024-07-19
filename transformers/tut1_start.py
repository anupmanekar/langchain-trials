import torch
from transformers import pipeline

tensors = torch.rand(5,6,82)
print(tensors)

#bdd_generator = pipeline(task="text-generation", model="microsoft/phi-2")
#generated = bdd_generator("Generate BDD tests for any general Oauth login requirement")
#print(generated)

classifier = pipeline("sentiment-analysis") # Downloads default distilbert-base-uncased-finetuned-sst-2-english
results = classifier("I am anxious if HanuMan will release in Hindi in Canada")
print (results)

