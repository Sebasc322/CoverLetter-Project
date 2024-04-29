from langchain.prompts import PromptTemplate

prompt_template_classic = PromptTemplate.from_template(
    """Craft a polished cover letter as part of a job application, drawing from the provided resume and job listing details. 
    Your expertise as a professional technical recruiter is crucial in ensuring the cover letter is concise, containing only salutations, 
    a body of four to five information-dense lines, and no more than three paragraphs. 
    Employ a business casual tone to strike the perfect balance between professionalism and approachability. 
    Your task is to seamlessly highlight the synergies between the job requirements and the candidate's experience, 
    specifically focusing on shared technologies, responsibilities, or domains. 
    Illuminate why the candidate is an ideal match for the role, using optimistic and affirmative language throughout. 
    Conclude with an engaging call to action, inviting further discussion or an interview, without including any contact information. 
    Your aim is to create a compelling narrative that underscores the candidate's suitability and eagerness to contribute to the prospective role.
------------        
Resume(Assume that the first two lines are personal details such as name and contact information):
{resume}
------------
Job Listing:
{job_listing}"""
)

prompt_template_modern = PromptTemplate.from_template(
    """Craft a compelling introduction message as part of the job application process, utilizing your expertise as a professional technical recruiter. 
    Start the message with a dynamic opener: 'Hi, I'm [Your Name], [a uniquely crafted tagline that encapsulates your professional essence].' 
    Follow this with a concise, yet richly informative paragraph. 
    This paragraph should employ a business casual tone, seamlessly weaving together highlights of the candidate's resume and key aspects of the job listing. 
    Focus on pinpointing and elaborating on the synergies in technologies, responsibilities, or domains that align the candidate's background with the role's requirements.
    Use language that is both optimistic and assertive to articulate why the candidate is not just a fit, but the right choice for the position. 
    Culminate your message with a compelling call to action that naturally invites further engagement or discussion. 
    Your goal is to create a snapshot of the candidate's professional identity that is both memorable and persuasive, 
    setting the stage for a deeper exploration of their potential contribution to the team.
------------        
Resume(Assume that the first two lines are personal details such as name and contact information):
{resume}
------------
Job Listing:
{job_listing}
------------"""
)

resume_prompt = PromptTemplate.from_template(
    """As a professional technical recruiter, and given the provided resume and job listing details, 
    generate a recommendation to improve the provided resume so it aligns with the job description, include examples in the recommendation, 
    and if possible generate a recommended resume at the end. The recommendations to improve the provided resume should be tailored to the specific job requirements, 
    emphasizing the candidate's relevant skills, experiences, and qualifications. Ensure that the resume is well-structured, concise, and professional, 
    highlighting key achievements and competencies that match the job listing. 
    Use a clear and engaging writing style to capture the attention of potential employers and showcase the candidate's potential value to the organization. 
    Your goal is to create a compelling resume that effectively communicates the candidate's suitability for the position and increases their chances of securing an interview. 
    Give examples, and if possible, provide specific suggestions for improvement based on the job requirements, and a recommended resume.
------------        
Resume(Assume that the first two lines are personal details such as name and contact information):
{resume}
------------
Job Listing:
{job_listing}
------------"""
)
