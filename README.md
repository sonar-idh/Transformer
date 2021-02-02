# Transformer

# Transformation MARC21 

**Eingabeformat**: MARC21

**Ausgabeformat**: JSON, GRAPHML

**Optionen**: 
- `dataType={'Authority', 'Bibliographic'}`. Der Datentyp `'Authority'` entspricht Normdaten, der Datentyp `'Bibliographic'` - Metadaten;
 - `dataType='Authority'` ist in Kombination mit `entityType={"PerName", "CorpName", "MeetName", "UniTitle", "TopicTerm", "GeoName"}` möglich; 
  - `dataType='Bibliographic'` ist in Kombination mit `entityType={"Zdb", "Dnb1", "Dnb2", "Dnb3", "Dnb4"}` möglich;
- `entityType={"PerName", "CorpName", "MeetName", "UniTitle", "TopicTerm", "GeoName", "Zdb", "Dnb1", "Dnb2", "Dnb3", "Dnb4"}`;
- `dataSelection={True, False}`;
- `outputFormat={"json", "graphml"}`: 
 - `outputFormat="graphml"` ist nur in Kombination mit `dataSelection=True` möglich

## Duplikate aus der GND und ZDB

 **Gilt für Transformation zu GRAPHML**

Gleiche Ressourcen (bezüglich Identifikatoren), die in der DNB und ZDB vorkommen, sind zusammen verbunden.

