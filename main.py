# Autor: David Trupp
# Datum: 18.03.2026
# Kurzbeschreibung: Menü

# Verschiedenen Optionen für die Lagerverwaltung werden angezeigt.

print("Willkommen bei der Lagerverwaltung!")
print("Bitte wählen Sie eine Option:")
print("1. Artikel hinzufügen")
print("2. Artikel entfernen")
print("3. Artikel anzeigen")
print("4. Ändern Sie die Artikelinformationen")


while True:      #Endlosschleife, bis eine gültige Option eingegeben wird
    option = input("Option: ")
    if option in ("1", "2", "3", "4"):
        break
    print("Ungültige Option, bitte wählen Sie eine gültige Option.")

# Je nach gewählter Option wird eine entsprechende Nachricht ausgegeben

if option == "1":   
    print("Sie haben Artikel hinzufügen gewählt.")
elif option == "2":
    print("Sie haben Artikel entfernen gewählt.")
elif option == "3":
    print("Sie haben Artikel anzeigen gewählt.")
elif option == "4":
    print("Sie haben Artikel ändern gewählt.")

import thinker as tk

root = tk.Tk()
root.title("Lagerverwaltung")
root.geometry("400x300")

label = tk.Label(root, text="Willkommen bei der Lagerverwaltung!")
label.pack(pady=20)

button1 = tk.Button(root, text="Artikel hinzufügen", command=lambda: print("Artikel hinzufügen"))
button1.pack(pady=10)

button2 = tk.Button(root, text="Artikel entfernen", command=lambda: print("Artikel entfernen"))
button2.pack(pady=10)

button3 = tk.Button(root, text="Artikel anzeigen", command=lambda: print("Artikel anzeigen"))
button3.pack(pady=10)
button4 = tk.Button(root, text="Artikel ändern", command=lambda: print("Artikel ändern"))
button4.pack(pady=10)
root.mainloop()





