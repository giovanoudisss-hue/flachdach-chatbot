import streamlit as st
from openai import OpenAI

# --- App Setup ---
st.set_page_config(page_title="Smart Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 Chatbot – dein digitaler Assistent")
st.write("Stelle Fragen oder lass dir Ideen geben. Nutze ihn für Social Media, Lernen oder Beratung!")

# --- OpenAI Setup ---
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# --- Chatverlauf ---
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Schreibe hier deine Frage oder Nachricht:")

if st.button("Senden") and user_input:
    # Nachricht zum Verlauf hinzufügen
    st.session_state.messages.append({"role": "user", "content": user_input})

    # ChatGPT anrufen
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages,
            temperature=0.7,
            max_tokens=200
        )
        bot_reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    except Exception as e:
        st.error(f"Fehler: {e}")

# --- Chatverlauf anzeigen ---
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**Du:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")

st.markdown("---")
st.caption("Erstellt mit ❤️ – dein eigener Chatbot")
