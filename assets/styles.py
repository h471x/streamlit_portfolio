from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), "..")))

from utils.utils import file_to_base64

# Path to the local files
font_path = "font/NerdFont.ttf"

font = file_to_base64(font_path)

css_styles = f"""
  <style>
  /* root element for theme changing */
  :root {{
    --primary-color: #c9d1d9;
    --background-color: #010409;
    --highlight-color: #2e9aff;
  }}

  .lightmode {{
    --primary-color: #252525;
    --background-color: #dddddd;
    --highlight-color: #0969da;
  }}

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
    color: var(--primary-color);
    */overflow: hidden !important;*/
  }}

  /* Set the background color to black */
  .stApp {{
    background-color: var(--background-color);
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

  .footer {{
    text-align: center;
    font-size: 16px;
  }}

  .highlight {{
    font-weight: bold;
    color: var(--highlight-color);
  }}

  /* Apply colors for links */
  .custom-link {{
    font-weight: bold;
    color: var(--highlight-color) !important;
  }}
  </style>
"""