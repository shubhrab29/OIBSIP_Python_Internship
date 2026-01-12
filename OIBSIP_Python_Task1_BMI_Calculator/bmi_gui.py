#oasis infobyte python project
#bmi calculator

import tkinter as tk
from tkinter import messagebox

# Main window
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("360x350")
window.resizable(False, False)
window.configure(bg="mistyrose")

# Title
tk.Label(
    window,
    text="BMI Calculator",
    font=("Calibri", 18, "bold"),
    bg="#e8ebe9",
    fg="#0a7cee"
).pack(pady=15)

# Card Frame
card = tk.Frame(window, bg="white", bd=2, relief="flat")
card.pack(padx=20, pady=10, fill="both", expand=True)

# Weight
tk.Label(
    card,
    text="Weight (kg)",
    font=("Calibri", 11),
    bg="white"
).pack(pady=(15, 5))

weight_entry = tk.Entry(card, font=("Calibri", 11), justify="center")
weight_entry.pack(pady=5)

# Height
tk.Label(
    card,
    text="Height (m)",
    font=("Calibri", 11),
    bg="white"
).pack(pady=(15, 5))

height_entry = tk.Entry(card, font=("Calibri", 11), justify="center")
height_entry.pack(pady=5)

# BMI Calculation
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError

        bmi = weight / (height * height)

        if bmi < 18.5:
            category = "Underweight"
            tips = (
                "- Eat nutritious, calorie-rich foods.\n"
                "- Have regular, balanced meals.\n"
                "- Light exercises may help."
            )
        elif bmi < 24.9:
            category = "Normal weight"
            tips = (
                "- Maintain a balanced diet.\n"
                "- Stay physically active.\n"
                "- Get enough rest and hydration."
            )
        elif bmi < 29.9:
            category = "Overweight"
            tips = (
                "- Increase physical activity gradually.\n"
                "- Watch portion sizes.\n"
                "- Prefer whole foods."
            )
        else:
            category = "Obese"
            tips = (
                "- Make gradual lifestyle changes.\n"
                "- Gentle activity can help.\n"
                "- Consider professional guidance."
            )

        messagebox.showinfo(
            "BMI Result",
            f"Your BMI: {bmi:.2f}\n"
            f"Category: {category}\n\n"
            f"Health Tips:\n{tips}"
        )

    except:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid positive numbers."
        )

# Buttons Frame
btn_frame = tk.Frame(card, bg="white")
btn_frame.pack(pady=20)

tk.Button(
    btn_frame,
    text="Calculate BMI",
    width=15,
    bg="#4CAF50",
    fg="white",
    font=("Calibri", 10, "bold"),
    command=calculate_bmi
).grid(row=0, column=0, padx=5)

def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    weight_entry.focus()

tk.Button(
    btn_frame,
    text="Clear",
    width=15,
    bg="#e74c3c",
    fg="white",
    font=("Calibri", 10, "bold"),
    command=clear_fields
).grid(row=0, column=1, padx=5)

weight_entry.focus()

window.mainloop()
