from tts import main
import streamlit as st

st.set_page_config("Озвучивание текста")
text_input = st.text_area('', placeholder='Введите ваш текст:')

st.base = "dark"
st.markdown(
    """
    <style>
    textarea {
    height: 300px;
    width: 100%;
    border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
if st.button('Отправить'):
    main(text_input)
    print(11)
    try:
        if st.audio('./files/audio_file.wav'):
            st.text('Можете прослушать и скачать ваш файл')

    except:
        st.text('Файл не создан.\nПопробуйте ввести другой текст на русском языке')
