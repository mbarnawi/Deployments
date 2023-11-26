# Streamlit Documentation: https://docs.streamlit.io/


import pickle
import requests
import json
import streamlit as st
import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OrdinalEncoder
import joblib

def load_model():
   
    model = joblib.load("final_model_with_encoder.pkl")

    return model

# Title/Text
st.title("Car Price Predection.")
def main():
    

    # Load the machine learning model and pipeline
     model = load_model()
     hp_kw = st.sidebar.slider("What is the horse bower in kilowatts?", 40, 294, step=1)
     age = st.sidebar.selectbox("What is the age of the car?",(0, 1, 2, 3))
     km = st.sidebar.slider("What is the total kilometer?", 0, 317000, step=1)
# Gears = st.sidebar.slider("How many gears in the car?", 5, 8, step=1)  
     Gears = st.sidebar.selectbox("How many gears in the car?", (5, 6, 7, 8))
     make_model = st.sidebar.selectbox("Select car's model", ('Audi A3', 'Opel Insignia', 'Audi A1', 'Opel Astra', 'Opel Corsa', 'Renault Clio', 'Renault Espace'))
     my_dict = {
     "hp_kW": hp_kw,
     "age": age,
     "km": km,
     'Gears': Gears,
     "make_model": make_model,
     }
     df = pd.DataFrame.from_dict([my_dict])
     st.table(df)
     predict = st.button("Predict")
     result = model.predict(df)
     if predict :
      st.success(result[0])
     

if __name__ == "__main__":
    main()


# To load machine learning model
# import joblib
# filename = "final_model_with_encoder.pkl"
# model=joblib.load(filename)



# Prediction with user inputs
# predict = st.button("Predict")
# result = model.predict(df)
# st.write(f"Predicted Car Price: {result[0]}")

# df = pd.DataFrame.from_dict([my_dict])

# # displaying user inputs before prediction
# st.header("The values you selected is below")
# st.table(df)

# # Prediction with user inputs
# predict = st.button("Predict")
# result = model.predict(df)
# if predict :
#     st.success(result[0])

