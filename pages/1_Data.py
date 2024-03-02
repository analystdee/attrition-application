import streamlit as st
import pandas as pd
import pyodbc


st.set_page_config(
    page_title='View Data',
    page_icon='',
    layout='wide'
)

st.title('properiority Data')


def initialize_connection():
    connection = pyodbc.connect(
        'DRIVER={{ODBC Driver 18 for SQL Server}}'
        + st.secrets['server_name'],
        'DATABASE={database}'
        + st.secrets['database'],
        'UID={username}'
        + st.secrets['user'],
        'PWD={password}'
        + st. secrets['password']
    )

    return connection


conn= initialize_connection


st.cache_data()
def query_database(query):
    with  conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()

        df= pd.DataFrame.from_records(data=rows, columns=[column[0]for column in cur.description])

    
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


if __name__ == "__main__":
    col1,col2= st.columns(2)
    with col1:
        st.selectbox("select type of feature ", options= ['All features', 'numeric features'],
        key= "selected_columns")

    with col2:
        pass

    if st.session_state['selected_columns']== 'All features':
        select_all_features()
