# import streamlit as st
# import pandas as pd
# import pyodbc
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Page title and icon
# st.set_page_config(
#     page_title="Dashboard",
#     page_icon=":chart_with_upwards_trend:"
# )
 
# # Function to connect to the database
# @st.cache_resource(show_spinner='Connecting to Database......')
# def initialize_connection():
#     connection = pyodbc.connect(
#         "DRIVER={ODBC Driver 18 for SQL Server};SERVER="
#         + st.secrets["SERVER"]
#         +";DATABASE="
#         + st.secrets["DATABASE"]
#         +";UID="
#         + st.secrets["UID"]
#         +";PWD="
#         + st.secrets["PWD"]
#     )
#     return connection
 
# # Function to execute SQL query and return DataFrame
# @st.cache_data()
# def query_database(query):
#     with conn.cursor() as cur:
#         cur.execute(query)
#         rows = cur.fetchall()
#         df = pd.DataFrame.from_records(data=rows, columns=[column[0] for column in cur.description])
#     return df
 
# # Function to load dataset from file
# def load_dataset(file_path):
#     df = pd.read_csv(file_path) if file_path.endswith('.csv') else pd.read_excel(file_path)
#     return df
 
# # Function to display visualizations for each feature
# def display_visualizations(data):
#     st.subheader('Visualizations')
 
#     # Set style
#     sns.set_style('whitegrid')
 
#     # Create columns layout
#     col1, col2 = st.columns(2)
 
#     # Chart for Gender
#     with col1:
#         st.write("### Gender Distribution")
#         gender_counts = data['gender'].value_counts()
#         plt.figure(figsize=(10, 6))
#         gender_plot = sns.barplot(x=gender_counts.index, y=gender_counts.values, palette='pastel')
#         gender_plot.set_title('Gender Distribution')
#         gender_plot.set_xlabel('Gender')
#         gender_plot.set_ylabel('Count')
#         st.pyplot(fig=gender_plot.figure)
 
#     # Chart for Tenure
#     with col2:
#         st.write("### Tenure Distribution")
#         plt.figure(figsize=(10, 6))
#         tenure_plot = sns.histplot(data['tenure'], bins=20, kde=True, color='skyblue')
#         tenure_plot.set_title('Tenure Distribution')
#         tenure_plot.set_xlabel('Tenure')
#         tenure_plot.set_ylabel('Frequency')
#         st.pyplot(fig=tenure_plot.figure)
 
#     # Chart for Contract
#     with col1:
#         st.write("### Contract Distribution")
#         contract_counts = data['Contract'].value_counts()
#         plt.figure(figsize=(10, 6))
#         contract_plot = sns.barplot(x=contract_counts.index, y=contract_counts.values, palette='pastel')
#         contract_plot.set_title('Contract Distribution')
#         contract_plot.set_xlabel('Contract Type')
#         contract_plot.set_ylabel('Count')
#         st.pyplot(fig=contract_plot.figure)
 
#     # Chart for Payment Method
#     with col2:
#         st.write("### Payment Method Distribution")
#         payment_counts = data['PaymentMethod'].value_counts()
#         plt.figure(figsize=(10, 6))
#         payment_plot = sns.barplot(x=payment_counts.index, y=payment_counts.values, palette='pastel')
#         payment_plot.set_title('Payment Method Distribution')
#         payment_plot.set_xlabel('Payment Method')
#         payment_plot.set_ylabel('Count')
#         payment_plot.set_xticklabels(payment_plot.get_xticklabels(), rotation=45, horizontalalignment='right')
#         st.pyplot(fig=payment_plot.figure)
 
#     # Chart for Monthly Charges
#     with col1:
#         st.write("### Monthly Charges Distribution")
#         plt.figure(figsize=(10, 6))
#         monthly_charges_plot = sns.histplot(data['MonthlyCharges'], bins=20, kde=True, color='lightgreen')
#         monthly_charges_plot.set_title('Monthly Charges Distribution')
#         monthly_charges_plot.set_xlabel('Monthly Charges')
#         monthly_charges_plot.set_ylabel('Frequency')
#         st.pyplot(fig=monthly_charges_plot.figure)
 
