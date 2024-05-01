from PyPDF2 import PdfReader
from langchain.chat_models import ChatOpenAI
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack
import joblib
import en_core_web_sm
import pandas as pd


def parse_pdf(path):
    loader = PdfReader(path)
    text = loader.pages[0].extract_text()
    return text

def generate_cover_letter(resume_text, job_listing_text, prompt_template, openai_api_key):
    agent = ChatOpenAI(model="gpt-4-turbo", temperature=0.9, openai_api_key=openai_api_key)
    resp = agent.invoke(prompt_template.format(resume=resume_text, job_listing=job_listing_text))
    text = resp.content
    return text

def create_df(text):
    df = pd.DataFrame({'text': [text]})
    return df

def clean_text(text):

    text = text.lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z0-9]', ' ', text)
    tokens = nltk.word_tokenize(text)
    stop_words = set(nltk.corpus.stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    cleaned_text = ' '.join(tokens)

    return cleaned_text

nlp = en_core_web_sm.load()
def normalize_text(text):
    # Tokenize the text and apply lemmatization
    doc = nlp(text)
    normalized_words = [token.lemma_ for token in doc]
    normalized_text = ' '.join(normalized_words)
    return normalized_text

def vectorize_text(text):
    # Vectorize the text using TF-IDF
    tfidf = joblib.load('/mount/src/coverletter-project/Project_code/utils/TfidVectr.pkl')
    vectorized_text = tfidf.transform(text)
    return vectorized_text

def load_model():
    # Load the pre-trained model
    model = joblib.load('/mount/src/coverletter-project/Project_code/utils/job_classifier_model.pkl')
    return model
