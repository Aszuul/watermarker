import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import filedialog
import os

IMG_WIDTH = 750

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("850x500+500+150")
        self.resizable(width=True, height=True)
        self.title("Watermarker")

        self.btn = tk.Button(self, text='open image', command=self.open_img).pack()
        self.btn = tk.Button(self, text='add watermark', command=self.add_watermark).pack()
        self.image_label = tk.Label(self, name='image', text='open a file to add watermark.')
        self.image_label.pack()
        self.btn = tk.Button(self, text='save image', command=self.save_img).pack()

    def open_img(self):
        self.filename = openfn()
        self.img = Image.open(self.filename).convert('RGBA')
        width_ratio = IMG_WIDTH / self.img.width
        self.img = self.img.resize((IMG_WIDTH, round(self.img.height * width_ratio)), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(self.img, master=self)
        self.image_label = tk.Label(self, image=img_tk, name='image')
        self.image_label.image = img_tk
        self.image_label.pack()
    
    def add_watermark(self):
        width, height = self.img.size
        txt = Image.new('RGBA', self.img.size, (255,255,255,0))
        fnt = ImageFont.truetype('arial.ttf', 30)
        d = ImageDraw.Draw(txt)
        x = width/3
        y = height/3
        d.text((x,y), "Scott Abernathy", font=fnt, fill=(255,255,255,128))
        txt = txt.rotate(45)

        new_img = Image.alpha_composite(self.img, txt)
        new_img_tk = ImageTk.PhotoImage(new_img)
        self.image_label.configure(image=new_img_tk)
        self.image_label.image = new_img_tk
        self.image_label.pack()

    def save_img(self):
        filepath, filename = os.path.split(self.filename)
        new_filename = filepath + "\wm_" + filename
        self.img = self.img.convert('RGB')
        self.img.save(new_filename)

def openfn():
    filename = tk.filedialog.askopenfilename(title='open')
    return filename

if __name__ == "__main__":
    app = App()
    app.mainloop()

    # Reese & Nolan