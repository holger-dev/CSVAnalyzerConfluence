# CSV Analyser für Confluence
***
Dieses Tool dient zur Analyse von CSV-Benutzerdateien direkt aus Confluence.
## Anleitung
1. Laden Sie eine CSV-Benutzerdatei von Confluence herunter. Diese finden Sie unter
Benutzer -> drei Punkte -> Benutzer Exportieren.
Wichtig! Die Datei muss die Gruppen als Extra-Zeilen ausgeben. Dazu bei Zusätzliche Daten das Kästchen
Gruppen-Mitgliedschaft aktivieren und auch darunter das Kästchen Zu Spalte pivotieren aktivieren.
2. Das Programm starten.
3. Oben die CSV-Datei laden. Hinweis: Die Datei wird nur in das Programm geladen! Es werden keine
weiteren Daten oder andere Elemente gespeichert. Wird das Programm beendet, sind alle Daten zur Laufzeit
ebenfalls entfernt.
4. Nun kann im Programm über Gruppen/Benutzer gefiltert werden. Weitere Infos direkt im Programm
***
## Dists erstellen
Zum erstellen der einzelnen Dist-Files diesen Befehl im Terminal eingeben, vorher ins Git navigieren:
'''
pyinstaller --onefile --windowed --add-data "/opt/homebrew/Cellar/tcl-tk/9.0.0_1/lib/libtcl9.0.dylib:." --add-data "/opt/homebrew/Cellar/tcl-tk/9.0.0_1/lib/libtcl9tk9.0.dylib:." main.py
'''