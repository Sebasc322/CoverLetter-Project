import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


st.set_page_config(page_title="Exploratory Data Analysis", page_icon="📊", layout="wide")

st.title('Exploratory Data Analysis! :bar_chart:')

st.write('Please Upload your CSV file')


uploaded_file = st.file_uploader("Choose a file", type=['csv'])
if uploaded_file is not None:
    st.write('You have uploaded a CSV file.')
    df = pd.read_csv(uploaded_file, index_col=0)
    st.write('Here is a sample of your data:')
    st.write(df.head())
    st.write(f'Your dataset contains {len(df.columns)} columns and {len(df)} rows')

    st.write("The following button will generate a quick Exploratory Data Analysis of your data")
    eda = st.button("Generate a quick EDA")
    if eda:
        st.write('Exploratory Data Analysis - Profiler')
        
        pr = ProfileReport(df, explorative=True)
        st_profile_report(pr)

else:
    st.warning("Upload a CSV, your file is not in CSV format.",icon='⚠')