# data_source Modul Dokumentation

Diese Dokumentation bietet eine Übersicht und Gebrauchsanweisungen für das data source Modul, das die Datenabfrage
aus Excel-Dateien oder SQLite-Datenbanken unterstützt. Es umfasst die Handhabung verschiedener Datenebenen und die
Metadatenextraktion.

## Übersicht

Das data source Modul ist darauf ausgelegt, eine einheitliche Schnittstelle für den Zugriff auf Daten aus verschiedenen
Quellen wie Excel-Dateien und SQLite-Datenbanken bereitzustellen. Es unterstützt das Filtern von Daten nach
verschiedenen
Ebenen und das Extrahieren von Metadaten aus der Datenquelle.

## Klassen und Enums

### `DataLevel` (Enum)

Enumeration zur Definition der Datenebenen.

- `LEVEL1 = '1'`
- `LEVEL2 = '2'`
- `LEVEL3 = '3'`

### `BaseDataSource` (ABC)

Abstrakte Basisklasse für Datenquellen, alle nachfolgenden Datenquellen müssen davon erben.

#### Methoden

- `get_data(self, table_name: str, data_level: DataLevel) -> pd.DataFrame`: Abstrakte Methode zur Datenabfrage.
- `get_metadata(self, table_name: str) -> pd.DataFrame`: Abstrakte Methode zur Metadatenabfrage.

### `FileDataSource` (BaseDataSource)

Abstrakte Basisklasse für dateibasierte Datenquellen.

#### Methoden

- `get_data(self, table_name: str, data_level: DataLevel) -> pd.DataFrame`: Abstrakte Methode zur Datenabfrage.
- `get_metadata(self, table_name: str) -> pd.DataFrame`: Abstrakte Methode zur Metadatenabfrage.

### `ExcelDataSource` (FileDataSource)

Klasse für datenquellenbasierte auf Excel-Dateien.

#### Methoden

- `__init__(self, file_name: str)`: Initialisiert die Excel-Datenquelle mit dem angegebenen Dateinamen.
- `get_data(self, table_name: str, data_level: DataLevel) -> pd.DataFrame`: Ruft Daten aus dem angegebenen Excel-Blatt
  und der Datenebene ab.
- `get_metadata(self, table_name: str) -> pd.DataFrame`: Ruft Metadaten aus dem angegebenen Excel-Blatt ab.

### `DatabaseDataSource` (BaseDataSource)

Semi-abstrakte Basisklasse für datenbankbasierte Datenquellen.

#### Methoden

- `__init__(self, connection_string)`: Initialisiert die Datenbank-Datenquelle mit dem angegebenen Verbindungsstring.
- `get_data(self, table_name, data_level: DataLevel) -> pd.DataFrame`: Ruft Daten aus der angegebenen Datenbanktabelle
  und der Datenebene ab.
- `get_metadata(self, table_name: str) -> pd.DataFrame`: Abstrakte Methode zur Metadatenabfrage.

### `SQLiteDataSource` (DatabaseDataSource)

Klasse für datenquellenbasierte auf SQLite-Datenbanken. Diese Datenquelle unterstützt das Erstellen einer Datenbank aus
einer Excel-Datei, falls erforderlich. Bitte beachten Sie, dass nur '1.1' und '3.1' Tabellen automatisch generiert
werden. Diese Entscheidung wurde getroffen, um eine schnelle Erstellung der Datenbank in diesem begrenzten Projekt zu
ermöglichen.

#### Methoden

- `__init__(self, db_path: str, create_tables_from_excel: bool = False, excel_file: str = None)`: Initialisiert die
  SQLite
  Datenquelle mit dem angegebenen Datenbankpfad und optionaler Excel-Datei zur Tabellenerstellung.
- `create_tables_from_excel_file(self)`: Erstellt Datenbanktabellen aus der angegebenen Excel-Datei.
- `create_table_from_sheet(self, sheet_name: str, sheet_data: pd.DataFrame)`: Erstellt eine Tabelle in der Datenbank aus
  den angegebenen Blattdaten.
- `get_data(self, table_name, data_level: DataLevel) -> pd.DataFrame`: Ruft Daten aus der angegebenen Datenbanktabelle
  und der Datenebene ab.
- `get_metadata(self, table_name: str) -> pd.DataFrame`: Methode zur Metadatenabfrage, diese Methode ist nicht
  implementiert,
  da die Definition von Metadaten in diesem Projekt von der traditionellen Definition abweicht und die Handhabung eine
  weitere Tabelle mit Projektmetadaten erfordert, was der Einfachheit halber übersprungen wurde.

### `get_data_source(config)`

Funktion zur Auswahl der geeigneten Datenquelle basierend auf der Konfiguration.

#### Parameter

- `config` (dict): Konfigurationswörterbuch, das den Typ und die Parameter der Datenquelle enthält.

#### Rückgaben

- `BaseDataSource`: Eine Instanz der entsprechenden Datenquellenklasse.

## Ausnahmen

### `MetadataNotFoundException` (Exception)

Wird ausgelöst, wenn Metadaten nicht gefunden werden können.

### `DataNotFoundException` (Exception)

Wird ausgelöst, wenn Daten nicht gefunden werden können.

### `DataSourceException` (Exception)

Wird für allgemeine Datenquellenbezogene Fehler ausgelöst.

## Anwendungsbeispiel

```python
from app.data_source import get_data_source, DataLevel

config = {
    'data_source': {
        'type': 'sqlite',
        'sqlite': {
            'db_path': 'my_database.db',
            'create_tables_from_excel': False,
            'excel_file': 'example.xlsx'
        }
    }
}

data_source = get_data_source(config)
data = data_source.get_data('table_name', DataLevel.LEVEL1)
metadata = data_source.get_metadata('table_name')
```
