# Flask Application Setup Dokumentation

Diese Dokumentation bietet eine Übersicht und Anweisungen zur Einrichtung einer Flask-Anwendung mit Konfiguration,
Protokollierung, Datenquelleninitialisierung und API-Endpunktregistrierung.

## Übersicht

Diese Flask-Anwendung ist darauf ausgelegt, Konfigurationseinstellungen aus einer YAML-Datei zu laden, die
Protokollierung
einzurichten, eine Datenquelle zu initialisieren und verschiedene API-Endpunkte und Blueprints zu registrieren,
einschließlich
Swagger UI für die API-Dokumentation.

## Hauptabhängigkeiten

- `flask`: Zum Erstellen der Webanwendung.
- `flask-RESTful`: Zum Erstellen von RESTful APIs mit Flask.
- `flask_cors`: Zum Aktivieren von Cross-Origin Resource Sharing (CORS) in Flask-Anwendungen.
- `flask_swagger`: Zum Generieren von Swagger-Dokumentationen aus der Flask-App.
- `flask_swagger_ui`: Zum Bereitstellen von Swagger UI zur Dokumentation der API.
- `pyyaml`: Zum Laden der Konfiguration aus YAML-Dateien.
- `cerberus`: Zum Validieren von Konfigurationsdaten.

## Anwendungsstruktur

- `config`: Verzeichnis mit den Konfigurationsdateien.
- `app`: Paket, das den Quellcode der Anwendung enthält, einschließlich:
    - `__init__.py`: Hauptmodul, ermöglicht die Erstellung der App.
    - `config.py`: Modul zum Laden und Validieren der Konfiguration.
    - `data_source.py`: Modul zur Initialisierung der Datenquelle.
    - `exceptions.py`: Modul mit benutzerdefinierten Ausnahmen.
    - `logger.py`: Modul zur Einrichtung der Protokollierung.
    - `routes.py`: Modul zur Erstellung und Registrierung von API- und Home-Blueprints.
- `templates`: Verzeichnis mit den Vorlagendateien.
- `tests`: Verzeichnis mit Tests.

## Hauptfunktion

### `create_app(config_file='config/config.yaml')`

Diese Funktion erstellt und konfiguriert die Flask-Anwendung.

#### Parameter

- `config_file` (str): Pfad zur Konfigurationsdatei. Standard ist `'config/config.yaml'`.

Bitte lesen Sie die [Konfigurationsdokumentation](config.md) für weitere Informationen über diese Konfigurationsdatei.

#### Rückgaben

- `app` (Flask): Die konfigurierte Flask-Anwendung.

#### Beispiel

```python
from app import create_app

app = create_app('path/to/config.yaml')
```

### `register_blueprints(app, data_source)`

Diese Funktion registriert die Blueprints für die API-Endpunkte und Swagger UI mit der Flask-Anwendung.

#### Parameter

- `app` (Flask): Die Flask-Anwendung.
- `data_source` (BaseDataSource): Die Datenquelle für die Anwendung.

#### Beispiel

```python
from flask import Flask

from app import register_blueprints
from app.config import load_config
from app.data_source import get_data_source

config = load_config('config_file')

app = Flask(__name__)
data_source = get_data_source(config)

register_blueprints(app, data_source)
```

## Anwendungsbeispiel

1. Installieren Sie die erforderlichen Abhängigkeiten:

    ```sh
    pip install -r /path/to/requirements.txt
    ```

2. Erstellen oder konfigurieren Sie die Konfigurationsdatei config/config.yaml mit den erforderlichen Einstellungen.

3. Erstellen Sie die Flask-Anwendungsinstanz:

    ```python
    from app import create_app
    
    app = create_app('config/config.yaml')
    
    if __name__ == '__main__':
        app.run()
    ```


4. Greifen Sie auf die API und Swagger UI zu:
    - Eine einfache Homepage, die eine Liste von APIs unter `/` enthält.
    - API-Endpunkte sind unter `/api` verfügbar.
    - API-Spezifikationen sind unter `/api/spec` verfügbar.
    - Swagger UI ist unter `/swagger` verfügbar.

## Fehlerbehandlung

Die Anwendung umfasst eine grundlegende Fehlerbehandlung für das Laden und Validieren der Konfiguration. Wenn die
Konfigurationsvalidierung fehlschlägt, wird ein ValueError mit Details zu den Validierungsfehlern ausgelöst.
