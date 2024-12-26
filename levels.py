# levels.py
from tkinter import Button, Frame, Label
from game_logic import start_level

levels_status = [False] * 100  # False = Incomplete, True = Complete

def levels_screen(app):
    clear_screen(app)
    Label(app, text="Levels", font=("Arial", 20)).pack(pady=10)
    frame = Frame(app)
    frame.pack()

    for i in range(10):  # 10 rows
        for j in range(10):  # 10 columns
            level_num = i * 10 + j + 1
            status = "✓" if levels_status[level_num - 1] else "✗"
            color = "green" if levels_status[level_num - 1] else "red"
            Button(frame, text=f"{level_num}\n{status}", bg=color, 
                   command=lambda lvl=level_num: start_level(app, lvl), width=5, height=2).grid(row=i, column=j, padx=5, pady=5)

    Button(app, text="Back", command=lambda: home_screen(app)).pack(pady=20)
