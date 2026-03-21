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

Verhindert doppelte Artikelnummern beim Hinzufügen neuer Artikel
"""
def article_exists(products, article_id):
    for product in products:
        if product["article_id"] == article_id:
            return True
    return False


"""
Prüft, ob Produktname bereits existiert
Neuer Produktname wird mit der Liste der Produktnamen verglichen (case-insensitiv)

True -> Produktname existiert bereits
False -> Produktname ist noch frei

Verhindert doppelte Produktnamen beim Hinzufügen neuer Artikel
"""
def product_name_exists(products, name):
    name_lower = name.lower()
    for product in products:
        if product["name"].lower() == name_lower:
            return True
    return False


"""
Fügt neuen Artikel zur Liste hinzu

Prüft zuerst, ob Artikelnummer oder Produktname schon vergeben sind
Ja -> Fehlermeldung
Nein -> Artikel wird erstellt und hinzugefügt zur Liste

Rückgabe:
True -> Artikel wurde erfolgreich hinzugefügt
False -> Artikelnummer oder Produktname ist bereits vorhanden
"""
def add_product(products, article_id, name, stock, minimum_stock):

    if article_exists(products, article_id):
        return False, "Artikelnummer bereits vorhanden, andere wählen bitte"
    
    if product_name_exists(products, name):
        return False, "Produktname bereits vorhanden, anderen Namen wählen bitte"

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

"""
def find_product_by_id(products, article_id):

    for product in products:
        if product["article_id"] == article_id:
            return product
        
    return None


"""
Löscht Artikel durch Artikelnummer 
Funktion sucht mit find_product_by_id() nach dem Artikel

Wenn keine Artikel gefunden wurden --> Fehldermeldung
Wenn ein Artikel gefunden wurde, wird dieser entfernt


"""
def delete_product(products, article_id):
    product = find_product_by_id(products, article_id)

    if product is None:
        return False, "Artikel nicht gefunden"
    
    products.remove(product) 
    #Artikel entfernen aus der Liste

    return True, "Artikel wurde gelöscht"

"""
Aktualisiert einen bestehenden Artikel

Sucht Artikel anhand der Artikelnummer und aktualisiert die Werte
Es können Bestand und Mindestbestand angepasst werden

Rückgabe:
True -> Artikel wurde erfolgreich aktualisiert
False -> Artikel nicht gefunden
"""
def update_product(products, article_id, stock=None, minimum_stock=None):
    product = find_product_by_id(products, article_id)
    
    if product is None:
        return False, "Artikel nicht gefunden"
    
    if stock is not None:
        product["stock"] = stock
    
    if minimum_stock is not None:
        product["minimum_stock"] = minimum_stock
    
    return True, "Artikel erfolgreich aktualisiert"


"""
Prüft alle Artikel auf Mindestbestand

Vergleicht den aktuellen Bestand mit dem Mindestbestand
und zeigt alle Artikel an, deren Bestand unter dem Minimum liegt

Rückgabe:
Liste mit Artikeln mit zu niedrigem Bestand
"""
def check_low_stock(products):
    low_stock_items = []
    
    for product in products:
        if product["stock"] < product["minimum_stock"]:
            low_stock_items.append(product)
    
    if len(low_stock_items) == 0:
        print("Alle Artikel haben Bestand über Mindestbestand")
        return []
    
    print("\nWARNUNG - Folgende Artikel haben zu niedrigen Bestand:")
    print(f"{'Artikelnummer':<15}{'Bezeichnung':<20}{'Bestand':<12}{'Mindestbestand':<15}")
    
    for product in low_stock_items:
        print(
            f"{product['article_id']:<15}"
            f"{product['name']:<20}"
            f"{product['stock']:<12}"
            f"{product['minimum_stock']:<15}"
        )
    
    return low_stock_items


"""
Zeigt alle Artikel im Lager als Tabelle an

Wenn keine Artikel vorhandensind, wird eine Meldung ausgegeben  
Sonst werden alle Artikel angezeigt 
"""

def show_products(products):

    if len(products) == 0: 
        print("Keine Artikel im Lager vorhanden")
        return
    
    print("\n == Lagerbestand ==")
    print(f"{'Artikelnummer':<15}{'Bezeichnung':<20}{'Bestand':<12}{'Mindestbestand':<15}")

    for product in products:
        print(
            f"{product['article_id']:<15}"
            f"{product['name']:<20}"
            f"{product['stock']:<12}"
            f"{product['minimum_stock']:<15}"
        )


"""
Sucht Artikel nach Artikelnummer oder Produktname

Funktion sucht in Produktliste und vergleicht entweder:
1. Artikelnummer 
2. Produktname 

Rückgabe:
- Bei 'id' Suche: list mit einem oder null Produkten
- Bei 'name' Suche: list mit allen gefundenen Produkten
"""
def search_products(products, search_type, search_value):
    results = []
    
    if search_type.lower() == 'id':
        # Suche nach Artikelnummer (exakte Übereinstimmung)
        for product in products:
            if str(product["article_id"]) == str(search_value):
                results.append(product)
    
    elif search_type.lower() == 'name':
        # Suche nach Produktname (Teilübereinstimmung, case-insensitiv)
        search_value_lower = str(search_value).lower()
        for product in products:
            if search_value_lower in product["name"].lower():
                results.append(product)
    
    return results