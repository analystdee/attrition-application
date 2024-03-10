# from imaplib import _Authenticator
# import streamlit as st  
# import yaml
# from yaml.loader import SafeLoader
# import streamlit_authenticator as stauth


# st.set_page_config(
#     page_title='Home page',
#     page_icon=':globe_with_meridians:',
#     layout='wide'
# )

# def main():
#     # Initialize session state
#     if 'authenticated' not in st.session_state:
#         st.session_state.authenticated = False

#     if not st.session_state.authenticated:
#         with st.sidebar:
#             st.title('Login')

#              # Test Account
#             st.subheader('Test Account')
#             st.write('Username: khadija')
#             st.write('Password: 123')
    
#             with open('./attrition-application/config.yaml') as file:
#                 config = yaml.load(file, Loader=SafeLoader)

#             authenticator = stauth.Authenticate(
#                 config['credentials'],
#                 config['cookie']['name'],
#                 config['cookie']['key'],
#                 config['cookie']['expiry_days'],
#                 config['preauthorized']           
#     )
#             authenticator.login()
#             st.session_state.authenticated = True

#     else:
#         st.title('Home Page')
#         st.write('Welcome to my attrition prediction App!Attrition prediction app is a Machine Learning application that predicts the likelihood of a customer to leave the services based on various factors')
#         st.write('Please login to access the features.')

#         # Add sections explaining how the app works
#         st.header('How the App Works')
#         st.write('To make a prediction, users need to provide certain input features such as customer information and service usage.')
#         st.write('The model then processes this information and outputs the likelihood of a customer churning.')
        
#         st.subheader('Key Features')
#         st.write("""
#         - View Data
#         - Dashboard
#         - Prediction
#         - History
#         """)
        

    

#         # Feedback Mechanism
#         st.subheader('Feedback')
#         feedback = st.text_area('Please share your feedback or suggestions here:', height=100)
#         submit_button = st.button('Submit Feedback')

#         if submit_button:
#             if feedback:
#                 # Process the feedback (you can save it to a database, send it via email, etc.)
#                 st.success('Thank you for your feedback! We appreciate your input.')
#             else:
#                 st.warning('Please provide your feedback before submitting.')

#         # Contact Information
#         st.subheader('Contact Us')
#         st.write('If you need assistance or have any questions, please contact us at deedahahmed01@gmail.com.')


# if __name__ == "__main__":
#         main()


import streamlit as st
import yaml
 
# Load YAML configuration
try:
    with open('config.yaml') as file:
        config = yaml.safe_load(file)
        print("Config loaded successfully:", config)  # Add this line to check if config is loaded correctly
except FileNotFoundError:
    st.error("Config file not found. Please make sure 'config.yaml' exists.")
    st.stop()
except yaml.YAMLError:
    st.error("Error loading config file. Please check the format and content.")
    st.stop()
 
# Define functions
def layout_for_logged_in_users(username):
    st.title(f'Welcome to the main page, {username}')
    # Add content for logged-in users here
 
    # Display Attrition Insight content
    st.write("""
    Attrition application is a Machine Learning application that predicts the likelihood of a customer to leave
              the company based on various demographic and job-related factors.
         **Key Features**
        - View Data: Access proprietary data from SQL Server.
        - Dashboard: Explore interactive data visualizations for insights.
        - Real-time Prediction: Instantly see predictions for employee attrition.
        - History: See past predictions made.
    
        **User Benefits**
        - Data-driven Decisions: Make informed decisions backed by data analytics.
        - Easy Machine Learning: Utilize powerful machine learning algorithms effortlessly.
        - Live Demo: Watch a demo video to see the app in action.
 
        **How to run application**
            
        # activate virtual environment
        env/scripts/activate
        streamlit run main.py
        
 
        **Machine Learning Integration**
        - Model Selection: Choose between two advanced models for accurate predictions.
        - Seamless Integration: Integrate predictions into your workflow with a user-friendly interface.
        - Probability Estimates: Gain insights into the likelihood of predicted outcomes.
    
        **Need Help?**
        For collaborations contact me at deedahahmed01@gmail.com.
    """)
 
def authenticate(username, password):
    if username in config['credentials']['usernames']:
        stored_password = config['credentials']['usernames'][username]['password']
        if password == stored_password:
            return True
    return False
 
# Initialize Streamlit
st.set_page_config(page_title="Home Page", page_icon=":globe_with_meridians:")
 
# Main content area
if 'name' not in st.session_state:
    with st.sidebar:
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if authenticate(username, password):
                st.session_state["name"] = username
            else:
                st.error("Invalid username or password. Please try again.")
else:
    with st.sidebar:
        st.title("Logout")
        if st.button("Logout"):
            del st.session_state["name"]
 
# Main content area
if 'name' in st.session_state:
    layout_for_logged_in_users(st.session_state['name'])
else:
    st.success("Enter username and password to use the app.")
    st.write("Test Accounts:")
    for username in config['credentials']['usernames']:
        st.write(f"Username: {username}, Password: {config['credentials']['usernames'][username]['password']}")
 
 
       