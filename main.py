import tkinter as tk
from tkinter import messagebox
import re

def assess_password_strength(password):
    length_score = min(5, len(password) // 4)
    upper_score = 1 if re.search(r"[A-Z]", password) else 0
    lower_score = 1 if re.search(r"[a-z]", password) else 0
    digit_score = 1 if re.search(r"\d", password) else 0
    special_score = 1 if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) else 0

    total_possible_score = 5 + 1 + 1 + 1 + 1  
    total_score = length_score + upper_score + lower_score + digit_score + special_score

    strength_percentage = (total_score / total_possible_score) * 100

    if total_score < 4:
        strength = "Weak"
    elif total_score < 7:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, strength_percentage

def check_password_strength():
    password = entry_password.get()
    strength, strength_percentage = assess_password_strength(password)
    messagebox.showinfo("Password Strength", f"Strength: {strength} ({strength_percentage:.2f}%)")

# Create the main window
window = tk.Tk()
window.title("Password Strength Assessment")
window.geometry("300x150")

# Create input field for password
label_password = tk.Label(window, text="Enter your password:")
label_password.pack(pady=(20, 5))
entry_password = tk.Entry(window, show="")
entry_password.pack(pady=5)

# Create button to check password strength
button_check = tk.Button(window, text="Check Strength", command=check_password_strength)
button_check.pack(pady=10)

# Start the GUI event loop
window.mainloop()
