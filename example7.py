"""
# Plot a map
With st.map() you can display data points on a map. Let's use Numpy to generate some sample data and plot it on a map of San Francisco.
"""

import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
