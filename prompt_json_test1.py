from dotenv import load_dotenv
import os
from openai import OpenAI
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL")
)

prompt = """
你是文本分类助手。
请把下面用户文本做情感分类，输出严格JSON格式，不要额外解释。
字段：content原文，sentiment情感(正面/负面/中性), score(0~1分数)
文本：这家店服务很好，菜品味道很不错。
"""

resp = client.chat.completions.create(
    model="deepseek-v4.1-flash",
    messages=[{"role":"user", "content":prompt}]
)
result_str = resp.choices[0].message.content
print("原始返回字符串：")
print(result_str)

# 把字符串转为Python字典，程序直接读取字段
result_json = json.loads(result_str)
print("\n解析后的结果：")
print("原文：", result_json["content"])
print("情感：", result_json["sentiment"])
print("分数：", result_json["score"])
