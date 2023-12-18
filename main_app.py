import streamlit as st
from streamlit_gsheets import GSheetsConnection




url = "https://docs.google.com/spreadsheets/d/1JDy9md2VZPz4JbYtRPJLs81_3jUK47nx6GYQjgU8qNY/edit?usp=sharing" #サンプル(date&births)

conn = st.experimental_connection("gsheets", type=GSheetsConnection)
# conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(spreadsheet=url, usecols=["date"])
st.title("date&births")
st.write(df)
