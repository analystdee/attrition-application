import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title='Predict',
    page_icon='',
    layout='wide'
)


def random_model():
    with open('models/Random_Model.pkl', 'rb') as file:
        model= pickle.load(file)
    return model


def svc_model():
    with open ('models/svc_model.pkl', 'rb') as file:
        model= pickle.load(file)
    return model
 
def model_selection():
    st.selectbox('Select a Model', options= ['Random Forest', 'SVC'], key= 'selected_model')
    if st.session_state['selected_model']== 'Random Forest':
        model=random_model()
    else:
        model= svc_model()

    
    with open('models/encoder.pkl', 'rb') as file:
        encoder= pickle.load(file)
    

    return model,encoder


def make_prediction(model,encoder):
    gender= st.session_state['gender']
    SeniorCitizen = st.session_state['SeniorCitizen']
    partner= st.session_state['partner']
    dependent= st.session_state['dependent']
    tenure = st.session_state['tenure']
    phoneservice = st.session_state['phoneservice']
    multiplelines = st.session_state['multiplelines']
    internetservice = st.session_state['internetservice']
    onlinesecurity = st.session_state['onlinesecurity']
    onlinebackup = st.session_state['onlinebackup']
    deviceprotection = st.session_state['deviceprotection']
    techsupport = st.session_state['techsupport']
    streamingtv = st.session_state['streamingtv']
    contract = st.session_state['contract']
    paperlessbilling= st.session_state['paperlessbilling']
    payment_method = st.session_state['payment_method']
    monthly_charges = st.session_state['monthly_charges']
    total_charges = st.session_state['total_charges']

    columns = ['gender', 'SeniorCitizen','Partner','Dependents','tenure','PhoneService',	
        'MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport',
         'StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod','MonthlyCharges',
          'TotalCharges']
    data=  [[gender,SeniorCitizen,partner,dependent,tenure,phoneservice,multiplelines,internetservice,onlinesecurity,
            onlinebackup,deviceprotection,techsupport,streamingtv,contract,paperlessbilling,payment_method,
            monthly_charges,total_charges]]
    df= pd.DataFrame(data, columns= columns)

    prediction= model.predict(df)
    return prediction


def prediction():
    model, encoder= model_selection()
    with st.form('input-feature'):
        column1,column2,column3= st.columns(3)

        with column1:
            st.write('### Personal info')
            st.selectbox('Enter gender', options=['Male','Female'], key= 'gender')
            st.selectbox('Are you a SeniorCitizen', options=['Yes','No'], key= 'SeniorCitizen')
            st.selectbox('Do you have a partner', options=['Yes','No'],key='partner')
            st.selectbox('Do you have Dependents', options=['Yes','No'],key='dependent')
            st.number_input('customer term(tenure)', min_value=0, max_value=72,key='tenure')


        with column2:
            st.write('### Services offered')
            st.selectbox('Are you subscribed to a PhoneService', options=['Yes','No'],key='phoneservice')
            st.selectbox('Do you have MultipleLines', options=['No', 'No phone service', 'Yes'],key='multiplelines')
            st.selectbox('Which internetService do you use', options=['DSL', 'Fiber optic', 'No'],key='internetservice')
            st.selectbox('Do you have OnlineSecurity', options=['No', 'Yes', 'No internet service'],key='onlinesecurity')
            st.selectbox('Do you have OnlineBackup', options=['No', 'Yes'],key='onlinebackup')
            st.selectbox('Do you have DeviceProtection', options=['No', 'Yes'],key='deviceprotection')
            st.selectbox('Are you subscribed to TechSupport', options=['No', 'Yes'],key='techsupport')
            st.selectbox('Are you subscribed to StreamingTV', options=['No', 'Yes'],key='streamingtv')
            st.selectbox('Are you subscribed to streamingMovies', options=['No', 'Yes'],key='streamingmovies')

        with column3:
            st.write('### Contract and Payments')
            st.selectbox('Which Contract clause are you on', options= ['Month-to-month', 'Two year', 'One year'],key='contract')
            st.selectbox('Have you subscribed to PaperlessBilling', options=['Yes','No'],key='paperlessbilling')
            st.selectbox('Which payment method do you use', options=['Credit card (automatic)', 'Electronic check', 'Mailed check',
       'Bank transfer (automatic)'],key='payment_method')
            st.number_input('What are your monthlycharges',min_value=18 , max_value= 120,key='monthly_charges')
            st.number_input('What are your TotalCharges',min_value=18, max_value=8700,key='total_charges')



        st.form_submit_button('Submit', on_click=make_prediction, kwargs=dict(model=model,encoder=encoder))

if __name__ == "__main__":
    st.title('Make a Prediction')
    # model_selection()
    prediction()

    










# [customerID	gender	SeniorCitizen	Partner	Dependents	tenure	PhoneService	
# MultipleLines	InternetService	OnlineSecurity	OnlineBackup	DeviceProtection	T
# echSupport	StreamingTV	StreamingMovies	Contract	
# PaperlessBilling	PaymentMethod	MonthlyCharges	TotalCharges]
