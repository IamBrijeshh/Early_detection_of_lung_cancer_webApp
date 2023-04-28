# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 21:51:31 2023

@author: ASUS
"""

#import basic libraries

import numpy as np #used for working with numpy arrays
import pickle  #used for load the model
import streamlit as st #used for model deployment

#load the saved model
#Also we have to set path of directory where this model file is exists
#rb = reading the read binary file
load_model = pickle.load(open('trained_model.sav','rb'))


#create function 

#in input_data variable all features value will be stored 
def lung_cancer (input_data):
    
    # first take the input data from the user for prediction
    # whenever we will call this function user will enter the input, it will stored in input_data variable
    # Once it is done we will converting the input into numpy array

    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # from this load_model.predict(input_data_reshaped) we will get 0,1 value
    prediction = load_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 1):
      return 'High Posibilites of lung cancer'
    else:
      return'No risk of lung cancer'
      
#create UI
       
def main():

      #giving a title
      st.title('Early Detection of Lung Cancer')
      
      #the data should be same as in our datset frame
      #A part from the lung cancer column we have to take input data
      
      # create input data fields and create variable 
            
      GENDER = st.selectbox('Select Your Gender: MALE(1) and FEMALE(0)',(1,0))
      AGE = st.text_input('Enter Your Age: ')
      SMOKING = st.selectbox('Are you Smoker YES(2) or NO(1)?',(1,2))
      PEER_PRESSURE = st.selectbox('Are you feeling problem of PEER_PRESSURE YES(2) or NO(1)?',(1,2))
      FATIGUE = st.selectbox('Do you have problem of FATIGUE YES(2) or NO(1)?',(1,2))
      ALLERGY = st.selectbox('Do you have any particular ALLERGY YES(2) or NO(1)?',(1,2))
      WHEEZING = st.selectbox('Are you facing problem of WHEEZING YES(2) or NO(1)?',(1,2))
      COUGHING = st.selectbox('Do you have regular cough problem YES(2) or NO(1)?',(1,2))
      SWALLOWING_DIFFICULTY = st.selectbox('Do you have problem of SWALLOWING_DIFFICULTY YES(2) or NO(1)?',(1,2))
      CHEST_PAIN = st.selectbox('Are you facing problem of CHEST_PAIN YES(2) or NO(1)?',(1,2))
      
      #Code for Prediction part
      #calling lung_cancer function it will return the predict value based on labels
      
      diagnosis = ''  #null string
      #diagnosis variable will store lung_cancer function retrun value
      
      #creating button for prediction
      
      if st.button("Predict Result"):
          diagnosis = lung_cancer([GENDER,AGE,SMOKING,PEER_PRESSURE,FATIGUE,ALLERGY,WHEEZING,COUGHING,SWALLOWING_DIFFICULTY,CHEST_PAIN])
          
      st.success(diagnosis)
      #print the output
      
if __name__ == '__main__':
    main()      
      
      