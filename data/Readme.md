# Hier werden transformierte Daten gespeichert

# Unten gibt es Bespiele für Ausgansgformate Version 2019 (GraphML, JSON)

### Beispiel für ein Record transformiert zu JSON
#### mit Parametern outputFormat="json", dataSelection=True

```gfm
{
    "CorpDateApprox": "",
    "CorpDateStrict": "",
    "CorpInfo": [],
    "EntityGenType": "b",
    "EntityId": "(DE-588)5048734-6",
    "EntityName": "Deutsches Forschungszentrum für Künstliche Intelligenz",
    "EntityOldId": [
        "(DE-588)1088215157",
        "(DE-588)6526229-3"
    ],
    "EntitySpecType": [
        "kiz"
    ],
    "EntityType": "CorpName",
    "EntityUri": "http://d-nb.info/gnd/5048734-6",
    "EntityVariantName": [
        "Deutsches Forschungszentrum für Künstliche Intelligenz GmbH",
        "DFKI",
        "DFKI GmbH",
        "Forschungszentrum für Künstliche Intelligenz",
        "German Research Center for Artificial Intelligence",
        "German Research Center for Artificial Intelligence GmbH",
        "Research Center for Artificial Intelligence",
        "Deutsches Forschungszentrum für Künstliche Intelligenz",
        "Universität des Saarlandes",
        "German Research Center for Artificial Intelligence",
        "Universität des Saarlandes",
        "Forschungszentrum für Künstliche Intelligenz",
        "Universität des Saarlandes"
    ],
    "RelationList": [
        {
            "EntityId": "1988-",
            "RelationGndType": "dateOfEstablishment",
            "RelationSource": "GND",
            "RelationTempValidity": "",
            "RelationType": "RelationToChronTerm",
            "RelationTypeAddInfo": ""
        },
        {
            "EntityId": "(DE-588)4029261-7",
            "RelationGndType": "placeOfBusiness",
            "RelationSource": "GND",
            "RelationTempValidity": "",
            "RelationType": "RelationToGeoName",
            "RelationTypeAddInfo": ""
        },
        {
            "EntityId": "(DE-588)4076912-4",
            "RelationGndType": "placeOfBusiness",
            "RelationSource": "GND",
            "RelationTempValidity": "",
            "RelationType": "RelationToGeoName",
            "RelationTypeAddInfo": ""
        },
        {
            "EntityId": "(DE-588)4008135-7",
            "RelationGndType": "placeOfBusiness",
            "RelationSource": "GND",
            "RelationTempValidity": "",
            "RelationType": "RelationToGeoName",
            "RelationTypeAddInfo": ""
        },
        {
            "EntityId": "(DE-588)4005728-8",
            "RelationGndType": "placeOfBusiness",
            "RelationSource": "GND",
            "RelationTempValidity": "",
            "RelationType": "RelationToGeoName",
            "RelationTypeAddInfo": ""
        }
    ]
}
```

