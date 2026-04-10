# 🤖 Agentic AI: Hybrid Multi-Agent Task Solving System

An intelligent AI-powered system that processes user queries using a **Hybrid Static–Dynamic Multi-Agent Architecture**.
The system integrates multiple APIs and LLMs to solve real-world tasks across domains like weather, jobs, and general queries.

---

## 📁 Project Structure

```
agenticai/
│
├── app.py                  # Main Streamlit application
├── agents/                 # Static & Dynamic agent implementations
├── utils/                  # Preprocessing & helper functions
├── models/                 # LLM and API integration
├── config/                 # Configuration files
└── requirements.txt        # Dependencies
```

---

## ⚙️ Prerequisites

Make sure the following are installed on your system:

| Requirement | Version | Download           |
| ----------- | ------- | ------------------ |
| Python      | 3.9+    | https://python.org |
| pip         | Latest  | Comes with Python  |

---

## 🚀 Step-by-Step Setup & Execution

### Step 1 — Clone the Project

```bash
git clone https://github.com/RekhaT2911/agenticai.git
cd agenticai
```

---

### Step 2 — Install Required Python Libraries

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit requests python-dotenv groq pandas
```

---

### Step 3 — Configure API Keys

Create a `.env` file in your project folder:

```
agenticai/
└── .env
```

Add the following:

```env
OPENWEATHER_API_KEY=your_openweather_key
RAPID_API_KEY=your_rapidapi_key
ADZUNA_APP_ID=your_adzuna_app_id
ADZUNA_APP_KEY=your_adzuna_app_key
GROQ_API_KEY=your_groq_api_key
```

> Replace all values with your actual API keys.

---

## 🔑 APIs Used

| API             | Purpose                       |
| --------------- | ----------------------------- |
| OpenWeather API | Fetch weather data            |
| RapidAPI        | Multi-domain API support      |
| Adzuna API      | Job search data               |
| Groq API        | LLM-based response generation |

---

### Step 4 — Run the Application

```bash
streamlit run app.py
```

The app will open automatically in your browser at:

```
http://localhost:8501
```

---

## 🧠 How the System Works

### Step-by-Step Flow

1. User enters a natural language query
2. Query is preprocessed (cleaning & normalization)
3. Intent classification determines the domain
4. System routes query:

   * Static Agent → predefined domains (weather, jobs, etc.)
   * Dynamic Agent → unknown or complex queries
5. Agent processes using APIs or LLM
6. Response is generated and displayed

---

## ✨ Features Overview

| Feature                   | Description                      |
| ------------------------- | -------------------------------- |
| Hybrid Multi-Agent System | Static + Dynamic agents          |
| Intelligent Routing       | Automatically selects best agent |
| API Integration           | Weather, jobs, and more          |
| LLM Support               | Handles complex queries          |
| Modular Design            | Easy to extend                   |
| Multi-domain Support      | Works across domains             |

---

## 🧩 Dependencies

```
streamlit
requests
python-dotenv
groq
pandas
```

---

## 🐞 Common Errors & Fixes

### API Key Not Working

→ Check `.env` file
→ Ensure no extra spaces

---

### ModuleNotFoundError

```bash
pip install <module-name>
```

---

### App Not Running

→ Ensure Streamlit is installed
→ Run:

```bash
streamlit run app.py
```

---

### No Response from APIs

→ Check internet connection
→ Verify API keys are valid

---

