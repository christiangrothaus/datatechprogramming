# run using:
# streamlit run Grothaus_Christian_Week10_Code.py

import streamlit as st
import pandas as pd
import altair as alt

df = pd.read_csv('diamonds.csv', index_col=0)

st.write("Table:")
st.write(df)

df = df[0:2000]

st.write("Line Chart:")
st.line_chart(df, x='carat', y='price')

webExampleDf = pd.DataFrame({
  'value': [850, 925, 900, 920, 1300, 1350, 1300],
  'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
})

chart = alt.Chart(webExampleDf).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(x=alt.X('day', sort=None, title=None), y=alt.Y('value', title=None))
st.write('Streamlit ECharts Demo Example:')
st.altair_chart(chart, use_container_width=True)