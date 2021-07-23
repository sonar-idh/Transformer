# -*- coding: utf-8 -*-
per_wd = { "DateOfDeath": "SELECT ?Todestag WHERE { wd:%s wdt:P570 ?Todestag}",
           "DateOfBirth": "SELECT ?Geburtsdatum WHERE { wd:%s wdt:P569 ?Geburtsdatum}",
           "Gender": 
                 """SELECT ?GeschlechtLabel WHERE { wd:%s wdt:P21 ?Geschlecht . 
                 SERVICE wikibase:label { 
                bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
                """,
           "PlaceOfBirthName":
               """SELECT ?GeburtsortLabel WHERE {wd:%s wdt:P19 ?Geburtsort .
               SERVICE wikibase:label { 
               bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}""",
           "PlaceOfDeathName": 
               """SELECT ?SterbeortLabel WHERE { wd:%s wdt:P20 ?Sterbeort .
               SERVICE wikibase:label { 
               bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}""",
              "PlaceOfBirth": "SELECT ?Geburtsort WHERE {wd:%s wdt:P19 ?Geburtsort}",
              "PlaceOfDeath": "SELECT ?Sterbeort WHERE { wd:%s wdt:P20 ?Sterbeort}",
            "professionOrOccupation": "SELECT ?Beruf WHERE { wd:%s wdt:P106 ?Beruf}"
         }

