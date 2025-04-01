'''Use a selectbox for options
Use st.selectbox to choose from a series. You can write in the options you want, or pass through an array or data frame column.

Let's use the df data frame we created earlier.'''

import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option