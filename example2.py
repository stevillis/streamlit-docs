"""
# Write a data frame
Along with magic commands, st.write() is Streamlit's "Swiss Army knife". 
You can pass almost anything to st.write(): text, data, Matplotlib figures, Altair charts, and more. 
Don't worry, Streamlit will figure it out and render things the right way.
"""

import streamlit as st
import pandas as pd

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
