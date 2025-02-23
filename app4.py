import streamlit as st
import requests
import uuid
import json

API_URL = "http://localhost:3000/api/v1/prediction/eae195bf-677a-4b55-9e5b-17f63cfdf4a3"

st.title("Multi-Agent AI Stock/ETF Analysis Tool 📉 📈")
st.markdown("## 📌 Overview")
st.markdown("""
    Advanced analytics platform combining three AI-powered analysis methodologies:
    A supervisor oversees three workers and deligates tasks to the following workers:
    1. **📊 Fundamental Analysis** - Financial health & valuation metrics  
    2. **📈 Technical Analysis** - Price patterns & trading signals  
    3. **🧠 Sentiment Analysis** - Market psychology & news trends  
""")

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'chat_id' not in st.session_state:
    st.session_state.chat_id = str(uuid.uuid4())

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about a stock/ETF..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # Prepare payload
        payload = {
            "question": prompt,
            "chatId": st.session_state.chat_id,
            "streaming": True
        }

        # Create placeholder and initialize variables
        full_response = ""
        placeholder = st.empty()
        current_section = None
        section_content = ""
        sources = set()

        with requests.post(API_URL, json=payload, stream=True) as response:
            response.raise_for_status()

            for chunk in response.iter_lines():
                if chunk:
                    decoded_chunk = chunk.decode('utf-8')
                    
                    if decoded_chunk.startswith('data:'):
                        try:
                            data = json.loads(decoded_chunk[5:])
                            
                            # Handle agent reasoning events
                            if data.get('event') == 'agentReasoning':
                                for agent in data.get('data', []):
                                    agent_name = agent.get('agentName', '')
                                    messages = agent.get('messages', [])
                                    
                                    if agent_name and messages:
                                        # Detect section changes
                                        if "Fundamental Analysis Specialist" in agent_name:
                                            current_section = "📊 Fundamental Analysis"
                                        elif "Technical Analysis Expert" in agent_name:
                                            current_section = "📈 Technical Analysis"
                                        elif "Market Sentiment Analyst" in agent_name:
                                            current_section = "🧠 Sentiment Analysis"
                                        
                                        if current_section:
                                            section_header = f"\n## {current_section}\n"
                                            if section_header not in full_response:
                                                full_response += section_header
                                            
                                            # Add messages
                                            for msg in messages:
                                                if isinstance(msg, str) and msg.strip():
                                                    cleaned_msg = msg.replace("**", "").strip()
                                                    full_response += f"{cleaned_msg}\n\n"
                                                    placeholder.markdown(full_response + "▌")
                                            
                            # Handle token events (final output)
                            elif data.get('event') == 'token':
                                token_data = data.get('data', '')
                                if token_data:
                                    full_response += token_data + "\n\n"
                                    placeholder.markdown(full_response + "▌")
                            
                            # Capture sources
                            if data.get('event') == 'usedTools':
                                for tool in data.get('data', []):
                                    if output := tool.get('toolOutput'):
                                        sources.add(output)

                        except json.JSONDecodeError:
                            continue

        # Add sources section if any
        if sources:
            full_response += "\n## 🔍 Data Sources\n"
            full_response += "\n".join(f"- {source}" for source in sources)

        # Final update
        placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

    except Exception as e:
        st.error(f"Error: {str(e)}")