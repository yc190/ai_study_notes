from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL")
)

resp = client.chat.completions.create(
    model="deepseek-v4.1-flash",
    messages=[{"role":"user", "content":"用一句话介绍什么是RAG"}]
)
print(resp.choices[0].message.content)
