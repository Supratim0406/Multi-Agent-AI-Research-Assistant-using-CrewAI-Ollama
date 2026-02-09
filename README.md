# 🔬 AI Research Assistant – Multi‑Agent System

An intelligent **multi‑agent research assistant** built using CrewAI, Streamlit, and local/cloud LLMs.

It automatically:
1. 🔍 Researches a topic
2. 📊 Analyzes findings
3. ✍️ Writes a professional report

All powered by specialized AI agents collaborating together.

---

## 🚀 Features

✅ Multi‑Agent architecture (Research → Analysis → Writing)  
✅ Works with Ollama (local & free) OR Groq/OpenAI (cloud)  
✅ Fully automated research pipeline  
✅ Structured markdown reports  
✅ Streamlit UI  
✅ Fast & lightweight (runs on laptop)  
✅ Modular agents + tasks  

---

## 🧠 Architecture
```
User Topic  
   ↓  
Research Agent → collects facts  
   ↓  
Analyst Agent → extracts insights  
   ↓  
Writer Agent → generates report  
   ↓  
Markdown files + Streamlit UI  

```

![alt text](image.png)


## 🧩 Tech Stack

- Python
- CrewAI
- Streamlit
- Ollama
- Groq / OpenAI (optional)
- Serper API

---

## 📁 Project Structure

```
ResearchAssistant/
│
├── agents/
│ ├── research_specialist.py
│ ├── data_analyst.py
│ └── content_writer.py
│
├── tasks/
│ ├── research_task.py
│ ├── analysis_task.py
│ └── writing_task.py
│
├── crew.py
├── app.py
├── .env
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1️⃣ Clone repo
```bash

git clone <your-repo-url>
cd ResearchAssistant

```

### 2️⃣ Create virtual environment
```bash

python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies
```bash

pip install -r requirements.txt
```

## 🤖 LLM Setup

### 🟢 Local (Recommended – FREE with Ollama)
```
Install Ollama:
https://ollama.com

Pull model:
ollama pull mistral

.env:
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434/v1
SERPER_API_KEY=your_key
CREWAI_TELEMETRY_DISABLED=true

Start server:
ollama serve
```

### 🟡 Groq
```
.env:
LLM_PROVIDER=groq
GROQ_API_KEY=your_key
SERPER_API_KEY=your_key
```

### 🔵 OpenAI
```
.env:
LLM_PROVIDER=openai
OPENAI_API_KEY=your_key
SERPER_API_KEY=your_key
```

## ▶️ Run App
```
streamlit run app.py

Open:
http://localhost:8501

```

## 📄 Output Files

```
- research_findings.md
- analysis_report.md
- final_report.md

```

## 🧠 Agents


🔍 Research Specialist – gathers info  
📊 Data Analyst – extracts insights  
✍️ Content Writer – writes final report  

---

## 🎥 Demo
[▶️ Watch Demo Video](https://github.com/user-attachments/assets/9d316a2b-c55b-43a4-8ec2-0d695ea0b03e)


## 💡 Use Cases

- Market research
- Trend analysis
- Academic summaries
- Business reports
- Competitive intelligence

---

## 🚀 Future Improvements

- Streaming responses
- PDF export
- RAG + vector DB
- Docker deployment
- Scheduled research

---

## 📜 License

MIT

---


Built with ❤️ using CrewAI + Streamlit

