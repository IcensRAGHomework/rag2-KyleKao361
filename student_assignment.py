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
    text = ''
    for page in docs:
        text += page.page_content
    splitter2 = RecursiveCharacterTextSplitter(
           separators=[r'\n\s*第\s*.{1,3}\s*章', r'\n\s*第\s*.{1,5}\s*條'],  # 使用正則表達式來匹配 "第 [中文數字] 章" 或 "第 [阿拉伯數字] 條"
    chunk_size=10,
    chunk_overlap=0,
    is_separator_regex=True  # 啟用正則表達式模式
        )
    
    return len(splitter2.split_text(text))

