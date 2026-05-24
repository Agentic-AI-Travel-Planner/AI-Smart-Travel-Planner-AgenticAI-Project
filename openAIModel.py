import os
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()

model_client = OpenAIChatCompletionClient(
    model="gemini-2.5-flash",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.getenv("GEMINI_API_KEY"),
)