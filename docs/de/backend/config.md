# config Modul Dokumentation

Diese Dokumentation bietet eine Übersicht und Gebrauchsanweisungen für das `config` Modul, das zum Laden und
Validieren der Anwendungskonfiguration mit YAML und Cerberus entwickelt wurde.

## Übersicht

Das `config` Modul ist dafür verantwortlich, Konfigurationsdateien, die in YAML geschrieben sind, zu laden und
sie anhand eines vordefinierten Schemas mit der Cerberus-Bibliothek zu validieren. Dieses Modul stellt sicher, dass
Konfigurationseinstellungen die erwartete Struktur und Wertbeschränkungen erfüllen, bevor sie von der Anwendung
verwendet werden.

## Schema-Definition

Das Konfigurationsschema ist im `config_schema` Wörterbuch definiert. Das Schema umfasst zwei Hauptabschnitte: `app`
und `data_source`.

### `app` Schema

- `secret_key`: String, Standard: `'default_secret_key'`
- `debug`: Boolean, Standard: `False`
- `log_file`: String, Standard: `'app.log'`
- `log_level`: String, erlaubte Werte: `['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']`, Standard: `'INFO'`
- `log_format`: String, Standard: `'%(asctime)s - %(name)s - %(levelname)s - %(message)s'`
- `log_to_console`: Boolean, Standard: `True`
- `log_to_file`: Boolean, Standard: `True`
- `log_max_bytes`: Integer, Minimum: `100`, Standard: `10000`
- `log_backup_count`: Integer, Minimum: `0`, Standard: `1`

### `data_source` Schema

- `type`: String, erlaubte Werte: `['sqlite', 'excel']`, Standard: `'sqlite'`
- `sqlite`: Wörterbuch (Optional)
    - `db_path`: String, Standard: `'my_database.db'`
    - `create_tables_from_excel`: Boolean, Standard: `False`
    - `excel_file`: String, Standard: `'example.xlsx'`
- `excel`: Wörterbuch (Optional)
    - `file_name`: String, Standard: `'example.xlsx'`

Bitte beachten Sie, dass `secret_key` hier nur der Vollständigkeit halber definiert ist und in diesem Projekt keine
direkte Verwendung hat.

### Beispiel-Konfigurationsdatei

```yaml
app:
  secret_key: "your_secret_key"
  debug: true
  log_file: "app.log"
  log_level: "DEBUG"  # Kann DEBUG, INFO, WARNING, ERROR, CRITICAL sein
  log_format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  log_to_console: true
  log_to_file: true
  log_max_bytes: 10000  # Maximale Protokolldateigröße in Bytes vor Rotation
  log_backup_count: 1  # Anzahl der zu speichernden Sicherungsdateien

data_source:
  type: "excel"  # Kann "sqlite" oder "excel" sein
  sqlite:
    db_path: "my_database.db"
    create_tables_from_excel: true  # Flag zum Erstellen von Tabellen aus Excel, wenn die Datenbank nicht gefunden wird
    excel_file: "../vgrdl_r2b1_bs2022_0.xlsx"
  excel:
    file_name: "../vgrdl_r2b1_bs2022_0.xlsx"
```

## Funktionen

### `load_config(config_file='config/config.yaml')`

Diese Funktion lädt die Konfigurationsdatei, die durch den Parameter `config_file` angegeben ist.

Diese Funktion verwendet intern `validate_config`, um die Konfiguration zu validieren und zu normalisieren.

#### Parameter

- `config_file` (str): Pfad zur Konfigurationsdatei. Standard ist `'config/config.yaml'`.

#### Rückgaben

- `config` (dict): Die geladene Konfiguration als Wörterbuch.

### `validate_config(config, schema)`

Diese Funktion validiert die geladene Konfiguration anhand des bereitgestellten Schemas.

#### Parameter

- `config` (dict): Das zu validierende Konfigurationswörterbuch.
- `schema` (dict): Das Schema, gegen das validiert werden soll.

#### Rückgaben

- `normalized_config` (dict): Das normalisierte Konfigurationswörterbuch.

#### Löst aus

- `ValueError`: Wenn die Konfiguration nicht dem Schema entspricht.

## Anwendungsbeispiel

```python
from app.config import load_config, validate_config

config_schema = {
    # Definieren Sie hier Ihr Schema...
}

if __name__ == '__main__':
    config = load_config('file_name')
    validated_config = validate_config(config, config_schema)
    print(validated_config)
```

## Fehlerbehandlung

Wenn die Konfigurationsvalidierung fehlschlägt, wird ein `ValueError` ausgelöst, der Details zu den Validierungsfehlern
enthält.