#     # Chart for Total Charges
#     with col2:
#         st.write("### Total Charges Distribution")
#         total_charges_numeric = pd.to_numeric(data['TotalCharges'], errors='coerce').dropna()
#         plt.figure(figsize=(10, 6))
#         total_charges_plot = sns.histplot(total_charges_numeric, bins=20, kde=True, color='salmon')
#         total_charges_plot.set_title('Total Charges Distribution')
#         total_charges_plot.set_xlabel('Total Charges')
#         total_charges_plot.set_ylabel('Frequency')
#         st.pyplot(fig=total_charges_plot.figure)
 
# # Function to perform Exploratory Data Analysis (EDA)
# def perform_eda(data):
#     st.subheader('Exploratory Data Analysis (EDA)')
 

# # Function to calculate Key Performance Indicators (KPIs)
# def calculate_kpis(data):
#     st.subheader('Key Performance Indicators (KPIs)')
#      # Calculate KPIs
#     total_customers = len(data)
#     average_tenure = data['tenure'].mean()
#     total_monthly_charges = data['MonthlyCharges'].sum()
#     churned_customers = len(data == 'Yes')
#     churn_rate= (churned_customers / total_customers) * 100
#     total_revenue = data['TotalCharges'].sum()
#     average_revenue = total_revenue / total_customers


#      # Create a DataFrame to hold KPIs
#     kpi_data = {
#          'KPI Name': ['Total Customers', 'Average Tenure', 'Total Monthly Charges','churned_customers','churn_rate','total_revenue', 'average_revenue'],
#          'Value': [total_customers, f"{average_tenure:.2f}", f"${total_monthly_charges:.2f}", churned_customers,f"{churn_rate:.2f}",f"${total_revenue:.2f}", f"${average_revenue:.2f}"]
#      }
#     kpi_df = pd.DataFrame(kpi_data)
    
#     st.table(kpi_df)
 
# # Load data from the database
# conn = initialize_connection()
 
# # Title of the dashboard
# st.title('Churn Analysis')
 
# # Add selectbox to choose between EDA and KPIs
# selected_analysis = st.selectbox('Select Analysis Type', ['Exploratory Data Analysis (EDA)', 'Key Performance Indicators (KPIs)'])
 
# # Add selectbox to choose dataset
# selected_dataset = st.selectbox('Select Dataset', ['LP2_Telco_churn_first_3000', 'Telco-churn-last-2000.xlsx', 'LP2_Telco-churn-second-2000.csv'])
 
# if selected_dataset == 'LP2_Telco_churn_first_3000':
#     # Load data from the first dataset
#     data = query_database("SELECT gender, tenure, Contract, PaymentMethod, MonthlyCharges, TotalCharges FROM LP2_Telco_churn_first_3000")
# else:
#     # Load data from the selected file
#     file_path = f"data/{selected_dataset}"
#     data = load_dataset(file_path)
 
# # Perform the selected analysis
# if selected_analysis == 'Exploratory Data Analysis (EDA)':
#     perform_eda(data)
# else:
#     calculate_kpis(data)
 
# # Display visualizations (always shown regardless of the selected analysis)
# display_visualizations(data)
    

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
from io import StringIO

# Page title and icon
st.set_page_config(
    page_title="Dashboard",
    page_icon=":chart_with_upwards_trend:"
)

# Function to load dataset from URL
def load_dataset_from_url(csv_url):
    response = requests.get(csv_url)
    if response.status_code == 200:
        content = response.content.decode('utf-8')
        df = pd.read_csv(StringIO(content))
        return df
    else:
        st.error(f"Failed to load data from URL. Status code: {response.status_code}")
        return None

