# shop.py
from tkinter import Button, Frame, Label, messagebox

coins = 100
current_background = None

def shop_screen(app):
    clear_screen(app)
    global coins, current_background

    Label(app, text=f"Shop - Coins: {coins}", font=("Arial", 20)).pack(pady=10)

    # Background options
    backgrounds = ["Background 1", "Background 2", "Background 3"]
    prices = [50, 100, 150]

    for i, bg in enumerate(backgrounds):
        frame = Frame(app)
        frame.pack(pady=5)
        Label(frame, text=bg, font=("Arial", 16)).pack(side="left", padx=10)
        Button(frame, text=f"Buy ({prices[i]} Coins)", 
               command=lambda price=prices[i], bg=bg: buy_background(price, bg)).pack(side="left")

    Button(app, text="Back", command=lambda: home_screen(app)).pack(pady=20)

def buy_background(price, bg):
    global coins, current_background
    if coins >= price:
        coins -= price
        current_background = bg
        messagebox.showinfo("Shop", f"Purchased {bg}!")
    else:
        messagebox.showerror("Shop", "Not enough coins!")
