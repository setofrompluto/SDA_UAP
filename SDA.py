import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import csv

class AplikasiTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Tkinter Sederhana")
        self.lebar = root.winfo_screenwidth()
        self.tinggi = root.winfo_screenheight()
        self.lebar_layar = 940
        self.tinggi_layar = 788
        pos_x = (self.lebar - self.lebar_layar) // 2
        pos_y = (self.tinggi - self.tinggi_layar) // 2
        self.root.geometry(f"{self.lebar_layar}x{self.tinggi_layar}+{pos_x}+{pos_y}")
        self.root.resizable(False, False)

        self.bg_image = Image.open("gi.png").resize((940, 788))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.flag_red = ImageTk.PhotoImage(Image.open("merah.jpg").resize((100, 60)))
        self.flag_blue = ImageTk.PhotoImage(Image.open("biru.jpg").resize((100, 60)))

        self.frame_awal = tk.Frame(root, width=400, height=400)
        self.frame_awal.pack(fill="both", expand=True)

        self.canvas_awal = tk.Canvas(self.frame_awal, width=940, height=788, highlightthickness=0)
        self.canvas_awal.pack(fill="both", expand=True)
        self.canvas_awal.create_image(0, 0, anchor="nw", image=self.bg_photo)

        self.canvas_awal.create_text(500, 200, text="Welcome To Our Project!",
                                     font=("Courier New", 30, "bold"), fill="white")

        self.btn_masuk = tk.Button(self.frame_awal, text="Click To Start",
                                   font=("Courier New", 19, "italic"),
                                   command=self.buka_halaman_perkenalan)
        self.canvas_awal.create_window(500, 500, window=self.btn_masuk)

        self.frame_perkenalan = tk.Frame(root, width=400, height=400)
        self.frame_utama = tk.Frame(root)

    def buka_halaman_perkenalan(self):
        self.frame_awal.pack_forget()
        self.frame_perkenalan.pack(fill="both", expand=True)

        self.canvas_perkenalan = tk.Canvas(self.frame_perkenalan, width=400, height=400, highlightthickness=0)
        self.canvas_perkenalan.pack(fill="both", expand=True)
        self.canvas_perkenalan.create_image(0, 0, anchor="nw", image=self.bg_photo)

        self.canvas_perkenalan.create_text(500, 150, text="Kelompok 13",
                                           font=("Helvetica", 25, "bold"), fill="white")
        anggota = [
            "1. Dimas Seto Aji - 2417051052",
            "2. Yusuf Alif Bahari - 2417051043",
            "3. Muhamad Arif - 2417051045",
            "4. Chayyarra Igda - 2417051001"
        ]

        for i, nama in enumerate(anggota):
            y_pos = 250 + i * 50
            self.canvas_perkenalan.create_text(500, y_pos, text=nama,
                                               font=("Courier New", 20, "bold"), fill="white")

        self.btn_lanjut = tk.Button(self.frame_perkenalan, text="Masuk ke Menu Utama",
                                    font=("Courier New", 20, "italic"),
                                    bg="white", fg="black", activebackground="gray20",
                                    activeforeground="white", borderwidth=0,
                                    command=self.buka_halaman_utama)
        self.canvas_perkenalan.create_window(500, 500, window=self.btn_lanjut)

    def buka_halaman_utama(self):
        self.frame_awal.pack_forget()
        self.frame_perkenalan.pack_forget()
        self.root.state("zoomed")
        self.tampilkan_halaman_utama()

    def tampilkan_halaman_utama(self):
        self.frame_kiri = tk.Frame(root, bg="red", width=350, height=400)
        self.frame_kiri.pack(side="left", fill="both", expand=True)

        # Bendera Merah
        self.label_flag_merah = tk.Label(self.frame_kiri, image=self.flag_red, bg="red")
        self.label_flag_merah.pack(pady=(20, 5))

        self.label_biru_skor = tk.Label(self.frame_kiri, text="0", font=("Arial", 80), bg="red", fg="white")
        self.label_biru_skor.pack(pady=(5, 20))

        # Tombol
        self.frame_btn_merah = tk.Frame(self.frame_kiri, bg="red")
        self.frame_btn_merah.pack(pady=10)
        self.btn_biru_tambah = tk.Button(self.frame_btn_merah, text="+1", font=("Arial", 24), command=self.tambah_skor_biru)
        self.btn_biru_tambah.pack(side="left", padx=5)
        self.btn_biru_kurang = tk.Button(self.frame_btn_merah, text="-1", font=("Arial", 24), command=self.kurang_skor_biru)
        self.btn_biru_kurang.pack(side="left", padx=5)

        self.frame_kanan = tk.Frame(root, bg="blue", width=350, height=400)
        self.frame_kanan.pack(side="right", fill="both", expand=True)

        # Bendera Biru
        self.label_flag_biru = tk.Label(self.frame_kanan, image=self.flag_blue, bg="blue")
        self.label_flag_biru.pack(pady=(20, 5))

        self.label_merah_skor = tk.Label(self.frame_kanan, text="0", font=("Arial", 80), bg="blue", fg="white")
        self.label_merah_skor.pack(pady=(5, 20))

        # Tombol
        self.frame_btn_biru = tk.Frame(self.frame_kanan, bg="blue")
        self.frame_btn_biru.pack(pady=10)
        self.btn_merah_tambah = tk.Button(self.frame_btn_biru, text="+1", font=("Arial", 24), command=self.tambah_skor_merah)
        self.btn_merah_tambah.pack(side="left", padx=5)
        self.btn_merah_kurang = tk.Button(self.frame_btn_biru, text="-1", font=("Arial", 24), command=self.kurang_skor_merah)
        self.btn_merah_kurang.pack(side="left", padx=5)

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

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiTkinter(root)
    root.mainloop()
