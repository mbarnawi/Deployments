import timeit
import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
import requests
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


# Set the background color
st.markdown("<style>body {background-color: #949191;}</style>", unsafe_allow_html=True)

# Larger title with white color
st.markdown("<h1 style='text-align: center; font-size: 3.5em; color: white;'>Credit Card Fraud !</h1>", unsafe_allow_html=True)

# Add empty space
st.markdown("<br><br>", unsafe_allow_html=True)

# Display your Lottie animation with increased height
animation_url = "https://lottie.host/e03cc179-08ac-4afa-9d56-765cbb67fcf6/082ASWRCYT.json"
st_lottie(animation_url, speed=1, height=300, key="animation")

#@st.cache_data
#def load_data():
  #  return pd.read_csv('creditcard.csv')

#df = load_data()

# Load the data using st.cache_data to speed up the app
def load_data():
    return pd.read_csv('data2.csv.gz', compression='gzip')

df = load_data()

# Show what the dataframe looks like
if st.sidebar.checkbox('Show what the dataframe looks like'):
    st.write(df.head(100))
    st.write('Shape of the dataframe: ', df.shape)

# Checkbox to show pie chart
show_pie_chart = st.sidebar.checkbox('Show Pie Chart')

# Display pie chart if the checkbox is checked
if show_pie_chart:
    fig, ax = plt.subplots(figsize=(6, 6))
    df['Class'].value_counts().plot.pie(autopct='%1.1f%%', colors=['green', 'red'], labels=['Valid', 'Fraud'], explode=(0, 0.1), startangle=90)
    plt.title('Distribution of Classes (Pie Chart)')
    st.pyplot(fig)

# Print valid and fraud transactions
fraud = df[df.Class == 1]
valid = df[df.Class == 0]
outlier_percentage = (fraud.shape[0] / valid.shape[0]) * 100

# Show fraud and valid transaction details
if st.sidebar.checkbox('Show fraud and valid transaction details'):
    st.write('Fraudulent transactions are: %.3f%%' % outlier_percentage)

    # Display the length of Fraud with a bigger header
    st.header('Fraud Cases: ')
    st.header(len(fraud))

    # Fetch and display the first Lottie animation
    url_animation_1 = "https://lottie.host/4ee5ebad-c8b0-4d88-ac7e-3dee416b0c7e/rlCKHLcGdu.json"
    st_lottie(url_animation_1, speed=1, height=100, key="animation_1")

    # Display the length of Valid with a bigger header
    st.header('Valid Cases: ')
    st.header(len(valid))

    # Fetch and display the second Lottie animation
    url_animation_2 = "https://lottie.host/6855c37e-68d0-4aab-b388-304bfe44314d/csB7V96sSw.json"
    st_lottie(url_animation_2, speed=1, height=100, key="animation_2")
