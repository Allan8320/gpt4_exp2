import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"


def generate_content(prompt):
    data = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json=data,
            timeout=300
        )

        response.raise_for_status()

        result = response.json()

        return result["response"]

    except requests.exceptions.RequestException as e:
        return "Error connecting to Ollama: " + str(e)


if __name__ == "__main__":
    prompt = "Write three sentences about Artificial Intelligence."

    result = generate_content(prompt)

    print("\nAI RESPONSE:")
    print(result)