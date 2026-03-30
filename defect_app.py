import streamlit as st
from dotenv import load_dotenv
load_dotenv()# to access the API Key from .env file
import google.generativeai as genai # to access the models
from PIL import Image # pillow is used to load,save,convertthe format and mnupulate the image
st.set_page_config(page_title='structural defect analysis using AI',page_icon='֎',layout='wide')


st.title('AI Assistant for :green[Structural Defect Analysis]')
st.divider()
st.subheader('A Web based app using streamlit that allows users to upload image of a building structures and to analyze the defects using a :blue[gemini model]',divider=False)
with st.expander('About'):
    st.markdown(f'This is used to detect the structural defect in given images like cracks,misallignments using AI system')
st.subheader('Input the image here : ')
input_image=st.file_uploader('click here',type=['png','jpeg','jpg'])
img=''
if input_image:
    img=Image.open(input_image).convert('RGB')
    st.image(img,caption='Uploaded Successfully')
    
prompt=f'''Act as a Structural and civil engineer and provide the necessary details in the proper bullet points
more precise way(maximum 5 points) for the following questions :

1. is there any structural defect such as cracks,bends,damages in the given image ?
2. what id the probablity of the detected defect ?
3. what si the severity level of the defect like minor,moderate,major ?
4. what is the possible cause for the given defect,considering the material damage,envirnment damage ?
5. Say whether we can repair the defect or not ? If not say whether we need to replace this or not ?
6. Suggest the remedies to repair the defect
7. say whether the defect  will cause any damage to the surrounding and give probablity for it.
8. say whether we need to monitor the defected area after the repair or replacements?
9. Give the cost range for repair or replacement in rupees
10. generate the summary on the insights.

'''

import os
key=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)

def generate_result(prompt,img):
    model =genai.GenerativeModel('gemini-2.5-flash')
    result=model.generate_content([prompt, img])
    return result.text
submit=st.button('Analyse the defect 🔗 ')
if submit:
    with st.spinner('Analyzing....🌐'):
        response=generate_result(prompt,img)
        st.markdown('## green:[Results]')
        st.write(response)  