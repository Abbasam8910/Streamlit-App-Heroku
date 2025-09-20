import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved model

diabetes_model = pickle.load(open('../Day 44/trained_model.sav', 'rb'))
heart_disease_model = pickle.load(open('../Day 44/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('../Day 44/parkinsons_model.sav', 'rb'))

# Sidebar for Saved Model

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System', 
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'], icons=['activity', 'heart', 'person'], default_index=0 )


# Diabetes Prediction Page

if (selected =='Diabetes Prediction'):

    # Page Title
    st.title('Diabetes Prediction ')

    # Getting the input from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnencies = st.text_input('Number of Pregnencies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input("Blood Pressure Level")

    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')

    with col2:
        Insulin = st.text_input('Insulin Value')

    with col3:
        BMI = st.text_input("BMI Value")
    
    with col1:
        DiabetesPedegreeFunction = st.text_input('Diabetes Pedegree Function Value')

    with col2:
        Age = st.text_input('Age')


    # Code of Prediction

    diabetes_diagnosis = ''

    if st.button('Diabetes Test Result'):
        diabetes_prediction = diabetes_model.predict([[Pregnencies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedegreeFunction, Age]])


        if diabetes_prediction[0] == 1:
            diabetes_diagnosis  = 'This Person is Diabetic'
        else:
            diabetes_diagnosis = 'This Person is Not Diabetic'

    st.success(diabetes_diagnosis)


# Heart Prediction Page

elif(selected =='Heart Disease Prediction'):

    # Page title

    st.title("Heart Disease Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")
    
    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain Type')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestrol in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalch = st.text_input('Maximum Heart Rate Achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    
    with col2:
        slope = st.text_input('Slope of Peak exercise ST segment')
    
    with col3:
        ca = st.text_input('Major vessel colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    
    # Code for Prediction

    heart_diagnosis = ''

    # Creating a button for prediction

    if st.button('Heart Disease Result'):
        heart_prediction = heart_disease_model.predict([[float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs), float(restecg), float(thalch), float(exang), float(oldpeak), float(slope), float(ca), float(thal)]])

        if(heart_prediction[0] ==1):
            heart_diagnosis = 'The person is having Heart Disease'
        else:
            heart_diagnosis = 'The person does not have Heart Disease'

    st.success(heart_diagnosis)
    
# Parkinson Disease Page

if(selected =='Parkinsons Prediction'):
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs), float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB), float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR), float(HNR), float(RPDE), float(DFA), float(spread1), float(spread2), float(D2), float(PPE)]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)



