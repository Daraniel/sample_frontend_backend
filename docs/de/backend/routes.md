# routes Modul Dokumentation

Dieses Modul richtet Flask-Blueprints und RESTful-API-Ressourcen für die Verarbeitung von Datenanfragen ein. Es umfasst die Konfiguration für Swagger UI und API-Dokumentation sowie Dienstprogramme zum Registrieren von Ressourcen- und Metadaten-Endpunkten.

Diese Datei ermöglicht das Registrieren von APIs für jede Tabelle (mit einer ähnlichen Datenstruktur wie die aktuellen Tabellen) in einer einzigen Zeile und erstellt dynamisch den Endpunkt und die Swagger/API-Dokumentation für sie.

## Klassen

### `GenericDataResource`

Eine generische Klasse zur Verarbeitung von Datenanfragen, die das Registrieren neuer Datenquellen (Tabellen), die dem Schema der vorhandenen Tabellen entsprechen, in einer Zeile ermöglicht.

#### `__init__(self, data_source: BaseDataSource, table_name: str, data_description: str)`

Initialisiert die Ressource mit einer Datenquelle, einem Tabellennamen und einer Datenbeschreibung.

#### `handle_data_request(get_data_func, table_name, data_level)`

Holt Daten für ein bestimmtes Datenlevel.

#### `handle_metadata_request(get_metadata_func, table_name)`

Holt Metadaten.

#### `get(self, data_level)`

Verarbeitet GET-Anfragen, um Daten für ein bestimmtes Level aus der Tabelle abzurufen.

#### `get_metadata(self)`

Verarbeitet GET-Anfragen, um Metadaten aus der Tabelle abzurufen.

## Funktionen

### `add_resource_to_api(api, resource_name, table_name, data_source)`

Hilfsfunktion zum Erstellen und Hinzufügen von Ressourcen und deren Metadaten zur API, ermöglicht das Hinzufügen neuer Tabellen in einer Zeile.

#### Parameter

- **api**: Das API-Objekt.
- **resource_name**: Der Name der Ressource, die zur Erstellung der API-URL verwendet wird.
- **table_name**: Der Name der Tabelle, aus der die Ressourcen abgerufen werden.
- **data_source**: Datenquelle, aus der die Daten abgerufen werden (BaseDataSource-Objekt).

#### Beispielverwendung

```python
from flask import Blueprint
from flask_restful import Api
from app.data_source import BaseDataSource
from app.routes import add_resource_to_api


# Erstellen und Konfigurieren Ihrer Datenquelle
class MyDataSource(BaseDataSource):
    pass


data_source = MyDataSource()

# Erstellen eines Blueprints
data_bp = Blueprint('data', __name__)
api = Api(data_bp)

# Ressourcen in einer Zeile zum Endpunkt hinzufügen
add_resource_to_api(api, resource_name='Bruftoinlandsprodukt_in_jeweiligen_Preisen', table_name='1.1',
                    data_source=data_source)
add_resource_to_api(api, resource_name='Erwerbstaefige', table_name='3.1', data_source=data_source)
```

Dies führt zur Erstellung der folgenden Endpunkte, wobei `data_level` `'1'`, `'2'` oder `'3'` ist:

##### bruftoinlandsprodukt_in_jeweiligen_preisen

- **Daten auf gewünschtem Level {data_level}**:
  [http://127.0.0.1:5000/api/bruftoinlandsprodukt_in_jeweiligen_preisen/{data_level}](http://127.0.0.1:5000/api/bruftoinlandsprodukt_in_jeweiligen_preisen/{data_level})
- **Metadaten**:
  [http://127.0.0.1:5000/api/bruftoinlandsprodukt_in_jeweiligen_preisen/metadata](http://127.0.0.1:5000/api/bruftoinlandsprodukt_in_jeweiligen_preisen/metadata)

##### erwerbstaefige

- **Daten auf gewünschtem Level {data_level}**:
  [http://127.0.0.1:5000/api/erwerbstaefige/{data_level}](http://127.0.0.1:5000/api/erwerbstaefige/{data_level})
- **Metadaten**:
  [http://127.0.0.1:5000/api/erwerbstaefige/metadata](http://127.0.0.1:5000/api/erwerbstaefige/metadata)

Bitte beachten Sie, dass die Weiterleitung zur API je nach Projektkonfiguration unterschiedlich sein kann.

### `create_data_blueprint(data_source)`

Erstellt einen Flask-Blueprint für die Datenendpunkte (Daten auf einem bestimmten Level abrufen und Metadaten abrufen).

#### Parameter

- **data_source**: Datenquelle, aus der die Daten abgerufen werden.

#### Rückgaben

- **Blueprint**: Der erstellte Daten-Blueprint.

### `create_home_blueprint()`

Erstellt einen Flask-Blueprint für die Homepage, die Informationen über den Daten-Blueprint enthält.

#### Parameter

- **api_spec_url**: URL, unter der die API-Spezifikation bereitgestellt wird.
- **swagger_url**: URL, unter der Swagger bereitgestellt wird.

#### Rückgaben

- **Blueprint**: Der erstellte Home-Blueprint.

## Beispielverwendung

```python
from flask import Flask
from app.data_source import BaseDataSource
from app.routes import create_data_blueprint, create_home_blueprint

app = Flask(__name__)


# Erstellen und Konfigurieren Ihrer Datenquelle
class MyDataSource(BaseDataSource):
    pass


data_source = MyDataSource()

# Registrieren des Daten-Blueprints
data_blueprint = create_data_blueprint(data_source)
app.register_blueprint(data_blueprint, url_prefix='/data')

# Registrieren des Home-Blueprints
home_blueprint = create_home_blueprint()
app.register_blueprint(home_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
```
