import streamlit as st
import streamlit.components.v1 as components

# HTML code that triggers an automatic redirect
html_code = """
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="refresh" content="0; url=https://huggingface.co/spaces/DebabrataHalder/RecommendMovies" />
  </head>
  <body>
    <p>If you are not redirected automatically, click 
      <a href="https://huggingface.co/spaces/DebabrataHalder/RecommendMovies">here</a>.
    </p>
  </body>
</html>
"""

# Render the HTML code in a Streamlit component
components.html(html_code, height=0, width=0)
