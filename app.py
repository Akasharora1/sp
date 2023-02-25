pip install openai
pip install python-dotenv

import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

openai.api_key = os.getenv("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")  # Set OpenAI API key

# Set the model ID and prompt for the Spongebob Squarepants dialogue
model_id = "text-davinci-002"
prompt = (
    "Spongebob Squarepants: Hi, I'm Spongebob! What would you like to ask me today?"
)

def get_response(prompt, model_id):
    # Use OpenAI API to generate a response based on the prompt and the GPT-3 model
    response = openai.Completion.create(
        engine=model_id,
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract the generated text from the response
    answer = response.choices[0].text.strip()

    return answer

# Example usage
response = get_response(prompt, model_id)
print(response)
