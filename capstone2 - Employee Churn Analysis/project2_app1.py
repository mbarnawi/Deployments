import streamlit as st
from streamlit_lottie import st_lottie
import requests
from io import BytesIO

# title of the body
html_temp = """
<div style="background-color:lightblue;padding:10px">
<h2 style="color:black;text-align:center;">Employee Churn Prediction</h2>
</div>"""

st.markdown(html_temp, unsafe_allow_html=True)

# Lottie animation container
lottie_url = "https://lottie.host/cc14a055-8eae-4a82-811c-377ee2e17932/TIEjmWHTsp.json"
lottie_response = requests.get(lottie_url)
lottie_json = lottie_response.json()

st.markdown('<div class="lottie-container">', unsafe_allow_html=True)
st_lottie(lottie_json, speed=1, key="lottie")
st.markdown('</div>', unsafe_allow_html=True)

# Add black background and custom styles
st.markdown(
    """
    <style>
        body {
            background-color: black;
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
        }
        .main-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            padding: 20px;
        }
        .content-container {
            padding: 20px;
        }
        .welcome {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
            font-family: cursive;
        }
        .objective {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
            font-family: cursive;
            white-space: pre-line;
        }
        .inner-header {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
            font-family: cursive;
        }
        .button-container {
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .button {
            background-color: lightgray;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            font-size: 16px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.title("Welcome to Our Prediction System")

# Inner header about employee churn
st.markdown('<h2 class="inner-header">Employee Churn</h2>', unsafe_allow_html=True)
st.markdown(
    '<p class="objective">The objective of this project is to\npredict whether an employee will leave the company or not. By analyzing various factors and using machine learning algorithms, we aim to provide insights into employee churn and help organizations make data-driven decisions.</p>',
    unsafe_allow_html=True
)

# Group members section
st.markdown('<h3 class="inner-header">Conducted by:</h3>', unsafe_allow_html=True)
members = ["Afnan Alotaibi", "Hussan Alzain", "Marwah Barnawi", "Rahaf Saeed", "Salma Mohammed", "Waad Alharthi", "Aeshah Mater", "Atheer Rashed", "Sarah Moshabab"]
for i in range(0, len(members), 2):
    if i + 1 < len(members):
        st.markdown(f'<p class="welcome">{members[i]}, {members[i+1]}</p>', unsafe_allow_html=True)
    else:
        st.markdown(f'<p class="welcome">{members[i]}</p>', unsafe_allow_html=True)

# Button to go to the prediction page
st.markdown('<div class="button-container"><a href="http://localhost:8502/" class="button">Let\'s Predict</a></div>', unsafe_allow_html=True)

# Close main container
st.markdown('</div>', unsafe_allow_html=True)