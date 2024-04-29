import streamlit as st 
from utils.util import *
from utils.prompts import *
import pyperclip
from langchain_openai import OpenAIEmbeddings, ChatOpenAI


st.set_page_config(page_title="Tool", page_icon=":hammer_and_wrench:")

st.title("Check your Resume")

st.write("""Please fill all the fields below to help you generate and check your Resume to be accord the Job Description.    
         - After uploading your Resume click the submit button, your resume will be checked and compared against the job description and will give you a way to improve your resume. 
         """)

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')


job_title = st.text_input("Job Title", "i.e. Data Scientist")
job_desc = st.text_area("Job Description", "Job Description, Responsabilities, Requirements, etc.")
loc = st.text_input("Location", "i.e New York, NY")
comp_name = st.text_input("Company", "i.e. Google")
comp_desc = st.text_area("Company Description", "i.e. Google is a multinational technology company that specializes in Internet-related services and products.")

# Concatenate the input fields into a single text
job_listing_text = f"Job Title: {job_title}\n\nJob Description:\n{job_desc}\n\nLocation: {loc}\n\nCompany: {comp_name}\n\nCompany Description: {comp_desc}"



resume_one = st.file_uploader("Upload your Resume", type=['pdf'], key="resume")
resume_text = None
if resume_one is not None:
    resume_text = parse_cv(resume_one)
    if resume_one is not None:
        st.write('You have uploaded a PDF file.')
        st.write("The following button will check your resume against the job description.")
        cl_submit1 = st.button("Submit", key='resume_check')
        if not openai_api_key.startswith('sk-'):
            st.warning('Please enter your OpenAI API key!', icon='⚠')
        if cl_submit1 and openai_api_key.startswith('sk-'):
            if resume_text is not None and job_listing_text is not None:
                resume_new = generate_cover_letter(resume_text, job_listing_text, resume_prompt, openai_api_key)
                st.subheader("Resume:")
                st.caption(resume_new)
                st.session_state.resume_new = resume_new
            else:
                st.warning("Please upload a resume and provide a job listing.")
        pass