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
   - Erscheinungsjahr	`Date`
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
1. `Source` = computed
2. `SourceType` = associatedRelation, areCoAuthors, areCoEditors, affiliatedRelation, correspondedRelation, knows
3. `SourceTypeAddInfo` = undirected, directed

![](https://trello-attachments.s3.amazonaws.com/5d25058e9162b567b860149f/5e3c13bb607286561cc56f57/bdfd88869d7f3edeafc6b2c102caffc4/UmlModel.svg)
