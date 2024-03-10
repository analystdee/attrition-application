from imaplib import _Authenticator
import streamlit as st  
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth


st.set_page_config(
    page_title='Home page',
    page_icon=':globe_with_meridians:',
    layout='wide'
)

def main():
    # Initialize session state
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        with st.sidebar:
            st.title('Login')

             # Test Account
            st.subheader('Test Account')
            st.write('Username: khadija')
            st.write('Password: 123')
    
            with open('./attrition-application/config.yaml') as file:
                config = yaml.load(file, Loader=SafeLoader)

            authenticator = stauth.Authenticate(
                config['credentials'],
                config['cookie']['name'],
                config['cookie']['key'],
                config['cookie']['expiry_days'],
                config['preauthorized']           
    )
            authenticator.login()
            st.session_state.authenticated = True

    else:
        st.title('Home Page')
        st.write('Welcome to my attrition prediction App!Attrition prediction app is a Machine Learning application that predicts the likelihood of a customer to leave the services based on various factors')
        st.write('Please login to access the features.')

        # Add sections explaining how the app works
        st.header('How the App Works')
        st.write('To make a prediction, users need to provide certain input features such as customer information and service usage.')
        st.write('The model then processes this information and outputs the likelihood of a customer churning.')
        
        st.subheader('Key Features')
        st.write("""
        - View Data
        - Dashboard
        - Prediction
        - History
        """)
        

    

        # Feedback Mechanism
        st.subheader('Feedback')
        feedback = st.text_area('Please share your feedback or suggestions here:', height=100)
        submit_button = st.button('Submit Feedback')

        if submit_button:
            if feedback:
                # Process the feedback (you can save it to a database, send it via email, etc.)
                st.success('Thank you for your feedback! We appreciate your input.')
            else:
                st.warning('Please provide your feedback before submitting.')

        # Contact Information
        st.subheader('Contact Us')
        st.write('If you need assistance or have any questions, please contact us at deedahahmed01@gmail.com.')


if __name__ == "__main__":
        main()


