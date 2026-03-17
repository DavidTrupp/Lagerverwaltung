"""Autor: Harun
Datum: 17.03.2026
Kurzbeschreibung: Enthält die Logikfunktionen für die Lagerverwaltung.
"""

def search_products_by_name(products, search_term):
    """Sucht Produkte anhand eines Suchbegriffs im Namen.

    Argumente:
        products (list): Liste der Produkte.
        search_term (str): Suchbegriff.

    Returns:
        list: Liste der gefundenen Produkte.
    """
    search_term = search_term.lower()               #wandelt den Suchbegriff in Kleinbuchstaben um, um die Suche nicht case-sensitive zu machen (Groß- und Kleinschreibung wird ignoriert)
    found_products = []
    for product in products:                        #durchläuft die Liste der Produkte komplett
        if search_term in product['name'].lower():  #wenn eine Produktname den Suchbegriff enthält wird es ebenfalls klein geschrieben wegen Vergleich
            found_products.append(product)          #wird der neuen Liste hinzugefügt
    return found_products                           #gibt die neue Liste zurück

def increase_stock(products, product_id, amount):
    """Erhöht den Lagerbestand eines Produkts."""
    for product in products:                        #durchläuft die Liste der Produkte komplett
        if product['article_id'] == product_id:             #wenn die ID des Produkts mit der gesuchten ID übereinstimmt
            product['stock'] += amount              #wird der Lagerbestand um die angegebene Menge erhöht
            return True                             #gibt True zurück, wenn die Erhöhung erfolgreich war
    return False                                    #gibt False zurück, wenn kein Produkt mit der angegebenen ID gefunden wurde