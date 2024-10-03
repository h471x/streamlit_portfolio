from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__))))

from utils import file_to_base64

# Path to the local files
font_path = "font/NerdFont.ttf"

font = file_to_base64(font_path)

css_styles = f"""
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
"""