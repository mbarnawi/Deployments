import streamlit as st
import pandas as pd
import numpy as np
import pickle
from streamlit_lottie import st_lottie

# Load the model
filename = r"rf_model_f.pkl"
model = pickle.load(open(filename, "rb"))

# Function to load the CSV file
def load_data(file):
    try:
        df = pd.read_csv(file)
        return df
    except Exception as e:
        st.sidebar.error(f"Error loading CSV file: {e}") 
        return None

# Function to perform fraud detection prediction
def predict_fraud(data, entry=None):
    if 'Class' in data.columns:
        X = data.drop('Class', axis=1)
    else:
        X = data

    if entry:
        # Convert entry dictionary to numeric array-like format
        entry_array = np.array(list(entry.values())).reshape(1, -1)

        # Predict for a specific entry
        prediction = model.predict(entry_array)
        return prediction
    else:
        # Predict for all entries
        predictions = model.predict(X)
        return predictions

# Main function
def main():
    # Center-aligned title with increased height and black color
    st.markdown("<h1 style='text-align: center; color: white;'> Credit Card Prediction</h1>", unsafe_allow_html=True)

    # Display Lottie animation with increased height
    animation_url = "https://lottie.host/437a402f-a348-4cb4-bc75-b60fb0c77725/RkipOfCtFJ.json"
    st_lottie(animation_url, speed=1, height=800, key="animation")

    # Sidebar options
    st.sidebar.title("Options")
    option = st.sidebar.radio("Select an option", ("Upload CSV", "Enter Values"))

    if option == "Upload CSV":
        file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])
        if file is not None:
            data = load_data(file)

            if data is not None:
                st.subheader("CSV File")
                st.write(data)

                predictions = predict_fraud(data)
                st.subheader("Predictions")

                # Center-align the entire "Predictions" section
                st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

                # Add styling to the table (set border properties)
                st.write("<style>table {margin: 0 auto; border: 1px solid black; border-collapse: collapse;}</style>", unsafe_allow_html=True)
                
                # Map predictions to "Safe Transaction" or "Likely Fraud"
                prediction_texts = ["Safe Transaction" if pred == 0 else "Likely Fraud" for pred in predictions]

                # If there's only one prediction, convert it to DataFrame
                if len(predictions) == 1:
                    st.table(pd.DataFrame({"Prediction": [prediction_texts[0]]}).style.set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]))
                else:
                    # Center-align the table
                    prediction_df = pd.DataFrame({"Prediction": prediction_texts})
                    st.table(prediction_df.style.set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]))

                # Close the center-align div
                st.markdown("</div>", unsafe_allow_html=True)

    elif option == "Enter Values":
        st.sidebar.subheader("Enter Credit Card Details")

        # Ranges for specific entries
        ranges = {
            'V12': (-18.6837, 7.8484),
            'V17': (-25.1628, 9.253526),
            'V14': (-19.2143, 10.5268),
            'V16': (-14.1299, 17.3151),
            'V10': (-24.5883, 23.7451),
            'V11': (-4.7975, 12.0189),
            'V18': (-9.4987, 5.0411),
            'V9': (-13.4341, 15.5950),
            'V4': (-5.6832, 16.8753),
            'V7': (-43.5572, 120.5895)
        }

        # Collect credit card details from the user
        entry = {}

        for column, (min_val, max_val) in ranges.items():
            value = st.sidebar.text_input(column, type="default", placeholder=f"Enter value ({min_val} to {max_val})")
            
            # Validation for non-numeric values
            if not value.replace('.', '', 1).isdigit() and value:
                st.sidebar.warning(f"Invalid entry for {column}. Please enter a numeric value.")
            else:
                # Validation for value within the specified range
                if value and not (min_val <= float(value) <= max_val):
                    st.sidebar.warning(f"Please enter a value for {column} within the range {min_val} to {max_val}.")
                else:
                    entry[column] = float(value) if value else None

        if st.sidebar.button("Predict"):
            # Validation for empty values
            missing_values = [col for col, val in entry.items() if val is None]
            
            if missing_values:
                st.sidebar.warning(f"Please enter a value for {', '.join(missing_values)}")
            else:
                data = pd.DataFrame([entry])

                # Check if the entry dictionary is empty before making predictions
                if not entry:
                    st.sidebar.warning("Please enter values before predicting.")
                else:
                    predictions = predict_fraud(data, entry)
                    st.subheader("Prediction")

                    # Center-align the entire "Predictions" section
                    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
                    # Add styling to the table (set border properties)
                    st.write("<style>table {margin: 0 auto; border: 1px solid black; border-collapse: collapse;}</style>", unsafe_allow_html=True)
                    # Map predictions to "Safe Transaction" or "Likely Fraud"
                    prediction_texts = ["Safe Transaction" if pred == 0 else "Likely Fraud" for pred in predictions]
                    # If there's only one prediction, convert it to DataFrame
                    if len(predictions) == 1:
                        st.table(pd.DataFrame({"Prediction": [prediction_texts[0]]}).style.set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]))
                    else:
                        # Center-align the table
                        prediction_df = pd.DataFrame({"Prediction": prediction_texts})
                        st.table(prediction_df.style.set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]))

                    # Close the center-align div
                    st.markdown("</div>", unsafe_allow_html=True)

# Run the app
if __name__ == '__main__':
    main()
