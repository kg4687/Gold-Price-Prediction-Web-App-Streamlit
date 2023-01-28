# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 16:07:12 2023

@author: HP
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('gold_price_predictor.sav','rb'))

#creating a function for prediction
''' def gold_price_prediction(input_data):
    #changing the input_data to numpy data
    input_data_as_numpy_array = np.asarray(input_data)
    
    #reshape the array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)'''
    
def main():
    #giving the title
    st.title('Gold Price Predictor Web App')
    
    #getting input from user
    
    SPX = st.text_input('Sequenced Packet Exchange or SPX value : ')
    USO = st.text_input('USO value : ')
    SLV = st.text_input('SLV value : ')
    EUR_USD = st.text_input('EUR or USD value : ')
    
    predicted_price = ''
   
    #getting input data from the user
    if st.button('Predicted price of Gold : '):
        input_data = [SPX,USO,SLV,EUR_USD]
        input_data_as_numpy_array = np.asarray(input_data)
    
        #reshape the array
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
        prediction = loaded_model.predict(input_data_reshaped)
        print(prediction)
     
    st.success(predicted_price)

#Driver Code
if __name__ == '__main__':
    main()
