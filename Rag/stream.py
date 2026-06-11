import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Import your RAG chain
from    app import chain

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="🌱 FarmerBot",
    page_icon="",
    layout="centered"
)

# =====================================
# HEADER
# =====================================

st.title("🌱 FarmerBot")
st.markdown(
    """
    Ask questions about weeds in:

    - English
    - Hindi
    - Tamil
    - Tanglish
    """
)

# =====================================
# SESSION STATE
# =====================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# =====================================
# DISPLAY CHAT HISTORY
# =====================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# =====================================
# CHAT INPUT
# =====================================

question = st.chat_input(
    "Ask a weed-related question..."
)

# =====================================
# PROCESS QUESTION
# =====================================

if question:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Generate answer
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = chain.invoke(question)

                answer = (
                    response.content
                    if hasattr(response, "content")
                    else str(response)
                )

            except Exception as e:

                answer = f"Error: {str(e)}"

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.header("About")

    st.write(
        """
        FarmerBot is a Weed Identification Assistant
        powered by:
        
        - LangChain
        - ChromaDB
        - OpenAI
        - Streamlit
        """
    )

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()