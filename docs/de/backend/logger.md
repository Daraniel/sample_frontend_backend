# logger Modul Dokumentation

Diese Dokumentation bietet eine Übersicht und Gebrauchsanweisungen für die `setup_logger` Funktion, die das Logging für eine Flask-Anwendung konfiguriert. Die Funktion richtet das Logging basierend auf den Konfigurationseinstellungen der Anwendung ein.

## Übersicht

Die `setup_logger` Funktion initialisiert die Logging-Konfiguration für eine Flask-Anwendung. Sie unterstützt das Logging sowohl in die Konsole als auch in eine Datei, mit Optionen für Log-Level, Format, Dateigrößenbeschränkungen und Anzahl der Sicherungskopien.

#### Parameter

- **app**: Die Flask-Anwendungsinstanz.

#### Konfigurationsoptionen

Die Funktion verwendet die folgenden Konfigurationsoptionen aus der Konfiguration der Flask-Anwendung:

- **log_level**: Das Logging-Level (Standard: 'DEBUG'). Mögliche Werte sind 'DEBUG', 'INFO', 'WARNING', 'ERROR' und 'CRITICAL'.
- **log_format**: Das Format für Log-Nachrichten (Standard: '%(asctime)s - %(name)s - %(levelname)s - %(message)s').
- **log_to_console**: Boolean-Flag, um das Logging in die Konsole zu aktivieren/deaktivieren (Standard: True).
- **log_to_file**: Boolean-Flag, um das Logging in eine Datei zu aktivieren/deaktivieren (Standard: True).
- **log_file**: Der Dateipfad für die Log-Datei (Standard: 'app.log').
- **log_max_bytes**: Die maximale Größe in Bytes für die Log-Datei, bevor sie rotiert wird (Standard: 10.000 Bytes).
- **log_backup_count**: Die Anzahl der Sicherungskopien, die aufbewahrt werden, wenn die Log-Datei rotiert wird (Standard: 1).

Bitte beachten Sie die Dokumentation des Python Loggers für weitere Informationen zu diesen Parametern.

#### Beispielkonfiguration

```python
from flask import Flask
from app.logger import setup_logger

app = Flask(__name__)

# Aktualisiere die Konfiguration der App
app.config.update(
    log_level='INFO',
    log_format='%(asctime)s - %(levelname)s - %(message)s',
    log_to_console=True,
    log_to_file=True,
    log_file='my_app.log',
    log_max_bytes=1048576,  # 1 MB
    log_backup_count=3
)

# Logger einrichten
setup_logger(app)
```
