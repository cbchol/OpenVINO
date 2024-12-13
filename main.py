import openai

# Replace 'you=r-api-key' with your actual OpenAI API key
openai.api_key = 'your-api-key'

# Example function to generate a response from OpenAI
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Example usage
if __name__ == "__main__":
    prompt = "Once upon a time"
    print(generate_response(prompt))