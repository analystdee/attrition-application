import streamlit as st
import streamlit as st
import pandas as pd
import mysql.connector
import csv

st.set_page_config(
    page_title='View Data',
    page_icon='',
    layout='wide'
)



# Define the path to your CSV file
csv_file_path = r'C:\Users\Said Ahmed\Desktop\personalprojects\attrition-application\ml_dataset.csv'

# Initialize an empty list to store the data
csv_data = []

# Reading data from the CSV file and storing it in the list
with open(csv_file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Append each row as a dictionary to the csv_data list
        csv_data.append(row)
