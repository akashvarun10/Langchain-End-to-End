#Q&A Chatbot 
from warnings import filterwarnings
filterwarnings('ignore')


from langchain import OpenAI
from dotenv import load_dotenv
import streamlit as st



load_dotenv()


#Function to load OpenAI model and gerenate response
def get_response(question):
    llm=OpenAI(model_name="gpt-3.5-turbo",temperature=0.5)
    response = llm(question)
    return response

##Initialize streamlit app

st.set_page_config(page_title="Q&A Chatbot")

st.header("Langchain Q&A Chatbot")

input = st.text_input("Input:",key = "input")
response = get_response(input)

submit = st.button("Ask Question")

## is ask button is clicked

if submit:
    st.subheader("The Response is:")
    st.write(response)


