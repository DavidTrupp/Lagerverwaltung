# Autor: David Trupp
# Datum: 18.03.2026
# Kurzbeschreibung: Menü

# Verschiedenen Optionen für die Lagerverwaltung werden angezeigt.

import tkinter as tk     # Ein GUI-Menü mit Tkinter
import tkinter.messagebox as messagebox   # Fehlermeldungen anzeigen
import efesdevelope as le                # Logik für die Lagerverwaltung
import logic_Harun as lh              # Logik für die Lagerverwaltung
# import sqlite3 as sql                   # Datenbank für die Lagerverwaltung
# con = sql.connect("Lager.db")   # Verbindung zur Datenbank herstellen

#Memory-Datenstruktur für die Artikel
products = dict()  # Produkte werden in einem Dictionary gespeichert, um schnellen Zugriff auf Artikelinformationen zu ermöglichen
products = []        

def fenster_Artikel_hinzufugen():
        hinzufugen = tk.Toplevel(root)
        hinzufugen.title("Artikel hinzufügen")
        hinzufugen.geometry("300x500")
        tk.Label(hinzufugen, text="Bitte geben Sie die Artikelinformationen ein!").pack(pady=20)

        tk.Label(hinzufugen, text="Artikelname:").pack(pady=10)
        hinzufugen_Artikelname_entry = tk.Entry(hinzufugen)
        hinzufugen_Artikelname_entry.pack(pady=10)

        tk.Label(hinzufugen, text="Artikelnummer:").pack(pady=10)
        hinzufugen_Artikelnummer_entry = tk.Entry(hinzufugen)
        hinzufugen_Artikelnummer_entry.pack(pady=10)

        tk.Label(hinzufugen, text="Menge:").pack(pady=10)
        hinzufugen_Menge_entry = tk.Entry(hinzufugen)
        hinzufugen_Menge_entry.pack(pady=10)

        tk.Label(hinzufugen, text="Mindestbestand:").pack(pady=10)
        hinzufugen_Mindestbestand_entry = tk.Entry(hinzufugen)
        hinzufugen_Mindestbestand_entry.pack(pady=10)

        def add_article():
                name = hinzufugen_Artikelname_entry.get().strip()
                article_id = hinzufugen_Artikelnummer_entry.get().strip()
                stock = hinzufugen_Menge_entry.get().strip()
                minimum_stock = hinzufugen_Mindestbestand_entry.get().strip()

                if not name or not article_id or not stock or not minimum_stock:
                        tk.messagebox.showerror("Fehler", "Alle Felder müssen ausgefüllt werden!")
                        return
                
                try:
                        article_id = int(article_id)
                        stock = int(stock)
                        minimum_stock = int(minimum_stock)
                except ValueError:
                        tk.messagebox.showerror("Fehler", "Artikelnummer,Menge und Mindestbestand müssen ganze Zahlen sein!")
                        return
                
                success, message = le.add_product(products, article_id, name, stock, minimum_stock)
                
                if success:
                        messagebox.showinfo("Erfolg", message)
                        hinzufugen.destroy()  # Fenster schließen nach erfolgreichem Hinzufügen
                else:
                        messagebox.showerror("Fehler", message)

        # Nutze le.add_product funktion, um den Artikel hinzuzufügen

        tk.Button(hinzufugen, text="Artikel hinzufügen", command=add_article).pack(pady=20)

def fenster_Artikel_entfernen():
        entfernen = tk.Toplevel(root)
        entfernen.title("Artikel entfernen")
        entfernen.geometry("400x200")
        tk.Label(entfernen, text="Bitte geben Sie die Artikelnummer ein!").pack(pady=20)

        artikel_entfernen_entry = tk.Entry(entfernen)
        artikel_entfernen_entry.pack(pady=10)

        def remove_article():
                article_id = artikel_entfernen_entry.get().strip()

                if not article_id:
                        messagebox.showerror("Fehler", "Die Artikelnummer muss eingegeben werden!")
                        return
                
                try:
                        article_id = int(article_id)
                except ValueError:
                        messagebox.showerror("Fehler", "Die Artikelnummer muss eine ganze Zahl sein!")
                        return

                success, message = le.remove_product(products, article_id)

                if success:
                        messagebox.showinfo("Erfolg", message)
                        entfernen.destroy()  # Fenster schließen nach erfolgreichem Entfernen
                else:
                        messagebox.showerror("Fehler", message)
                
        tk.Button(entfernen, text="Artikel entfernen", command=remove_article).pack(pady=20)

