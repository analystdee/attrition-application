import streamlit as st
import pandas as pd
import requests
from io import StringIO
 
st.title('VODAFONE CLASSIFICATION AND PREDICTING CUSTOMER CHURN')
if 'name' not in st.session_state:
    st.error("You need to log in to access this page.")
 
# Function to read CSV files from URL
def read_csv_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            csv_data = response.text
            df = pd.read_csv(StringIO(csv_data))
            return df
        else:
            st.error("Failed to download CSV file from the specified URL.")
            return None
    except Exception as e:
        st.error(f"Error occurred while downloading CSV file: {e}")
        return None
 
# Define the URL to the CSV file on GitHub
csv_url = 'https://github.com/analystdee/attrition-application/blob/main/ml_dataset.csv'
 
# Read the CSV file from the URL
data = read_csv_from_url(csv_url)
 
if data is not None:
    st.title("Data Page")
    st.write("This is the data page.")
 
    @st.cache_data()
    def select_all_features(df):
        return df
 
    @st.cache_data()
    def select_numeric_features(df):
        numeric_df = df.select_dtypes(include=['number'])
        return numeric_df
    

def feature_explanations():
    # Define feature explanations
    explanations = {
        'gender': 'Gender of the customer',
        'SeniorCitizen': 'Whether the customer is a senior citizen (1) or not (0)',
        'Partner': 'Whether the customer has a partner (Yes) or not (No)',
        'Dependents': 'Whether the customer has dependents (Yes) or not (No)',
        'tenure': 'Number of months the customer has stayed with the company',
        'PhoneService': 'Whether the customer has a phone service (Yes) or not (No)',
        'MultipleLines': 'Whether the customer has multiple lines (Yes, No, or No phone service)',
        'InternetService': 'Customers internet service provider (DSL, Fiber optic, or No)',
        'OnlineSecurity': 'Whether the customer has online security service (Yes, No, or No internet service)',
        'OnlineBackup': 'Whether the customer has online backup service (Yes, No, or No internet service)',
        'DeviceProtection': 'Whether the customer has device protection service (Yes, No, or No internet service)',
        'TechSupport': 'Whether the customer has tech support service (Yes, No, or No internet service)',
        'StreamingTV': 'Whether the customer has streaming TV service (Yes, No, or No internet service)',
        'StreamingMovies': 'Whether the customer has streaming movies service (Yes, No, or No internet service)',
        'Contract': 'The contract term of the customer (Month-to-month, One year, Two year)',
        'PaperlessBilling': 'Whether the customer has paperless billing (Yes) or not (No)',
        'PaymentMethod': "The customer payment method",
        'MonthlyCharges': 'The amount charged to the customer monthly',
        'TotalCharges': 'The total amount charged to the customer',
    }
    return explanations

if __name__ == "__main__":
 
    col1, col2 = st.columns(2)
 
    with col1:
        selected_option = st.selectbox("Select type of features", options=['All features', 'Numeric features'], key="selected_columns")
 
    with col2:
        pass
 
    if selected_option == "All features":
        data_to_display = select_all_features(data)
    elif selected_option == "Numeric features":
        data_to_display = select_numeric_features(data)
 
    st.dataframe(data_to_display)

    # Display feature explanations
    explanations = feature_explanations()
    for col in data.columns:
        if col in explanations:
            st.write(f"**{col}:** {explanations[col]}")


    st.write(st.session_state)
 
