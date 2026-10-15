from dotenv import load_dotenv
import os
from openai import OpenAI
import json

# 加载环境变量，只加载一次
load_dotenv()

client = OpenAI(
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL")
)
MODEL_NAME = "deepseek-v4.1-flash"


def llm_invoke(prompt: str, model: str = MODEL_NAME):
    """
    通用LLM调用函数
    :param prompt: 用户提示词
    :param model: 模型名称
    :return: 返回文本结果
    """
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.choices[0].message.content


def llm_invoke_json(prompt: str, model: str = MODEL_NAME):
    """
    调用LLM并且自动解析返回JSON
    """
    res_str = llm_invoke(prompt, model)
    return json.loads(res_str)
