from openai import AzureOpenAI

ENDPOINT = "https://mango-bush-0a9e12903.5.azurestaticapps.net/api/v1"
API_KEY = "4e49e4fb-bf76-47ae-b158-69028640aac6"

API_VERSION = "2024-02-01"
MODEL_NAME = "gpt-4"

client = AzureOpenAI(
    azure_endpoint=ENDPOINT,
    api_key=API_KEY,
    api_version=API_VERSION,
)

MESSAGES = [
    {"role": "user", "content": "In Minecraft terms, explain how 2+2=4."},
]

completion = client.chat.completions.create(
    model=MODEL_NAME,
    messages=MESSAGES,
)

# print(completion.model_dump_json(indent=2))
print(completion.choices[0].message.content)
