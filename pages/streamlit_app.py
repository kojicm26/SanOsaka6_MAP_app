# streamlit_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()
st.title("pet.ss")
st.write(df)

# Print results.
# for row in df.itertuples():
#     st.write(f"{row.name} has a :{row.pet}:")