from transformers import pipeline

def data():
    for i in range(10):
        yield f"Today's weather is {i}"


pipe = pipeline(model="gpt2")
generated_characters = 0
for out in pipe(data()):
    generated_characters = out[0]["generated_text"]
    print(generated_characters)