### Beispiel für Knoten und Kanten transformierten zu GRAPHML
#### mit Parametern outputFormat="graphml", dataSelection=True
```xml
...
<node id="Aut5036103_X" labels=":CorpName">
    <data key="labels">:CorpName</data>
    <data key="CorpDateApprox"></data>
    <data key="CorpDateStrict"></data>
    <data key="CorpInfo"></data>
    <data key="EntityGenType">b</data>
    <data key="EntityId">(DE-588)5036103-X</data>
    <data key="EntityName">Staatsbibliothek zu Berlin</data>
    <data key="EntityOldId">(DE-588)1086254929;;;
                            (DE-588)108610434X;;;
                            (DE-588)4069301-6;;;
                            (DE-588)16319300-9;;;
                            (DE-588)16270567-0</data>
    <data key="EntitySpecType">kiz</data>
    <data key="EntityType">CorpName</data>
    <data key="EntityUri">http://d-nb.info/gnd/5036103-X</data>
    <data key="EntityVariantName">Staatsbibliothek zu Berlin - Preußischer Kulturbesitz;;;
                                  Staatsbibliothek zu Berlin - PK;;;
                                  Staatsbibliothek Preußischer Kulturbesitz;;;
                                  Stiftung Preußischer Kulturbesitz;;;
                                  Gosudarstvennaja Biblioteka;;;
                                  Biblioteka Państwowa;;;
                                  State Library at Berlin;;;
                                  Stiftung Preußischer Kulturbesitz;;;
                                  SBB-PK;;;
                                  Stiftung Preußischer Kulturbesitz;;;
                                  Gosudarstvennaja Biblioteka v Berline - Prusskoe Kulʹturnoe Nasledie;;;
                                  Biblioteka Państwowa w Berlinie - Dziedzictwo Kultury Pruskiej;;;
                                  State Library at Berlin - Prussian Cultural Heritage Foundation;;;
                                  Stabi;;;
                                  SBB;;;
                                  Staatsbibliothek;;;
                                  Berliner Staatsbibliothek</data>
</node>
<node id="AutChronTerm01Dot01Dot1992To" labels=":ChronTerm">
    <data key="labels">:ChronTerm</data>
    <data key="EntityName">01.01.1992-</data>
</node>
<edge id="FromAut5036103_XToAut1011349_6" 
      source="Aut5036103_X"
      target="Aut1011349_6"
      label="RelationToCorpName">
    <data key="label">RelationToCorpName</data>
    <data key="RelationSource">GND</data>
    <data key="RelationGndType">precedingCorporateBody</data>
    <data key="RelationTypeAddInfo"></data>
    <data key="RelationTempValidity"></data>
</edge>
<edge id="FromAut5036103_XToAut1011355_1"
      source="Aut5036103_X"
      target="Aut1011355_1"
      label="RelationToCorpName">
    <data key="label">RelationToCorpName</data>
    <data key="RelationSource">GND</data>
    <data key="RelationGndType">precedingCorporateBody</data>
    <data key="RelationTypeAddInfo"></data>
    <data key="RelationTempValidity"></data>
</edge>
<edge id="FromAut5036103_XToAut35353_X"
      source="Aut5036103_X"
      target="Aut35353_X"
      label="RelationToCorpName">
    <data key="label">RelationToCorpName</data>
    <data key="RelationSource">GND</data>
    <data key="RelationGndType">hierarchicalSuperiorOfTheCorporateBody</data>
    <data key="RelationTypeAddInfo"></data>
    <data key="RelationTempValidity"></data>
</edge>
<edge id="FromAut5036103_XToAut1073559289"
      source="Aut5036103_X"
      target="Aut1073559289"
      label="RelationToUniTitle">
    <data key="label">RelationToUniTitle</data>
    <data key="RelationSource">GND</data>
    <data key="RelationGndType">relatedWork</data>
    <data key="RelationTypeAddInfo"></data>
    <data key="RelationTempValidity"></data>
</edge>
<edge id="FromAut5036103_XToAut1194892531"
      source="Aut5036103_X"
      target="Aut1194892531"
      label="RelationToUniTitle">
    <data key="label">RelationToUniTitle</data>
    <data key="RelationSource">GND</data>
    <data key="RelationGndType">relatedWork</data>
    <data key="RelationTypeAddInfo"></data>
    <data key="RelationTempValidity"></data>
</edge>
<edge id="FromAut5036103_XToAut1193154553"
      source="Aut5036103_X"
      target="Aut1193154553"
      label="RelationToUniTitle">
    <data key="label">RelationToUniTitle</data>
    <data key="RelationSource">GND</data>
    <data key="RelationGndType">relatedWork</data>
    <data key="RelationTypeAddInfo"></data>
    <data key="RelationTempValidity"></data>
</edge>
<edge id="FromAut5036103_XToAut119320786X"
      source="Aut5036103_X"
      target="Aut119320786X"
      label="RelationToUniTitle">
    <data key="label">RelationToUniTitle</data>
    <data key="RelationSource">GND</data>
    <data key="RelationGndType">relatedWork</data>
    <data key="RelationTypeAddInfo"></data>
    <data key="RelationTempValidity"></data>
</edge>
<edge id="FromAut5036103_XToAutAutChronTerm01Dot01Dot1992To"
      source="Aut5036103_X"
      target="AutAutChronTerm01Dot01Dot1992To"
      label="RelationToChronTerm">
    <data key="label">RelationToChronTerm</data>
    <data key="RelationSource">GND</data>
    <data key="RelationGndType">dateOfEstablishment</data>
    <data key="RelationTypeAddInfo"></data>
    <data key="RelationTempValidity"></data>
</edge>
<edge id="FromAut5036103_XToAut4066573_2"
      source="Aut5036103_X"
      target="Aut4066573_2"
      label="RelationToTopicTerm">
    <data key="label">RelationToTopicTerm</data>
    <data key="RelationSource">GND</data>
    <data key="RelationGndType">broaderTermInstantial</data>
    <data key="RelationTypeAddInfo"></data>
    <data key="RelationTempValidity"></data>
</edge>
<edge id="FromAut5036103_XToAut4005728_8"
      source="Aut5036103_X"
      target="Aut4005728_8"
      label="RelationToGeoName">
    <data key="label">RelationToGeoName</data>
    <data key="RelationSource">GND</data>
    <data key="RelationGndType">placeOfBusiness</data>
    <data key="RelationTypeAddInfo"></data>
    <data key="RelationTempValidity"></data>
</edge>
<edge id="FromAut5036103_XToAut4005728_8"
      source="Aut5036103_X"
      target="Aut4005728_8"
      label="RelationToGeoName">
    <data key="label">RelationToGeoName</data>
    <data key="RelationSource">GND</data>
    <data key="RelationGndType">spatialAreaOfActivity</data>
    <data key="RelationTypeAddInfo"></data>
    <data key="RelationTempValidity"></data>
</edge>
...
```


