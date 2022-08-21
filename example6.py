"""
# Draw charts and maps
Streamlit supports several popular data charting libraries like Matplotlib, Altair, deck.gl, and more. 
In this section, you'll add a bar chart, line chart, and a map to your app.

# Draw a line chart
You can easily add a line chart to your app with st.line_chart(). We'll generate a random sample using Numpy and then chart it.
"""

import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)
