# Hier werden Fehler geschrieben, die bei der Transformation der Ausgangsdaten gefunden wurden. Sie werden nach der Quelle (z.B. DNB, ZDB usw.) sortiert.

# Fehlermeldungen:
## `InputError`

Fehlermeldungen bezüglich der primären Eingaben. Es wird folgendes auf Konsistenz geprüft:
- Datentyp (`Authority`, `Bibliographic`)
- Entitäten- oder Ressourcentyp (`PerName`, `GeoName`, `Zdb`, `Dnb1` etc.), kombinierbar mit entsprechenden Datentypen
- Ausgabeformat (`json`, `graphml`)
- Selektion der Daten (True, False). Für `graphml` nun mit dem Parameter `selection=True` möglich

## `ValueError`

Es werden folgende Merkmale geprüft und Fehlern gemeldet, wenn:
- ein Identifikator `EntityId` (GND-Datendump) fehlt
- ein Name `EntityId` (GND-Datendump) fehlt
- ein veralteter Identifikator `EntityId` in Relationen vorkommt
- ein Identifikator `ResourceId` (DNB- und ZDB-Datendump) fehlt
- ein Titel `ResourceTitle` (DNB- und ZDB-Datendump) fehlt

```python
ValueError: old EntityId (DE-588)106900749 found in ResourceUri - http://d-nb.info/458721212
```

## `CodeError`

Es werden auch vordefinierte Codes geprüft:
- [gndgen](https://wiki.dnb.de/display/ILTIS/Informationsseite+zur+GND?preview=/90411323/149487812/entitaetenSatztypen.pdf) `EntityGenType`
- [gndspec](https://wiki.dnb.de/display/ILTIS/Informationsseite+zur+GND?preview=/90411323/148701892/entitaetenCodes.pdf) `EntitySpecType`
- [Ländercodes](https://wiki.dnb.de/display/ILTIS/Informationsseite+zur+GND?preview=/90411323/160151404/02-laendercodes_2020-01-28_alph.pdf) nach ISO-3166 `GeoArea`
- Elemente aus der [GND-Ontologie](https://d-nb.info/standards/elementset/gnd) `RelationGndType`


## `TypeError` (z.Z. ausgeklammert in Code)

- wiederholbare/nicht wiederholbare Felder/Unterfelder
