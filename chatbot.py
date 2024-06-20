import openai
import streamlit as st
import re

# Set Streamlit page configuration
st.set_page_config(page_title='Conversational Chatbot', layout='wide', page_icon="🤖")

# Initialize session states
if 'history' not in st.session_state:
    st.session_state.history = [{"role": "system", "content": "You are a helpful assistant."}]
if 'user_input' not in st.session_state:
    st.session_state.user_input = ""
if "generated" not in st.session_state:
    st.session_state["generated"] = []
if "past" not in st.session_state:
    st.session_state["past"] = []
if "input" not in st.session_state:
    st.session_state["input"] = ""
if "stored_session" not in st.session_state:
    st.session_state["stored_session"] = []
if "selected_session" not in st.session_state:
    st.session_state["selected_session"] = None

# Sidebar
with st.sidebar:
    st.markdown("# About")
    st.markdown("This is a conversational chatbot interface powered by OpenAI's GPT-3.5 model. It allows you to have interactive conversations and get helpful responses.")
    st.markdown("---")
    # Let user select version
    st.write("Choose ChatGPT version:")
    version = st.selectbox("Choose ChatGPT version", ("3.5", "4.5"))
    if version == "3.5":
        # Use GPT-3.5 model
        MODEL = "gpt-3.5-turbo"
    else:
        # Use GPT-4.5 model
        MODEL = "gpt-4-turbo"
    
    # Ask the user to enter their OpenAI API key
    API_O = st.text_input("API-KEY", type="password")

# Custom CSS for styling
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden; }
    footer {visibility: hidden;}
    .stTextInput div {background-color: #1E1E1E; color: white; border: 1px solid #4B4B4B; border-radius: 5px; padding: 10px; margin-bottom: 10px;}
    .stButton button {background-color: #4B4B4B; color: white; border: none; border-radius: 5px; padding: 10px; margin: 5px;}
    .stButton button:hover {background-color: #3E3E3E; color: white;}
    .chat-container {max-height: 400px; overflow-y: auto; background-color: #1E1E1E; color: white; border-radius: 10px; padding: 10px; margin-bottom: 10px;}
    .user-message {background-color: #4B4B4B; border-radius: 10px; padding: 10px; margin: 5px 0; text-align: right; color: white;}
    .bot-message {background-color: #3E3E3E; border-radius: 10px; padding: 10px; margin: 5px 0; text-align: left; color: white;}
    .message-content {display: inline-block; max-width: 80%;}
    </style>
    """,
    unsafe_allow_html=True
)

def get_openai_response(messages):
    if API_O:
        openai.api_key = API_O
    else:
        st.sidebar.warning('API key required to try this app.')
        st.stop()

    client = openai.OpenAI(api_key=openai.api_key)
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_tokens=200,
        temperature=0
    )
    return response.choices[0].message.content

def is_four_digit_number(string):
    pattern = r'^\d{4}$'  # Matches exactly four digits
    return bool(re.match(pattern, string))

# Display the conversation history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = ""

chat_history_placeholder = st.empty()

def update_chat_history():
    chat_html = "<div class='chat-container'>"
    for message in st.session_state.history:
        if message["role"] == "user":
            chat_html += f"<div class='user-message'><span class='message-content'>{message['content']}</span></div>"
        elif message["role"] == "assistant":
            chat_html += f"<div class='bot-message'><span class='message-content'>{message['content']}</span></div>"
    chat_html += "</div>"
    st.session_state.chat_history = chat_html

update_chat_history()
chat_history_placeholder.markdown(st.session_state.chat_history, unsafe_allow_html=True)

# Input text
def clear_text():
    st.session_state["user_input"] = ""

# JavaScript to clear the input field when it gains focus
clear_input_script = """
<script>
document.getElementById('input-field').addEventListener('focus', function(){
    this.value = '';
});
</script>
"""

user_input = st.text_input("Message ChatGPT", value=st.session_state.user_input, key="input", placeholder="Type your message here...", label_visibility="collapsed")

st.markdown(f'<div id="input-field"></div>', unsafe_allow_html=True)
st.markdown(clear_input_script, unsafe_allow_html=True)

# Centered buttons next to each other below the text area
col1, col2, col3 = st.columns([1, 4, 1])

with col1:
    pass  # Empty column for centering

with col2:
    button_cols = st.columns(3)
    with button_cols[0]:
        send_button = st.button("Send")
    with button_cols[1]:
        clear_button = st.button("Clear")
    with button_cols[2]:
        view_history_button = st.button("View History")

with col3:
    pass  # Empty column for centering

# Button to send the input
if send_button:
    if user_input:
        # Append user input to history
        st.session_state.history.append({"role": "user", "content": user_input})
        
        # Get the response from the model
        bot_response = get_openai_response(st.session_state.history)
        
        # Append bot response to history
        st.session_state.history.append({"role": "assistant", "content": bot_response})
        
        # Update the chat history
        update_chat_history()
        chat_history_placeholder.markdown(st.session_state.chat_history, unsafe_allow_html=True)
        
        # Clear the input field after sending
        st.session_state.user_input = ""
        st.experimental_rerun()

# Button to clear the input field
if clear_button:
    st.session_state.user_input = ""
    st.experimental_rerun()

# Button to view conversation history
if view_history_button:
    st.write("Conversation History:")
    for message in st.session_state.history:
        if message["role"] != "system":
            st.write(f"{message['role'].capitalize()}: {message['content']}")

# JavaScript to auto-scroll the chat history
st.markdown(
    """
    <script>
    const chatContainer = document.querySelector('.chat-container');
    chatContainer.scrollTop = chatContainer.scrollHeight;
    </script>
    """,
    unsafe_allow_html=True
)

# Additional elements and functionalities
hide_default_format = """
<style>
#MainMenu {visibility: hidden; }
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_default_format, unsafe_allow_html=True)

# Define function to start a new chat
def new_chat():
    """
    Clears session state and starts a new chat.
    """
    save = []
    for i in range(len(st.session_state.history)-1, -1, -1):
        message = st.session_state.history[i]
        if message["role"] == "user":
            save.append("User:" + message["content"])
        elif message["role"] == "assistant":
            save.append("Bot:" + message["content"])
    st.session_state["stored_session"].append(save)
    st.session_state["generated"] = []
    st.session_state["past"] = []
    st.session_state.history = [{"role": "system", "content": "You are a helpful assistant."}]
    st.session_state.selected_session = None
    st.experimental_rerun()

# Function to display a selected session
def display_session(session):
    st.session_state.history = [{"role": "system", "content": "You are a helpful assistant."}]
    for i in range(len(session)):
        if session[i].startswith("User:"):
            st.session_state.history.append({"role": "user", "content": session[i][5:]})
        elif session[i].startswith("Bot:"):
            st.session_state.history.append({"role": "assistant", "content": session[i][4:]})
    update_chat_history()

# Sidebar for new chat and session management
with st.sidebar:
    if st.button("New Chat"):
        new_chat()
    if st.session_state.stored_session:
        if st.button("Clear-all"):
            del st.session_state.stored_session
        for i, sublist in enumerate(st.session_state.stored_session):
            if st.button(f"Conversation-Session:{i}"):
                display_session(sublist)
                
        if st.session_state.selected_session is not None:
            with st.expander(label=f"Conversation-Session:{st.session_state.selected_session}"):
                for message in st.session_state.history:
                    if message["role"] == "user":
                        st.write(f"User: {message['content']}")
                    elif message["role"] == "assistant":
                        st.write(f"Bot: {message['content']}")

# Update the chat history for display
update_chat_history()
