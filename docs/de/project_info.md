# Simple Frontend Backend

Dieses Projekt ist eine Beispiel-Webanwendung, die mit einem Flask-Backend und einem React-Frontend erstellt wurde.

Es ermöglicht den Zugriff auf Daten aus der bereitgestellten Datenquelle (standardmäßig: Excel-Datendatei) und den
Zugriff auf verschiedene Tabellen daraus.

Das Hauptziel besteht darin, ein relativ generisches und einfach zu erweiterndes Backend zu erstellen, das das
Hinzufügen eines neuen API-Endpunkts für jede Tabelle in einer einzigen Zeile ermöglicht. Außerdem wird Swagger für die
API automatisch erstellt.

Ein Frontend wird bereitgestellt, um den Zugriff auf die Daten und deren Ansicht zu ermöglichen.

## Allgemeine Informationen

Dieses Projekt besteht aus zwei Teilen: einem Python-Flask-Backend und einem Javascript-Frontend.

Das allgemeine Design dieses Projekts ist wie folgt:

![project_structure_diagram](../project_structure.svg)

In diesem Diagramm erstellt der Routing-Generator Routing für den Zugriff auf Daten aus Tabellen der Datenquelle.
Darüber hinaus ist das Backend durch eine YAML-Datei konfigurierbar und verfügt über eine
Konfigurationsdatei-Validierung. Schließlich verfügt das Backend über einen Logger, um verschiedene Ereignisse zu
protokollieren.

Zur einfachen Zugänglichkeit zeigt die Startseite des Backends eine Liste seiner APIs. Es verfügt auch über eine
Swagger-UI mit relevanter API-Dokumentation.

Das Frontend ist eine einfache Single-Page-React-Anwendung, die die Visualisierung der Daten ermöglicht.

## Ordnerstruktur

- `backend`: Enthält den Backend-Code der Webanwendung. Weitere Informationen zur Einrichtung finden Sie in
  der `README.md`-Datei im Backend-Ordner oder alternativ in der Dokumentation.
- `frontend`: Enthält den Frontend-Code der Webanwendung. Weitere Informationen zur Einrichtung finden Sie in
  der `README.md`-Datei im Frontend-Ordner oder alternativ in der
  Dokumentation.
- `docs`: Enthält Dokumentationsdateien mit detaillierten Informationen zur Projekteinrichtung, Konfiguration, Nutzung
  und mehr.

## Erste Schritte

Um mehr über das Projekt zu erfahren:

1. **Backend-Einrichtung**: Navigieren Sie zum `backend`-Ordner und lesen Sie die `README.md`-Datei im Backend-Ordner
   für Anweisungen zur Einrichtung und Ausführung des Backends.

2. **Frontend-Einrichtung**: Navigieren Sie zum `frontend`-Ordner und lesen Sie
   die `README.md`-Datei im Frontend-Ordner für Anweisungen zur Einrichtung und Ausführung des
   Frontends.

3. **Dokumentation**: Erkunden Sie den `docs`-Ordner für detaillierte Dokumentation zu verschiedenen Aspekten des
   Projekts, einschließlich Konfiguration, Nutzung und mehr.

## Dockerisierung

Um das Projekt mit Docker auszuführen, befolgen Sie diese Schritte:

1. **Docker-Images erstellen**:

    ```bash
    docker-compose build
    ```

2. **Docker-Container ausführen**:

    ```bash
    docker-compose up
    ```

3. **Auf die Anwendung zugreifen**:

   Das Frontend ist verfügbar unter [http://localhost:3000](http://localhost:3000) und das Backend
   unter [http://localhost:5000](http://localhost:5000).
