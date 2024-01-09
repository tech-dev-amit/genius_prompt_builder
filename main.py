# main_code.py
from openai import OpenAI
import streamlit as st
from chat_template import generate_prompt_template

# Set Streamlit theme
st.set_page_config(
    layout="wide",
    page_title="GeniusPrompter Chatbot",
    page_icon="💡",
    initial_sidebar_state="collapsed",
)

# Sidebar for OpenAI API key
with st.sidebar:
    st.image("logo.png", width=100)  # Replace with your logo
    st.title("GeniusPrompter Settings")
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")

# Main content
st.title("💬 Genius:orange[Prompter] Chatbot")
st.caption("🚀 A smart chatbot powered by OpenAI")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Tell me basics requirement from AI, so I can Build you perfect Prompt"}]

# Display chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Input from the user
if user_input := st.text_input("You:", key="user_input"):
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    task = user_input  # Set user input as the task

    # Generate prompt using the template
    prompt_template = generate_prompt_template(task)

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "system", "content": prompt_template})
    st.chat_message("user").write(task)  # Display the task in the chat UI

    # Get response from OpenAI
    response = client.chat.completions.create(model="gpt-4-1106-preview", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
