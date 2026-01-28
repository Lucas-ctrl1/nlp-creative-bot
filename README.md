# 🎨 The Creative Muse Chatbot

**A Multi-Modal AI Brainstorming Partner**

The **Creative Muse** is an advanced, local AI application designed to overcome creative blocks. Unlike standard chatbots, this "Avant-Garde Muse" accepts **Text**, **Images**, and **Voice Recordings** to generate wild plot twists, detailed visual prompts for Midjourney/DALL-E, and atmospheric soundscapes.

Built with **Streamlit**, **Ollama**, and **Faster-Whisper**.

---

## 🌟 Features

* **🗣️ Multi-Modal Input:**
    * **Text:** Enter keywords or themes.
    * **Visuals:** Upload sketches or mood boards (analyzed by LLaVA).
    * **Audio:** Record your voice ideas (transcribed by Whisper).
* **🧠 Local AI Intelligence:**
    * Uses **Mistral** for creative logic and "Avant-Garde" persona.
    * Uses **LLaVA** for image understanding.
    * Uses **Whisper (Tiny)** for fast, local speech-to-text.
* **🔥 Provocative Mode:** The bot doesn't just agree with you; it challenges you with constraints to push your creativity.
* **💾 Export Ready:** Download your generated creative briefs directly as Markdown files.

---

## 🛠️ Prerequisites

Before running the app, ensure you have the following installed:

1.  **Python 3.8+**
2.  **Ollama** (Required for the AI models)
    * Download from [ollama.com](https://ollama.com/)
    * Once installed, run these commands in your terminal to download the necessary brains:
        ```bash
        ollama pull mistral
        ollama pull llava
        ```

---

## 🚀 Installation (Conda Method)

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/Lucas-ctrl1/nlp-creative-bot.git](https://github.com/Lucas-ctrl1/nlp-creative-bot.git)
    cd nlp-creative-bot
    ```

2.  **Create and Activate Conda Environment**
    ```bash
    # Create a new environment named 'creative-muse' with Python 3.10
    conda create -n creative-muse python=3.10 -y

    # Activate the environment
    conda activate creative-muse
    ```

3.  **Install Dependencies**
    ```bash
    # We use pip inside conda to ensure all specific libraries install correctly
    pip install -r requirements.txt
    ```


---

## ▶️ How to Run

# 1.  Make sure **Ollama** is running in the background.
# 2.  Run the Streamlit app:
    ```bash
    streamlit run run_chatbot.py
    ```
# 3.  The app will open in your browser at `http://localhost:8501`.

---

## 📂 Project Structure
```
nlp-creative-bot/
├── README.md              # Project documentation and setup guide
├── requirements.txt       # List of dependencies (streamlit, ollama, etc.)
├── chatbot_base.py        # Parent class (Blueprint for all bots)
├── creative_bot.py        # Logic file (Inherits from Base, handles AI models)
└── run_chatbot.py         # Main file (Streamlit User Interface)
```
## File Breakdown
run_chatbot.py: The entry point. Run this file to start the app.
creative_bot.py: The brain. Contains the CreativeChatbot class and AI logic.
chatbot_base.py: The skeleton. Contains the ChatbotBase class.
requirements.txt: The toolkit. Defines what libraries to install.

---

## 🧩 Usage Guide

1.  **Upload Context:**
    * Drag and drop an image that inspires you.
    * Upload a voice note describing a fleeting thought.
    * Type a few keywords (e.g., "Cyberpunk, Jazz, Rain").
2.  **Generate:** Click "Generate Creative Output".
3.  **Review:** The AI will analyze your inputs and provide:
    * A twisted Plot Summary.
    * A high-fidelity Image Prompt.
    * An Audio Cue description.
4.  **Challenge:** Click **"🔥 Challenge Me"** to receive a creative constraint to rewrite your idea.

---

## 📜 License

This project is created for educational purposes as part of the NLP Creative AI module.


