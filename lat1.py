import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt

st.write("KyayaPuput Tabel Coding")
df = pd.DataFrame({
    'No' : [1,2,3,4],
    'Nama' : ['Nadia','Zahwa','Putri','Kia'],
    'Nilai' : [99,98,100,94]
})

df