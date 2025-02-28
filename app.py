import streamlit as st

# Define the URL to redirect to
redirect_url = "https://huggingface.co/spaces/DebabrataHalder/RecommendMovies"

# Use an HTML meta refresh tag to perform an immediate redirect
st.markdown(
    f'<meta http-equiv="refresh" content="0; url={redirect_url}" />',
    unsafe_allow_html=True
)
