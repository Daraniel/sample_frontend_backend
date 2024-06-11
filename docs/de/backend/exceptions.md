# exceptions Modul Dokumentation

Diese Dokumentation bietet eine Übersicht und Gebrauchsanweisungen für die benutzerdefinierten Ausnahmen, die in der
Anwendung verwendet werden. Diese Ausnahmen helfen bei der Handhabung und Kategorisierung verschiedener Fehler, die in
der Anwendung auftreten können, insbesondere im Zusammenhang mit Datenquellen.

## Übersicht

Das exceptions Modul definiert benutzerdefinierte Ausnahme-Klassen, um eine spezifischere Fehlerbehandlung zu
ermöglichen. Diese Ausnahmen sind hierarchisch strukturiert, sodass sowohl spezifische Fehler als auch breitere
Fehlerkategorien abgefangen werden können.

## Klassen

### `AppException` (Exception)

Basisklasse für alle Anwendungsfehler.

### `DataSourceException` (AppException)

Basisklasse für datenquellenbezogene Fehler. Erbt von `AppException`.

### `DataNotFoundException` (DataSourceException)

Wird ausgelöst, wenn keine Daten in der angegebenen Tabelle gefunden werden. Erbt von `DataSourceException`.

### `MetadataNotFoundException` (DataSourceException)

Wird ausgelöst, wenn keine Metadaten in der angegebenen Tabelle gefunden werden. Erbt von `DataSourceException`.

## Anwendungsbeispiel

Diese Ausnahmen können verwendet werden, um spezifische Fehlerfälle in der Anwendung zu handhaben, insbesondere beim
Arbeiten mit Datenquellen wie Datenbanken oder Dateien. Hier ist ein Beispiel für eine Verwendungsszenario innerhalb
eines data source Moduls:

```python
from app.exceptions import DataNotFoundException, MetadataNotFoundException


def get_data(table_name):
    try:
        # Code, um Daten aus einer Tabelle abzurufen
        if not data:
            raise DataNotFoundException(f"No data found for table {table_name}")
    except DataNotFoundException as e:
        print(f"Error: {e}")
        # Den Fehler behandeln, z.B. einen Standardwert zurückgeben oder die Ausnahme erneut auslösen


def get_metadata(table_name):
    try:
        # Code, um Metadaten aus einer Tabelle abzurufen
        if not metadata:
            raise MetadataNotFoundException(f"No metadata found for table {table_name}")
    except MetadataNotFoundException as e:
        print(f"Error: {e}")
        # Den Fehler behandeln, z.B. einen Standardwert zurückgeben oder die Ausnahme erneut auslösen
```
