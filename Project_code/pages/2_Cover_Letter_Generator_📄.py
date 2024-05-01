import streamlit as st 
from utils.util import *
from utils.prompts import *
import pyperclip
from langchain_openai import OpenAIEmbeddings, ChatOpenAI


st.set_page_config(page_title="Tool", page_icon=":hammer_and_wrench:")

st.title("Is your job posting real or fake?")

st.write("""Please fill all the fields below to verify if the job posting is real or fake.  
         - If the job posting is fake, a message will show to let you know that the job posting is fake.  
         - If the job posting is real, an uploading prompt will show for you to upload your Resume in PDF format.  
         - After uploading your Resume click the submit button, a cover letter will be generated for you based on the job posting and your Resume. 
         """)

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')


job_title = st.text_input("Job Title", "i.e. Data Scientist")
job_desc = st.text_area("Job Description", "Job Description, Responsabilities, Requirements, etc.")
loc = st.text_input("Location", "i.e New York, NY")
comp_name = st.text_input("Company", "i.e. Google")
comp_desc = st.text_area("Company Description", "i.e. Google is a multinational technology company that specializes in Internet-related services and products.")

# Concatenate the input fields into a single text
job_listing_text = f"Job Title: {job_title}\n\nJob Description:\n{job_desc}\n\nLocation: {loc}\n\nCompany: {comp_name}\n\nCompany Description: {comp_desc}"
combined_text = job_title+' '+job_desc+' '+loc+' '+comp_name+' '+comp_desc

tab1, tab2 = st.tabs(['Verify and Generate Cover Letter', 'Just Generate Cover Letter'])

with tab1:
    if 'verified' not in st.session_state:
        st.session_state.verified = False  # Initialize state
    
    verify = st.button("Verify")

    if verify:
        df = create_df(combined_text)
        text = df["text"]
        clean_text_combined=text.apply(clean_text)
        normalize_text_combined = clean_text_combined.apply(normalize_text)
        vectorized_text_combined = vectorize_text(normalize_text_combined)
        model = load_model()
        classif = model.predict(vectorized_text_combined)
        if classif == 0:
            st.session_state.verified = True
            st.success('The job posting is REAL!', icon="✅")
        else:
            st.warning("The job posting is FAKE!", icon='⚠')

    if st.session_state.verified:
        resume_one = st.file_uploader("Upload your Resume", type=['pdf'], key="very_and_cover")
        resume_text = None
        if resume_one is not None:
            resume_text = parse_pdf(resume_one)
        if resume_one is not None:
            st.write('You have uploaded a PDF file.')
            st.write("The following button will generate a cover letter for you based on the job posting and your Resume")
            st.write("Please select also the style of the cover letter")
            cover_letter_style = st.radio("Select style", ("Classic", "Modern"))
            cl_submit1 = st.button("Submit", key='very_and_cover_submit')
            if not openai_api_key.startswith('sk-'):
                st.warning('Please enter your OpenAI API key!', icon='⚠')
            if cl_submit1 and openai_api_key.startswith('sk-'):
                if resume_text is not None and job_listing_text is not None:
                    prompt_template = prompt_template_classic if cover_letter_style == "Classic" else prompt_template_modern
                    cover_letter = generate_cover_letter(resume_text, job_listing_text, prompt_template, openai_api_key)
                    st.subheader("Cover Letter:")
                    st.caption(cover_letter)
                    st.session_state.cover_letter = cover_letter
                else:
                    st.warning("Please upload a resume and provide a job listing.")
            else:
                st.warning("Upload a PDF, your file is not in PDF format.",icon='⚠')
            pass

with tab2:
    resume_2 = st.file_uploader("Upload your Resume", type=['pdf'], key="cover")
    resume_text = None
    if resume_2 is not None:
        resume_text = parse_pdf(resume_2)
    if resume_2 is not None:
        st.write('You have uploaded a PDF file.')
        st.write("The following button will generate a cover letter for you based on the job posting and your Resume")
        st.write("Please select also the style of the cover letter")
        cover_letter_style_2 = st.radio("Select style", ("Classic", "Modern"), key="cover_letter_style_2")
        cl_submit2 = st.button("Submit", key='very_and_cover_submit2')
        if not openai_api_key.startswith('sk-'):
            st.warning('Please enter your OpenAI API key!', icon='⚠')
        if cl_submit2 and openai_api_key.startswith('sk-'):
            if resume_text is not None and job_listing_text is not None:
                prompt_template = prompt_template_classic if cover_letter_style_2 == "Classic" else prompt_template_modern
                cover_letter = generate_cover_letter(resume_text, job_listing_text, prompt_template, openai_api_key)
                st.subheader("Cover Letter:")
                st.caption(cover_letter)
                st.session_state.cover_letter = cover_letter
            else:
                st.warning("Please upload a resume and provide a job listing.")
        pass
