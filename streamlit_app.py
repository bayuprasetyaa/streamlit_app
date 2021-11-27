import streamlit as st
from home import pageB

st.title("My First App using streamlit")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# Sidebar
page_a = st.sidebar.button("Page A")
page_b = st.sidebar.button("Page B")

# Navigation
if page_a:
    st.header("Page A")
elif page_b:
    pageB()
else:
    st.header("ini_header")
