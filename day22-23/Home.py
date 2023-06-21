import streamlit as st
import pandas


st.set_page_config(layout="wide")

st.title(str("The best company").title())
content = """Bash is an sh-compatible command language interpreter that executes
       commands read from the standard input or from a file.  Bash also
       incorporates useful features from the Korn and C shells (ksh and csh)
    """
st.write(content)
st.subheader("Our Team")
col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data.csv")
with col1:
    for index, row in df[:4].iterrows():
        st.header(str(f"{row['first name']} {row['last name']}").title())
        st.write(row["role"])
        st.image("images/"+ row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.header(str(f"{row['first name']} {row['last name']}").title())
        st.write(row["role"])
        st.image("images/"+ row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.header(str(f"{row['first name']} {row['last name']}").title())
        st.write(row["role"])
        st.image("images/"+ row["image"])