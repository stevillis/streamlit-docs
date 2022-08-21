"""
There are other data specific functions like st.dataframe() and st.table() that you can also use for displaying data. Let's understand when to use these features and how to add colors and styling to your data frames.

You might be asking yourself, "why wouldn't I always use st.write()?" There are a few reasons:

1. Magic and st.write() inspect the type of data that you've passed in, and then decide how to best render it in the app. Sometimes you want to draw it another way. 
For example, instead of drawing a dataframe as an interactive table, you may want to draw it as a static table by using st.table(df).
2. The second reason is that other methods return an object that can be used and modified, either by adding data to it or replacing it.
3. Finally, if you use a more specific Streamlit method you can pass additional arguments to customize its behavior.

For example, let's create a data frame and change its formatting with a Pandas Styler object. 
In this example, you'll use Numpy to generate a random sample, and the st.dataframe() method to draw an interactive table.
"""

import streamlit as st
import numpy as np

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)
