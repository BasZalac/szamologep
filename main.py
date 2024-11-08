import tkinter as tk

# Funkciók a műveletekhez
def gombnyom(event):
    szam = entry.get()
    uj_karakter = event.widget.cget("text")
    
    if uj_karakter == "=":
        try:
            # Az = gomb lenyomása után próbáljuk kiértékelni a kifejezést
            eredmeny = eval(szam)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(eredmeny))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Hiba!")
    elif uj_karakter == "C":
        # A C gomb a mező törlésére szolgál
        entry.delete(0, tk.END)
    else:
        # Bármely más gomb a szöveg hozzáadása a mezőhöz
        entry.insert(tk.END, uj_karakter)

# Ablak létrehozása
root = tk.Tk()
root.config(bg="#2d2d2d")
root.title("Számológép")
# Képernyő mező (ahova a számokat írjuk)
entry = tk.Entry(root, width=15, font=("Arial", 24), borderwidth=2, relief="solid", justify="right", bg="#f1f1f1", fg="#333", bd=3)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Gombok létrehozása
gombok = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
    ("=", 5, 0, 4)  # A "C" gomb most szélesebb, mert lefoglalja az utolsó sort
]

# Gombok hozzáadása a GUI-hoz
for szoveg, sor, oszlop, *meret in gombok:
    gomb = tk.Button(root, text=szoveg, width=5, height=2, font=("Arial", 18), bg="#4d4d4d", fg="#fff", bd=2, relief="raised", activebackground="#616161", activeforeground="#fff")
    gomb.grid(row=sor, column=oszlop, columnspan=meret[0] if meret else 1, padx=5, pady=5)
    gomb.bind("<Button-1>", gombnyom)

# A GUI futtatása
root.mainloop()
