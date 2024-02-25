import streamlit as st 

st.set_page_config(page_title="Tool", page_icon=":hammer_and_wrench:")

st.title("Is your job posting real or fake?")

st.write("""Please fill all the fields below to verify if the job posting is real or fake.  
         - If the job posting is fake, a message will show to let you know that the job posting is fake.  
         - If the job posting is real, an uploading prompt will show for you to upload your Resume in PDF format.  
         - After uploading your Resume click the submit button, a cover letter will be generated for you based on the job posting and your Resume. 
         """)

st.text_input("Job Title", "Data Scientist")
st.text_input("Job Description", "sdfghjklññlkjhgfd")
st.text_input("Location", "Baltimore,Maryland")

tab1, tab2 = st.tabs(['Verify and Generate Cover Letter', 'Just Generate Cover Letter'])

with tab1:
    if 'verified' not in st.session_state:
        st.session_state.verified = False  # Initialize state
    
    verify = st.button("Verify")

    if verify:
        classif = 'real'  # Assume classification happens here
        if classif == 'real':
            st.session_state.verified = True
            st.success('The job posting is REAL!', icon="✅")
        else:
            st.warning("The job posting is FAKE!", icon='⚠')

    if st.session_state.verified:
        resume_one = st.file_uploader("Upload your Resume", type=['pdf'], key="very_and_cover")
        if resume_one is not None:
            st.write('You have uploaded a PDF file.')
            st.write("The following button will generate a cover letter for you based on the job posting and your Resume")
            cl_submit1 = st.button("Submit", key='very_and_cover_submit')
            if cl_submit1:
                st.write("Your cover letter has been generated and is ready for you to copy.")
                st.caption('''  
                        
                        Dear Hiring Manager,  

                        I am a Data Scientist with 3 years of experience
                        
                        wanted to
                        ''')
            else:
                st.warning("Upload a PDF, your file is not in PDF format.",icon='⚠')
            pass

with tab2:
    resume_2 = st.file_uploader("Upload your Resume", type=['pdf'], key="cover")
    if resume_2 is not None:
        st.write('You have uploaded a PDF file.')
        st.write("The following button will generate a cover letter for you based on the job posting and your Resume")
        cl_submit = st.button("Submit")
        if cl_submit:
            st.write("Your cover letter has been generated and is ready for you to copy.")
            st.caption('''  
                    
                    Dear Hiring Manager,  

                    I am a Data Scientist with 3 years of experience
                     
                    wanted to
                    ''')
    else:
        st.warning("Upload your resume in PDF format",icon='⚠')