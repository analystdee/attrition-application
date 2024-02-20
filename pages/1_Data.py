import streamlit as st
import streamlit as st
import pandas as pd
import mysql.connector

st.set_page_config(
    page_title='View Data',
    page_icon='',
    layout='wide'
)


# Connect to MySQL database
def connect_to_database():
    try:
        conn = mysql.connector.connect(
         host='dap-projects-database.database.windows.net',
         user='LP2_project',
         password='Stat$AndD@t@Rul3',
         database='dapDB'
        )
        return conn
    except mysql.connector.Error as e:
        st.error(f"Error connecting to MySQL database: {e}")
        return None

# Execute SQL query and return result as pandas DataFrame
def execute_query(conn, query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        columns = [i[0] for i in cursor.description]
        df = pd.DataFrame(result, columns=columns)
        cursor.close()
        return df
    except mysql.connector.Error as e:
        st.error(f"Error executing SQL query: {e}")
        return None

# Main function
def main():
    st.title("Streamlit App with MySQL Integration")

    # Connect to MySQL database
    conn = connect_to_database()
    if conn is None:
        return

    # Example SQL query
    query = "SELECT * FROM your_table"

    # Execute query and get data
    data = execute_query(conn, query)

    # Display data in Streamlit app
    if data is not None:
        st.write("Data from MySQL database:")
        st.write(data)

# Run the app
if __name__ == "__main__":
    main()
