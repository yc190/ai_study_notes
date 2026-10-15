from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL")
)
model_name = "deepseek-v4.1-flash"

# 测试问题（简单逻辑推理题，适合观察CoT效果）
question = """
商店里一支笔5元，一个本子比笔贵3元。
买2支笔和3个本子一共要多少钱？
"""

# 1. 普通提问
prompt_normal = f"直接给出答案，只输出最终数字：{question}"

# 2. CoT 思维链提示
prompt_cot = f"""
一步步思考，先写出推理过程，最后给出答案。
问题：{question}
"""

print("=====【普通Prompt结果】=====")
res1 = client.chat.completions.create(model=model_name, messages=[{"role":"user", "content":prompt_normal}])
print(res1.choices[0].message.content)

print("\n=====【CoT思维链Prompt结果】=====")
res2 = client.chat.completions.create(model=model_name, messages=[{"role":"user", "content":prompt_cot}])
print(res2.choices[0].message.content)
