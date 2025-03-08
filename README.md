
# 🌍 AI Travel Planner 🛫

## 🚀 Overview
**AI Travel Planner** is a powerful **Streamlit-based web application** that leverages **Large Language Models (LLMs)**, APIs, and AI-driven itinerary generation to provide users with **personalized travel plans**. Users can input their trip details, budget, and preferences, and the AI generates an **optimized travel itinerary** while also offering **Google Calendar integration** and **email notifications**.

This project integrates **Groq Llama, SerpAPI, Airtable API**, and **email services** to automate and enhance the travel planning experience.

---

## 📌 Features
✔️ **AI-driven travel itinerary generation**  
✔️ **Groq Llama-powered destination research**  
✔️ **Real-time fetching of attraction and hotel links using SerpAPI**  
✔️ **Google Calendar event booking integration**  
✔️ **Airtable storage for user travel plans**  
✔️ **Email dispatch for trip itineraries with rich HTML formatting**  
✔️ **Interactive Q&A for travel-related queries**  
✔️ **Secure API handling using environment variables**  

---

## 💡 AI Concepts Utilized

### 🧠 Prompt Engineering Techniques
- **Single-shot prompting**: Used for generating **individual day-wise travel plans** based on input preferences.
- **Few-shot prompting**: Used for **fine-tuning recommendations**, ensuring high-quality itinerary suggestions based on examples.

### 🔄 Conversational & Chat AI
- **Context-aware responses** ensure accurate and relevant travel advice.

### 🌍 Chat Completion API Usage
- **LLM-based content generation** for travel itineraries.

---

## 🛠️ Tech Stack

| **Technology**  | **Purpose**  |
|---------------|-------------|
| **Python**  | Backend logic and AI processing  |
| **Streamlit**  | Frontend framework for interactive UI  |
| **Groq Llama**  | LLM used for AI-generated trip plans  |
| **SerpAPI**  | Fetches live travel details like hotels, restaurants, and attractions  |
| **Airtable API**  | Cloud-based storage for trip details  |
| **Email SMTP**  | Sends trip plans via email  |
| **Markdown & HTML**  | Renders structured itinerary emails  |
| **dotenv**  | Securely loads API keys from `.env`  |

---

### 📂 File Descriptions

- **`main.py`** - Handles the Streamlit UI and coordinates AI-powered travel planning logic.
- **`airtable_utils.py`** - Manages data storage and retrieval via the Airtable API.
- **`email_utils.py`** - Implements functionality for sending travel itineraries via email.
- **`calendar_utils.py`** - Integrates Google Calendar API for event scheduling.
- **`itinerary_generator.py`** - Uses AI to generate optimized travel itineraries based on user input.
- **`.env`** - Stores API credentials securely to avoid hardcoding sensitive data.
- **`requirements.txt`** - Lists all necessary dependencies for the project.
- **`README.md`** - Contains project documentation and usage instructions.

---

This structure ensures a **modular and scalable** approach, making it easy to maintain and expand the functionality of AI Travel Planner. 🚀


