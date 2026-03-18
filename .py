

import tkinter as tk

def oeffne_neues_fenster():
    neues = tk.Toplevel(root)
    neues.title("Neues Fenster")
    neues.geometry("300x150")
    tk.Label(neues, text="Das ist ein neues Fenster!").pack(pady=20)
    tk.Button(neues, text="Schließen", command=neues.destroy).pack()

root = tk.Tk()
root.title("Hauptfenster")
root.geometry("400x250")

tk.Button(root, text="Weiter öffnen", command=oeffne_neues_fenster).pack(pady=30)

root.mainloop()