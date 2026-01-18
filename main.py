import streamlit as st
from chains import Chain
from portfolio import Portfolio
from utils import clean_text
from langchain_community.document_loaders import WebBaseLoader


def create_streamlit_app(llm,portfolio,clean_text):
 st.title("Email Generator")
 url_input=st.text_input("Enter a URL: ", value="GIVEN_URL")
 submit_button=st.button("Submit")

 if submit_button:
    try:
        loader=WebBaseLoader([url_input])
        raw_data=loader.load()
        data=clean_text(raw_data[0].page_content)
        portfolio.load_portfolio()
        jobs=llm.extract_jobs(data)
        for job in jobs:
            skills=job.get('skills',[])
            links=portfolio.query_links(skills)
            email=llm.write_mail(job,links)
            st.code(email,language='markdown')
    except Exception as e:
        st.error(f"An Error Occured: {e}")

if __name__ == "__main__":
    chain=Chain()
    portfolio=Portfolio()
    st.set_page_config(layout="wide",page_title="Email Generator",page_icon="")
    create_streamlit_app(chain,portfolio,clean_text)



