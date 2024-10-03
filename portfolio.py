import streamlit as st

from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__))))

from styles import css_styles
from html_contents import html_portfolio

pic_path = "imgs/logo.png"

# Hide the menu and set page title
st.set_page_config(
    page_title="Hatix Ntsoa",
    page_icon=pic_path,
    layout="centered",
    initial_sidebar_state="collapsed",
)

# CSS Styles
st.markdown(css_styles, unsafe_allow_html=True)

# portfolio content
st.markdown(html_portfolio, unsafe_allow_html=True)