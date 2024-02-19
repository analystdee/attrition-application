import streamlit as st  

def main():
    st.title('Home Page')
    st.write('Welcome to my attrition prediction App!')
    st.write('This is a demo churning prediction application built with Streamlit.')
    st.write('Please login to access the features.')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    login_button = st.button('Login')

    if login_button:
        if username == 'Deedah' and password == 'password':
            st.success('Logged in successfully!')
            st.write('Welcome, {}'.format(username))
        else:
            st.error('Invalid username or password')


    # Instructions
    st.subheader('Instructions')
    st.markdown("""
    1. **Login**: Enter your username and password to login.
    2. **Navigate**: After logging in, you can navigate to different pages using the sidebar.
    3. **Explore**: Explore the features of each page and interact with the elements provided.
    """)

    # Contact Information
    st.subheader('Contact Us')
    st.write('If you need assistance or have any questions, please contact us at deedahahmed01@gmail.com.')



if __name__ == "__main__":
    main()

