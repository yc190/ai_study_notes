'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2026-10-16 22:11:10
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2026-10-16 22:12:04
FilePath: \ai-study\rag_01_load_pdf.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from langchain_community.document_loaders import PyPDFLoader
import re

# 加载PDF文档
loader = PyPDFLoader("test.pdf")
pages = loader.load_and_split()

print(f"PDF总页数：{len(pages)}")

# 合并所有页面文本
raw_text = "\n".join([page.page_content for page in pages])
print("\n====原始文本（前500字符）====")
print(raw_text[:500])

# 文本清洗函数
def clean_text(text: str) -> str:
    # 去除多余换行、多个空格
    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

cleaned_text = clean_text(raw_text)
print("\n====清洗后文本（前500字符）====")
print(cleaned_text[:500])

# 保存清洗后的文本，供后续实验使用
with open("cleaned_doc.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text)

print("\n✅ 文档处理完成，已保存 cleaned_doc.txt")
