import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class AplikasiTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Tkinter Sederhana")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        
        self.frame_awal = tk.Frame(root, bg="white")
        self.frame_awal.pack(fill="both", expand=True)
        
        self.label_nama = tk.Label(self.frame_awal, text="Welcome To Our Projeck!",font=("Courier New", 20, "bold"), bg="white")
        self.label_nama.pack(pady=100)

        self.btn_masuk = tk.Button(self.frame_awal, text="Click To start", font=("Courier New", 14,"italic"), command=self.buka_halaman_utama)
        self.btn_masuk.pack()

        self.frame_utama = tk.Frame(root)
    
    def buka_halaman_utama(self):
        self.frame_awal.pack_forget()
        self.root.state("zoomed")
        self.tampilkan_halaman_utama()

    def tampilkan_halaman_utama(self):
        self.frame_kiri = tk.Frame(root, width=350, height=400)
        self.frame_kiri.pack(side="left", fill="both", expand=False)

        self.frame_kanan = tk.Frame(root, bg="white", width=350, height=400)
        self.frame_kanan.pack(side="right", fill="both", expand=True)
        
        self.label_judul = tk.Label(root, text="Testing How This Work", font=("Helvetica", 16))
        self.label_judul.pack(pady=10)
        
        self.tampilkan_gambar()

    def tampilkan_gambar(self):
        img = Image.open("test.png")
        img = img.resize((200, 200))
        self.photo = ImageTk.PhotoImage(img)
        self.label_gambar = tk.Label(self.root, image=self.photo)
        self.label_gambar.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiTkinter(root)
    root.mainloop()

    
