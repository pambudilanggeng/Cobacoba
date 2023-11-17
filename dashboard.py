import streamlit as st
import pandas as pd

st.markdown(
  """
  Selamat datang di dashboard Langgeng Pambudi!
  """
)

st.title('Belajar Analisis Data')
st.header('Pengembangan Dashboard')
st.caption('Copyright 2023')

with st.sidebar:

	st.text('Daftar isi')

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Tab1", "Tab2", "Tab3", "Tab4", "Tab5", "Tab6", "Tab7"])

with tab1:
	st.header("Tab 1")
	st.image("https://asset.kompas.com/crops/omxM17lGj0pcdrwKaY_6V2zHs2s=/193x48:770x433/750x500/data/photo/2019/12/21/5dfd6dab1565d.jpg")

with tab2:
	st.header("Tab 2")
	st.image("https://drive.google.com/file/d/1h0hYrirIc0io62PT3H1BcV6W842WooeE/view")

with tab3:
	st.header("Tab 3")
	st.image("https://drive.google.com/file/d/1h290eshTIfMHx-s1IwDy9scQ0nMLPn0K/view")


with tab4:
	st.header("Tab 4")
	st.image("https://drive.google.com/file/d/1553DvDB_8FD03kETers933p4FaU8DNKg/view")


with tab5:
	st.header("Tab 5")
	st.image("https://drive.google.com/file/d/1ycz6ybFFejAD_vi_Y2mtYYKuDJ3FNC4I/view")


with tab6:
	st.header("Tab 6")
	st.image("https://drive.google.com/file/d/1UmR3j-opUJgaYsMvUcAHapNph_Q0GQ9-/view")



with tab7:
	st.header("Tab 7")
	st.image("none")
