# Autor: David Trupp
# Datum: 18.03.2026
# Kurzbeschreibung: Menü

import tkinter as tk
import tkinter.messagebox as messagebox
import efesdevelope as le
import logic_Harun as lh

# Memory-Datenstruktur für die Artikel
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
                        messagebox.showerror("Fehler", "Alle Felder müssen ausgefüllt werden!")
                        return

                try:
                        article_id = int(article_id)
                        stock = int(stock)
                        minimum_stock = int(minimum_stock)
                except ValueError:
                        messagebox.showerror("Fehler", "Artikelnummer, Menge und Mindestbestand müssen ganze Zahlen sein!")
                        return

                # EFE: doppelte Artikelnummer prüfen
                if le.article_exists(products, article_id):
                        messagebox.showerror("Fehler", "Artikelnummer bereits vorhanden!")
                        return

                # EFE: doppelten Produktnamen prüfen
                if le.product_name_exists(products, name):
                        messagebox.showerror("Fehler", "Produktname bereits vorhanden!")
                        return

                # EFE: Artikel hinzufügen
                success, message = le.add_product(products, article_id, name, stock, minimum_stock)

                # Workaround für Haruns min_stock-Key
                if success:
                        product = le.find_product_by_id(products, article_id)   # EFE: Artikel suchen
                        if product is not None:
                                product["min_stock"] = minimum_stock

                        messagebox.showinfo("Erfolg", message)
                        hinzufugen.destroy()
                else:
                        messagebox.showerror("Fehler", message)

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

                # EFE: Artikel vorher suchen
                product = le.find_product_by_id(products, article_id)
                if product is None:
                        messagebox.showerror("Fehler", "Artikel nicht gefunden!")
                        return

                # EFE: Artikel löschen
                success, message = le.delete_product(products, article_id)

                if success:
                        messagebox.showinfo("Erfolg", message)
                        entfernen.destroy()
                else:
                        messagebox.showerror("Fehler", message)

        tk.Button(entfernen, text="Artikel entfernen", command=remove_article).pack(pady=20)


def fenster_Artikel_anzeigen():
        anzeigen = tk.Toplevel(root)
        anzeigen.title("Artikel anzeigen")
        anzeigen.geometry("400x200")

        tk.Label(anzeigen, text="Geben Sie die Artikelnummer oder den Artikelnamen ein!").pack(pady=20)
        anzeigen_entry = tk.Entry(anzeigen)
        anzeigen_entry.pack(pady=10)

        def fenster_Artikel_angezeigt(results):
                angezeigt = tk.Toplevel(root)
                angezeigt.title("Artikel angezeigt")
                angezeigt.geometry("450x300")

                text = tk.Text(angezeigt, width=55, height=15)
                text.pack()

                for p in results:
                        text.insert(
                                tk.END,
                                f"Artikelname: {p['name']}\n"
                                f"Artikelnummer: {p['article_id']}\n"
                                f"Menge: {p['stock']}\n"
                                f"Mindestbestand: {p['minimum_stock']}\n"
                                "-------------------------\n"
                        )

                text.config(state=tk.DISABLED)

        def show_article():
                value = anzeigen_entry.get().strip()

                if not value:
                        messagebox.showerror("Fehler", "Bitte geben Sie eine Artikelnummer oder einen Artikelnamen ein!")
                        return

                result = []

                # EFE: Suche über search_products (ID)
                try:
                        article_id = int(value)
                        result = le.search_products(products, "id", article_id)
                except ValueError:
                        pass

                # HARUN: Namenssuche
                if not result:
                        result = lh.search_products_by_name(products, value)

                # EFE: Falls nötig nochmal direkte ID-Suche
                if not result:
                        try:
                                article_id = int(value)
                                product = le.find_product_by_id(products, article_id)
                                if product:
                                        result = [product]
                        except ValueError:
                                pass

                if result:
                        fenster_Artikel_angezeigt(result)
                        anzeigen.destroy()
                else:
                        messagebox.showerror("Fehler", "Kein Artikel mit dieser Artikelnummer oder diesem Namen gefunden!")

        tk.Button(anzeigen, text="Artikel anzeigen", command=show_article).pack(pady=20)


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

                if not article_id:
                        messagebox.showerror("Fehler", "Die Artikelnummer muss eingegeben werden!")
                        return

                try:
                        article_id = int(article_id)
                except ValueError:
                        messagebox.showerror("Fehler", "Die Artikelnummer muss eine ganze Zahl sein!")
                        return

                if new_stock == "" and new_minimum_stock == "":
                        messagebox.showerror("Fehler", "Bitte geben Sie mindestens einen Wert zum Ändern ein!")
                        return

                try:
                        new_stock = int(new_stock) if new_stock != "" else None
                        new_minimum_stock = int(new_minimum_stock) if new_minimum_stock != "" else None
                except ValueError:
                        messagebox.showerror("Fehler", "Menge und Mindestbestand müssen ganze Zahlen sein!")
                        return

                # EFE: Artikel aktualisieren
                success, message = le.update_product(products, article_id, stock=new_stock, minimum_stock=new_minimum_stock)

                # Workaround für Haruns min_stock-Key
                if success:
                        product = le.find_product_by_id(products, article_id)
                        if product is not None:
                                if new_minimum_stock is not None:
                                        product["min_stock"] = new_minimum_stock
                        messagebox.showinfo("Erfolg", message)
                        andern.destroy()
                else:
                        messagebox.showerror("Fehler", message)

        tk.Button(andern, text="Artikel ändern", command=ander_article).pack(pady=20)


