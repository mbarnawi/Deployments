# Streamlit Documentation: https://docs.streamlit.io/

import pickle
import requests
import json
import streamlit as st
import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OrdinalEncoder
import joblib
import requests  
from streamlit_lottie import st_lottie 
from datetime import date
import locale

def load_model():
    model = joblib.load("final_model_with_encoder.pkl")
    return model

# Title/Text
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_coding = load_lottiefile("Animation - 1701071073741.json")

st.markdown(
    """
    <style>
    body {
        background-color: lightgray;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def main():
    # Load the machine learning model and pipeline
    model = load_model()

    # Custom styling
    st.markdown(
        """
        <style>
        .main-container {
            background-color: lightgray;
            padding: 20px;
            border-radius: 10px;
        }
        .title {
            color: midnightblue;
            text-align: center;
            margin-bottom: 20px;
            font-size: 28px;
            font-family: Arial, sans-serif;
        }
        .input-label {
            color: navy;
            font-weight: bold;
            font-size: 18px;
            font-family: Arial, sans-serif;
        }
        .result-text {
            color: darkgreen;
            font-size: 20px;
            font-family: Arial, sans-serif;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
    """
       <style>
    .custom-table {
        border-collapse: collapse;
        width: 100%;
        font-family: Arial, sans-serif;
        font-size: 14px;
        color: #333;
    }
    .custom-table th {
        background-color: #f2f2f2;
        font-weight: bold;
        padding: 8px;
        text-align: left;
        border: 1px solid #ddd;
        color: #fff;
        background-color: #007bff;
    }
    .custom-table td {
        padding: 8px;
        border: 1px solid #ddd;
    }
    </style>
    """,
     unsafe_allow_html=True
    )
    # Main container
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Title
    st.markdown('<h1 class="title">Car Price Prediction</h1>', unsafe_allow_html=True)

    # Display the Lottie animation
    st_lottie(lottie_coding, width=400, height=400, speed=1, reverse=False, loop=True)


    # Input form
    st.markdown('<h2 class="input-label">Enter car properties </h2>', unsafe_allow_html=True)

    hp_kw = st.slider("Horsepower in kilowatts", 40, 294, step=1)
    age = st.selectbox("Age of the car", (0, 1, 2, 3))
    km = st.slider("Total kilometers", 0, 317000, step=1)
    gears = st.selectbox("Number of gears in the car", (5, 6, 7, 8))
    make_model = st.selectbox("Select car's model", ('Audi A3', 'Opel Insignia', 'Audi A1', 'Opel Astra', 'Opel Corsa', 'Renault Clio', 'Renault Espace'))

    my_dict = {
        "hp_kW": hp_kw,
        "age": age,
        "km": km,
        'Gears': gears,
        "make_model": make_model
    }
    
    df = pd.DataFrame.from_dict([my_dict])
    st.markdown('<table class="custom-table">', unsafe_allow_html=True)
    st.write(df.to_html(index=False, escape=False), unsafe_allow_html=True)
    st.markdown('</table>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    predict = st.button("Predict")
    
    if predict:
        result = model.predict(df)
        current_date = date.today().strftime("%Y-%m-%d")

        # Set the desired currency
        currency_symbol = "$"
        # Set the desired locale (e.g., "en_US.UTF-8" for US English)
        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

        rounded_price = int(result[0])  # Convert the price to an integer

        # Format the price with the currency symbol and thousands separator
        formatted_price = locale.format_string("%d", rounded_price, grouping=True)

        st.markdown(
            f'<div style="background-color: #cce5ff; padding: 10px;">Predicted Car Price ({current_date}): {formatted_price}{currency_symbol}</div>',
            unsafe_allow_html=True
        )
    # Close the main container
   

if __name__ == "__main__":
    main()