# ✈️ Multi-Agent AI Travel Planning System using LangGraph

A production-ready **Multi-Agent AI Travel Planning System** built with **LangGraph, Groq Llama 3.3 70B, PostgreSQL Memory, Tavily Search, AviationStack API, and Streamlit**.

The system simulates how multiple AI agents collaborate to automatically generate complete travel plans, including flights, hotels, and itineraries.

---

## 🚀 Features

* ✈️ Flight Search Agent
* 🏨 Hotel Search Agent
* 🗓️ Itinerary Planning Agent
* 🤖 Final Response Agent
* 🧠 Persistent Memory using PostgreSQL
* 🌐 Real-Time API Integration
* 🔄 LangGraph Multi-Agent Workflow
* 💻 Professional Streamlit Interface
* 📂 Auto Save Travel Plans
* 📥 Download Generated Plans

---

## 🏗️ Architecture

```text
User Request
      │
      ▼
Flight Agent
      │
      ▼
Hotel Agent
      │
      ▼
Itinerary Agent
      │
      ▼
Final Agent
      │
      ▼
Final Travel Plan
      │
      ▼
PostgreSQL Memory
```

---

## 🛠️ Tech Stack

### Frameworks

* LangGraph
* LangChain
* Streamlit

### LLM

* Groq
* Llama 3.3 70B

### Database

* PostgreSQL

### APIs

* Tavily Search API
* AviationStack API

### Libraries

* Python
* Requests
* Psycopg
* Python Dotenv

---

# 📁 Project Structure

```text
Multi_Agent_System/
│
├── frontend.py
├── main.py
├── .env
│
├── tools/
│   ├── flight_tool.py
│   └── tavily_tool.py
│
├── travel_plans/
│
└── requirements.txt
```

---

# ⚙️ Setup Instructions

## Step 1: Create Virtual Environment

```bash
python -m venv langgraph_env3
```

Activate the environment:

### Windows

```bash
langgraph_env3\Scripts\activate
```

---

## Step 2: Install Dependencies

```bash
pip install langgraph langchain langchain-openai langchain-groq langchain-community langchain-tavily psycopg[binary] psycopg_pool python-dotenv tavily-python requests streamlit
```

Install PostgreSQL checkpoint support:

```bash
pip install -U "psycopg[binary,pool]" langgraph-checkpoint-postgres
```

---

## Step 3: Install PostgreSQL

Download PostgreSQL:

https://www.postgresql.org/download/

While installing PostgreSQL, remember:

* Database password
* Port number

These will be required for the database connection string.

---

## Step 4: Create Database

Open PostgreSQL and execute:

```sql
CREATE DATABASE langgraph_memory_demo;
```

---

## Step 5: Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key

TAVILY_API_KEY=your_tavily_api_key

AVIATIONSTACK_API_KEY=your_aviationstack_api_key

DATABASE_URL=postgresql://postgres:password@localhost:5432/langgraph_memory_demo
```

---

# 🔑 API Keys

### Groq

https://console.groq.com

### Tavily

https://tavily.com

### AviationStack

https://aviationstack.com

---

# ▶️ Run the Application

## Run the Multi-Agent System

```bash
python main.py
```

This runs the system inside the terminal.

---

## Launch Streamlit UI

```bash
streamlit run frontend.py
```

---

# 💡 Example Prompt

```text
Plan a complete 7-day trip to Japan, including flights, hotels, and sightseeing, for under ₹2 Lakhs.
```

---

# 🔄 Workflow

### 1. Flight Agent

Searches flight information using AviationStack API.

### 2. Hotel Agent

Searches hotel recommendations using Tavily.

### 3. Itinerary Agent

Creates a detailed travel itinerary using Llama 3.3 70B.

### 4. Final Agent

Combines all outputs into a final response.

### 5. PostgreSQL Memory

Stores conversations and maintains context across sessions.

---

---
---

# Future Improvements

* 🌍 Weather Agent
* 💰 Budget Optimization Agent
* 🍽️ Restaurant Recommendation Agent
* 🎟️ Activity Planner Agent
* 🗺️ Google Maps Integration
* 🛫 Real Flight Booking APIs
* PDF Export Support

---

# Author

**Amit Yadav**

GitHub: https://github.com/amityadav108

---

## ⭐ If you found this project useful, consider giving it a star.
