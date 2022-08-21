"""
Display and style data
There are a few ways to display data (tables, arrays, data frames) in Streamlit apps. 
Below, you will be introduced to magic and st.write(), which can be used to write anything from text to tables. 
After that, let's take a look at methods designed specifically for visualizing data.

# Use magic
You can also write to your app without calling any Streamlit methods. 
Streamlit supports "magic commands," which means you don't have to use st.write() at all! To see this in action try this snippet:

# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'first_column': [1, 2, 3, 4],
    'second_column': [10, 20, 30, 40]
})

df
