# game_logic.py
from tkinter import Button, Entry, Label, messagebox
from levels import levels_status

coins = 100

def start_game(app):
    start_level(app, 1)  # Start with level 1

def start_level(app, level):
    clear_screen(app)
    Label(app, text=f"Level {level}", font=("Arial", 24)).pack(pady=20)

    question = f"Solve the problem for level {level}: What is {level} + 2?"
    correct_answer = str(level + 2)
    
    Label(app, text=question, font=("Arial", 16)).pack(pady=10)
    answer = Entry(app)
    answer.pack(pady=10)
    
    Button(app, text="Submit", 
           command=lambda: submit_answer(app, level, answer.get(), correct_answer)).pack(pady=10)
    Button(app, text="Back", command=lambda: levels_screen(app)).pack(pady=10)

def submit_answer(app, level, user_answer, correct_answer):
    global coins
    if user_answer == correct_answer:
        levels_status[level - 1] = True
        coins += 10
        messagebox.showinfo("Level Complete", f"Level {level} completed! +10 coins.")
        levels_screen(app)
    else:
        messagebox.showerror("Incorrect", "Try again!")

def clear_screen(app):
    for widget in app.winfo_children():
        widget.destroy()
