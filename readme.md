# Conversational Chatbot

## Overview
This project is a conversational chatbot interface powered by OpenAI's GPT-3.5 and GPT-4 models. It allows users to have interactive conversations, remembers the conversation history, and can manage multiple chat sessions.

## Features
- **Interactive Conversations**: Engage in natural language conversations with the chatbot.
- **Memory Management**: The chatbot remembers the context of the conversation.
- **Multiple Sessions**: Ability to start new chat sessions and view previous ones.
- **Enhanced User Interface**: Custom CSS for a better user experience.

## Installation and Usage

### Prerequisites
- Python 3.10.0
- OpenAI API key

### Files
- `chatbot.py`: Main application code.
- `.python-version`: Specifies Python version 3.10.0.
- `requirements.txt`: Contains the necessary Python packages.
- `.env`: Contains the API key for testing (to be provided for demo purposes).

### Setup

1. **Clone the Repository**:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Set Up Virtual Environment**:
    ```sh
    python3 -m venv chatbot_env
    source chatbot_env/bin/activate
    ```

3. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Create `.env` File**:
    Create a `.env` file in the root directory of the project and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

5. **Run the Application**:
    ```sh
    streamlit run chatbot.py
    ```

6. **Put The API Key in the API Key Field on the USer Interface and hit enter**

 ### Example Usage

1. **Start a New Chat**:
    - Open the application and start a new chat session.
    - Enter Your API Key and hit enter.
    - Enter your message in the text input field and click "Send".

2. **View Conversation History**:
    - Click the "View History" button to see the conversation history.

3. **Manage Sessions**:
    - Use the sidebar to start a new chat or switch between saved sessions.
    - To move to a past chat, you must click twice.

4. **Clear Input**:
    - Click the "Clear" button to clear the History box below.

5. **Select you desired Model**:
   - Select between GPT-3.5-Turbo and GPT4 Models from OpenAI.

---

## Deployment
Deploy the application using Streamlit

## Technical Decisions and Tools
- **Language Model**: OpenAI's GPT-3.5 and GPT-4 for conversational capabilities.
- **Framework**: Streamlit for building the user interface.
- **Environment Management**: Python virtual environment for dependency management.
- **Styling**: Custom CSS for enhancing the user interface.
- **Version Control**: GitHub for source code management.

## Future Enhancements
- Improved UI/UX with additional functionalities.
- Implement RAG for a more informative conversational experience.

## License
This project is licensed under the MIT License 



---

Thank you for using this Conversational Chatbot! Enjoy interacting with the AI.

---


