from llm_utils import llm_invoke, llm_invoke_json

# 普通调用
ans1 = llm_invoke("一句话解释什么是思维链CoT")
print("普通调用结果：", ans1)

# JSON结构化调用
prompt = """
对下面句子情感分析，输出JSON：content原文，sentiment，score
文本：这家奶茶味道很不错！
"""
ans2 = llm_invoke_json(prompt)
print("\nJSON结果：", ans2)
