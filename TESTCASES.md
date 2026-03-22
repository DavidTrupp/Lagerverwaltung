# TESTCASES

## Testfall 1: Artikel erfolgreich hinzufügen
**Input:**
- Artikelname: Tastatur
- Artikelnummer: 101
- Menge: 10
- Mindestbestand: 5

**Erwartetes Ergebnis:**
- Artikel wird gespeichert
- Erfolgsmeldung erscheint

**Tatsächliches Ergebnis:**
- Artikel erfolgreich hinzugefügt.

---

## Testfall 2: Artikel hinzufügen mit leerem Feld
**Input:**
- Artikelname: ""
- Artikelnummer: 102
- Menge: 5
- Mindestbestand: 2

**Erwartetes Ergebnis:**
- Fehlermeldung
- Artikel wird nicht gespeichert

**Tatsächliches Ergebnis:**
- Fehler: Alle Felder müssen ausgefüllt werden!

---

## Testfall 3: Artikel hinzufügen mit ungültiger Zahl
**Input:**
- Artikelnummer: "abc"

**Erwartetes Ergebnis:**
- Fehlermeldung

**Tatsächliches Ergebnis:**
- Fehler: Artikelnummer, Menge und Mindestbestand müssen ganze Zahlen sein!

---

## Testfall 4: Doppelte Artikelnummer
**Input:**
- Artikelnummer: 101 (existiert bereits)

**Erwartetes Ergebnis:**
- Fehlermeldung

**Tatsächliches Ergebnis:**
- Fehler: Artikelnummer bereits vorhanden!

---

## Testfall 5: Artikel löschen erfolgreich
**Input:**
- Artikelnummer: 101

**Erwartetes Ergebnis:**
- Artikel wird entfernt
- Erfolgsmeldung

**Tatsächliches Ergebnis:**
- Artikel erfolgreich gelöscht.

---

## Testfall 6: Artikel löschen – nicht vorhanden
**Input:**
- Artikelnummer: 999

**Erwartetes Ergebnis:**
- Fehlermeldung

**Tatsächliches Ergebnis:**
- Fehler: Artikel nicht gefunden!

---

## Testfall 7: Artikel nach ID suchen
**Input:**
- Suche: 101

**Erwartetes Ergebnis:**
- Artikel wird angezeigt

**Tatsächliches Ergebnis:**
- Artikel mit korrekten Daten angezeigt

---

## Testfall 8: Artikel nach Name suchen
**Input:**
- Suche: "tast"

**Erwartetes Ergebnis:**
- Artikel "Tastatur" wird gefunden

**Tatsächliches Ergebnis:**
- Passende Artikel werden angezeigt

---

## Testfall 9: Artikel suchen – nicht vorhanden
**Input:**
- Suche: "xyz"

**Erwartetes Ergebnis:**
- Fehlermeldung

**Tatsächliches Ergebnis:**
- Kein Artikel mit dieser Artikelnummer oder diesem Namen gefunden!

---

## Testfall 10: Bestand erhöhen
**Input:**
- Artikelnummer: 101
- Menge: +5

**Erwartetes Ergebnis:**
- Bestand erhöht sich um 5

**Tatsächliches Ergebnis:**
- Bestand erfolgreich erhöht

---

## Testfall 11: Bestand erhöhen – ungültige Eingabe
**Input:**
- Menge: "abc"

**Erwartetes Ergebnis:**
- Fehlermeldung

**Tatsächliches Ergebnis:**
- Fehler: Artikelnummer und Menge müssen ganze Zahlen sein!

---

## Testfall 12: Bestand verringern erfolgreich
**Input:**
- Artikelnummer: 101
- Menge: -3

**Erwartetes Ergebnis:**
- Bestand reduziert sich

**Tatsächliches Ergebnis:**
- Lagerbestand erfolgreich verringert

---

## Testfall 13: Bestand verringern – zu wenig Bestand
**Input:**
- Menge größer als vorhandener Bestand

**Erwartetes Ergebnis:**
- Fehlermeldung

**Tatsächliches Ergebnis:**
- Fehler: Nicht genügend Lagerbestand

---

## Testfall 14: Artikel ändern (Bestand)
**Input:**
- Artikelnummer: 101
- Neue Menge: 20

**Erwartetes Ergebnis:**
- Bestand wird aktualisiert

**Tatsächliches Ergebnis:**
- Artikel erfolgreich geändert

---

## Testfall 15: Artikel ändern – keine Werte eingegeben
**Input:**
- Keine Änderung eingegeben

**Erwartetes Ergebnis:**
- Fehlermeldung

**Tatsächliches Ergebnis:**
- Fehler: Bitte geben Sie mindestens einen Wert zum Ändern ein!

---

## Testfall 16: Niedrigen Bestand anzeigen
**Input:**
- Artikel mit Bestand <= Mindestbestand

**Erwartetes Ergebnis:**
- Liste der betroffenen Artikel

**Tatsächliches Ergebnis:**
- Artikel werden korrekt angezeigt

---

## Testfall 17: Niedriger Bestand – keine Treffer
**Input:**
- Alle Artikel über Mindestbestand

**Erwartetes Ergebnis:**
- Hinweis "keine Artikel"

**Tatsächliches Ergebnis:**
- Keine Artikel mit niedrigem Bestand vorhanden.

---

## Testfall 18: Statistik anzeigen
**Input:**
- Mehrere Artikel im System

**Erwartetes Ergebnis:**
- Anzahl Artikel korrekt
- Gesamtbestand korrekt
- Low-Stock korrekt

**Tatsächliches Ergebnis:**
- Statistik wird korrekt angezeigt

---

## Testfall 19: Alle Artikel anzeigen
**Input:**
- Mehrere Artikel vorhanden

**Erwartetes Ergebnis:**
- Alle Artikel werden angezeigt

**Tatsächliches Ergebnis:**
- Alle Artikel korrekt dargestellt

---

## Testfall 20: Alle Artikel anzeigen – leeres Lager
**Input:**
- Keine Artikel vorhanden

**Erwartetes Ergebnis:**
- Hinweis auf leeres Lager

**Tatsächliches Ergebnis:**
- Keine Artikel im Lager vorhanden.

## Hinweis
Die Testfälle wurden manuell über die grafische Benutzeroberfläche (Tkinter) durchgeführt.
Alle erwarteten Ergebnisse konnten erfolgreich reproduziert werden.