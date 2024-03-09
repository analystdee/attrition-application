import streamlit as st
import pandas as pd
import pyodbc


st.set_page_config(
    page_title='View Data',
    page_icon=':clipboard:',
    layout='wide'
)

st.title('propriertory Data')


st.cache_resource(show_spinner='Connecting to Database...')
def initialize_connection():
    connection = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};SERVER="
        + st.secrets["SERVER"]
        +";DATABASE="
        + st.secrets["DATABASE"]
        +";UID="
        + st.secrets["UID"]
        +";PWD="
        + st. secrets["PWD"]
    )

    return connection


conn= initialize_connection()


st.cache_data()
def query_database(query):
    with  conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()

        df= pd.DataFrame.from_records(data=rows, columns=[column[0] for column in cur.description])

    
    return df


st.cache_data()
def select_all_features():
    query= "Select * from LP2_Telco_churn_first_3000"
    df= query_database(query)
    return df
     

# def select_numeric_features():
#     query= "Select * from LP2_Telco_churn_first_3000"
#     df= query_database(query)
#     return df


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
    col1,col2= st.columns(2)
    with col1:
        st.selectbox("select type of feature ", options= ['All features', 'numeric features'],
        key= "selected_columns")

    with col2:
        pass

    if st.session_state['selected_columns']== 'All features':
        data = select_all_features()
        st.dataframe(data)

        # Display feature explanations
        explanations = feature_explanations()
        for col in data.columns:
            if col in explanations:
                st.write(f"**{col}:** {explanations[col]}")


    st.write(st.session_state)

