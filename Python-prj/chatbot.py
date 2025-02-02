import openai
import sqlite3
import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import scrolledtext
import streamlit as st

# Set your OpenAI API key
OPENAI_API_KEY = "your-api-key-here"

# Initialize text-to-speech
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Voice recognition
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand."
        except sr.RequestError:
            return "API request error."

# Connect to database
def init_db():
    conn = sqlite3.connect("chatbot_memory.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            bot TEXT
        )
    """)
    conn.commit()
    return conn

def save_to_db(user_text, bot_response, conn):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chat_history (user, bot) VALUES (?, ?)", (user_text, bot_response))
    conn.commit()

def fetch_chat_history(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM chat_history")
    return cursor.fetchall()

def chat_with_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        api_key=OPENAI_API_KEY
    )
    return response["choices"][0]["message"]["content"].strip()

# GUI - Tkinter
class ChatbotGUI:
    def __init__(self, root, conn):
        self.root = root
        self.root.title("LLM Chatbot")

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
        self.text_area.grid(column=0, row=0, padx=10, pady=10)
        self.text_area.insert(tk.END, "Chat History:\n")

        self.entry = tk.Entry(root, width=50)
        self.entry.grid(column=0, row=1, padx=10, pady=10)
        self.entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.grid(column=0, row=2, padx=10, pady=10)

        self.voice_button = tk.Button(root, text="🎤 Speak", command=self.voice_input)
        self.voice_button.grid(column=0, row=3, padx=10, pady=10)

        self.conn = conn

    def send_message(self, event=None):
        user_text = self.entry.get()
        if user_text.strip():
            self.text_area.insert(tk.END, f"You: {user_text}\n")
            bot_response = chat_with_openai(user_text)
            self.text_area.insert(tk.END, f"Bot: {bot_response}\n")
            speak(bot_response)
            save_to_db(user_text, bot_response, self.conn)
        self.entry.delete(0, tk.END)

    def voice_input(self):
        user_text = recognize_speech()
        self.entry.insert(0, user_text)
        self.send_message()

# GUI - Streamlit
def chatbot_streamlit():
    st.title("LLM Chatbot")
    conn = init_db()
    chat_history = fetch_chat_history(conn)
    
    for chat in chat_history:
        st.text(f"You: {chat[1]}")
        st.text(f"Bot: {chat[2]}")

    user_text = st.text_input("Type your message:")
    if st.button("Send"):
        bot_response = chat_with_openai(user_text)
        save_to_db(user_text, bot_response, conn)
        st.text(f"Bot: {bot_response}")
        speak(bot_response)

# Run GUI
if __name__ == "__main__":
    conn = init_db()
    mode = input("Choose interface: 1 for Tkinter, 2 for Streamlit: ")
    
    if mode == "1":
        root = tk.Tk()
        app = ChatbotGUI(root, conn)
        root.mainloop()
    elif mode == "2":
        chatbot_streamlit()
