# Frontend-Dokumentation

## Übersicht

Die `Tablee`-Komponente ist die Haupt-React-Komponente in dieser App, die Daten im Tabellenformat abruft und anzeigt.
Sie ermöglicht es den Benutzern, verschiedene Tabellen und Datenebenen auszuwählen, um die entsprechenden Daten
anzuzeigen. Diese Komponente verwendet Axios zum Abrufen von Daten und Material UI für das Styling sowie Bootstrap für
das Layout.

Obwohl es üblich ist, den Zustand der Anwendung zu verwalten, wurde in diesem einfachen Projekt darauf verzichtet.

## Komponentenstruktur

### Zustandsvariablen

- `level`: Repräsentiert die ausgewählte Datenebene (Standard: `"1"`).
- `table`: Repräsentiert die ausgewählte Tabelle (Standard: `"bruftoinlandsprodukt_in_jeweiligen_preisen"`).
- `data`: Speichert die abgerufenen Daten für die ausgewählte Tabelle und Ebene.
- `metadata`: Speichert Metadateninformationen für die ausgewählte Tabelle.

### Effekte

1. **Daten abrufen**:
    - Ruft Daten von der API basierend auf der ausgewählten `table` und `level` ab.
    - Parst die Antwort und aktualisiert den Zustand `data`.

2. **Metadaten abrufen**:
    - Ruft Metadaten von der API basierend auf der ausgewählten `table` ab.
    - Parst die Antwort und aktualisiert den Zustand `metadata`.

## Hauptmerkmale

- **Dynamische Tabellen- und Ebenenauswahl**: Die `TableDrop`- und `LevelDrop`-Komponenten ermöglichen es den Benutzern,
  verschiedene Tabellen und Ebenen dynamisch auszuwählen.
- **Metadatenanzeige**: Zeigt Metadateninformationen oben in der Tabelle an.
- **Scrollbare Tabelle**: Die Tabelle ist scrollbar für eine einfachere Navigation durch große Datensätze.
- **Sortierte Header**: Header werden so sortiert, dass string-basierte Header zuerst angezeigt werden.

## Fehlerbehandlung

- Beide `useEffect`-Hooks enthalten eine Fehlerbehandlung, um alle Probleme, die beim Abrufen der Daten auftreten, in
  der Konsole zu protokollieren.