### Beispiel für ein Record transformiert zu JSON
#### mit Parametern outputFormat="json", dataSelection=False

```gfm
{
    "001": "010000941",
    "003": "DE-101",
    "005": "20181220003241.0",
    "007": "tu",
    "008": "991118d19501989gw u||p|  r|| 0||||1ger c",
    ...
    "035": [
        {
            "a": [
                "(DE-599)ZDB123-5"
            ],
            "ind1": " ",
            "ind2": " "
        },
        {
            "a": [
                "(OCoLC)231020543"
            ],
            "ind1": " ",
            "ind2": " "
        }
    ],
    ...
    "245": [
        {
            "a": [
                "Adressbuch deutscher Chemiker"
            ],
            "c": [
                "gemeinsam hrsg. von Ges. Deutscher Chemiker u. Verl. Chemie"
            ],
            "ind1": "0",
            "ind2": "0"
        }
    ],
    "264": [
        {
            "a": [
                "Weinheim, Bergstr."
            ],
            "b": [
                "Verl. Chemie"
            ],
            "c": [
                "1950-1989"
            ],
            "ind1": "3",
            "ind2": "1"
        }
    ],
    ...
    "610": [
        {
            "0": [
                "(DE-588)2012027-8",
                "http://d-nb.info/gnd/2012027-8",
                "(DE-101)004713532"
            ],
            "2": [
                "gnd"
            ],
            "a": [
                "Gesellschaft Deutscher Chemiker"
            ],
            "ind1": "2",
            "ind2": "7"
        }
    ],
    "650": [
        {
            "0": [
                "(DE-588)4170173-2",
                "http://d-nb.info/gnd/4170173-2",
                "(DE-101)041701739"
            ],
            "2": [
                "gnd"
            ],
            "a": [
                "Mitgliederverzeichnis"
            ],
            "ind1": " ",
            "ind2": "7"
        },
        {
            "0": [
                "(DE-588)4009836-9",
                "http://d-nb.info/gnd/4009836-9",
                "(DE-101)040098362"
            ],
            "2": [
                "gnd"
            ],
            "a": [
                "Chemiker"
            ],
            "ind1": " ",
            "ind2": "7"
        },
        {
            "0": [
                "(DE-588)4141451-2",
                "http://d-nb.info/gnd/4141451-2",
                "(DE-101)041414519"
            ],
            "2": [
                "gnd"
            ],
            "a": [
                "Adressbuch"
            ],
            "ind1": " ",
            "ind2": "7"
        }
    ],
    "651": [
        {
            "0": [
                "(DE-588)4011889-7",
                "http://d-nb.info/gnd/4011889-7",
                "(DE-101)040118894"
            ],
            "2": [
                "gnd"
            ],
            "a": [
                "Deutschland"
            ],
            "g": [
                "Bundesrepublik"
            ],
            "ind1": " ",
            "ind2": "7"
        },
        {
            "0": [
                "(DE-588)4011882-4",
                "http://d-nb.info/gnd/4011882-4",
                "(DE-101)040118827"
            ],
            "2": [
                "gnd"
            ],
            "a": [
                "Deutschland"
            ],
            "ind1": " ",
            "ind2": "7"
        }
    ],
    "655": [
        {
            "0": [
                "(DE-588)4067488-5",
                "http://d-nb.info/gnd/4067488-5",
                "(DE-101)040674886"
            ],
            "2": [
                "gnd-content"
            ],
            "a": [
                "Zeitschrift"
            ],
            "ind1": " ",
            "ind2": "7"
        },
        {
            "0": [
                "(DE-588)4188171-0",
                "http://d-nb.info/gnd/4188171-0",
                "(DE-101)041881710"
            ],
            "2": [
                "gnd-content"
            ],
            "a": [
                "Verzeichnis"
            ],
            "ind1": " ",
            "ind2": "7"
        },
        {
            "0": [
                "(DE-588)4141451-2",
                "http://d-nb.info/gnd/4141451-2",
                "(DE-101)041414519"
            ],
            "2": [
                "gnd-content"
            ],
            "a": [
                "Adressbuch"
            ],
            "ind1": " ",
            "ind2": "7"
        },
        {
            "2": [
                "gnd"
            ],
            "a": [
                "Adreßbuch"
            ],
            "ind1": " ",
            "ind2": "7"
        },
        {
            "2": [
                "gnd"
            ],
            "a": [
                "Adressbuch"
            ],
            "ind1": " ",
            "ind2": "7"
        }
    ],
    ...
```