def fenster_Artikel_anzeigen():
        anzeigen = tk.Toplevel(root)
        anzeigen.title("Artikel anzeigen")
        anzeigen.geometry("400x200")

        tk.Label(anzeigen, text="Geben sie die Artikelnummer ein oder den Artikelnamen!").pack(pady=20)#
        anzeigen_entry = tk.Entry(anzeigen)
        anzeigen_entry.pack(pady=10)

        def show_article():
                search_term = anzeigen_entry.get().strip()
                if not search_term:
                        tk.messagebox.showerror("Fehler", "Bitte geben Sie eine Artikelnummer oder einen Artikelnamen ein!")
                        return
                
                found_products = lh.search_products_by_name(products, search_term) or le.find_product_by_id(products, search_term)
                if found_products:
                        # Hier wird die Logik zum Anzeigen der gefundenen Artikel eingefügt
                        fenster_Artikel_angezeigt()
                        anzeigen.destroy()  # Fenster schließen nach erfolgreichem Anzeigen
                else:
                        tk.messagebox.showerror("Fehler", "Keine Artikel gefunden!")

        tk.Button(anzeigen, text="Artikel anzeigen", command=show_article).pack(pady=20)

def fenster_Artikel_angezeigt():
        angezeigt = tk.Toplevel(root)
        angezeigt.title("Artikel angezeigt")
        angezeigt.geometry("300x400")
        tk.Label(angezeigt, text="Artikeldetails:").pack(pady=20)

        tk.Label(angezeigt, text="Artikelname:").pack(pady=10)
        tk.Label(angezeigt, text=products["name"]).pack(pady=5)

        tk.Label(angezeigt, text="Artikelnummer:").pack(pady=10)
        tk.Label(angezeigt, text=products["article_id"]).pack(pady=5)

        tk.Label(angezeigt, text="Menge:").pack(pady=10)
        tk.Label(angezeigt, text=products["stock"]).pack(pady=5)

        tk.Label(angezeigt, text="Mindestbestand:").pack(pady=10)
        tk.Label(angezeigt, text=products["minimum_stock"]).pack(pady=5)

def fenster_Artikel_andern():
        andern = tk.Toplevel(root)
        andern.title("Artikel ändern")
        andern.geometry("300x200")
        tk.Label(andern, text="Hier können Sie die Artikelinformationen ändern!").pack(pady=20)
        #
        tk.Label(andern, text="Artikelnummer:").pack(pady=10)

        tk.Entry(andern).pack(pady=10)
        tk.Button(andern, text="Artikel ändern", command=fenster_Artikel_geandert).pack(pady=20)

def fenster_Artikel_geandert():
        geandert = tk.Toplevel(root)
        geandert.title("Artikel geändert")
        geandert.geometry("200x400")
        # tk.Label(geandert, text="Artikeldaten ändern:").pack(pady=20)
        # tk.Label(geandert, text="Artikelname:").pack(pady=10)
        # tk.Label(geandert, text="artikelnummer").pack(pady=10)
        # tk.Label(geandert, text=andern_artikelnummer.get()).pack(pady=10)
        # tk.Entry(geandert).pack(pady=10)
        # tk.Label(geandert, text="Menge:").pack(pady=10)
        # tk.Entry(geandert).pack(pady=10)
        # tk.Label(geandert, text="Mindestbestand:").pack(pady=10)
        # tk.Entry(geandert).pack(pady=10)



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


