# main.py
from tkinter import Tk
from home_screen import home_screen

# Initialize the app
def main():
    app = Tk()
    app.title("Ultimate Game")
    app.geometry("800x600")
    app.resizable(False, False)
    home_screen(app)
    app.mainloop()

if __name__ == "__main__":
    main()