### Beispiel für ein Record transformiert zu JSON
#### mit Parametern outputFormat="json", dataSelection=False
 
 ````gfm
{
    "ead": {
        "@schemaLocation": "urn:isbn:1-931666-22-9 http://www.loc.gov/ead/ead.xsd"
    },
    "ead/archdesc": {
        "@audience": "external",
        "@id": "DE-2498-BF00012800",
        "@level": "collection"
    },
    ...
    "ead/archdesc/controlaccess/genreform": {
        "text": "Nachlaß"
    },
    "ead/archdesc/controlaccess/head": {
        "text": "Gattung"
    },
    ...
    "ead/archdesc/did/origination/persname": {
        "@authfilenumber": "118615483",
        "@normal": "Sommer, Ernst",
        "@role": "Bestandsbildner",
        "@source": "GND",
        "text": "Sommer, Ernst (1889-1955)"
    },
    ...
    "ead/archdesc/did/repository/corpname": {
        "@authfilenumber": "DE-2498",
        "@role": "Bestandshaltende Institution",
        "@source": "ISIL",
        "text": "Deutsches Literaturarchiv Marbach, Archiv [Handschriftensammlung]"
    },
    "ead/archdesc/did/unitid": {
        "@label": "Signatur",
        "@repositorycode": "DE-2498",
        "text": "A:Sommer"
    },
    "ead/archdesc/did/unittitle": {
        "@label": "Titel",
        "text": "A:Sommer - [Bestand, Nachlaß]"
    },
    "ead/archdesc/dsc/c": {
        "@audience": "external",
        "@id": "DE-2498-BF00038791",
        "@level": "class"
    },
    ...
    "ead/archdesc/dsc/c/c": {
        "@audience": "external",
        "@id": "DE-2498-HS00910017",
        "@level": "item"
    },
    ...
    "ead/archdesc/dsc/c/c/controlaccess/genreform": {
        "text": "Prosa"
    },
    "ead/archdesc/dsc/c/c/controlaccess/head": {
        "text": "Gattungen"
    },
    "ead/archdesc/dsc/c/c/controlaccess/persname": {
        "@authfilenumber": "118615483",
        "@normal": "Sommer, Ernst",
        "@role": "Verfasser",
        "@source": "GND",
        "text": "Sommer, Ernst (1889-1955)"
    },
    "ead/archdesc/dsc/c/c/did/dao": {
        "@actuate": "onLoad",
        "@href": "http://www.dla-marbach.de/kallias/aDISWeb/hs/index.html?ADISDB=HS&WEB=JA&ADISOI=00910017",
        "@show": "replace",
        "@title": "Katalogeintrag im OPAC des DLA",
        "@type": "simple"
    },
    "ead/archdesc/dsc/c/c/did/langmaterial/language": {
        "@langcode": "ger",
        "text": "deutsch"
    },
    ...
    "ead/archdesc/dsc/c/c/did/unittitle": {
        "@label": "Titel von Bearbeiter/in",
        "text": "6 Erzählungen (Prosa)"
    },
    "ead/archdesc/dsc/c/controlaccess/genreform": {
        "text": "Standortkonvolut"
    },
    ...
    "ead/archdesc/dsc/c/did/origination/persname": {
        "@authfilenumber": "118615483",
        "@normal": "Sommer, Ernst",
        "@role": "Bestandsbildner",
        "@source": "GND",
        "text": "Sommer, Ernst (1889-1955)"
    },
    "ead/archdesc/dsc/c/did/repository/corpname": {
        "@role": "Bestandshaltende Institution",
        "text": "Deutsches Literaturarchiv Marbach, Archiv [Handschriftensammlung]"
    },
    "ead/archdesc/dsc/c/did/unitid": {
        "@label": "Signatur",
        "@repositorycode": "DE-2498",
        "text": "A:Sommer/Kopien"
    },
    "ead/archdesc/dsc/c/did/unittitle": {
        "@label": "Titel",
        "text": "A:Sommer/Kopien - [Standortkonvolut]"
    },
    "ead/eadheader": {
        "@audience": "external",
        "@countryencoding": "iso3166-1",
        "@dateencoding": "iso8601",
        "@langencoding": "iso639-2b",
        "@repositoryencoding": "iso15511",
        "@scriptencoding": "iso15924"
    },
    "ead/eadheader/eadid": {
        "@countrycode": "DE",
        "@mainagencycode": "DE-2498"
    },
    "ead/eadheader/filedesc/titlestmt/titleproper": {
        "text": "A:Sommer - [Bestand, Nachlaß]"
    }
},
...
```
