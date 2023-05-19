import streamlit as st
st.title("The Home Page")
st.subheader("An App for EDA and Model Deployment")
# import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# get the data
data=pd.read_csv("data.csv")
data.drop('Unnamed: 0', axis=1, inplace=True)
zerofiller=lambda x: x.replace(0, x.median())
cols=data.columns[1:6].tolist()
data[cols]=data[cols].apply(zerofiller, axis=0)

st.write(data.describe().T)