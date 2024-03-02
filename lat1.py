import streamlit as st
#import pandas as pd
#import matplotlib.pyplot as plt

# st.write("Kyaya Tabel Coding")
# df = pd.DataFrame({
#     'No' : [1,2,3,4],
#     'Nama' : ['Nadia','Zahwa','Putri','Kia'],
#     'Nilai' : [99,98,100,94]
# })

# df

def page_1():
    st.title("Halaman")
    st.write("Halaman ini digunakan untuk Intro")
def page_2():
    st.title("Halaman")
    st.write("Halaman ini digunakan untuk Menampilkan youtube")
def page_3():
    st.title("Halaman")
    st.write("Halaman ini digunakan untuk Menampilkan Rumus Matematika")

PAGES = {
    "Page 1" : page_1,
    "Page 2" : page_2,
    "Page 3" : page_3
}

page = st.sidebar.radio("Halaman", list(PAGES.keys()))
PAGES[page]()


