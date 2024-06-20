import openai
import streamlit as st

# Set the OpenAI API key directly in the script
openai.api_key = 'sk-proj-4XML6Zyl96jTT2AZcHNaT3BlbkFJxJPprPLZT6SqgMb54NPI'

# Create an OpenAI client instance
client = openai.OpenAI(api_key=openai.api_key)

def get_openai_response(messages):
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=messages,
        max_tokens=200,
        temperature=0
    )
    return response.choices[0].message.content

# Initialize conversation history
if 'history' not in st.session_state:
    st.session_state.history = [{"role": "system", "content": "You are a helpful assistant."}]

if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stTextInput {
        background-color: #1E1E1E;
        color: white;
        border: 1px solid #4B4B4B;
        border-radius: 5px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .stButton button {
        background-color: #4B4B4B;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px;
        margin: 5px;
    }
    .stButton button:hover {
        background-color: #3E3E3E;
        color: white;
    }
    .chat-container {
        max-height: 400px;
        overflow-y: auto;
        background-color: #1E1E1E;
        color: white;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .user-message {
        background-color: #4B4B4B;
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
        text-align: right;
        color: white;
    }
    .bot-message {
        background-color: #3E3E3E;
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
        text-align: left;
        color: white;
    }
    .message-content {
        display: inline-block;
        max-width: 80%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Conversational Chatbot")

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
user_input = st.text_input("Message ChatGPT", value="", key="input", placeholder="Type your message here...", label_visibility="collapsed")

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