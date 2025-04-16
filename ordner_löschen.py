import os
import logging
import argparse

# Configuración del registro (logging)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def UeberpruefenUndLoeschenLeererOrdner(pfad):
    """
    Überprüft alle Ordner im angegebenen Pfad und löscht leere Ordner.

    Args:
        pfad (str): Der Pfad des Hauptordners, der überprüft werden soll.
    """
    for ordner_pfad, unterordner, _ in os.walk(pfad, topdown=False):
        for ordner in unterordner:
            ordner_vollständiger_pfad = os.path.join(ordner_pfad, ordner)
            try:
                # Überprüfen, ob der Ordner leer ist
                if not os.listdir(ordner_vollständiger_pfad):
                    # Wenn leer, dann löschen
                    os.rmdir(ordner_vollständiger_pfad)
                    logging.info(f"Leerer Ordner entfernt: {ordner_vollständiger_pfad}")
                else:
                    # Wenn er Dateien enthält, informieren
                    logging.warning(f"Ordner mit Dateien: {ordner_vollständiger_pfad}")
            except Exception as e:
                logging.error(f"Fehler beim Verarbeiten des Ordners {ordner_vollständiger_pfad}: {e}")

if __name__ == "__main__":
    # Argumentos de línea de comandos
    parser = argparse.ArgumentParser(description="Überprüfen und Löschen leerer Ordner.")
    parser.add_argument("pfad", type=str, help="Pfad des zu überprüfenden Ordners")
    args = parser.parse_args()

    # Validación del directorio principal
    if not os.path.exists(args.pfad):
        logging.error(f"Der angegebene Pfad existiert nicht: {args.pfad}")
    else:
        # Funktionsaufruf
        UeberpruefenUndLoeschenLeererOrdner(args.pfad)


####### WICHTIG!!!!! ##########   
# execute mit python ordner_löschen.py "C:/dein/Pfad/zum/Aufräumen"