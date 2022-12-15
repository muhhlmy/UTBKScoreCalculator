import streamlit as st

st.title('''UTBK Score Calculator
##### By Seazyn


#''')

st.subheader('Nilai TPS')
PU  = st.number_input('Penalaran Umum')
PBM = st.number_input('Pemahaman Bacaan dan Menulis')
PBU = st.number_input('Pengetahuan Umum')
PK  = st.number_input('Pengetahuan Kuantitatif')

st.subheader('Nilai TKA')
Biologi    = st.number_input('Biologi')
Fisika     = st.number_input('Fisika')
Kimia      = st.number_input('Kimia')
Matematika = st.number_input('Matematika')

st.subheader('Nilai Bahasa Inggris')
Bhs_Inggris = st.number_input('Bahasa Inggris')

Hitung = st.button('Hitung')

if Hitung:
    RataTKA = (Biologi + Fisika + Kimia + Matematika) / 4
    RataTPS = (PU + PBM + PBU + PK) / 4
    Total   = (RataTKA + RataTPS + Bhs_Inggris) / 3
    Total   = round(Total, 3)
    st.success(f'Skor UTBK Anda Adalah {Total}')
