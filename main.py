import streamlit as st

st.title("Ini aplikasi pertamaku")
st.header("By Maulana Malik Ibrahim")
st.chat_message("user")
nama = st.text_input("Masukkan nama Anda")
prompt = st.chat_input("Say something")
if not nama:
    st.stop()
st.markdown(f'Selamat <b>datang</b> {nama}', unsafe_allow_html=True)
if prompt:
    st.write(f"Prompt is: {prompt}")