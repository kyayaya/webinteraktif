import streamlit as st
from page1 import page_1
from page2 import page_2
from page3 import page_3
from page4 import page_4
from image1 import main
#import matplotlib.pyplot as plt

# st.write("Kyaya Tabel Coding")
# df = pd.DataFrame({
#     'No' : [1,2,3,4],
#     'Nama' : ['Nadia','Zahwa','Putri','Kia'],
#     'Nilai' : [99,98,100,94]
# })

# df






PAGES = {
    "Page 1" : page_1,
    "Page 2" : page_2,
    "Page 3" : page_3,
    "Page 4" : page_4,
    "gambar" : main
}

st.sidebar.image("rill.png", width=200)
page = st.sidebar.radio("Halaman", list(PAGES.keys()))
PAGES[page]()

st.markdown(
    """
        <style>
        [data-testid= "stActionButtonIcon"] {
            display: none;

        }
        [data-testid= "baseButton-header"] {
            display: none;
            
        }

        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        </style>
        """,

unsafe_allow_html=True,
)