def fenster_Bestand_erhoehen():
        erhoehen = tk.Toplevel(root)
        erhoehen.title("Bestand erhöhen")
        erhoehen.geometry("350x250")

        tk.Label(erhoehen, text="Artikelnummer:").pack(pady=10)
        artikelnummer_entry = tk.Entry(erhoehen)
        artikelnummer_entry.pack(pady=10)

        tk.Label(erhoehen, text="Menge zum Erhöhen:").pack(pady=10)
        menge_entry = tk.Entry(erhoehen)
        menge_entry.pack(pady=10)

        def increase():
                article_id = artikelnummer_entry.get().strip()
                amount = menge_entry.get().strip()

                if not article_id or not amount:
                        messagebox.showerror("Fehler", "Alle Felder müssen ausgefüllt werden!")
                        return

                try:
                        article_id = int(article_id)
                        amount = int(amount)
                except ValueError:
                        messagebox.showerror("Fehler", "Artikelnummer und Menge müssen ganze Zahlen sein!")
                        return

                # HARUN: Bestand erhöhen
                success = lh.increase_stock(products, article_id, amount)

                if success:
                        messagebox.showinfo("Erfolg", "Bestand erfolgreich erhöht!")
                        erhoehen.destroy()
                else:
                        messagebox.showerror("Fehler", "Artikel nicht gefunden!")

        tk.Button(erhoehen, text="Bestand erhöhen", command=increase).pack(pady=20)


def fenster_Bestand_verringern():
        verringern = tk.Toplevel(root)
        verringern.title("Bestand verringern")
        verringern.geometry("350x250")

        tk.Label(verringern, text="Artikelnummer:").pack(pady=10)
        artikelnummer_entry = tk.Entry(verringern)
        artikelnummer_entry.pack(pady=10)

        tk.Label(verringern, text="Menge zum Verringern:").pack(pady=10)
        menge_entry = tk.Entry(verringern)
        menge_entry.pack(pady=10)

        def decrease():
                article_id = artikelnummer_entry.get().strip()
                amount = menge_entry.get().strip()

                if not article_id or not amount:
                        messagebox.showerror("Fehler", "Alle Felder müssen ausgefüllt werden!")
                        return

                try:
                        article_id = int(article_id)
                        amount = int(amount)
                except ValueError:
                        messagebox.showerror("Fehler", "Artikelnummer und Menge müssen ganze Zahlen sein!")
                        return

                # HARUN: Bestand verringern
                success, message = lh.decrease_stock(products, article_id, amount)

                if success:
                        messagebox.showinfo("Erfolg", message)
                        verringern.destroy()
                else:
                        messagebox.showerror("Fehler", message)

        tk.Button(verringern, text="Bestand verringern", command=decrease).pack(pady=20)


def fenster_Niedriger_Bestand():
        niedrig = tk.Toplevel(root)
        niedrig.title("Niedriger Bestand")
        niedrig.geometry("500x300")

        text = tk.Text(niedrig, width=60, height=15)
        text.pack()

        # EFE: Low Stock Check
        le.check_low_stock(products)

        # HARUN: Low Stock Liste
        results = lh.get_low_stock_products(products)

        if not results:
                text.insert(tk.END, "Keine Artikel mit niedrigem Bestand vorhanden.")
        else:
                for p in results:
                        text.insert(
                                tk.END,
                                f"Artikelname: {p['name']}\n"
                                f"Artikelnummer: {p['article_id']}\n"
                                f"Bestand: {p['stock']}\n"
                                f"Mindestbestand: {p.get('min_stock', p.get('minimum_stock'))}\n"
                                "-------------------------\n"
                        )

        text.config(state=tk.DISABLED)


def fenster_Statistik():
        statistik = tk.Toplevel(root)
        statistik.title("Statistik")
        statistik.geometry("350x200")

        # HARUN: Statistik
        stats = lh.get_statistics(products)

        tk.Label(statistik, text=f"Anzahl Produkte: {stats['total_products']}").pack(pady=10)
        tk.Label(statistik, text=f"Gesamtbestand: {stats['total_stock']}").pack(pady=10)
        tk.Label(statistik, text=f"Produkte mit niedrigem Bestand: {stats['low_stock_count']}").pack(pady=10)


def fenster_Alle_Artikel():
        alle = tk.Toplevel(root)
        alle.title("Alle Artikel")
        alle.geometry("500x300")

        text = tk.Text(alle, width=60, height=15)
        text.pack()

        if len(products) == 0:
                text.insert(tk.END, "Keine Artikel im Lager vorhanden.")
        else:
                # EFE: show_products (Konsole)
                le.show_products(products)

                for p in products:
                        text.insert(
                                tk.END,
                                f"Artikelnummer: {p['article_id']} | "
                                f"Name: {p['name']} | "
                                f"Bestand: {p['stock']} | "
                                f"Mindestbestand: {p['minimum_stock']}\n"
                        )

        text.config(state=tk.DISABLED)


# Main GUI-Fenster
root = tk.Tk()
root.title("Lagerverwaltung")
root.geometry("450x500")

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

button5 = tk.Button(root, text="Bestand erhöhen", command=fenster_Bestand_erhoehen)
button5.pack(pady=10)

button6 = tk.Button(root, text="Bestand verringern", command=fenster_Bestand_verringern)
button6.pack(pady=10)

button7 = tk.Button(root, text="Niedrigen Bestand anzeigen", command=fenster_Niedriger_Bestand)
button7.pack(pady=10)

button8 = tk.Button(root, text="Statistik anzeigen", command=fenster_Statistik)
button8.pack(pady=10)

button9 = tk.Button(root, text="Alle Artikel anzeigen", command=fenster_Alle_Artikel)
button9.pack(pady=10)

root.mainloop()