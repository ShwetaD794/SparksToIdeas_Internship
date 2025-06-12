import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkFont
import numpy as np
import joblib

# Load model and scaler
model = joblib.load('diabetes_model.pkl')
scaler = joblib.load('scaler.pkl')

# Prediction function
def predict_diabetes():
    try:
        input_data = [float(entry.get()) for entry in entries]
        input_array = np.array([input_data])
        input_scaled = scaler.transform(input_array)
        prediction = model.predict(input_scaled)
        result = "Diabetic ❌" if prediction[0] == 1 else "Non-Diabetic ✅"
        result_label.config(text=f"Prediction: {result}", fg="red" if prediction[0] == 1 else "green")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# GUI setup
root = tk.Tk()
root.title("💉 Diabetes Prediction App")
root.state("zoomed")
root.configure(bg="#F5F3FF")  # Soft lavender white

# Fonts
heading_font = tkFont.Font(family="Helvetica", size=28, weight="bold")
label_font = tkFont.Font(family="Helvetica", size=14)
entry_font = tkFont.Font(family="Helvetica", size=12)
button_font = tkFont.Font(family="Helvetica", size=14, weight="bold")
result_font = tkFont.Font(family="Helvetica", size=16, weight="bold")

# Labels for input
labels = [
    "Pregnancies", "Glucose", "Blood Pressure", "Skin Thickness",
    "Insulin", "BMI", "Diabetes Pedigree Function", "Age"
]

entries = []

# Main wrapper
wrapper = tk.Frame(root, bg="#FFFFFF", padx=50, pady=50, bd=2, relief="groove")
wrapper.place(relx=0.5, rely=0.5, anchor="center")

# Heading
heading = tk.Label(wrapper, text="🩺 Diabetes Prediction System", font=heading_font, bg="#FFFFFF", fg="#6A5ACD")
heading.grid(row=0, column=0, columnspan=2, pady=(0, 40))

# Input fields
for i, label_text in enumerate(labels):
    label = tk.Label(wrapper, text=label_text + ":", font=label_font, bg="#FFFFFF", anchor="w")
    label.grid(row=i+1, column=0, padx=(10, 20), pady=10, sticky="e")

    entry = tk.Entry(wrapper, font=entry_font, width=30, bg="#F8F8FF", relief="flat", highlightthickness=1, highlightcolor="#9370DB")
    entry.grid(row=i+1, column=1, padx=(0, 10), pady=10, sticky="w")
    entries.append(entry)

# Predict Button
predict_btn = tk.Button(
    wrapper,
    text="🔍 Predict",
    command=predict_diabetes,
    font=button_font,
    bg="#9370DB",
    fg="white",
    activebackground="#7B68EE",
    relief="flat",
    width=20,
    pady=10,
    cursor="hand2"
)
predict_btn.grid(row=len(labels)+1, column=0, columnspan=2, pady=30)

# Result Label
result_label = tk.Label(wrapper, text="", font=result_font, bg="#FFFFFF")
result_label.grid(row=len(labels)+2, column=0, columnspan=2, pady=10)

# Run GUI
root.mainloop()
