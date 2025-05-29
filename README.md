# 🤖 AI Chat Bot (Auto Responder)

This project is an AI-powered auto-responder chat bot that simulates human-like replies using Google Gemini. It reads chat messages directly from the screen, identifies the sender, and automatically types a short, realistic response into the chat input.

---

## 💡 What It Does

- 🖱️ Monitors on-screen chat using `pyautogui` (no direct chat API required)
- 📋 Copies and reads new messages from the clipboard
- 🔍 Checks if the last message was sent by a specific user (e.g., "Jio Rk")
- 💬 Uses **Google Gemini** to analyze the chat and generate human-like replies
- ⌨️ Automatically pastes and sends the response back into the chat

---

## 🛠️ Technologies & Libraries Used

- Python 3
- `pyautogui` – to simulate mouse and keyboard actions
- `pyperclip` – to handle clipboard operations
- `time` – for timing delays
- `google.generativeai` – for AI-based reply generation
- Google Gemini (via API key)

---

## 📂 File Structure

ai_chat_bot/
├── ai_chat_bot.py
├── myApiKeys.py # Contains your Gemini API key
└── README.md