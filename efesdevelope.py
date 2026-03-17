"""
Autor: Efe Yücel
Datum: 17.03.2026
Kurzbeschreibung: Logikfunktionen
"""


"""
Prüft, ob Artikelnummer bereits existiert
Neue Artikelnummer wird mit der Liste der Artikelnummern verglichen

True -> Artikelnummer existiert bereits
False -> Artikelnummer ist noch frei

Verhindert doppelte Artikelnummern beim hinzufügen neuer Artikel
"""
def article_exists(products, article_id):
    for product in products:
        if product["article_id"] == article_id:
            return True
    return False



"""
Fügt neuen Artikel zur Liste hinzu

Prüft zuerst, ob Artikelnummer schon vergeben ist
Ja -> Fehlermeldung
Nein -> Artikel wird erstellt und hinzugefügt zur Liste

Rückgabe:
True -> Artikel wurde erfolgreich hinzugefügt
False -> Artikelnummer ist bereits vorhanden
"""
def add_product(products, article_id, name, stock, minimum_stock):

    if article_exists(products, article_id):
        return False, "Artikelnummer bereits vorhanden, andere wählen bitte"

    new_product = {
        "article_id": article_id,
        "name": name,
        "stock": stock,
        "minimum_stock": minimum_stock
    }

    products.append(new_product)        #fügt neuen Artikel zur Liste hinzu

    return True, "Artikel erfolgreich hinzugefügt"





"""
Sucht einen Artikel anhand der Artikelnummer

Funktion sucht in Produktliste und vergleicht Artikelnummern mit der gesuchten Nummer
Wenn kein Artikel gefunden wurde, wird ein None zurückgegeben
Wenn Artikel mit passender Nummer gefunden wird, wird das Produkt zurückgegeben


Wird später verwendet für:
- Artikel ändern
- Artikel suchen
- Artikel löschen
"""
def find_product_by_id(products, article_id):

    for product in products:
        if product["article_id"] == article_id:
            return product
        
    return None