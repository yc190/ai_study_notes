from dotenv import load_dotenv
import os
from openai import OpenAI
import json

load_dotenv()
client = OpenAI(
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL")
)
model_name = "deepseek-v4.1-flash"

# 待处理文本列表
text_list = [
    "这家餐厅口味很棒，上菜速度很快，强烈推荐！",
    "商品收到有破损，客服回复很慢，体验很差。",
    "东西中规中矩，没有特别惊喜也没有明显缺点。",
    "快递速度很快，包装完好，整体满意。",
    "质量太差，用了两天就坏了，不推荐购买。"
]

result_list = []

for idx, text in enumerate(text_list):
    print(f"\n==== 正在处理第{idx+1}条 ====")
    prompt = f"""
对下面文本做情感分析，只输出JSON，不要多余文字。
字段：content原文，sentiment（正面/负面/中性），score(0~1)
文本：{text}
"""
    resp = client.chat.completions.create(
        model=model_name,
        messages=[{"role":"user", "content":prompt}]
    )
    res_str = resp.choices[0].message.content
    res_data = json.loads(res_str)
    result_list.append(res_data)
    print(res_data)

# 全部处理完成，保存结果到json文件
with open("batch_result.json", "w", encoding="utf-8") as f:
    json.dump(result_list, f, ensure_ascii=False, indent=2)

print("\n✅ 全部处理完成！结果已保存至 batch_result.json")
print(result_list)
