import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import csv

class AplikasiTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Tkinter Sederhana")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        self.bg_image = Image.open("background.png").resize((400, 400))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        self.frame_awal = tk.Frame(root, width=800, height=600)
        self.frame_awal.pack(fill="both", expand=True)
        
        self.canvas_awal = tk.Canvas(self.frame_awal, width=400, height=400, highlightthickness=0)
        self.canvas_awal.pack(fill="both", expand=True)
        self.canvas_awal.create_image(0, 0, anchor="nw", image=self.bg_photo)

        self.canvas_awal.create_text(200, 100, text="Welcome To Our Projeck!",
                                     font=("Courier New", 20, "bold"), fill="white")

        self.btn_masuk = tk.Button(self.frame_awal, text="Click To Start",
                                   font=("Courier New", 14, "italic"),
                                   command=self.buka_halaman_perkenalan)
        self.canvas_awal.create_window(200, 200, window=self.btn_masuk)

        self.frame_perkenalan = tk.Frame(root, width=400, height=400)
        self.frame_utama = tk.Frame(root)

    def buka_halaman_perkenalan(self):
        self.frame_awal.pack_forget()
        self.frame_perkenalan.pack(fill="both", expand=True)

        self.canvas_perkenalan = tk.Canvas(self.frame_perkenalan, width=400, height=400, highlightthickness=0)
        self.canvas_perkenalan.pack(fill="both", expand=True)
        self.canvas_perkenalan.create_image(0, 0, anchor="nw", image=self.bg_photo)

        self.canvas_perkenalan.create_text(200, 60, text="Kelompok 13",
                                           font=("Helvetica", 16, "bold"), fill="white")
        anggota = [
            "1. Dimas Seto Aji - 2417051052",
            "2. Yusuf Alif Bahari - 2417051043",
            "3. Muhamad Arif - 2417051045",
            "4. Chayyarra Igda - 2417051001"
        ]

        for i, nama in enumerate(anggota):
            y_pos = 100 + i * 30
            self.canvas_perkenalan.create_text(200, y_pos, text=nama,
                                               font=("Courier New", 13, "bold"), fill="white")

        self.btn_lanjut = tk.Button(self.frame_perkenalan, text="Masuk ke Menu Utama",
                                    font=("Courier New", 14, "italic"),
                                    bg="white", fg="black", activebackground="gray20",
                                    activeforeground="white", borderwidth=0,
                                    command=self.buka_halaman_utama)
        self.canvas_perkenalan.create_window(200, 280, window=self.btn_lanjut)

    
    def buka_halaman_utama(self):
        self.frame_awal.pack_forget()
        self.frame_perkenalan.pack_forget()
        self.root.state("zoomed")
        self.tampilkan_halaman_utama()

    def tampilkan_halaman_utama(self):
        self.frame_kiri = tk.Frame(root, bg="red",width=350, height=400)
        self.frame_kiri.pack(side="left", fill="both", expand=True)

        self.label_biru_skor = tk.Label(self.frame_kiri, text="0", font=("Arial", 80), bg="red", fg="white")
        self.label_biru_skor.pack(pady=20)
        
        self.btn_biru_tambah = tk.Button(self.frame_kiri, text="+1", font=("Arial", 24), command=self.tambah_skor_biru)
        self.btn_biru_tambah.pack(pady=10)
        
        self.btn_biru_kurang = tk.Button(self.frame_kiri, text="-1", font=("Arial", 24), command=self.kurang_skor_biru)
        self.btn_biru_kurang.pack(pady=10)

        self.frame_kanan = tk.Frame(root, bg="blue", width=350, height=400)
        self.frame_kanan.pack(side="right", fill="both", expand=True)
    
        self.label_merah_skor = tk.Label(self.frame_kanan, text="0", font=("Arial", 80), bg="blue", fg="white")
        self.label_merah_skor.pack(pady=20)
        
        self.btn_merah_tambah = tk.Button(self.frame_kanan, text="+1", font=("Arial", 24), command=self.tambah_skor_merah)
        self.btn_merah_tambah.pack(pady=10)
        
        self.btn_merah_kurang = tk.Button(self.frame_kanan, text="-1", font=("Arial", 24), command=self.kurang_skor_merah)
        self.btn_merah_kurang.pack(pady=10)
        
        self.skor_biru = 0
        self.skor_merah = 0
        
    def tambah_skor_biru(self):
        self.skor_biru += 1
        self.label_biru_skor.config(text=str(self.skor_biru))

    def kurang_skor_biru(self):
        self.skor_biru = max(0, self.skor_biru - 1)
        self.label_biru_skor.config(text=str(self.skor_biru))

    def tambah_skor_merah(self):
        self.skor_merah += 1
        self.label_merah_skor.config(text=str(self.skor_merah))

    def kurang_skor_merah(self):
        self.skor_merah = max(0, self.skor_merah - 1)
        self.label_merah_skor.config(text=str(self.skor_merah))
    
    def buka_halaman_kedua(self):
        self.frame_kiri.pack_forget()
        self.frame_kanan.pack_forget()
        self.tampilkan_halaman_kedua()
    
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
