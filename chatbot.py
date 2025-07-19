import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
import time

# Streamlit app title
st.title("Basic Groq-Powered Chatbot")

# Input for Groq API key
groq_api_key = st.text_input("Enter your Groq Cloud API key:", type="password")

if groq_api_key:
    # Initialize the Groq LLM with the best open-source model (Llama 3 70B)
    llm = ChatGroq(
        groq_api_key=groq_api_key,
        model_name="llama3-70b-8192"  # Best open-source model on Groq for general tasks
    )

    # Initialize memory for conversation history
    if "memory" not in st.session_state:
        st.session_state.memory = ConversationBufferMemory()

    # Initialize the conversation chain with memory
    if "conversation" not in st.session_state:
        st.session_state.conversation = ConversationChain(
            llm=llm,
            verbose=True,
            memory=st.session_state.memory
        )

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    if prompt := st.chat_input("Type your message here..."):
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response with memory
        with st.chat_message("assistant"):
            # Get the full response from the chain
            full_response = st.session_state.conversation.predict(input=prompt)

            # Stream the response line by line for a nice feel
            response_container = st.empty()
            streamed_response = ""
            lines = full_response.split("\n")  # Split into lines
            for line in lines:
                words = line.split()  # Split line into words
                for word in words:
                    streamed_response += word + " "
                    response_container.markdown(streamed_response)
                    time.sleep(0.05)  # Delay for streaming effect
                streamed_response += "\n"  # Add newline after each line
                response_container.markdown(streamed_response)
                time.sleep(0.1)  # Slight delay between lines

        # Add assistant response to history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

else:
    st.warning("Please enter your Groq API key to start chatting.")
