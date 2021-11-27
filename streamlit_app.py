import streamlit as st

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
    st.header("Page B")
else:
    st.header("ini_header")
