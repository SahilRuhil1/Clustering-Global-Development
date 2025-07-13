# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 13:02:09 2024

@author: Admin
"""

import streamlit as st
import pandas as pd
import joblib

# Load the pipeline
pipeline = joblib.load('cluster_pipeline.pkl')

# Define the prediction function
def predict(input_df):
    cluster = pipeline.predict(input_df)[0]  # Get the cluster label
    return cluster

def main():
    st.title("Global Development Measurement Cluster Prediction")
    st.write("Enter the values for the following features:")

    # Input fields with validation
    BirthRate = st.number_input("Birth Rate", value=0.0, step=0.1)
    BusinessTaxRate = st.number_input("Business Tax Rate", value=0.0, step=0.1)
    CO2Emissions = st.number_input("CO2 Emissions", value=0.0, step=0.1)
    Country = st.number_input("Country", value = 0.0, step=0.1)
    DaystoStartBusiness = st.number_input("DaystoStartBusiness", value=0.0, step=0.1)
    EnergyUsage = st.number_input("EnergyUsage", value=0.0, step=0.1)
    GDP = st.number_input("GDP", value=0.0, step=0.1)
    HealthExpGDP = st.number_input("HealthExpGDP", value=0.0, step=0.1)
    HealthExpCapita = st.number_input("Health Exp/Capita", value=0.0, step=0.1)
    InfantMortalityRate = st.number_input("Infant Mortality Rate", value=0.0, step=0.1)
    InternetUsage = st.number_input("Internet Usage", value=0.0, step=0.1)
    LendingInterest = st.number_input("Lending Interest", value=0.0, step=0.1)
    LifeExpectancyFemale = st.number_input("Life Expectancy Female", value=0.0, step=0.1)
    LifeExpectancyMale = st.number_input("LifeExpectancyMale", value=0.0, step=0.1)
    MobilePhoneUsage = st.number_input("Mobile Phone Usage", value=0.0, step=0.1)
    Population0to14 = st.number_input("Population0to14", value=0.0, step=0.1)
    Population15to64 = st.number_input("Population15to64", value=0.0, step=0.1)
    Populationmorethan65 = st.number_input("Populationmorethan65", value=8.0, step=0.1)
    PopulationTotal = st.number_input("Population Total", value=0.0, step=0.1)
    PopulationUrban = st.number_input("PopulationUrban", value=0.0, step=0.1)
    TourismInbound = st.number_input("TourismInbound", value=0.0, step=0.1)
    TourismOutbound = st.number_input("TourismOutbound", value=0.0, step=0.1)
    
    # Create input DataFrame
    input_df = pd.DataFrame({
        'BirthRate': [BirthRate],
        'BusinessTaxRate': [BusinessTaxRate],
        'CO2Emissions': [CO2Emissions],
        'Country' : [Country],
        'DaystoStartBusiness' : [DaystoStartBusiness],
        'EnergyUsage' : [EnergyUsage],
        'GDP': [GDP],
        'HealthExpGDP' : [HealthExpGDP],
        'HealthExpCapita': [HealthExpCapita],
        'InfantMortalityRate': [InfantMortalityRate],
        'InternetUsage': [InternetUsage],
        'LendingInterest': [LendingInterest],
        'LifeExpectancyFemale': [LifeExpectancyFemale],
        'LifeExpectancyMale': [LifeExpectancyMale],
        'MobilePhoneUsage': [MobilePhoneUsage],
        'Population0to14': [Population0to14],
        'Population15to64' : [Population15to64],
        'Populationmorethan65' :[Populationmorethan65],
        'PopulationTotal': [PopulationTotal],
        'PopulationUrban' : [PopulationUrban],
        'TourismInbound' : [TourismInbound],
        'TourismOutbound': [TourismOutbound]
    })

    # Make prediction
    if st.button("Predict"):
        cluster = predict(input_df)
        st.write(f"Predicted Cluster: {cluster}")
      
if __name__ == "__main__":
    main()