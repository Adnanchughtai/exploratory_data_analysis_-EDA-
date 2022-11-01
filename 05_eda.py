import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Web ap title
st.markdown('''
# **Ecploratory Data Analysis web application**
This web application is created to perform exploratory data analysis on the dataset **EDA app**
''')

# How to upload a file from pc

with st.sidebar.header("Upload your dataset (.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload your file", type=['csv'])
    df = sns.load_dataset('titanic')
    st.sidebar.markdown("[Example CSV file](df)")
    
# Profiling report for pandas

if uploaded_file is not None:
    
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DF**')
    st.write(df)
    st.write('---')
    st.header('**Profiling report with pandas**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded')
    if st.button('Press to use example data'):
         # Example data
        @st.cache
        def load_data():
            a = pd.DataFrame( np.random.rand(100,5),
                                columns=['name', 'Adnan', 'mubashir', 'Usman', 'muzammil'])
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DF**')
        st.write(df)
        st.write('---')
        st.header('**Profiling report with pandas**')
        st_profile_report(pr)
