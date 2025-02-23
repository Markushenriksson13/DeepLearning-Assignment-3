# DeepLearning-Assignment-3

# 📌 Multi-Agent AI Stock/ETF Analysis Tool 📉 📈  

Welcome to the **Multi-Agent AI Stock/ETF Analysis Tool**, an advanced AI-powered application that leverages multiple agents to analyze stocks and ETFs in real time. This tool provides insights using three key analysis methodologies:  

- **📊 Fundamental Analysis** – Evaluates financial health & valuation metrics  
- **📈 Technical Analysis** – Examines price patterns & trading signals  
- **🧠 Sentiment Analysis** – Analyzes market psychology & news trends  

## 🚀 Features  
- **Real-time stock & ETF insights** 🏦  
- **Multi-agent AI-driven analysis** 🤖  
- **Data scraping & internet search integration** 🌎  
- **Interactive chat-based interface** 💬  

---

## 📥 Installation  

### **1️⃣ Clone the Repository**  

git clone https://github.com/YOUR_GITHUB_USERNAME/multi-agent-stock-etf-analysis.git
cd multi-agent-stock-etf-analysis
2️⃣ Install Dependencies
Ensure you have Python installed, then install the required dependencies:


pip install -r requirements.txt
3️⃣ Start Flowise with Docker
Flowise is used as the backend for this intelligent stock analysis tool. To set it up:


docker run -d -p 3000:3000 --name flowise natbusa/flowise
This will start Flowise on http://localhost:3000.

4️⃣ Import Test Agents
Open Flowise
Navigate to Import
Select Test Agents.json from this repository
🎯 How to Use
Run the Streamlit app


streamlit run app4.py
Enter a stock/ETF symbol in the chat input
The AI agents will fetch the latest data from the internet
Get analysis based on fundamental, technical, and sentiment metrics
View data sources for credibility
🛠️ File Structure
bash
Kopiér
Rediger
📂 multi-agent-stock-etf-analysis
│── app4.py               # Streamlit application
│── requirements.txt       # Required dependencies
│── Test Agents.json       # Flowise agent configuration
│── README.md              # Documentation
📡 API Overview
The app interacts with Flowise AI via an API for real-time analysis. It:
✅ Sends stock/ETF queries to Flowise
✅ Processes responses from multi-agent AI
✅ Displays structured insights in a user-friendly format

API Endpoint:

POST http://localhost:3000/api/v1/prediction/eae195bf-677a-4b55-9e5b-17f63cfdf4a3
🔍 Example Query
💬 "Analyze TSLA stock performance"
🔹 📊 Fundamental Analysis – P/E ratio, revenue trends
🔹 📈 Technical Analysis – Moving averages, RSI, MACD
🔹 🧠 Sentiment Analysis – Latest news & market sentiment

📝 Notes
Ensure Docker is running before starting Flowise.
If needed, modify API_URL in app4.py to match your Flowise instance.
The app streams responses in real time for a smooth user experience.
🏆 Contributors
Created by [Your Name] – feel free to contribute via pull requests!

📜 License
MIT License.

Enjoy real-time, AI-powered stock analysis! 🚀
