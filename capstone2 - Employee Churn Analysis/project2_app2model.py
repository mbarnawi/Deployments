import streamlit as st
import pickle
import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OrdinalEncoder
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

# Custom styling using HTML and CSS
html_temp = """
<div style="background-color:#87CEFA;padding:3px">
<h2 style="color:white;text-align:center;">Leaving The Company Prediction </h2>
</div>"""
st.markdown(html_temp, unsafe_allow_html=True)

st.lottie("https://lottie.host/c0e42f8e-e9dd-4890-9ad5-f4e7e35919f0/27pkQuzhD7.json", width=700, height=300)

EXAMPLE_NO = 1

def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Which department is the employee working in?",  # required
                options=["Sales", "Technical", "Support", "IT", "RandD", "Product manager", "Marketing", "Accounting", "HR", "Management"],  # required
                icons=['server', 'tools', "pencil-square", 'pc-display', 'house-gear', 'database-gear', 'cart-check', 'currency-exchange', 'person-gear', 'clipboard-data']
            )
        return selected

selected = streamlit_menu(example=EXAMPLE_NO)

if selected == "Sales":
    st.title(f"You have selected {selected} department")
if selected == "Technical":
    st.title(f"You have selected {selected} department")
if selected == "Support":
    st.title(f"You have selected {selected} department")
if selected == "IT":
    st.title(f"You have selected {selected} department")
if selected == "RandD":
    st.title(f"You have selected {selected} department")
if selected == "Product manager":
    st.title(f"You have selected {selected} department")
if selected == "Marketing":
    st.title(f"You have selected {selected} department")
if selected == "Accounting":
    st.title(f"You have selected {selected} department")
if selected == "HR":
    st.title(f"You have selected {selected} department")
if selected == "Management":
    st.title(f"You have selected {selected} department")

model_selection = st.selectbox("Select Model", ["", "Random Forest", "XGBoost model", "SVC model"], key="model_selection")

if model_selection == "Random Forest":
    model = pickle.load(open("rf2_model", "rb"))
elif model_selection == "XGBoost model":
    model = pickle.load(open("xgb_classifier", "rb"))
elif model_selection == "SVC model":
    model = pickle.load(open("SVC_model_2", "rb"))
else:
    st.warning("Please select a model.")
    st.stop()

avg_monthly_hours = st.slider("Average Monthly Hours", 40, 400, step=1,
                              help="Adjust the slider to input the average monthly hours.")
satisfaction_level = st.slider('Satisfaction Level', 0, 100, step=1,
                               help="Adjust the slider to input the satisfaction level.")
last_evaluation = st.slider("Last Evaluation", 0, 100, step=1,
                            help="Adjust the slider to input the last evaluation.")
num_project = st.slider("Number of Projects", 1, 10, step=1,
                        help="Adjust the slider to input the number of projects.")
time_in_company = st.slider("Time in Company (years)", 1, 20, step=1,
                             help="Adjust the slider to input the number of years the employee spent in the company.")
salary = st.radio("Employee Salary Category", ('Low', 'Medium', 'High'),
                  help="Select the category that describes the employee's salary.")

# Dataframe creation
my_dict = {
    "average_montly_hours": avg_monthly_hours,
    "satisfaction_level": satisfaction_level,
    "last_evaluation": last_evaluation,
    "number_project": num_project,
    "time_spend_company": time_in_company,
    "salary": salary,
    "Departments ": selected
}

df = pd.DataFrame.from_dict([my_dict])

# Display user input in a table
st.header("Your information as you selected is below")
st.table(df)

# Load another animation
st.lottie("https://lottie.host/cc14a055-8eae-4a82-811c-377ee2e17932/TIEjmWHTsp.json", width=800, height=300)

# Prediction
st.subheader("Press 'Predict' when you're ready")

if st.button("Predict"):
    prediction = model.predict(df)
    if prediction == 1:
        st.success("This employee will most likely leave the company soon 🙁")
    else:
        st.success("This employee is unlikely to leave the company soon 😃")
