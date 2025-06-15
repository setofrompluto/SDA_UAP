import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import csv
import time 

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

        self.bg_image = Image.open("background.png").resize((940, 788))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.flag_red = ImageTk.PhotoImage(Image.open("merah.jpg").resize((200, 200)))
        self.flag_blue = ImageTk.PhotoImage(Image.open("biru.jpg").resize((200, 200)))

        self.frame_awal = tk.Frame(root, width=400, height=400)
        self.frame_awal.pack(fill="both", expand=True)

        self.canvas_awal = tk.Canvas(self.frame_awal, width=940, height=788, highlightthickness=0)
        self.canvas_awal.pack(fill="both", expand=True)
        self.canvas_awal.create_image(0, 0, anchor="nw", image=self.bg_photo)

        self.canvas_awal.create_text(470, 200, text="Welcome To Our Project!",
                                     font=("Courier New", 30, "bold"), fill="white")

        self.btn_masuk = tk.Button(self.frame_awal, text="Click To Start",
                                   font=("Courier New", 19, "italic"),
                                   command=self.buka_halaman_perkenalan)
        self.canvas_awal.create_window(470, 500, window=self.btn_masuk)

        self.frame_perkenalan = tk.Frame(root, width=940, height=788)
        self.frame_utama = tk.Frame(root)
        self.tim_data = []
        self.load_tim_data()
        self.skor_tim = {}
        self.load_skor_tim()

        
        

    def load_tim_data(self, filepath="tim_data.csv"):
        self.tim_dict = {} 
        try:
            with open(filepath, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.tim_dict[row['nama_tim']] = {
                        "warna": row['warna'],
                        "bendera": row['bendera']
                    }
        except FileNotFoundError:
            print("File CSV tidak ditemukan.")

    
    def load_skor_tim(self, filepath="skor.csv"):
        try:
            with open(filepath, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.skor_tim[row['nama_tim']] = int(row['skor'])
        except FileNotFoundError:
            print("File skor.csv tidak ditemukan. Inisialisasi skor ke 0.")
            for nama_tim in self.tim_dict:
                self.skor_tim[nama_tim] = 0

    def simpan_skor_tim(self, filepath="skor.csv"):
        with open(filepath, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['nama_tim', 'skor'])
            writer.writeheader()
            for tim, skor in self.skor_tim.items():
                writer.writerow({'nama_tim': tim, 'skor': skor})
                
    def reset_semua_skor(self):
        for tim in self.skor_tim:
            self.skor_tim[tim] = 0
        self.simpan_skor_tim()
        self.skor_biru = 0
        self.skor_merah = 0
        self.label_biru_skor.config(text="0")
        self.label_merah_skor.config(text="0")
        messagebox.showinfo("Reset", "Semua skor telah direset ke 0.")
        
    def buka_halaman_perkenalan(self):
        self.root.state("normal")
        self.root.geometry("940x788")
        self.frame_awal.pack_forget()
        self.frame_perkenalan = tk.Frame(root, width=940, height=788)
        self.frame_perkenalan.pack(fill="both", expand=True)

        self.canvas_perkenalan = tk.Canvas(self.frame_perkenalan, width=940, height=788, highlightthickness=0)
        self.canvas_perkenalan.pack(fill="both", expand=True)
        self.canvas_perkenalan.create_image(0, 0, anchor="nw", image=self.bg_photo)

        self.canvas_perkenalan.create_text(470, 130, text="Kelompok 13",
                                           font=("Helvetica", 25, "bold"), fill="white")
        foto_paths = ["seto.png", "yusuf.png", "arif.png", "chay.png"]
        nama_anggota = [
            "Dimas Seto Aji\n2417051052",
            "Yusuf Alif Bahari\n2417051043",
            "Muhamad Arif\n2417051045",
            "Chayyarra Igda\n2417051001"
        ]

        self.foto_anggota = []
        start_x = 110
        spacing = 230
        y_foto = 300
        y_nama = 400

        for i in range(4):
            try:
                img = Image.open(foto_paths[i]).resize((150, 150))
            except:
                img = Image.new("RGB", (100, 100), color="gray") 

            img_tk = ImageTk.PhotoImage(img)
            self.foto_anggota.append(img_tk)

            x_pos = start_x + i * spacing
            self.canvas_perkenalan.create_image(x_pos, y_foto, image=img_tk)
            self.canvas_perkenalan.create_text(x_pos, y_nama, text=nama_anggota[i],
                                               font=("Courier New", 14, "bold"), fill="white")

        
        self.btn_lanjut = tk.Button(self.frame_perkenalan, text="Masuk ke Menu Utama",
                                    font=("Courier New", 20, "italic"),
                                    bg="white", fg="black", activebackground="gray20",
                                    activeforeground="white", borderwidth=0,
                                    command=self.buka_halaman_utama)
        self.canvas_perkenalan.create_window(470, 550, window=self.btn_lanjut)
               
    def kembali_ke_halaman_perkenalan(self):
        self.frame_kiri.pack_forget()
        self.frame_kanan.pack_forget()
        self.frame_atas.pack_forget()
        self.frame_bawah.pack_forget()
        self.buka_halaman_perkenalan()

    def buka_halaman_utama(self):
        self.frame_awal.pack_forget()
        self.frame_perkenalan.pack_forget()
        self.tampilkan_halaman_utama()
    def toggle_zoom(self, event=None):
        if self.root.state() == "zoomed":
            self.root.state("normal") 
        else:
            self.root.state("zoomed") 
            
    def update_jam(self):
        waktu_sekarang = time.strftime("%H:%M")
        self.timer_label.config(text=waktu_sekarang)
        self.root.after(60000, self.update_jam)

    def update_tim_merah(self, event=None):
        nama_tim = self.pilihan_tim_merah.get()
        info = self.tim_dict[nama_tim]
        
        self.label_nama_merah.config(text=nama_tim)

        self.frame_kiri.config(bg=info["warna"])
        self.label_biru_skor.config(bg=info["warna"])
        self.frame_btn_merah.config(bg=info["warna"])
        self.label_flag_merah.config(bg=info["warna"])

        try:
            img = Image.open(info["bendera"]).resize((200, 200))
        except:
            img = Image.new("RGB", (200, 200), color="gray")

        self.flag_red = ImageTk.PhotoImage(img)
        self.label_flag_merah.config(image=self.flag_red)
        self.label_flag_merah.image = self.flag_red
       
    def update_tim_biru(self, event=None):
        nama_tim = self.pilihan_tim_biru.get()
        info = self.tim_dict[nama_tim]

        self.label_nama_biru.config(text=nama_tim)

        self.frame_kanan.config(bg=info["warna"])
        self.label_merah_skor.config(bg=info["warna"])
        self.frame_btn_biru.config(bg=info["warna"])
        self.label_flag_biru.config(bg=info["warna"])

        try:
            img = Image.open(info["bendera"]).resize((200, 200))
        except:
            img = Image.new("RGB", (200, 200), color="gray")

        self.flag_blue = ImageTk.PhotoImage(img)
        self.label_flag_biru.config(image=self.flag_blue)
        self.label_flag_biru.image = self.flag_blue 


    def tampilkan_halaman_utama(self):
        self.frame_atas = tk.Frame(self.root, height=50, bg="gray20")
        self.frame_atas.pack(side="top", fill="x")
        
        self.root.bind("<Escape>", self.toggle_zoom)
        
        self.frame_bawah = tk.Frame(self.root, height=50, bg="gray20")
        self.frame_bawah.pack(side="bottom", fill="x")
        self.btn_reset = tk.Button(self.frame_bawah, text="Reset Skor",
                           font=("Arial", 20),
                           command=self.reset_semua_skor,
                           bg="gray20", fg="white")
        self.btn_reset.pack(pady=10, padx=10, side="right")
        btn_export = tk.Button(
        self.frame_bawah,
        text="Export CSV",
        font=("Verdana", 14),
        bg="#007ACC",
        fg="white",
        activebackground="white",
        activeforeground="#007ACC",
        cursor="hand2",
        command=self.simpan_skor_tim)
        btn_export.pack(side="right", padx=10, pady=10)


        self.pilihan_tim_merah = tk.StringVar()
        self.dropdown_merah = ttk.Combobox(self.frame_atas, textvariable=self.pilihan_tim_merah, state="readonly")
        self.dropdown_merah['values'] = list(self.tim_dict.keys())
        self.dropdown_merah.current(0)
        self.dropdown_merah.pack(side="left", padx=10)
        self.dropdown_merah.bind("<<ComboboxSelected>>", self.update_tim_merah)
        
        self.label_nama_merah = tk.Label(self.frame_atas, text="Tim Merah", font=("Arial", 14), fg="white", bg="gray20")
        self.label_nama_merah.pack(side="left", padx=20)

        self.timer_label = tk.Label(
            self.frame_atas,
            text="00:00",
            font=("Arial", 28, "bold"),
            fg="white",
            bg="gray20",
            width=10,
            height=2,
            relief="ridge",
            bd=3
        )
        self.timer_label.place(relx=0.5, rely=0.5, anchor="center")
        self.update_jam()

        self.pilihan_tim_biru = tk.StringVar()
        self.dropdown_biru = ttk.Combobox(self.frame_atas, textvariable=self.pilihan_tim_biru, state="readonly")
        self.dropdown_biru['values'] = list(self.tim_dict.keys())
        self.dropdown_biru.current(0)
        self.dropdown_biru.pack(side="right", padx=10)
        self.dropdown_biru.bind("<<ComboboxSelected>>", self.update_tim_biru)
        
        self.label_nama_biru = tk.Label(self.frame_atas, text="Tim Biru", font=("Arial", 14), fg="white", bg="gray20")
        self.label_nama_biru.pack(side="right", padx=20)

        self.frame_kiri = tk.Frame(self.root, bg="red", width=350, height=400)
        self.frame_kiri.pack(side="left", fill="both", expand=True)

        self.label_flag_merah = tk.Label(self.frame_kiri, image=self.flag_red, bg="red")
        self.label_flag_merah.pack(pady=(20, 5))

        self.label_biru_skor = tk.Label(self.frame_kiri, text="0", font=("DS-Digital", 160), bg="red", fg="white")
        self.label_biru_skor.pack(pady=(5, 20))

        self.frame_btn_merah = tk.Frame(self.frame_kiri, bg="red")
        self.frame_btn_merah.pack(pady=10)
        self.btn_biru_tambah = tk.Button(self.frame_btn_merah, text="+1", font=("Arial", 24), command=self.tambah_skor_biru)
        self.btn_biru_tambah.pack(side="left", padx=5)
        self.btn_biru_kurang = tk.Button(self.frame_btn_merah, text="-1", font=("Arial", 24), command=self.kurang_skor_biru)
        self.btn_biru_kurang.pack(side="left", padx=5)

        self.frame_kanan = tk.Frame(self.root, bg="blue", width=350, height=400)
        self.frame_kanan.pack(side="right", fill="both", expand=True)

        self.label_flag_biru = tk.Label(self.frame_kanan, image=self.flag_blue, bg="blue")
        self.label_flag_biru.pack(pady=(20, 5))

        self.label_merah_skor = tk.Label(self.frame_kanan, text="0", font=("DS-Digital", 160), bg="blue", fg="white")
        self.label_merah_skor.pack(pady=(5, 20))

        self.frame_btn_biru = tk.Frame(self.frame_kanan, bg="blue")
        self.frame_btn_biru.pack(pady=10)
        self.btn_merah_tambah = tk.Button(self.frame_btn_biru, text="+1", font=("Arial", 24), command=self.tambah_skor_merah)
        self.btn_merah_tambah.pack(side="left", padx=5)
        self.btn_merah_kurang = tk.Button(self.frame_btn_biru, text="-1", font=("Arial", 24), command=self.kurang_skor_merah)
        self.btn_merah_kurang.pack(side="left", padx=5)
               
        self.btn_kembali_perkenalan = tk.Button(self.frame_bawah, text="Kembali", 
                                                font=("Arial", 20), 
                                                command=self.kembali_ke_halaman_perkenalan,
                                                bg="gray20",
                                                fg="white")
        self.btn_kembali_perkenalan.pack(pady=10,padx=10 ,side="left")
        
        self.skor_biru = 0
        self.skor_merah = 0
        self.update_tim_merah()
        self.update_tim_biru()

    def tambah_skor_biru(self):
        self.skor_biru += 1
        self.label_biru_skor.config(text=str(self.skor_biru))
        self.skor_tim[self.pilihan_tim_merah.get()] = self.skor_biru
        self.simpan_skor_tim()

    def kurang_skor_biru(self):
        self.skor_biru = max(0, self.skor_biru - 1)
        self.label_biru_skor.config(text=str(self.skor_biru))
        self.skor_tim[self.pilihan_tim_merah.get()] = self.skor_biru
        self.simpan_skor_tim()

    def tambah_skor_merah(self):
        self.skor_merah += 1
        self.label_merah_skor.config(text=str(self.skor_merah))
        self.skor_tim[self.pilihan_tim_biru.get()] = self.skor_merah
        self.simpan_skor_tim()

    def kurang_skor_merah(self):
        self.skor_merah = max(0, self.skor_merah - 1)
        self.label_merah_skor.config(text=str(self.skor_merah))
        self.skor_tim[self.pilihan_tim_biru.get()] = self.skor_merah
        self.simpan_skor_tim()

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiTkinter(root)
    root.mainloop()
