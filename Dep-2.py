#important libraries
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

#Method for loading the model
def load_model():
    model = joblib.load("final_model_with_encoder.pkl")
    return model

#Method for loading lottie file
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
    # Load the machine learning model 
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
    #Saving the values comes from the user
    hp_kw = st.slider("Horsepower in kilowatts", 40, 294, step=10)
    age = st.selectbox("Age of the car", (0, 1, 2, 3))
    km = st.slider("Total kilometers", 0, 317000, step=1000)
    gears = st.selectbox("Number of gears in the car", (5, 6, 7, 8))
    make_model = st.selectbox("Select car's model", ('Audi A3', 'Opel Insignia', 'Audi A1', 'Opel Astra', 'Opel Corsa', 'Renault Clio', 'Renault Espace'))
    # Make a dictionary
    my_dict = {
        "hp_kW": hp_kw,
        "age": age,
        "km": km,
        'Gears': gears,
        "make_model": make_model
    }
    # Convert a dictionary into dataframe
    df = pd.DataFrame.from_dict([my_dict])

    st.markdown('<table class="custom-table">', unsafe_allow_html=True)

    # Customize the header names
    header_mapping = {
        'hp_kW': 'Horsepower in KW',
        'age': 'Car age',
        'km': 'Total kilometer',
        'Gears': 'Gears',
        'make_model':  'Car model>>'
    }

    # Create a list of custom headers in the correct order
    custom_headers = [header_mapping.get(original_header, original_header) for original_header in df.columns]

    # Create a list of custom headers in the correct order
    custom_headers = [header_mapping.get(original_header, original_header) for original_header in df.columns]

    # Write the table header with customized values
    table_header = '<tr>' + ''.join(f'<th>{header}</th>' for header in custom_headers) + '</tr>'
    table_header_html = f'<thead>{table_header}</thead>'

    # Remove the default header from the DataFrame
    table_data = df.to_html(index=False, header=False, escape=False)

    # Remove the border and class attributes from the table
    table_data = table_data.replace('border="1" ', '').replace('class="dataframe"', '')

    
    # Replace the ">" symbol
    table_data = table_data.replace('&gt;', '>')

    # Write the table data with custom headers
    table_data_with_headers = table_data.replace('<table', f'<table class="custom-table">{table_header_html}', 1)
    st.markdown(table_data_with_headers, unsafe_allow_html=True)

    st.markdown('</table>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    #Predect Button
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
