# home_screen.py
from tkinter import Button, Label
from shop import shop_screen
from levels import levels_screen
from game_logic import start_game

def home_screen(app):
    clear_screen(app)
    Label(app, text="Welcome to the Ultimate Game", font=("Arial", 24)).pack(pady=20)
    Button(app, text="Start Game", command=lambda: start_game(app), width=20, height=2).pack(pady=10)
    Button(app, text="Shop", command=lambda: shop_screen(app), width=20, height=2).pack(pady=10)
    Button(app, text="Levels", command=lambda: levels_screen(app), width=20, height=2).pack(pady=10)
    Button(app, text="Exit", command=app.quit, width=20, height=2).pack(pady=10)

def clear_screen(app):
    for widget in app.winfo_children():
        widget.destroy()