# Function to display visualizations for each feature
def display_visualizations(data):
    st.subheader('Visualizations')
 
    # Set style
    sns.set_style('whitegrid')
 
    # Create columns layout
    col1, col2 = st.columns(2)
 
    # Chart for Gender
    with col1:
        st.write("### Gender Distribution")
        gender_counts = data['gender'].value_counts()
        plt.figure(figsize=(10, 6))
        gender_plot = sns.barplot(x=gender_counts.index, y=gender_counts.values, palette='pastel')
        gender_plot.set_title('Gender Distribution')
        gender_plot.set_xlabel('Gender')
        gender_plot.set_ylabel('Count')
        st.pyplot(fig=gender_plot.figure)
 
    # Chart for Tenure
    with col2:
        st.write("### Tenure Distribution")
        plt.figure(figsize=(10, 6))
        tenure_plot = sns.histplot(data['tenure'], bins=20, kde=True, color='skyblue')
        tenure_plot.set_title('Tenure Distribution')
        tenure_plot.set_xlabel('Tenure')
        tenure_plot.set_ylabel('Frequency')
        st.pyplot(fig=tenure_plot.figure)
 
    # Chart for Contract
    with col1:
        st.write("### Contract Distribution")
        contract_counts = data['Contract'].value_counts()
        plt.figure(figsize=(10, 6))
        contract_plot = sns.barplot(x=contract_counts.index, y=contract_counts.values, palette='pastel')
        contract_plot.set_title('Contract Distribution')
        contract_plot.set_xlabel('Contract Type')
        contract_plot.set_ylabel('Count')
        st.pyplot(fig=contract_plot.figure)
 
    # Chart for Payment Method
    with col2:
        st.write("### Payment Method Distribution")
        payment_counts = data['PaymentMethod'].value_counts()
        plt.figure(figsize=(10, 6))
        payment_plot = sns.barplot(x=payment_counts.index, y=payment_counts.values, palette='pastel')
        payment_plot.set_title('Payment Method Distribution')
        payment_plot.set_xlabel('Payment Method')
        payment_plot.set_ylabel('Count')
        payment_plot.set_xticklabels(payment_plot.get_xticklabels(), rotation=45, horizontalalignment='right')
        st.pyplot(fig=payment_plot.figure)
 
    # Chart for Monthly Charges
    with col1:
        st.write("### Monthly Charges Distribution")
        plt.figure(figsize=(10, 6))
        monthly_charges_plot = sns.histplot(data['MonthlyCharges'], bins=20, kde=True, color='lightgreen')
        monthly_charges_plot.set_title('Monthly Charges Distribution')
        monthly_charges_plot.set_xlabel('Monthly Charges')
        monthly_charges_plot.set_ylabel('Frequency')
        st.pyplot(fig=monthly_charges_plot.figure)
 
    # Chart for Total Charges
    with col2:
        st.write("### Total Charges Distribution")
        total_charges_numeric = pd.to_numeric(data['TotalCharges'], errors='coerce').dropna()
        plt.figure(figsize=(10, 6))
        total_charges_plot = sns.histplot(total_charges_numeric, bins=20, kde=True, color='salmon')
        total_charges_plot.set_title('Total Charges Distribution')
        total_charges_plot.set_xlabel('Total Charges')
        total_charges_plot.set_ylabel('Frequency')
        st.pyplot(fig=total_charges_plot.figure)
 

# Function to perform Exploratory Data Analysis (EDA)
def perform_eda(data):
    st.subheader('Exploratory Data Analysis (EDA)')

# Function to calculate Key Performance Indicators (KPIs)
def calculate_kpis(data):
    st.subheader('Key Performance Indicators (KPIs)')
     # Calculate KPIs
    total_customers = len(data)
    average_tenure = data['tenure'].mean()
    total_monthly_charges = data['MonthlyCharges'].sum()
    churned_customers = len(data == 'Yes')
    churn_rate= (churned_customers / total_customers) * 100
    total_revenue = data['TotalCharges'].sum()
    average_revenue = total_revenue / total_customers


     # Create a DataFrame to hold KPIs
    kpi_data = {
         'KPI Name': ['Total Customers', 'Average Tenure', 'Total Monthly Charges','churned_customers','churn_rate','total_revenue', 'average_revenue'],
         'Value': [total_customers, f"{average_tenure:.2f}", f"${total_monthly_charges:.2f}", churned_customers,f"{churn_rate:.2f}",f"${total_revenue:.2f}", f"${average_revenue:.2f}"]
     }
    kpi_df = pd.DataFrame(kpi_data)
    
    st.table(kpi_df)

# Title of the dashboard
st.title('Churn Analysis')

# Add selectbox to choose between EDA and KPIs
selected_analysis = st.selectbox('Select Analysis Type', ['Exploratory Data Analysis (EDA)', 'Key Performance Indicators (KPIs)'])

# Add input box to enter CSV URL
csv_url = st.text_input('https://github.com/analystdee/attrition-application/raw/main/data/df_churn_first_3000.csv')

# Load data from the CSV URL
if csv_url:
    data = load_dataset_from_url(csv_url)
    if data is not None:
        # Perform the selected analysis
        if selected_analysis == 'Exploratory Data Analysis (EDA)':
            perform_eda(data)
        else:
            calculate_kpis(data)
        # Display visualizations (always shown regardless of the selected analysis)
        display_visualizations(data)
else:
    st.info('Please enter a CSV URL above.')

