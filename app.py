from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = input("Enter your prompt: ")
output = generator(prompt, max_length=80)

print("\nGenerated Text:\n")
print(output[0]["generated_text"])
