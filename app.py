import pandas as pd
import streamlit as st
import pickle
import numpy as np
import sklearn

DTR_model=pickle.load(open('DTR_model.pkl','rb'))

st.title("COOLING LOAD CALCULATOR")

def main():
    Relative_Compactness = st.number_input('Relative Compactness')
    Wall_Area = st.number_input('Wall Area')
    Overall_Height = st.number_input('Overall Height')
    Orientation = st.number_input('Orientation')
    Glazing_Area = st.number_input('Glazing Area')
    Glazing_Area_Distrubution = st.number_input('Glazing Area Distrubution')

    inputs=[[Relative_Compactness,Wall_Area,Overall_Height,Orientation,Glazing_Area,Glazing_Area_Distrubution]]
    cooling_load=DTR_model.predict(inputs)

    if st.button('Predict'):
        st.title("The Predicted Cooling Load Required is " +str(float(np.round(cooling_load[0],2))))

if __name__=='__main__':
    main()