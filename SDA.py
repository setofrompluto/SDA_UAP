import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class AplikasiTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Tkinter Sederhana")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.label_judul = tk.Label(root, text="Selamat Datang di Aplikasi Tkinter", font=("Helvetica", 16))
        self.label_judul.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiTkinter(root)
    root.mainloop()

    def tampilkan_gambar(self):
        img = Image.open("sehun.png")
        img = img.resize((200, 200))
        self.photo = ImageTk.PhotoImage(img)
        self.label_gambar = tk.Label(self.root, image=self.photo)
        self.label_gambar.pack(pady=10)
