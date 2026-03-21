# Autor: David Trupp
# Datum: 18.03.2026
# Kurzbeschreibung: Menü

# Verschiedenen Optionen für die Lagerverwaltung werden angezeigt.

import tkinter as tk     # Ein GUI-Menü mit Tkinter
import efesdevelope as le                # Logik für die Lagerverwaltung
import logic_Harun as lh              # Logik für die Lagerverwaltung
# import sqlite3 as sql                   # Datenbank für die Lagerverwaltung
# con = sql.connect("Lager.db")   # Verbindung zur Datenbank herstellen

def fenster_Artikel_hinzufugen():
        hinzufugen = tk.Toplevel(root)
        hinzufugen.title("Artikel hinzufügen")
        hinzufugen.geometry("300x500")
        tk.Label(hinzufugen, text="Bitte geben Sie die Artikelinformationen ein!").pack(pady=20)
        tk.Label(hinzufugen, text="Artikelname:").pack(pady=10)
        hinzufugen_Artikelname_entry = tk.Entry(hinzufugen).pack(pady=10)
        tk.Label(hinzufugen, text="Artikelnummer:").pack(pady=10)
        hinzufugen_Artikelnummer_entry = tk.Entry(hinzufugen).pack(pady=10)
        tk.Label(hinzufugen, text="Menge:").pack(pady=10)
        hinzufugen_Menge_entry = tk.Entry(hinzufugen).pack(pady=10)
        tk.Label(hinzufugen, text="Mindestbestand:").pack(pady=10)
        hinzufugen_Mindestbestand_entry = tk.Entry(hinzufugen).pack(pady=10)
        tk.Button(hinzufugen, text="Artikel hinzufügen", command=le.article_exists).pack(pady=20)

def fenster_Artikel_hinzugefugt(): 
        hinzugefugt = tk.Toplevel(root)
        hinzugefugt.title("Artikel hinzugefügt")
        hinzugefugt.geometry("200x60")
        tk.Label(hinzugefugt, text="Der Artikel wurde hinzugefügt!").pack(pady=20)

def fenster_Artikel_entfernen():
        entfernen = tk.Toplevel(root)
        entfernen.title("Artikel entfernen")
        entfernen.geometry("400x200")
        tk.Label(entfernen, text="Bitte geben Sie die Artikelnummer ein!").pack(pady=20)
        tk.Entry(entfernen).pack(pady=10)
        tk.Button(entfernen, text="Artikel entfernen", command=fenster_Artikel_geloscht).pack(pady=20)

def fenster_Artikel_geloscht():
        geloscht = tk.Toplevel(root)
        geloscht.title("Artikel gelöscht")
        geloscht.geometry("200x60")
        tk.Label(geloscht, text="Der Artikel + Artikelname + wurde gelöscht!").pack(pady=20)

def fenster_Artikel_anzeigen():
        anzeigen = tk.Toplevel(root)
        anzeigen.title("Artikel anzeigen")
        anzeigen.geometry("400x200")
        tk.Label(anzeigen, text="Geben sie die Artikelnummer ein oder den Artikelnamen!").pack(pady=20)#
        tk.Entry(anzeigen).pack(pady=10)
        tk.Button(anzeigen, text="Artikel anzeigen", command=fenster_Artikel_angezeigt).pack(pady=20)

def fenster_Artikel_angezeigt():
        angezeigt = tk.Toplevel(root)
        angezeigt.title("Artikel angezeigt")
        angezeigt.geometry("300x400")
        tk.Label(angezeigt, text="Der Artikel + Artikelname + wurde angezeigt!").pack(pady=20)
        tk.Label(angezeigt, text="Artikelname:").pack(pady=10)
        tk.Label(angezeigt, text="artikelname").pack(pady=10)
        tk.Label(angezeigt, text="Artikelnummer:").pack(pady=10)
        tk.Entry(angezeigt).pack(pady=10)
        tk.Label(angezeigt, text="Menge:").pack(pady=10)
        tk.Entry(angezeigt).pack(pady=10)
        tk.Label(angezeigt, text="Mindestbestand:").pack(pady=10)
        tk.Entry(angezeigt).pack(pady=10)
        tk.Button(angezeigt, text="Artikel hinzufügen", command=fenster_Artikel_hinzugefugt).pack(pady=20)

# artikelname =
# artikelnummer =
# menge =
# mindestbestand =

def fenster_Artikel_andern():
        andern = tk.Toplevel(root)
        andern.title("Artikel ändern")
        andern.geometry("300x200")
        tk.Label(andern, text="Hier können Sie die Artikelinformationen ändern!").pack(pady=20)
        global andern_artikelnummer
        andern_artikelnummer = tk.Label(andern, text="Artikelnummer:").pack(pady=10)
        tk.Entry(andern).pack(pady=10)
        tk.Button(andern, text="Artikel ändern", command=fenster_Artikel_geandert).pack(pady=20)

def fenster_Artikel_geandert():
        geandert = tk.Toplevel(root)
        geandert.title("Artikel geändert")
        geandert.geometry("200x400")
        tk.Label(geandert, text="Artikeldaten ändern:").pack(pady=20)
        tk.Label(geandert, text="Artikelname:").pack(pady=10)
        tk.Label(geandert, text="artikelnummer").pack(pady=10)
        tk.Label(geandert, text=andern_artikelnummer.get()).pack(pady=10)
        tk.Entry(geandert).pack(pady=10)
        tk.Label(geandert, text="Menge:").pack(pady=10)
        tk.Entry(geandert).pack(pady=10)
        tk.Label(geandert, text="Mindestbestand:").pack(pady=10)
        tk.Entry(geandert).pack(pady=10)



root = tk.Tk()
root.title("Lagerverwaltung")
root.geometry("400x300")

label = tk.Label(root, text="Willkommen bei der Lagerverwaltung!")
label.pack(pady=20)

button1 = tk.Button(root, text="Artikel hinzufügen", command=fenster_Artikel_hinzufugen)
button1.pack(pady=10)

button2 = tk.Button(root, text="Artikel entfernen", command=fenster_Artikel_entfernen)
button2.pack(pady=10)

button3 = tk.Button(root, text="Artikel anzeigen", command=fenster_Artikel_anzeigen)
button3.pack(pady=10)

button4 = tk.Button(root, text="Artikel ändern", command=fenster_Artikel_andern)
button4.pack(pady=10)
root.mainloop()


