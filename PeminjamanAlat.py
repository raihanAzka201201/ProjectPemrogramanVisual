import tkinter as tk

master = tk.Tk()
master.title("Peminjaman Alat UKM")
master.geometry("500x500")

inputNama = tk.Entry(master)
inputInstansi = tk.Entry(master)
inputNomor = tk.Entry(master)
inputAlamat = tk.Entry(master)
inputBarang = tk.Entry(master)
inputStatus = tk.Entry(master)


tk.Label(master, text = "Nama                        : ").grid(row=0, column=0)
inputNama.grid(row=0, column=1)
tk.Label(master, text = "Instansi                     : ").grid(row=1, column=0)
inputInstansi.grid(row=1, column=1)
tk.Label(master, text = "Nomor Telepon       : ").grid(row=2, column=0)
inputNomor.grid(row=2, column=1)
tk.Label(master, text = "Alamat                      : ").grid(row=3, column=0)
inputAlamat.grid(row=3, column=1)
tk.Label(master, text = "Barang                      : ").grid(row=4, column=0)
inputBarang.grid(row=4, column=1)
tk.Label(master, text = "Status Peminjaman : ").grid(row=5, column=0)
inputStatus.grid(row=5, column=1)

tk.mainloop()