# Teil I. 
# Entitäten

1. `PerName` von der GND
1. `CorpName` von der GND
1. `MeetName` von der GND
1. `UniTitle` von der GND
1. `TopicTerm` von der GND
1. `GeoName` von der GND
1. `ChronTerm` von der GND (aus Relationen)
1. `IsilTerm` von einer Liste mit ISILs
1. `Resource` von der DNB, ZDB, KPE, SBB


## 1. Entitäten GND

### 1.1. Allgemeine Merkmale
1. Identifikator (ISIL DE-588) `Id`
1. gelöschte Identifikatoren `OldId`
1. URI `Uri`
1. Weiterer Identifikator `id` Anmerkung: Nicht immer vorhanden, Identifikatoren sollten im nächsten Datenmodell überarbeitet werden. Da `id` nicht immer vorhanden, besser `Id` wählen für Abfragen.
1. Entitätentyp ([gndgen](https://wiki.dnb.de/display/ILTIS/Informationsseite+zur+GND?preview=/90411323/149487812/entitaetenSatztypen.pdf)) `GenType`
1. Entitätentyp ([gndspec](https://wiki.dnb.de/display/ILTIS/Informationsseite+zur+GND?preview=/90411323/148701892/entitaetenCodes.pdf)) `SpecType`
1. Entitätenname `Name`
1. Andere Entitätennamen `VariantName`

### 1.2. Spezifische Merkmale
#### 1.2.1. Personen `PerName`
   - Geschlecht	`Gender`
   - Lebensdaten	`DateApprox`
   - Anfangsdatum	`DateApproxBegin`
   - Enddatum	`DateApproxEnd`
   - exakte Lebensdaten	`DateStrict`
   - exaktes Anfangsdatum	`DateStrictBegin`
   - exaktes Enddatum	`DateStrictEnd`
#### 1.2.2. Körperschaften `CorpName`
   - Untergeordnete Körperschaft	`SubUnit`
   - Sonstige Informationen	`Info`
   - Entstehungsdaten	`DateApprox`
   - Anfangsdatum	`DateApproxBegin`
   - Enddatum	`DateApproxEnd`
   - exakte Entstehungsdaten	`DateStrict`
   - exaktes Anfangsdatum	`DateStrictBegin`
   - exaktes Enddatum	`DateStrictEnd`
#### 1.2.3. Kongresse `MeetName`
   - Ort des Kongresses	`Place`
   - Datum des Kongresses	`DateApprox`
   - Anfangsdatum des Kongresses	`DateApproxBegin`
   - Enddatum des Kongresses	`DateApproxEnd`
   - exaktes Datum des Kongresses	`DateStrict`
   - exaktes Anfangsdatum des Kongresses	`DateStrictBegin`
   - exaktes Enddatum des Kongresses	`DateStrictEnd`
   - Untergeordnete Einheit `SubUnit`
   - Sonstige Informationen `Info`
#### 1.2.4. Werke `UniTitle`
   - Beachte: Titel	`Name`
   - Verfasser/Urheber	`Creator`
   - insgesamt vier Merkmale für das Erscheinungsdatum möglich (sollte für das nächste Datenmodell anders gelöst werden):
	   - `DateApproxBegin`
	   - `DateApproxEnd`
	   - `DateStrictBegin` Anmerkung: Nur ein Werk besitzt dieses Merkmal
	   - `DateOriginal`
   - Medium	`Medium`
   - Sprache eines Werkes	`Lang`
#### 1.2.5. Sachbegriffe	`TopicTerm`
   - Sonstige Informationen	`Info`
   - Allgemeine Unterteilung	`GenSubdiv`
#### 1.2.6. Geografika `GeoName`
   - Sonstige Informationen	`Info`
   - Allgemeine Unterteilung	`GenSubdiv`
   - Code für geografische Gebiete	`GeoArea`
   - Koordinaten	`Coordinates`
   - Verknüpfung zu GeoNames	`IdGeonames`
#### 1.2.7. Zeitausdrücke `ChronTerm`
   - Zeitausdruck	`Name`
#### 1.2.8. ISIL-Einrichtungen` IsilTerm`
   - Einrichtung	`Name`

## 2. Ressourcen DNB, ZDB, SBB, KPE	

### 2.1. Allgemeine Merkmale
1. Identifikator (ISIL DE-611, DE-101, DE-599 ...)	`Id`
1. Titel	`Name`
1. Bestandsbildner (Person, Körperschaft)	`Creator`	
1. Erscheinungsjahr (-verlauf)	`Date`
1. Erscheinungsort	`Place`
1. Sprache	`Lang`
1. Gattung	`Genre`
1. Link zur Ressource	`Uri`

# Teil II
# Relationen
 1. `RelationToPerName`
 2.  `RelationToCorpName`
 3.  `RelationToMeetName`
 4.  `RelationToUniTitle`
 5. `RelationToTopicTerm`
 6.  `RelationToGeoName`
 7.  `RelationToChronTerm`
 8.  `RelationToIsilTerm`
 9.  `RelationToResource`
 10. `SocialRelation`
## 1. Explizite Relationen
### 1.1. Allgemeine Merkmale : 
1. Quelle einer Relation `Source` (entspricht der Ausgangsdaten)
	 - GND
	 - ZDB
	 - DNB (ZDB-Dubletten ausgefiltert)
	 - SBB (ggf. mit Dubletten aus der DNB)
	 - KPE
1. Relationentyp `SourceType`, der in Quelldaten entsprechend klassifiziert wird. Dazu zählt man folgende Typen:
	 - im GND-Datendump sind es Typen aus der [GND-Ontologie](https://d-nb.info/standards/elementset/gnd)
	 - im DNB-,ZDB- und SBB-Datendump (Format MARC21) sind es mit Codes verschlüsselte Typen, genannt [Relators](http://www.loc.gov/marc/relators/relacode.html), die für Relationen zu der GND-Entitäten typisch sind. Für Relationen zu Ressourcen sind je nach Datenfeld `SupplementToMainTitle`, `MainTitleToSupplement`, `LangVariant`, `ManifestLevel`, `Predecessor`, `Successor` vordefiniert.
	 - im KPE-Datendump sind es LevelToLevel-Typen, also `CollectionToClass`, `ClassToClass`, `ClassToItem` etc., die automatisch generiert werden.


### 1.2. Spezifische Merkmale : 
#### 1.2.1. DNB, ZDB, SBB (Format MARC21)
1. Zusätzliche Information zu einer Relation `TypeAddInfo`:
	 - im GND-Datendump sind es zusätzliche Information bezüglich Relationen aus dem Unterfeld `9v:`
	 - im DNB- und ZDB-Datendump sind es Beziehungskennzeichen aus dem Unterfeld `a` oder Beziehungsart bezüglich eines fortlaufenden Sammelwerks aus dem Unterfeld `i`
2. Zeitliche Gültigkeit einer Relationen `TypeValidity`
	 - im GND-Datendump sind es zeitliche Gültigkeit der Relationen aus dem Unterfeld `9Z:`
	 - im DNB- und ZDB-Datendump sind es sind es zeitliche Gültigkeit der Relationen je nach Datenfeld aus den Unterfeldern `b` oder `n`

 
## 2. Implizite Relationen (soziale Relation `SocialRelation` genannt)
### 2.1. Allgemeine Merkmale
1. `Source` = Identifikator der Quelle
2. `SourceType` = associatedRelation, areCoAuthors, areCoEditors, affiliatedRelation, correspondedRelation, knows
3. `TypeAddInfo` = undirected, directed
### 2.2. Detaillierte Darstellung der Merkmale je nach Regel (DRAFT)
| Nr. | Regel                                 | Quelle      | `Source` | `SourceType`              | `TypeAddInfo`           |
|-----|---------------------------------------|-------------|----------|---------------------------|-------------------------|
| 1   | „Folgerung“ sozialer Beziehungen      | MARC21, EAD | ID       | associatedRelation        | undirected              |
| 2   | Co-Autoren                            | MARC21      | ID       | areCoAuthors              | undirected              |
| 3   | Co-Herausgeber                        | MARC21      | ID       | areCoEditors              | undirected              |
| 4   | Affiliationen                         | EAD         | ID       | affiliatedRelation        | undirected              |
| 5   | Korrespondenzen                       | EAD         | ID       | correspondedRelation      | directed                |
| 6   | Tagebücher                            | EAD         | ID       | knows                     | undirected ~~directed~~ |
| 7   | Stammbücher / Stammbucheintrag, Alben | EAD         | ID       | knows                     | undirected              |
| 8   | Protokolle                            | EAD         | ID       | associatedRelation\|knows | undirected              |
| 9   | Archivbestände / Findbücher           | EAD         | ID       | associatedRelation\|knows | undirected              |

# Datenmodell

![](https://trello-attachments.s3.amazonaws.com/5d25058e9162b567b860149f/5e3c13bb607286561cc56f57/bdfd88869d7f3edeafc6b2c102caffc4/UmlModel.svg)

# Teil III. Volltexte
Onedrive Dokumentation (detaillierter, mehr Kommentare + Beispiele): https://1drv.ms/w/s!AsnDx7PkKZE7iGHyfxYvQnXUC-5z?e=K0OwXs 

## Übersicht erweitertes Datenmodell
- neue Entitäten: OCRDocument, WikiName
- neue Relationen: DocContainsEnt (OCRDocument → WikiName), SameAs (PerName ↔ WikiName; CorpName ↔ WikiName; GeoName ↔ WikiName)

## Entitäten
### OCRDocument
- id: “OCR” + Zdb Id + Date of Issue. Beispiel:  OCR1161410918821002 
- labels: “OCRDocument” 
- IdZDB: Entspricht der Zdb Id. Beispiel: 11614109 
- Name: Entspricht dem Dateinamen (ohne “.tsv”) 
- DateStrictBegin: Beispiel: 12.01.1975 
- DateApproxBegin: Beispiel: 1975 
- issue: (0 = morning issue, 1 = evening issue etc., Default = 0) 
- page: Seiten/Bild Nr. 
- article: Id des Artikels (nicht verwendet, Default = 0) 
- version: nicht verwendet, Default = 0 
- url: URL. Beispiel: https://content.staatsbibliothek-berlin.de/zefys/SNP11614109-18821002-0-1-0-0/full/full/0/default.jpg  

### WikiName
- id: “Wiki_“ + Wikidata Id. Beispiel: Wiki_Q20775499  
- labels: “WikiName“ 
- IdWikidata: Beispiel: Q20775499 
- IdGND: GND Id (falls Verlinkung bei Wikidata vorhanden) 
- Name: Name der Entität 
- Type: Entspricht dem Entitätstypen (PER; ORG; LOC) 

Wikidata Merkmale

- WdDateApproxBegin: Beispiel: 1893 
- WdDateStrictBegin: Beispiel: 01.01.1893 
- WdDateApproxOriginal: Beispiel: 1893-1976 
- WdDateStrictOriginal: Beispiel: 01.01.1893-01.01.1976 
- WdDateApproxEnd: Beispiel: 1976 
- WdDateStrictEnd: Beispiel: 01.01.1976 
- WdGender: Wert entweder 0 (weiblich) oder 1 (männlich)  
- WdPlaceOfBirth: Geburtsort Name 
- WdPlaceOfBirthId: Geburtsort Wikidata Id 
- WdPlaceOfDeath: Sterbeort Name 
- WdPlaceOfDeathId: Sterbeort Wikidata Id 

## Relationen
### DocContainsEnt
- id: “FromOCR” + OCRDocument Id + “ToWiki” + Entitätstyp + “_” + Wikidata Id + Nr. der Kante. Beispiel: FromOCR1161410918821002ToWikiORG_Q694714_1 
- label: “DocContainsEnt“ 
- source: Id des OCRDocuments, welches die Entität enthält. 
- target: Id der Entität WikiName 
- TypeAddInfo: “directed” (Gerichtete Relation) 
- Sent: indicates the sentence position (≥1, 0 marks sentence boundaries) 
- Name: Entspricht dem Namen der gefundenen Entität 
- Emb: contains the embedded entity label (BIO chunking) 
- (url: Entitätenspezifischer Url, hier werden die Koordinaten der Entität in den Url eingesetzt: https://content.staatsbibliothek-berlin.de/zefys/SNP11614109-18821002-0-1-0-0/382,746,1046,1104/full/0/default.jpg ) Anmerkung: Wird nur hinzugefügt, falls gewünscht (Stand 23.08.2021)

### SameAs
- id: “From” + GND Id + “ToWiki” + Entitätstyp +“_” + Wikidata Id. Beispiel: From(DE-588)4005728-8ToWikiLOC_Q64  
- label: “SameAs” 
- source: Id zum Source Node 
- target: Id zum Target Node  
- TypeAddInfo: “undirected” (= Die Relation ist ungerichtet) 

# Teil IV. Anpassung des Datenmodells
## 1. Entitätenspezifische Bezeichnungen ändern (Version 10.07.2020)
Entitätenspezifische Bezeichnungen der Merkmale auf allgemeine Bezeichnungen ändern. Statt `EntityUri`|`ResourceUri` Merkmal `Uri` benutzen etc (dokumentiert in [Arbeitspakete 03 > AP1 - Datenmodellierung](https://1drv.ms/x/s!AsnDx7PkKZE7h2kGMjcITS4INXGX?e=e6Pw6R));
## 2. Koordinaten für Geographika hinzufügen (Version 10.07.2020)
Für Entitäten `GeoName` wurde Merkmal `Coordinates` (z.B. N 52°28′00″ E 13°21′00″) hinzugefügt. Zusätzlich wurde es das Merkmal `UriGeonames` hinzugefügt, die Geographika mit dem Referenzsystem Geonames verbindet.
## 3. Akademische Grade (Version 10.07.2020)
Keine einheitliche Einstellung der Partner zu diesem Anpassungswunsch. Das Merkmal wurde nicht hinzugefügt (Stand 17.11.2020). 
## 4. Gesamtpfad für Kalliope-Ressourcen hinzufügen (Version 10.07.2020, 10.12.2020)
Die Darstellung vom Gesamtpfad für Kalliope-Ressourcen wurde als Merkmal `SourcePath` (CH-000015-0-1051777|CH-000015-0-1051786|CH-000015-0-1054519) hinzufügt. 
## 5. Zeitintervalle trennen (Version 10.07.2020, 10.12.2020)
Zeitintervalle wurden z.B. in zwei Merkmale `DateApproxBeginn`=„1931“ und `DateApproxEnd`=„1987“ getrennt. Einige Entitäten besitzen mehrere Zeitausdrücke, so wurde es nicht möglich, Anfang und Ende eines Datums entsprechend einzuordnen. Das Merkmal `DateOriginal` wurde wieder hinzugefügt.
## 6. Zeitausdrücke normalisieren (Version 10.07.2020)
Zeitausdrücke unterscheiden sich in EAD und MARC21, vgl. 1837-11-12 und 1923-06-02/1923-06-05 aus EAD, 1963-1975 und 00.03.1895- aus MARC21. Nicht normalisiert wurden solche Zeitausdrücke, die nicht nach Richtlinien MARC21, EAD zur Beschreibung der Zeitausdrücken aufgefasst wurden. Offene Intervalle wurden ggf. bei `DateApproxBeginn` bzw. `DateApproxEnd` mit „“ besetzt.
## 7. Schlagworte für Ressourcen übernehmen (Version 10.07.2020)
Schlagworte wurden folgend aufgenommen (s. [MARC21Codes.py](https://github.com/sonar-idh/Transformer/blob/main/src/MARC21Codes.py)):
```
{...'600': ['RelationToPerName', 'SubjectAddedEntry'],
'610': ['RelationToCorpName', 'SubjectAddedEntry'],
'611': ['RelationToMeetName', 'SubjectAddedEntry'],
'630': ['RelationToUniTitle', 'SubjectAddedEntry'],
'650': ['RelationToTopicTerm', 'SubjectAddedEntry'],
'651': ['RelationToGeoName', 'SubjectAddedEntry'],...}
```
Der Key deutet auf ein MARC21-Feld. Das erste Value ist ein Label für Relation, das zweite ist ein `SourceType`.
## 8. Genderspezifische Berufe vereinen (Version 10.07.2020)
TODO über Server
## 9.  GND mit anderen Referenzsystemen verbinden (Version 10.07.2020)
TODO über Server
## 10. Angaben in `Source` bei `SocialRelations` (Version 10.12.2020)
Statt `computed` wurde eine ID zu der Quelle hinzugefügt, woraus die Beziehung abgeleitet wurde.
## Zettelkasten
Gelöst durch folgende Änderung:

Die Liste der Rollenattribute wurde erweitert: Wenn "dokumentiert", "behandelt", "nicht-definiert", "Behandelt", "Erwähnt", "Erwähnte Person", "Behandelte Person", "Erwähnte Körperschaft", "Behandelte Körperschaft" vorkommt, wird keine Beziehung erstellt. 

# Teil V. Tippfehler
- ~~Merkmal `DateStrictEnd` und `DatestrictEnd`~~
- ~~`SourceTyp` und `SourceType`~~
- immer noch `Title` statt `Name` bei EAD. Warum?
- R6 `undirected`




