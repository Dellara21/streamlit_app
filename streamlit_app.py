import streamlit as st
import numpy as np
import altair as alt
import pandas as pd

#...

st.header('st.button')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

#...

st.header('st.write')

#example 1
st.write('Hello, *World!* :star:')

#example 2
st.write(1234)

#example 3
df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
    })
st.write(df)

#example 4
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

#example 5
df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns = ['a','b','c'])
st.write(df2)
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a','b','c'])
st.write(c)
