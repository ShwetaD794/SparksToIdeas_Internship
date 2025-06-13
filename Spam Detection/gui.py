import tkinter as tk
from tkinter import messagebox
import joblib

# Load trained model and vectorizer
model = joblib.load('spam_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Predict function
def predict():
    msg = entry.get("1.0", tk.END).strip()
    if not msg:
        messagebox.showwarning("Input Error", "Please enter a message.")
        return
    msg_vector = vectorizer.transform([msg])
    prediction = model.predict(msg_vector)
    result = "Spam ❌" if prediction[0] == 1 else "Not Spam ✅"
    result_label.config(
        text=f"Prediction: {result}",
        fg="#DC143C" if prediction[0] == 1 else "#228B22"
    )

# Exit fullscreen on Escape
def exit_fullscreen(event):
    root.attributes('-fullscreen', False)

# Hover effect for button
def on_enter(e):
    predict_btn.config(bg="#BDA0FF")

def on_leave(e):
    predict_btn.config(bg="#CBB4F2")

# Root window
root = tk.Tk()
root.title("📨 Spam Detector")
root.configure(bg="#F9F6FF")  # Very light pastel lavender (subtle tone)
root.attributes('-fullscreen', True)
root.bind("<Escape>", exit_fullscreen)

# Center card container
card = tk.Frame(root, bg="#FFFFFF", bd=0, padx=40, pady=40, relief="groove", highlightbackground="#EADCF8", highlightthickness=2)
card.place(relx=0.5, rely=0.5, anchor="center")

# Title
title = tk.Label(card, text="📩 Spam Message Detector", font=("Segoe UI", 26, "bold"), bg="#FFFFFF", fg="#5A3F9E")
title.pack(pady=(0, 30))

# Message entry box
entry = tk.Text(card, height=8, width=80, font=("Segoe UI", 14), bg="#FBFAFF", fg="#333", bd=0, relief="flat",
                highlightthickness=2, highlightbackground="#D5C8F3", wrap=tk.WORD)
entry.pack(pady=10)

# Predict Button
predict_btn = tk.Button(card, text="🔍 Check Spam", command=predict,
                        font=("Segoe UI", 14, "bold"), bg="#CBB4F2", fg="white",
                        activebackground="#BDA0FF", activeforeground="white",
                        relief="flat", padx=30, pady=12, cursor="hand2")
predict_btn.pack(pady=20)

# Hover effects
predict_btn.bind("<Enter>", on_enter)
predict_btn.bind("<Leave>", on_leave)

# Result label
result_label = tk.Label(card, text="", font=("Segoe UI", 18, "bold"), bg="#FFFFFF")
result_label.pack(pady=10)

# Run the application
root.mainloop()
