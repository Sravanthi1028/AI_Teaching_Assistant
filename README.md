# AI Teaching Assistant 🎓

An AI-powered educational platform designed to support teachers and students by making learning more interactive, personalized, and efficient.

## 📌 Project Overview

The AI Teaching Assistant helps teachers prepare educational content and supports students through lesson assistance, reading support, and interactive quizzes. It uses Python, Streamlit, and AI services to provide a user-friendly learning experience.

## ✨ Features

- **📚 Educational Content:** Supports educational content and learning activities.
- **📝 Lesson Assistance:** Helps teachers prepare lesson materials and explanations.
- **📖 Reading Support:** Provides reading-related learning assistance.
- **🎮 Educational Games and Quizzes:** Makes learning interactive through quizzes and educational activities.
- **🤖 AI-Powered Assistance:** Integrates AI services to generate helpful responses and educational content.
- **🖥️ Interactive Interface:** Uses Streamlit to provide a simple, accessible web interface.

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API (if configured in the project)
- AI and Large Language Model (LLM) concepts
- Python libraries listed in `requirements.txt`

## 📂 Project Structure

```text
AI_Teaching_Assistant/
│
├── app.py
├── ai_services.py
├── requirements.txt
├── .gitignore
│
└── modules/
    ├── games.py
    ├── knowledge.py
    ├── lesson.py
    └── reading.py
```

## ⚙️ Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/Sravanthi1028/AI_Teaching_Assistant.git
cd AI_Teaching_Assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API keys

If the project uses the Google Gemini API, create a `.env` file locally and add your API key using the environment variable expected by your code.

**Never upload API keys, passwords, or your `.env` file to GitHub.**

### 4. Run the application

```bash
streamlit run app.py
```

The application should open in your browser if the dependencies and configuration are correct.

## 🎯 Project Objective

The objective of this project is to explore how AI can support teaching and learning by providing educational assistance, interactive activities, and AI-generated learning content.

## 🚀 Future Enhancements

- Personalized learning recommendations
- Student progress tracking
- More interactive quizzes and educational games
- Additional AI-powered teaching tools
- Improved feedback and learning assessments

## 👩‍💻 Author

**Sravanthi Doddipatla**

AI and Machine Learning Enthusiast | Python Developer

---

*This project is developed for educational purposes to explore AI-powered learning solutions.*
