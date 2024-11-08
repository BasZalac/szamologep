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
root.title("Számológép")

# Képernyő mező (ahova a számokat írjuk)
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Gombok létrehozása
gombok = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

# Gombok hozzáadása a GUI-hoz
for szoveg, sor, oszlop in gombok:
    gomb = tk.Button(root, text=szoveg, width=5, height=2, font=("Arial", 18))
    gomb.grid(row=sor, column=oszlop)
    gomb.bind("<Button-1>", gombnyom)

# A GUI futtatása
root.mainloop()
