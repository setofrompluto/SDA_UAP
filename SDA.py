import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class AplikasiTkinter:
  def __init__ (self, root):
    self.root = root


if __name__ == "__main__":
  root = tk.Tk()
  app = AplikasiTkinter(root)
  root.mainloop()
