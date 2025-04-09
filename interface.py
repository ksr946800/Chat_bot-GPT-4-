# app.py
import tkinter as tk
from tkinter import scrolledtext
from bot import chat_bot1

# --- UI Theme ---
BG_COLOR = "#FFF3C7"
BOT_COLOR = "#D9F3FF"
USER_COLOR = "#E1FFDA"
FONT = ("Comic Sans MS", 12)
BOT_TAG = "bot"
USER_TAG = "user"

# --- App setup ---
root = tk.Tk()
root.title("Chatty Bot 🎈")
root.geometry("640x700")
root.config(bg=BG_COLOR)

# --- Title ---
title = tk.Label(root, text="🧠 Welcome to Chatty Bot!", font=("Comic Sans MS", 18, "bold"),
                 bg=BG_COLOR, fg="#333")
title.pack(pady=(10, 5))

# --- Chat Display ---
chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=FONT,
                                     bg="white", width=70, height=25, state='disabled')
chat_log.tag_config(USER_TAG, background=USER_COLOR)
chat_log.tag_config(BOT_TAG, background=BOT_COLOR)
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# --- Message Frame (for entry + button) ---
message_frame = tk.Frame(root, bg=BG_COLOR)
message_frame.pack(padx=10, pady=(0, 15), fill=tk.X)

entry = tk.Entry(message_frame, font=FONT)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
entry.focus()

# --- Functions ---

def send_message():
    user_input = entry.get()
    if not user_input.strip():
        return

    chat_log.config(state='normal')
    chat_log.insert(tk.END, f"You: {user_input}\n", USER_TAG)
    chat_log.insert(tk.END, "🤖 Bot is thinking...\n", BOT_TAG)
    chat_log.see(tk.END)

    entry.delete(0, tk.END)
    root.after(100, lambda: get_response(user_input))

def get_response(user_input):
    response = chat_bot1(user_input)
    chat_log.config(state='normal')
    chat_log.delete("end-2l", "end-1l")  # remove 'thinking...'
    chat_log.insert(tk.END, f"🤖 Bot: {response}\n\n", BOT_TAG)
    chat_log.config(state='disabled')
    chat_log.see(tk.END)

send_btn = tk.Button(message_frame, text="✨ Send", command=send_message,
                     font=FONT, bg="#FFD966", activebackground="#FFEB99")
send_btn.pack(side=tk.RIGHT)

# Bind Enter key
entry.bind("<Return>", lambda event: send_message())

# --- Start the app ---
root.mainloop()