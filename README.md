# Lagerverwaltungssystem (Python)

## Projektbeschreibung


Das vorliegende Projekt ist eine einfache Lagerverwaltung, die mit der Programmiersprache Python umgesetzt wurde. 
Ziel des Programms ist es, die Verwaltung von Artikeln in einem Lager zu ermöglichen und typische Funktionen einer Lagerverwaltung bereitzustellen.

Das Programm wurde im Team von Efe Yücel, David Trupp und Harun Smriko entwickelt und nutzt eine grafische Benutzeroberfläche (GUI), die mit dem Modul Tkinter erstellt wurde. Die Daten werden während der Laufzeit in einer Liste gespeichert und durch verschiedene Funktionen verwaltet.

Die Anwendung ermöglicht es dem Benutzer, Artikel anzulegen, zu bearbeiten, zu löschen und zu durchsuchen. Dabei wird besonders darauf geachtet, dass keine doppelten Artikelnummern oder Produktnamen vergeben werden.

---
### Funktionen: 

Das Programm bietet folgende Hauptfunktionen:

### Artikel hinzufügen
- Eingabe von:
  - Artikelname
  - Artikelnummer
  - Bestand 
  - Mindestbestand
- Prüfung auf:
  - leere Eingaben
  - gültige Zahlen
  - doppelte Artikelnummern
  - doppelte Produktnamen
- Erfolgs- oder Fehlermeldung wird ausgegeben

---

### Artikel löschen
- Löschen eines Artikels über die Artikelnummer
- Prüfung, ob Artikel existiert
- Rückmeldung über Erfolg oder Fehler

---

### Artikel suchen / anzeigen
- Suche nach:
  - Artikelnummer (exakte Übereinstimmung)
  - Produktname (Teilübereinstimmung (z. B. "schraube" = "Schraube"; Edelstahlschraube" usw.), unabhängig von Groß-/Kleinschreibung)
- Anzeige der gefundenen Artikel mit:
  - Name
  - Artikelnummer
  - Bestand
  - Mindestbestand

---

### Artikel ändern
- Anpassung von:
  - Bestand
  - Mindestbestand
- Artikel wird über die Artikelnummer identifiziert
- Eingaben werden überprüft
- Änderungen werden direkt übernommen

---

### Erweiterte Funktionen
- Prüfung auf niedrigen Lagerbestand
- Analyse von Lagerdaten (z. B. Anzahl der Artikel)

---

## Python-Version

Das Programm wurde entwickelt und getestet mit:

Python 3.14

---

## Beispielhafte Nutzung

Allgemein brauchen Branchen wie  Gesundheitswesen, Gastronomien, Industrien, Baufirmen usw. Lagerwaltungsprogramme zum checken von Medikamenten, Zutaten, Rohstoffen, Materialien, usw..

### Beispiel 1: Artikel hinzufügen

Eingabe:
- Name: Tastatur
- Artikelnummer: 1001
- Bestand: 20
- Mindestbestand: 5

Ausgabe:
→ „Artikel erfolgreich hinzugefügt“

---

### Beispiel 2: Artikel suchen

Eingabe:
- „Tastatur“

Ausgabe:
- Artikelname: Tastatur  
- Artikelnummer: 1001  
- Bestand: 20  
- Mindestbestand: 5  

---

### Beispiel 3: Artikel löschen

Eingabe:
- Artikelnummer: 1001

Ausgabe:
→ „Artikel wurde gelöscht“

---

## Teammitglieder

- Efe Yücel  
  → Logik (Artikelverwaltung)

- Harun  
  → Logik (Suche, Bestandsverwaltung, Zusatzfunktionen)

- David Trupp  
  → GUI (Tkinter, main.py, Benutzerinteraktion)

---

## Verwendete Module / Bibliotheken

### tkinter
Wird verwendet zur Erstellung der grafischen Benutzeroberfläche (Fenster, Buttons, Eingabefelder).

### tkinter.messagebox
Wird verwendet, um Fehlermeldungen und Erfolgsmeldungen für den Benutzer anzuzeigen.

---

### Eigene Module

#### efesdevelope.py
Enthält die Hauptlogik für:
- Artikel hinzufügen
- Artikel löschen
- Artikel suchen (ID)
- Artikel ändern
- Anzeige von Artikeln

---

#### logic_Harun.py
Enthält zusätzliche Funktionen:
- Suche nach Artikeln anhand des Namens
- Erhöhung und Verringerung von Beständen
- Analyse von Lagerdaten
- Erkennung von niedrigem Lagerbestand

---

## Datenstruktur

Die Artikel werden in einer Liste gespeichert:

- Jeder Artikel ist ein Dictionary mit:
  - article_id
  - name
  - stock
  - minimum_stock

Beispiel:

{
  "article_id": 76,
  "name": "Paracetamol 500mg ",
  "stock": 33,
  "minimum_stock": 10
}