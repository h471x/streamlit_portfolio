from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), "..")))

from utils.utils import file_to_base64, custom_link

hatix_img_path = "imgs/hatix.jpg"

# Get the base64 representation of files
hatix_img = file_to_base64(hatix_img_path)

html_portfolio = f"""
  <img src="data:image/jpg;base64,{hatix_img}" class="round-img"/>

  #### <span>    ~ whoami </span>
  <p style="font-size: 20px;">
  Hello, I'm 
  <span class="highlight">Hatix Ntsoa</span>,
  a <span class="highlight">software developer</span>
  specializing in <span style="font-weight: bold;">Python</span>,
  web  development,
  and <span class="highlight">open-source</span> projects.<br><br>
  I am a passionate <span class="highlight">cybersecurity</span> enthusiast
  with a focused aspiration to become
  a <span class="highlight">DevSecOps</span> professional.
  </p>

  <br>

  #### <span>    ~ cat projects </span>
  
  ● {custom_link(
    "https://github.com/h471x/git_gh",
    "Git & GitHub CLI",
    " : Simple Automation Scripts."
  )}

  ● {custom_link(
    "https://github.com/h471x/markdown_previewer",
    "markdown_previewer",
    " : A markdown note-taking tool."
  )}

  ● {custom_link(
    "https://github.com/h471x/password_generator",
    "password_generator",
    " : A Simple CLI Tool to generate passwords."
  )}

  ● {custom_link(
    "https://github.com/h471x/port_scanner",
    "port_scanner",
    " : A Simple CLI Tool to scan open ports."
  )}

  ● {custom_link(
    "https://github.com/h471x/web_scraper",
    "web_scraper",
    " : A Simple CLI Tool to srap the web."
  )}

  ● {custom_link(
    "https://github.com/h471x/whois_lookup",
    "whois_lookup",
    " : A Simple CLI Tool to perform whois lookup."
  )}

  <br>

  #### <span>    ~ cat reachme </span>
  <span style="font-size: 20px; display: inline;">
    Feel free to reach me out via
    {custom_link("mailto:hatixntsoa@gmail.com", "Gmail")},
    {custom_link("https://www.linkedin.com/in/hatixntsoa", "LinkedIn")} or
    {custom_link("https://github.com/h471x", "GitHub")}.
  </span>

  <br><br>

  <div class="footer">
    Copyright © 2024 h471x
  </div>
"""
