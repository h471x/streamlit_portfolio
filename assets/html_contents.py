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

  {custom_link(
      "● [Git & GitHub CLI](https://github.com/h471x/git_gh) : Simple Automation Scripts."
  )}

  {custom_link(
      "● [markdown_previewer](https://github.com/h471x/markdown_previewer) : A markdown note-taking tool."
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
  <span style="font-size: 20px;">Feel free to reach me out via [Gmail](mailto:hatixntsoa@gmail.com), [LinkedIn](https://www.linkedin.com/in/hatixntsoa) or [GitHub](https://github.com/h471x).</span>

  <br><br>

  <div class="footer">
    Copyright © 2024 h471x
  </div>
"""
