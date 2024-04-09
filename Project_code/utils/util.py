from PyPDF2 import PdfReader
from langchain.chat_models import ChatOpenAI

def parse_cv(path):
    loader = PdfReader(path)
    text = loader.pages[0].extract_text()
    return text


def get_agent(temperature=0.9):
    agent = ChatOpenAI(model="gpt-3.5-turbo", temperature=temperature)
    return agent

def generate_cover_letter(resume_text, job_listing_text, prompt_template, openai_api_key):
    agent = agent = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9, openai_api_key=openai_api_key)
    resp = agent.invoke(prompt_template.format(resume=resume_text, job_listing=job_listing_text))
    text = resp.content
    return text