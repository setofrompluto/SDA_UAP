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

        self.bg_image = Image.open("background.png").resize((800, 600))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        self.frame_awal = tk.Frame(root, width=800, height=600)
        self.frame_awal.pack(fill="both", expand=True)
        
        self.bg_label_awal = tk.Label(self.frame_awal, image=self.bg_photo)
        self.bg_label_awal.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.label_nama = tk.Label(self.frame_awal, text="Welcome To Our Projeck!",font=("Courier New", 20, "bold"), bg="white")
        self.label_nama.pack(pady=100)

        self.btn_masuk = tk.Button(self.frame_awal, text="Click To start", font=("Courier New", 14,"italic"), command=self.buka_halaman_perkenalan)
        self.btn_masuk.pack()

        self.frame_perkenalan = tk.Frame(root, width=800, height=600)
        self.frame_utama = tk.Frame(root)

    def buka_halaman_perkenalan(self):
        self.frame_awal.pack_forget()
        self.frame_perkenalan.pack(fill="both", expand=True)

        self.bg_label_perkenalan = tk.Label(self.frame_perkenalan, image=self.bg_photo)
        self.bg_label_perkenalan.place(x=0, y=0, relwidth=1, relheight=1)

        label_judul = tk.Label(self.frame_perkenalan, text="Kelompok 13 ",
                               font=("Helvetica", 16, "bold"), fg="black")
        label_judul.place(relx=0.5, rely=0.15, anchor="center")

        anggota = ["1. Dimas Seto Aji - 2417051052", "2. Yusuf Alif Bahari - 2417051043", "3. Muhamad Arif - 2417051045", "4. Chayyarra Igda - 2417051001"]
        for i, nama in enumerate(anggota):
            label = tk.Label(self.frame_perkenalan, text=nama, font=("Courier New", 14), fg="black")
            label.place(relx=0.5, rely=0.25 + i * 0.07, anchor="center")

        btn_lanjut = tk.Button(self.frame_perkenalan, text="Masuk ke Menu Utama", font=("Courier New", 14, "italic"),
                               bg="black", fg="white", activebackground="gray20",
                               activeforeground="white", borderwidth=0,
                               command=self.buka_halaman_utama)
        btn_lanjut.place(relx=0.5, rely=0.75, anchor="center")

    
    def buka_halaman_utama(self):
        self.frame_awal.pack_forget()
        self.frame_perkenalan.pack_forget()
        self.root.state("zoomed")
        self.tampilkan_halaman_utama()

    def tampilkan_halaman_utama(self):
        self.frame_kiri = tk.Frame(root, width=350, height=400)
        self.frame_kiri.pack(side="left", fill="both", expand=False)

        self.frame_kanan = tk.Frame(root, bg="white", width=350, height=400)
        self.frame_kanan.pack(side="right", fill="both", expand=True)
        
        self.label_judul = tk.Label(root, text="Testing How This Work", font=("Helvetica", 16))
        self.label_judul.pack(pady=10)

        self.tombol_ke_hal_kedua = tk.Button(self.frame_kiri, text = "Ke halaman selanjutnya", font = ("Courier New", 14,"italic"), command = self.buka_halaman_kedua)
        self.tombol_ke_hal_kedua.pack(pady = 100, padx = 100)
        
        self.tampilkan_gambar()

    def tampilkan_halaman_kedua(self):
        self.frame_csv = tk.Frame(root, bg = "white")
        self.frame_csv.pack(fill = "both", expand = True)
        
        self.label_nama = tk.Label(self.frame_csv, text = "Isi nama dan ujung NPM",font = ("Helvetica", 20, "bold"), bg = "white")
        self.label_nama.pack(pady=10)
        
        self.entry_nama = tk.Entry(self.frame_csv, font=("Courier New", 14))
        self.entry_nama.pack(pady=10)
        self.entry_nama.insert(0, "Nama")

        self.entry_npm = tk.Entry(self.frame_csv, font=("Courier New", 14))
        self.entry_npm.pack(pady=10)
        self.entry_npm.insert(0, "Ujung NPM")

        self.btn_simpan = tk.Button(self.frame_csv, text="Simpan", font=("Courier New", 14), command=self.simpan_data_csv)
        self.btn_simpan.pack(pady=10)
        
    def simpan_data_csv(self):
        nama = self.entry_nama.get()
        npm = self.entry_npm.get()

        if not nama or not npm or nama == "Nama" or npm == "Ujung NPM":
            messagebox.showwarning("Peringatan", "Isi semua data terlebih dahulu.")
            return

        try:
            with open("data_pengguna.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([nama, npm])
            messagebox.showinfo("Sukses", "Data berhasil disimpan!")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyimpan data: {e}")
    
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
