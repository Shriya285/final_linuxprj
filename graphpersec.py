import json
import os
import shlex
import subprocess

import pandas as pd
import streamlit as st

st.write("""
    # Per Second syscalls
    ##SUSSYSYS##
         """)

df = pd.read_csv("data3.csv")
st.line_chart(df)

st.subheader("Persec")
if st.checkbox("Show information"):
    st.write("persec")

df = pd.read_csv("persec.csv")
fig = ff.create distplot(df)
st.plotly_chart(fig)

st.area_chart(df)
df = pd.read_csv("step3.csv")
df.hist()
st.pyplot()
#i am not quite sure but ig i have to put line 20 here.

df = pd.read_csv("data2.csv")
st.bar_chart(df)






