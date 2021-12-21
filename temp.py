import streamlit as st
import pickle
import numpy as np
import pandas as pd

    
def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

xgboost = data["model"]
columns = ['Current_Loan_Amount','Annual_Income','Monthly_Debt',
                          'Current_Credit_Balance', 'Tax_Liens', 
                          'Home_Ownership_Home Mortgage', 'Loan_Status_Fully Paid',
                          'Purpose_Buy House', 'Years_in_current_job_10+ years']



def show_predict_page():
    st.title("Loan Predict")

    st.write("""### We need some information for prediction""")

    
    number1 = st.number_input('Insert Your Current Loan Amount')
    Current_Loan_Amount = st.write('Your Current Loan Amount is ', number1)
    
    number2 = st.number_input('Insert Your Annual Income')
    Annual_Income = st.write('Your Annual Income is ', number2)
    
    number3 = st.number_input('Insert Your Monthly Debt')
    Monthly_Debt = st.write('Your Monthly Debt is ', number3)
    
    number4 = st.number_input('Insert Your Current Credit Balance')
    Current_Credit_Balance = st.write('Your Current Credit Balance is ', number4)
    
  
    option1 = st.slider('Your Tax Liens:', 0, 15, 1)
    Tax_Liens = st.write('You selected:', option1)



    option2 = st.selectbox(
     'Select Your Home Ownership', (
         'Home Mortgage',
         'Own Home',
         'Rent',
         'Have Mortgage'
         ))
    Home_Ownership = st.write('You selected:', option2)
    
    
    option3 = st.selectbox(
     'Select Your Purpose', (
         'Debt Consolidation',
         'Buy House',
         'Home Improvements',
         'Other',
         'Business Loan', 
         'small business', 
         'Take a Trip', 
         'Buy a Car',
         'Medical Bills', 
         'major purchase', 
         'moving', 
         'wedding',
         'Educational Expenses', 
         'renewable energy', 
         'vacation'
         ))
    Purpose = st.write('You selected:', option3)
    
    
    option4 = st.selectbox(
     'Select Your Loan Status', (
         'Fully Paid', 
         'Charged Off'
         ))
    Loan_Status = st.write('You selected:', option4)
    
    
    option5 = st.selectbox(
     'Select How Many Years in Current Job', (
         '10 years or more', 
         '9 years', 
         '8 years', 
         '7 years', 
         '6 years',
         '5 years', 
         '4 years', 
         '3 years', 
         '2 years', 
         '1 year', 
         'less than year'
         ))
    Years_in_current_job = st.write('You selected:', option5)


    ok = st.button("Predict")

    if Tax_Liens == "0.":
        Tax_Liens = 1
    elif Tax_Liens == "1.":
        Tax_Liens = 1
    elif Tax_Liens == "2.":
        Tax_Liens = 1
    elif Tax_Liens == "3.":
        Tax_Liens = 1
    elif Tax_Liens == "4.":
        Tax_Liens = 1
    elif Tax_Liens == "5.":
        Tax_Liens = 1
    elif Tax_Liens == "6.":
        Tax_Liens = 1
    elif Tax_Liens == "9.":
        Tax_Liens = 1
    elif Tax_Liens == "10.":
        Tax_Liens = 1
    elif Tax_Liens == "11.":
        Tax_Liens = 1
    elif Tax_Liens == "15.":
        Tax_Liens = 1
    else:
        Tax_Liens = 0



    if Home_Ownership == "Own Home":
        Home_Ownership = 1
    else:
        Home_Ownership = 0


    if Purpose == 'Debt Consolidation':
        Purpose = 1
    elif Purpose == 'Buy House':
        Purpose = 1
    elif Purpose == 'Home Improvements':
        Purpose = 1
    elif Purpose == 'Other':
        Purpose = 1
    elif Purpose == 'Business Loan':
        Purpose = 1
    elif Purpose == 'small business':
        Purpose = 1
    elif Purpose == 'Take a Trip':
        Purpose = 1
    elif Purpose == 'Buy a Car':
        Purpose = 1
    elif Purpose == 'Medical Bills':
        Purpose = 1
    elif Purpose == 'major purchase':
        Purpose = 1
    elif Purpose == 'moving':
        Purpose = 1
    elif Purpose == 'wedding':
        Purpose = 1
    elif Purpose == 'Educational Expenses':
        Purpose = 1
    elif Purpose == 'renewable energy':
        Purpose = 1
    elif Purpose == 'vacation':
        Purpose = 1
    else:
        Purpose = 0


    if Loan_Status == 'Fully Paid':
        Loan_Status = 1
    else:
        Loan_Status = 0
         
      
    
    if Years_in_current_job ==  '10 years or more':
        Years_in_current_job = 1
    elif Years_in_current_job == '9 years':
        Years_in_current_job = 1
    elif Years_in_current_job == '8 years':
        Years_in_current_job = 1
    elif Years_in_current_job == '7 years':
        Years_in_current_job = 1
    elif Years_in_current_job == '6 years':
        Years_in_current_job = 1
    elif Years_in_current_job == '5 years':
        Years_in_current_job = 1
    else:
        Years_in_current_job = 0

    

    if ok:
        X = np.array([[ Current_Loan_Amount, Annual_Income, Monthly_Debt, 
                       Current_Credit_Balance, 
                       Tax_Liens, Home_Ownership, Purpose,
                       Loan_Status, Years_in_current_job]])
        
        X = pd.DataFrame(columns=columns)

        prediction = xgboost.predict(X)

        if prediction == 1:
            prediction = "Short Term Loan"
        else:
            prediction = "Long Term Loan"
            
        st.subheader(f"Your Loan Term is: \n {prediction}")


show_predict_page()