import streamlit as st
import base64

# Path to the local files
font_path = "font/NerdFont.ttf"
pic_path = "imgs/logo.png"
hatix_img_path = "imgs/hatix.jpg"

# Hide the menu and set page title
st.set_page_config(
    page_title="Hatix Ntsoa",
    page_icon=pic_path,
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Convert the font file to base64 and embed it directly in the CSS
def font_to_base64(font_path: str) -> str:
    with open(font_path, "rb") as font_file:
        data = font_file.read()
        encoded_font = base64.b64encode(data).decode("utf-8")
    return encoded_font

# generate customized link
def custom_link(link: str) -> str:
    return f"""<span style="font-size: 18px;">{link}</span>"""

# Get the base64 representation of the font, the image
font = font_to_base64(font_path)
hatix_img = font_to_base64(hatix_img_path)

# CSS Styles
st.markdown(
    f"""
    <style>
    /* Hide the Streamlit menu */
    header {{display: none; visibility: hidden;}}

    /* Load custom font */
    @font-face {{
        font-family: 'NerdFont';
        src: url(data:font/ttf;base64,{font}) format('truetype');
        font-weight: normal;
        font-style: normal;
    }}

    /* Apply nerd font to all the app */
    *{{
        /* margin: 0;
        padding: 0;
        box-sizing: border-box; */
        font-family: 'NerdFont', monospace !important;
        user-select: none;
        color: #c9d1d9;
        */overflow: hidden !important;*/
    }}

    /* Set the background color to black */
    .stApp {{
        background-color: #010409;
        /* display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        height: 100vh !important; */
    }}

    .content {{
        text-align: center;
    }}

    /* Make the image round */
    .round-img {{
        display: block;
        margin: 0 auto;
        margin-bottom: 20px;
        border-radius: 50%;
        width: 200px;
        height: 200px;
        object-fit: cover;
    }}
    </style>

    <script>
    // Hide the header immediately on load
    document.addEventListener("DOMContentLoaded", function() {{
        document.querySelector("header").style.display = "none";
    }});
    </script>
    """,
    unsafe_allow_html=True
)

# main content
st.markdown(
    f"""
    <img src="data:image/jpg;base64,{hatix_img}" class="round-img"/>

    #### <span>    ~ whoami </span>
    <p style="font-size: 20px;">
    Hello, I'm 
    <span style="font-weight: bold; color: #2e9aff;">Hatix Ntsoa</span>,
    a <span style="font-weight: bold; color: #2e9aff;">software developer</span>
    specializing in <span style="font-weight: bold;">Python</span>,
    web  development,
    and <span style="font-weight: bold; color: #2e9aff;">open-source</span> projects.<br><br>
    I am a passionate <span style="font-weight: bold; color: #2e9aff;">cybersecurity</span> enthusiast
    with a focused aspiration to become
    a <span style="font-weight: bold; color: #2e9aff;">DevSecOps</span> professional.
    </p>

    <br>

    #### <span>    ~ cat projects </span>

    {custom_link(
        "● [Git & GitHub CLI](https://github.com/h471x/git_gh) : Simple Automation Scripts."
    )}

    {custom_link(
        "● [markdown_previewer](https://github.com/h471x/markdown-previewer) : A markdown note-taking tool."
    )}

    {custom_link(
        "● [password_generator](https://github.com/h471x/password_generator) : A Simple CLI Tool to generate passwords."
    )}

    {custom_link(
        "● [port_scanner](https://github.com/h471x/port_scanner) : A Simple CLI Tool to scan open ports."
    )}

    {custom_link(
        "● [web_scraper](https://github.com/h471x/web_scraper) : A Simple CLI Tool to srap the web."
    )}

    {custom_link(
        "● [whois_lookup](https://github.com/h471x/whois_lookup) : A Simple CLI Tool to perform whois lookup."
    )}

    <br>

    #### <span>    ~ cat reachme </span>
    <span style="font-size: 20px;">Feel free to reach me out via [Gmail](mailto:hatixntsoa@gmail.com), [LinkedIn](https://www.linkedin.com/in/h471x) or [GitHub](https://github.com/h471x).</span>

    <br><br>

    <div style="text-align: center; font-size: 16px;">
        Copyright © 2024 h471x
    </div>
    """,
    unsafe_allow_html=True
)
