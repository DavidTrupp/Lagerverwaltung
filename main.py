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

                if not name or not article_id or not stock or not minimum_stock:        #überprüft, ob alle Felder ausgefüllt sind, bevor der Artikel hinzugefügt wird
                        tk.messagebox.showerror("Fehler", "Alle Felder müssen ausgefüllt werden!")
                        return
                
                try:    #versucht die Artikelnummer, Menge und Mindestbestand in ganze Zahlen umzuwandeln, um sicherzustellen, dass die Eingaben gültig sind
                        article_id = int(article_id)
                        stock = int(stock)
                        minimum_stock = int(minimum_stock)
                except ValueError:
                        tk.messagebox.showerror("Fehler", "Artikelnummer,Menge und Mindestbestand müssen ganze Zahlen sein!")
                        return
                
                success, message = le.add_product(products, article_id, name, stock, minimum_stock)
                
                if success: #zeigt eine Erfolgsmeldung an, wenn der Artikel erfolgreich hinzugefügt wurde, und schließt das Fenster nach dem Hinzufügen
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

                if not article_id: #überprüft, ob die Artikelnummer eingegeben wurde, bevor versucht wird, den Artikel zu entfernen
                        messagebox.showerror("Fehler", "Die Artikelnummer muss eingegeben werden!")
                        return
                
                try: #versucht die Artikelnummer in eine ganze Zahl umzuwandeln, um sicherzustellen, dass die Eingabe gültig ist
                        article_id = int(article_id)
                except ValueError:
                        messagebox.showerror("Fehler", "Die Artikelnummer muss eine ganze Zahl sein!")
                        return

                success, message = le.delete_product(products, article_id)

                if success: #zeigt eine Erfolgsmeldung an, wenn der Artikel erfolgreich entfernt wurde, und schließt das Fenster nach dem Entfernen
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
                value = anzeigen_entry.get().strip()
                if not value: #überprüft, ob eine Artikelnummer oder ein Artikelname eingegeben wurde, bevor versucht wird, den Artikel anzuzeigen
                        messagebox.showerror("Fehler", "Bitte geben Sie eine Artikelnummer oder einen Artikelnamen ein!")
                        return
                
                result = []
                # ID-Suche
                try: #versucht die Eingabe als Artikelnummer zu interpretieren, um den Artikel anhand der ID zu suchen. Wenn die Eingabe keine gültige Zahl ist, wird eine Fehlermeldung angezeigt
                        article_id = int(value)
                        product = le.find_product_by_id(products, article_id)
                        if product:
                                result = [product]
                except:
                        pass
                # Namenssuche
                if not result: #wenn die ID-Suche kein Ergebnis geliefert hat, wird die Eingabe als Artikelname interpretiert und die Suche anhand des Namens durchgeführt
                        result = lh.search_products_by_name(products, value)

                if result: #wenn entweder die ID-Suche oder die Namenssuche ein Ergebnis geliefert hat, wird das Ergebnis in einem neuen Fenster angezeigt, andernfalls wird eine Fehlermeldung angezeigt
                        fenster_Artikel_angezeigt(result)
                        fenster_Artikel_anzeigen.destroy()  # Fenster schließen nach erfolgreichem Anzeigen
                else:
                        messagebox.showerror("Fehler", "Kein Artikel mit dieser Artikelnummer oder diesem Namen gefunden!")

        tk.Button(anzeigen, text="Artikel anzeigen", command=show_article).pack(pady=20)

        def fenster_Artikel_angezeigt(results):
                angezeigt = tk.Toplevel(root)
                angezeigt.title("Artikel angezeigt")
                angezeigt.geometry("400x200")

                text = tk.Text(angezeigt, width=50, height=15)
                text.pack()

                for p in results: #durchläuft die Liste der gefundenen Produkte und fügt die Informationen jedes Produkts in das Textfeld ein, um sie anzuzeigen
                        text.insert(tk.END, 
                            f"Artikelname: {p['name']}\n"
                            f"Artikelnummer: {p['article_id']}\n"
                            f"Menge: {p['stock']}\n"
                            f"Mindestbestand: {p['minimum_stock']}\n"
                            "---------------\n")
                
                        text.config(state=tk.DISABLED)  # Textfeld schreibgeschützt machen

def fenster_Artikel_andern():
        andern = tk.Toplevel(root)
        andern.title("Artikel ändern")
        andern.geometry("400x500")
        tk.Label(andern, text="Hier können Sie die Artikelinformationen ändern!").pack(pady=20)
        
        tk.Label(andern, text="Artikelnummer:").pack(pady=10)
        andern_artikelnummer = tk.Entry(andern)
        andern_artikelnummer.pack(pady=10)

        tk.Label(andern, text="Neue Menge:").pack(pady=10)
        andern_menge = tk.Entry(andern)
        andern_menge.pack(pady=10)

        tk.Label(andern, text="Neuer Mindestbestand:").pack(pady=10)
        andern_mindestbestand = tk.Entry(andern)
        andern_mindestbestand.pack(pady=10)

        def ander_article():
                article_id = andern_artikelnummer.get().strip()
                new_stock = andern_menge.get().strip()
                new_minimum_stock = andern_mindestbestand.get().strip()

                if not article_id: #überprüft, ob die Artikelnummer eingegeben wurde, bevor versucht wird, den Artikel zu ändern        
                        messagebox.showerror("Fehler", "Die Artikelnummer muss eingegeben werden!")
                        return
                
                try: #versucht die Artikelnummer in eine ganze Zahl umzuwandeln, um sicherzustellen, dass die Eingabe gültig ist
                        article_id = int(article_id)
                except ValueError:
                        messagebox.showerror("Fehler", "Die Artikelnummer muss eine ganze Zahl sein!")
                        return

                if new_stock == "" and new_minimum_stock == "": #überprüft, ob mindestens eine der beiden Felder (Menge oder Mindestbestand) ausgefüllt ist, bevor versucht wird, den Artikel zu ändern
                        messagebox.showerror("Fehler", "Bitte geben Sie mindestens einen Wert zum Ändern ein!")
                        return

                try: #versucht die neue Menge und den neuen Mindestbestand in ganze Zahlen umzuwandeln, wenn sie eingegeben wurden, um sicherzustellen, dass die Eingaben gültig sind. Wenn eines der Felder leer ist, wird es als None behandelt, damit die update_product Funktion weiß, dass dieser Wert nicht geändert werden soll
                        new_stock = int(new_stock) if new_stock != "" else None
                        new_minimum_stock = int(new_minimum_stock) if new_minimum_stock != "" else None
                except ValueError:
                        messagebox.showerror("Fehler", "Menge und Mindestbestand müssen ganze Zahlen sein!")
                        return

                success, message = le.update_product(products, article_id, stock=new_stock, minimum_stock=new_minimum_stock)

                if success: #zeigt eine Erfolgsmeldung an, wenn der Artikel erfolgreich geändert wurde, und schließt das Fenster nach dem Ändern
                        messagebox.showinfo("Erfolg", message)
                        andern.destroy()  # Fenster schließen nach erfolgreichem Ändern
                else:
                        messagebox.showerror("Fehler", message)

        tk.Button(andern, text="Artikel ändern", command=ander_article).pack(pady=20)        

# Main GUI-Fenster
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


