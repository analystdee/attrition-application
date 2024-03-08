import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns


# Page title and icon
st.set_page_config(
    page_title="Dashboard",
    page_icon=":chart_with_upwards_trend:"
)
st.title("Data Visualization")

# Function to display visualizations for each feature
def display_visualizations(df):
    col1,col2=st.columns(2)
    with col1:
        st.write("### Gender Distribution")
        gender_counts = df['gender'].value_counts()
        st.bar_chart(gender_counts)

         # Chart for Tenure
        st.write("### Tenure Distribution")
        tenure_chart = px.histogram(df, x='tenure', nbins=20)
        # tenure_chart.update_layout(width=400, height=300, margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(tenure_chart)

        # Chart for Contract
        st.write("### Contract Distribution")
        contract_counts = df['Contract'].value_counts()
        st.bar_chart(contract_counts)

    with col2:
         # Chart for Payment Method
        st.write("### Payment Method Distribution")
        payment_counts = df['PaymentMethod'].value_counts()
        # payment_chart = px.bar(payment_counts, color=payment_counts.index, labels={'index': 'Payment Method', 'value': 'Count'})
        # Define a list of neutral colors
        # neutral_colors = ['#AD6F69', 'darkgray', '#808000', 'khaki']
        # Apply the neutral color palette to each bar
        # for i, color in enumerate(neutral_colors):
        #     payment_chart.data[i].marker.color = color
        # payment_chart.update_layout(width=400, height=300, margin=dict(l=20, r=20, t=20, b=20))
        st.bar_chart(payment_counts)
       
        # Chart for Monthly Charges
        st.write("### Monthly Charges Distribution")
        fig= px.histogram(df['MonthlyCharges'], nbins=20)
        st.plotly_chart(fig)

        # Chart for Total Charges
        st.write("### Total Charges Distribution")
        total_charges_numeric = pd.to_numeric(df['TotalCharges'], errors='coerce')
        fig= px.histogram(total_charges_numeric.dropna(), nbins=20)
        st.plotly_chart(fig)


# Function to display KPIs
def display_kpis(df):
    st.write("### Key Performance Indicators (KPIs)")

    # Calculate KPIs
    total_customers = len(df)
    average_tenure = df['tenure'].mean()
    total_monthly_charges = df['MonthlyCharges'].sum()


    # Create a DataFrame to hold KPIs
    kpi_data = {
        'KPI Name': ['Total Customers', 'Average Tenure', 'Total Monthly Charges'],
        'Value': [total_customers, f"{average_tenure:.2f}", f"${total_monthly_charges:.2f}"]
    }
    kpi_df = pd.DataFrame(kpi_data)
    
    st.table(kpi_df)
             

if __name__ == '__main__':
    df = pd.read_csv("ml_dataset.csv") 
    # Add a button to toggle between displaying graphs and KPIs
    if st.button("EDA"):
        display_visualizations(df)
    elif st.button("View KPIs"):
        display_kpis(df)
    

 
        