![](https://trello-attachments.s3.amazonaws.com/5e3c13bb607286561cc56f57/928x823/f3c06046ede30c6b3d679892fbc8e639/Anmerkung_2020-02-06_162043.png?raw=true)


## Konsistenzprüfung

Es gibt Fehlermeldungen, die in `errors...` geschrieben werden, wenn folgende Inkonsistenzen gefunden werden:
- 1. Felder mit fehlenden Identifikatoren, Namen oder Titeln;
- 2. Invalide Codes;
- 3. Veraltete Identifikatoren in Feldern 5XX.

### 1. Prüfung der Felder mit Identifikatoren, Namen und Titel
Es wird geprüft, ob es für einen Record Informationen zu Identifikator, Namen bzw. Titel existieren. Meldungen werden in `errors...` gespeichert, Datensätze bei der Transformation werden nicht geändert.


```xml
    <datafield tag="110" ind1="2" ind2=" ">
      <subfield code="b">Saint-Avold en Moselle</subfield>
    </datafield>
```

### 2. Prüfung wiederholender Felder mit gleicher Information
In Daten können sich sowohl Unterfelder, als auch Felder komplett wiederholen. Dies betrifft einen Unterfeld mit der Code "g" im folgenden Beispiel, der zweimal vorkommt:

```xml
    <datafield tag="551" ind1=" " ind2=" ">
      <subfield code="0">(DE-101)042567238</subfield>
      <subfield code="0">(DE-588)4256723-3</subfield>
      <subfield code="0">https://d-nb.info/gnd/4256723-3</subfield>
      <subfield code="a">Langer Gang</subfield>
      <subfield code="g">Dresden</subfield> <!-------Vorkommen Nr. 1----->
      <subfield code="g">Dresden</subfield> <!-------Vorkommen Nr. 2----->
      <subfield code="4">ortb</subfield>
      <subfield code="4">https://d-nb.info/standards/elementset/gnd#placeOfCustody</subfield>
      <subfield code="w">r</subfield>
      <subfield code="i">Aufbewahrungsort</subfield>
    </datafield>
```
Im nächsten Beispiel kommt ein Feld 400 zweimal, wobei unterschiedliche Unterfelder mit entsprechenden Codes sowie beide Indikatoren gleiche Information enthalten. Dies betrifft eine Person mit dem Vornamen (ind1="0") "Xenophon" (code="a"), Datumsangaben "ca. 430 v.Chr.-354 v. Chr." (code="d"), einen Titel "Athēnaiōn politeia" (code="t").

```xml
   ...
   <!-------Vorkommen Nr. 1---------------------------------->
    <datafield tag="400" ind1="0" ind2=" ">
      <subfield code="a">Xenophon</subfield>
      <subfield code="d">ca. 430 v.Chr.-354 v. Chr.</subfield>
      <subfield code="t">Athēnaiōn politeia</subfield>
    </datafield>
    <!------------------------------------------------------->
    
    
    <datafield tag="400" ind1="0" ind2=" ">
      <subfield code="a">Xenophon</subfield>
      <subfield code="d">ca. 430 v.Chr.-354 v. Chr.</subfield>
      <subfield code="t">Staatsverfassung der Athener</subfield>
    </datafield>
    ...
    
    
    <!-------Vorkommen Nr. 2--------------------------------->
    <datafield tag="400" ind1="0" ind2=" "> 
      <subfield code="a">Xenophon</subfield>
      <subfield code="d">ca. 430 v.Chr.-354 v. Chr.</subfield>
      <subfield code="t">Athēnaiōn politeia</subfield>
    </datafield>
    <!------------------------------------------------------->
```
Repetitive Felder bei der Transformation zu JSON, GRAPHML werden ignoriert. Transformiert wird das erste Vorkommen. Letztes Bespiel sieht in JSON folgend aus:

```
[
	...,
	{
	    "a": [
	        "Xenophon"
	    ],
	    "d": [
	        "ca. 430 v.Chr.-354 v. Chr."
	    ],
	    "t": [
	        "Athēnaiōn politeia"
	    ],
	    "ind1": "0",
        "ind2": " "
	},
	{
	    "a": [
	        "Xenophon"
	    ],
	    "d": [
	        "ca. 430 v.Chr.-354 v. Chr."
	    ],
	    "t": [
	        "Staatsverfassung der Athener"
	    ],
	    "ind1": "0",
        "ind2": " "
	},
	...
]
```
### 3. Prüfung der Codes
Es werden folgende Codes geprüft und Meldungen über Fehler in `log` gespeichert. Codes in Daten werden **nicht geändert**!

- Satztypen der GND (gndgen)
- Untersatztypen der GND (gndspec)

```xml
    <datafield tag="075" ind1=" " ind2=" ">
      <subfield code="b">saw</subfield>
      <subfield code="2">gndspec</subfield>
    </datafield>
```
- Ländercodes nach ISO 3166
- GND-Codes für die Art der Beziehung (Entity)
- Codes für Relators (Resource)

### 4. Prüfung der Identifikatoren (mit ISIL DE-588) in Feldern 5XX

 **Gilt für Transformation zu GRAPHML**

Veraltete Identifikatoren, die in Feldern 5XX gefunden werden, werden bei der Transformation zu GRAPHML durch aktuelle Identifikatoren ersetzt. Relationen mit fehlenden, nicht eindeutigen Identifikatoren bzw. ohne Identifikatoren (wieder in Feldern 5XX) werden ignoriert, also keine Verknüpfungen zu in Feldern 1XX/245 beschriebenen Entitäten/Ressourcen hergestellt.


### a) Entitäten mit veralteten Identifikatoren (betrifft nur GND-Entitäten, kann man aber bei allen Quellen, wo Relationen beschrieben sind, finden)
Veraltete Identifikatoren werden durch aktuelle ersetzt, um entsprechende Entitäten/Ressourcen angemessen zu verknüpfen. Eine Liste der veralteten und neuen Identifikatoren findet man in `OldIds.py`.

### b) Entitäten aus fehlenden Tn-Datensätzen (Stand 2019-2020, Datendump 2021 hat keine Tn-Datensätze)
Es gibt 4.185.374 Datensätze in der GND, die in unseren Daten fehlen. Es geht um Tn-Datensätze (nur Namensansetzungen). Diese Daten sind für SoNAR, so GM, nicht bedeutend, da die Datensätze nicht eine Entität (Person), sondern einen Namen diverser Entitäten (Personen) beschreiben. Somit werden keine Verknüpfungen zu diesen Entitäten hergestellt. Ihre Ids findet man in `nonEntities.txt`.

### c) Entitäten mit nicht eindeutigen veralteten Identifikatoren
Via neo4j werden nicht eindeutige veralteten Identifikatoren gefunden, die zwei neuen Identifikatoren entsprechen. Sie werden zu `src/nonEntities.txt` hinzugefügt, weil ihre Zuordnung zu neuen Identifikatoren widersprüchlich ist.

- **Veraltete ID (neue ID1, neue ID2)**
- 122945662 (10211787X, 118693484)
- 1059225026 (1027146961, 1061213641)
-  4196845-1 (2086834-0, 2142242-4)
- 4100306-8 (2065029-2, 4549912-3)

### d) Entitäten ohne Identifikatoren
Bei der Transformation zu GRAPHML werden Relationen zu Entitäten ohne Identifikatoren ignoriert. Eine angemessene Zuordnung dieser Entitäten zu GND-Entitäten ist nun manuell möglich.


# Teil II. Transformation EAD 

**Eingabeformat**: EAD

**Ausgabeformat**: JSON, GRAPHML

**Optionen**: 
- `dataType={'Bibliographic'}`. Der Datentyp `'Authority'` entspricht Normdaten, der Datentyp `'Bibliographic'` - Metadaten;
 - ~~`dataType='Bibliographic'` ist in Kombination mit `entityType={"Kpe"}` möglich;~~ Wenn Transformation als eine Pipeline (zusammen mit Transformation MARC21) eingesetzt wird, dann kommt das Merkmal `entityType="Kpe"` ins Spiel
- `dataSelection={True, False}`;
- `outputFormat={"json", "graphml"}`: 
 - `outputFormat="graphml"` ist nur in Kombination mit `dataSelection=True` möglich
 
 
 ## Relationen zwischen verschiedenen Levels in der KPE
 
 **Gilt für Transformation zu GRAPHML**

![](https://trello-attachments.s3.amazonaws.com/5e3c13bb607286561cc56f57/1024x537/b61b37cd472034596609d7f2f8ee5391/animiertes-gif-von-online-umwandeln-de.gif?raw=true)

## Konsistenzprüfung

Es findet gleiche Konsistenzprüfung wie bei MARC21 statt. Es gibt Fehlermeldungen, die in `errors...` geschrieben werden, wenn folgende Inkonsistenzen gefunden werden:
- 1. Felder mit fehlenden Identifikatoren, Namen oder Titeln;
- 2. Veraltete Identifikatoren bei Relationen.

