'''Use checkboxes to show/hide data
One use case for checkboxes is to hide or show a specific chart or 
section in an app. st.checkbox() takes a single argument, which is the widget label.
In this sample, the checkbox is used to toggle a conditional statement.'''


import streamlit as st
import numpy as np
import pandas as pd

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data