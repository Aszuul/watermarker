import tkinter as tk
from PIL import Image

def main():
    window = tk.Tk()

    greeting = tk.Label(text="Hello, Tkinter")

    greeting.pack()
    
    window.mainloop()
    

if __name__ == "__main__":
    main()
    