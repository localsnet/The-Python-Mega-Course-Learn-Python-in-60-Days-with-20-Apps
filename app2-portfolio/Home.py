import streamlit as st
import pandas


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image("images/run.jpg")
with col2:
    st.title ("Kids")
    content = """ Привет это мы - детишки :) ! Bash is an sh-compatible command language interpreter that executes
       commands read from the standard input or from a file.  Bash also
       incorporates useful features from the Korn and C shells (ksh and csh)
    """
    st.info(content)

content2 = """Наш позывной .-..--..-.-.--- . Copyright © 2023 Free Software Foundation, Inc.  License GPLv3+"""
st.text(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+ row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")
