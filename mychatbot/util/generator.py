import os
import warnings

from PyPDF2 import PdfReader
from langchain.chains.question_answering import load_qa_chain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS


def ready():
    warnings.filterwarnings("ignore")
    os.environ["OPENAI_API_KEY"] = "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"
    doc_reader = PdfReader('./data/guide_1.pdf')

    # Read data from the PDF and split it into chunks
    raw_text = ''
    for i, page in enumerate(doc_reader.pages):
        text = page.extract_text()
        if text:
            raw_text += text

    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
    )
    texts = text_splitter.split_text(raw_text)

    # Create embeddings and a vector store for similarity search
    embeddings = OpenAIEmbeddings()
    docsearch = FAISS.from_texts(texts, embeddings)

    # Load the question-answering chain
    return load_qa_chain(OpenAI(), chain_type="stuff"), docsearch


def give_output(chain, docsearch, query):
    # Perform similarity search and run the chain
    docs = docsearch.similarity_search(query)

    return chain.run(input_documents=docs, question=query)
