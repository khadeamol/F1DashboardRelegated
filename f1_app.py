import streamlit as st 
import pandas as pd
import os 
import fastf1 as ff
from time import time
import driver_trace
import trace_options

def yearList():
    yearList = os.listdir("Cache")
    print(yearList.sort())
    return yearList

def raceListGenerator(year):
    raceList = os.listdir(f"Cache/{year}")
    return raceList

schedule = pd.read_parquet("./races_by_year.pq")
yearSel = '2024'
eventList = schedule[schedule['EventYear'] == yearSel]
lapTimingDetails = ""



with st.sidebar:
    with st.form("Base Form"):
        yearSel = st.selectbox("Select Year",yearList())
        # yearSel = st.text_input("Enter Year:")
        raceSel = st.selectbox("Select Event:", eventList)
        sessionSel = st.selectbox("Select Session:",options=["Race","Qualifying","FP1","FP2", "FP3", "Sprint"])
        print("Good work!")
        typeSel = st.radio("Analysis Type:", options=['Driver Lap Speed Trace', 'Driver Speed Comparison'])
        typeSubmit = st.form_submit_button("Go!")
        if typeSel is "Driver Lap Speed Trace":
            driverSel = st.text_input("Enter Driver Identifier")
            lapSelect = st.text_input("Enter Lap Number", placeholder="Pick Fastest")
            submitted = st.form_submit_button("Submit")
            if submitted:
                print(driverSel)
                lapTimingDetails = driver_trace.plot_traces(int(yearSel), raceSel, sessionSel, driverSel, lapSelect)

        elif typeSel is 'Driver Speed Comparison':
            driverSel = st.text_input("Enter First Driver")
            driver2Sel = st.text_input("Enter Second Driver")
            lapSelect = st.text_input("Enter Lap Number", placeholder="Pick Fastest")
            submitted = st.form_submit_button("Submit")
            if submitted:
                print(driverSel)
                lapTimingDetails = driver_trace.plot_traces(int(yearSel), raceSel, sessionSel, driverSel, lapSelect)
        

        # driver2Sel = st.text_input("Add Second Driver for comparison")


st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(lapTimingDetails)

# Once user selects a year, the race dropdown will change
# depending on the races that happened that year
# Does this add