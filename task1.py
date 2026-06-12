import streamlit as st
from deep_translator import GoogleTranslator

# Page Settings
st.set_page_config(
    page_title="Language Translator",
    page_icon="🌍"
)

st.title("🌍 Language Translation Tool")

# Languages
languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Tamil": "ta",
    "Kannada": "kn"
}

# Text Input
text = st.text_area("Enter Text")

# Character Count
st.write(f"Characters: {len(text)}")

# Language Selection
source = st.selectbox(
    "Source Language",
    list(languages.keys())
)

target = st.selectbox(
    "Target Language",
    list(languages.keys())
)

# Translate Button
if st.button("Translate"):
    if text.strip():

        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        st.success("✅ Translation Complete")

        st.subheader("Translated Text")

        # Copy-friendly output
        st.code(translated)

    else:
        st.warning("⚠ Please enter some text")