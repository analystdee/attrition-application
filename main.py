from imaplib import _Authenticator
import streamlit as st  
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

def main():
        st.title('Home Page')
        st.write('Welcome to my attrition prediction App!')
        st.write('This is a demo churning prediction application built with Streamlit.')
        st.write('Please login to access the features.')
    


        with open('C:/Users/Said Ahmed/Desktop/personalprojects/attrition-application/config.yaml') as file:
            config = yaml.load(file, Loader=SafeLoader)

        authenticator = stauth.Authenticate(
            config['credentials'],
            config['cookie']['name'],
            config['cookie']['key'],
            config['cookie']['expiry_days'],
            config['preauthorized']
            
    )
        authenticator.login()

    



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

