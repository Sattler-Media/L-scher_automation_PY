import os

def UeberpruefenUndLoeschenLeererOrdner(pfad):
    # Überprüfen alle Ordner im angegebenen Pfad und seinen Unterordnern
    for ordner_pfad, unterordner, dateien in os.walk(pfad, topdown=False):
        # Gehe alle Unterordner durch
        for ordner in unterordner:
            ordner_vollständiger_pfad = os.path.join(ordner_pfad, ordner)
            
            # Überprüfen, ob der Ordner leer ist
            if not os.listdir(ordner_vollständiger_pfad):
                # Wenn leer, dann löschen
                os.rmdir(ordner_vollständiger_pfad)
                print(f"Leerer Ordner entfernt: {ordner_vollständiger_pfad}")
            else:
                # Wenn er Dateien enthält, informieren
                print(f"Ordner mit Dateien: {ordner_vollständiger_pfad}")

# Pfad des zu überprüfenden Ordners
haupt_ordner_pfad = "C:/pfad/zu/deinem/ordner"  # Passe diesen Pfad an dein System an


# Funktionsaufruf
UeberpruefenUndLoeschenLeererOrdner(haupt_ordner_pfad)
