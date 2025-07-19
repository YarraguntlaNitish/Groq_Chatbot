
# Groq-Powered Chatbot: AI Conversation Chatbot with LangChain and Streamlit 🚀



Welcome to the Groq-Powered Chatbot project! This is a sleek, interactive chatbot built using LangChain for smart conversations, Groq Cloud for lightning-fast AI inference, and Streamlit for an intuitive web interface. It features conversation memory, streaming responses and uses the powerhouse Llama 3 70B model – one of the best open-source options on Groq.

Whether you're a developer experimenting with AI or just want a fun chat companion, this project lets you deploy your own chatbot in minutes. Let's dive in!

🌟 Why This Chatbot Rocks
* Intelligent & Contextual: Remembers your conversation history for personalized, flowing dialogues.
* Blazing Fast: Powered by Groq's API for near-instant responses.
* User-Friendly UI: Streamlit makes it simple to chat – no complex setups needed.
* Open-Source Friendly: Uses the top-tier Llama 3 70B model for high-quality, ethical AI.
* Customizable: Easily tweak for your needs, like adding new models or features.


## Tech Stack

Tech Stack:

**LangChain**: For conversation logic and memory.

**Groq Cloud**: API for the Llama 3 70B model.

**Streamlit**: Web UI framework.

**Python**: Core language.


## 🛠️ Step-by-Step Setup Guide
Follow these steps to get your chatbot up and running locally. It's beginner-friendly – no prior AI experience required!

Step 1: Prerequisites
Install Python 3.8+ (download from python.org if needed).

Get a free Groq Cloud API key: Sign up at console.groq.com and generate one.

Install Git for cloning (optional, but handy).

Step 2: Clone the Repository
Open your terminal or command prompt.

* Run:
```bash
  git clone https://github.com/YarraguntlaNitish/Groq_Chatbot.git
```

* Navigate to the project folder:

```bash
  cd groq-chatbot
```

Step 3: Install Dependencies
* Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
* Install required packages:
```bash
pip install streamlit langchain-groq langchain
```
Pro Tip: Create a requirements.txt file with these lines for easy installs:
```bash
streamlit
langchain-groq
langchain
```
Step 4: Run the Chatbot Locally
* Save the provided code as chatbot.py (see the Code section below).

Launch the app:
```bash
streamlit run chatbot.py
```
* Open your browser to http://localhost:8501.

* Enter your Groq API key in the input field.

* Start chatting! Type messages and watch the AI respond with memory and streaming effects.
Troubleshooting: If you hit API errors, check your Groq key or rate limits in their dashboard.


## Contributing

Love this project? Fork it, make improvements (e.g., add more models or themes), and submit a pull request! Let's build something awesome together.


## License

[MIT](https://choosealicense.com/licenses/mit/)

This project is licensed under the MIT License – feel free to use, modify, and share.

Built with ❤️ by Nitish. Star the repo if it helped!
