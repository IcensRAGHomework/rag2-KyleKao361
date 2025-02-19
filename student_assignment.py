from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)
from rich import print as pprint

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    docs = loader.load()
    splitter = CharacterTextSplitter()
    result = splitter.split_documents(docs)
    return result[-1]

def hw02_2(q2_pdf):
    loader = PyPDFLoader(q2_pdf)
    docs = loader.load()
    full_text = "\n".join([page.page_content for page in docs])
    splitter2 = RecursiveCharacterTextSplitter(
           separators=[r"第 (?:.*) (?:條|章)(?: |\n)"],  # 使用正則表達式來匹配 "第 [中文數字] 章" 或 "第 [阿拉伯數字] 條"
    chunk_size=10,
    chunk_overlap=0,
    is_separator_regex=True  # 啟用正則表達式模式
        )
    
    return len(splitter2.split_text(full_text))

print(hw02_2(q2_pdf))

