import openai
import os
# Setting the API key
openai.api_key = "your api key!"


text1 = input("Paste the column here: ")
text2 = input("Enter the sentence here: ")


# Define the prompt for GPT-3
prompt = f"does {text1} agree with {text2}? reply in yes or no."

# Use the GPT-3 model to generate a response for the prompt
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Extract the generated response
comparison = response["choices"][0]["text"].strip()

# Print the comparison
print("Comparison:")
print(comparison)


