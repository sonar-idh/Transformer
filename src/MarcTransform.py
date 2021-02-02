# coding: utf-8

import xml.etree.ElementTree as etree
import json
import time
import src.MARC21Codes as codes
import src.AllOldAuthorityIdentifier as oldIds
from src.ValidIsilTerms import val_isils

        
class MARC21:
    """Class für Transormation der daten aus MARC21"""

    def __init__(self, filecontent,
                 dataSelection=False,
                 entityType = 'PerName', 
                 dataType='Authority', 
                 outputFormat = 'graphml'): 
        
        """Transformiert Datensätze aus MARC21.
        Init-Funktion auf Basis von einem XML-Parser (xml.etree), der record-weise Daten bearbeitet,
        also alle bzw. ausgewählte Informationen aus Feldern und Unterfeldern zu einem Dictionary (hier Python-Datentyp)
        sammelt und zu GRAPHML oder JSON überträgt.

        :param filecontent: Inhalt der Eingagbedatei
        :type filecontent: streem?
        :param dataSelection: Parameter für Transformation von allen/ausgewählten Feldern/Unterfeldern
        :type dataSelection: Boolean
        :param entityType: Typ der Entität
        :type entityType: PerName, CorpName, MeetName, UniTitle, TopicTerm, GeoName, Zdb, Dnb1, Dnb2, Dnb3, Dnb4
        :param dataType: Typ des Datensatzes
        :type dataType: Authority, Bibliographic
        :param outputFormat: Ausgabeformat der transformierten Daten
        :type outputFormat: json, graphml
        
        :return: no value
        :rtype: none
        """
        
        
        # CHECK: Argumente prüfen
        # dataType
        if dataType not in ["Authority", "Bibliographic"]: 
            raise Exception('InputError: invalid data type "{}", valid data types are "Authority", "Bibliographic".'.format(dataType))
        # entityType    
        if dataType == "Authority" and entityType not in ["PerName", "CorpName", "MeetName", "UniTitle", "TopicTerm", "GeoName"]: 
            raise Exception('InputError: invalide entity type "{}", valid entity types are "PerName", "CorpName", "MeetName", "UniTitle", "TopicTerm", "GeoName".'.format(entityType))          
        if dataType == "Bibliographic" and entityType[:3] not in ["Zdb", "Dnb", "Sbb"]: 
            raise Exception('InputError: invalide resource type "{}", valid resource types are "Zdb", "Dnb1", "Dnb2", "Dnb3", "Dnb4", "Sbb".'.format(entityType))          
        # outputFormat
        if outputFormat not in ["json", "graphml"]: 
            raise Exception('InputError: invalid output format "{}", valid output formats are "json", "graphml".'.format(outputFormat))
        # outputFormat
        if not dataSelection and outputFormat == "graphml": 
            raise Exception('InputError: Transformation to graphml is possible only with selected data. Please set dataSelection=True.'.format(outputFormat))
            

        # LOGFILE: für Fehler, befindet sich im gleichen Ordner mit diesem Skript
        # z.B. unter errorsAuthorityGeoName... (time.strftime("%Y-%m-%dT%H%M%S%z", time.localtime()))
        filename = 'log/' + dataType + entityType + '.txt'
        self.logfile = open(filename, 'w', encoding="utf8")

        self.DataType = dataType
        self.EntityType = entityType
        self.OutputFormat = outputFormat
        
#         # neue Dateien anlegen
        if self.OutputFormat ==  'json':
            self.jsonBegin = True
            if dataSelection: self.json = open('data/json/selected{}{}.json'.format(dataType, entityType), 'w', encoding="utf8")
            else: self.json = open('data/json/{}{}.json'.format(dataType, entityType), 'w', encoding="utf8")
            
        if self.OutputFormat ==  'graphml':
            self.gnodes = open('data/graphml/{}{}Nodes.graphml'.format(dataType, entityType), 'w', encoding="utf8")
            self.gedges = open('data/graphml/{}{}Edges.graphml'.format(dataType, entityType), 'w', encoding="utf8")
            if self.DataType == "Authority": self.chronTerms = open('data/graphml/{}{}ChronTerm.graphml'.format(dataType, entityType), 'w', encoding="utf8")

        self.val_isils = val_isils
        
        
        # LISTEN
        if self.DataType == "Authority": 
            self.RelationTypeList = codes.relationTypeListAut
            self.EntityGenCodes = codes.entityGenCodes
            self.EntitySpecCodes = codes.entitySpecCodes
            self.RelationGndTypeList = codes.relationGndTypeList
            self.GeoAreaCodes = codes.geoAreaCodes
            self.OldIdsList = oldIds.EntityOldIds
            
        if self.DataType == "Bibliographic": 
            self.RelationTypeList = codes.relationTypeListBib
            self.RelationBibTypeList = codes.relationBibTypeList
            self.OldIdsList = oldIds.EntityOldIds

        self.nodes = 0
        self.relations = 0
        
        self.relationWithOldId = 0
        self.relationWithoutId = 0
        self.relationToTn = 0
        
        self.recs = 0
        
        
        
        # FIX
#         self.nonIdsList = self.readList('nonEntities.txt')
        self.nonIdsList = self.readList('src/nonEntities.txt')
        self.duplicateIdsList = self.readList('src/dublesBibliographicRecords.txt')
            
        
        # XML (MARC21-Datei) record-weise parsen
        for event, elem in etree.iterparse(filecontent, events=('start', 'end'), parser=etree.XMLParser(encoding='UTF-8')):

            # ANFANG XML-TAGS
            if event == 'start':
                    
                if elem.tag == '{http://www.loc.gov/MARC21/slim}record':
                    self.record = dict()
                    self.recs += 1

                if elem.tag == '{http://www.loc.gov/MARC21/slim}controlfield':
                    self.currentTag = elem.attrib['tag']
                    if self.currentTag not in self.record: self.record[self.currentTag] = ''

                if elem.tag in ['{http://www.loc.gov/MARC21/slim}datafield']:
                    self.currentTag = elem.attrib['tag']
                    self.currentDatafield = dict()
                    if self.currentTag not in self.record: self.record[self.currentTag] = []
                    self.currentDatafield['ind1'] = elem.attrib['ind1']
                    self.currentDatafield['ind2'] = elem.attrib['ind2']

                # CODE in subfield
                if elem.tag == '{http://www.loc.gov/MARC21/slim}subfield':
                    self.currentCode = elem.attrib['code']
                    if self.currentCode not in self.currentDatafield: self.currentDatafield[self.currentCode] = []


            # ENDE XML-TAGS
            elif event == 'end':
                
                
                if elem.tag == '{http://www.loc.gov/MARC21/slim}collection':
                    if self.OutputFormat ==  'json':
                        self.json.write(']\n')
                        self.json.close()

                    if self.OutputFormat ==  'graphml':
                        self.gnodes.close()
                        self.gedges.close()
                        if self.DataType == "Authority": self.chronTerms.close()
                        
                    self.logfile.close()

                if elem.tag == '{http://www.loc.gov/MARC21/slim}record':
                                     
                    # Transformation zu JSON
                    if outputFormat == "json":
                        if dataType=='Authority':
                            if dataSelection: self.writeJson(self.entityDataSelection())
                            else: self.writeJson(self.record)

                        if dataType=='Bibliographic':
                            if dataSelection: self.writeJson(self.resourceDataSelection())
                            else: self.writeJson(self.record)

                     # Transformation zu GRAPHML    
                    elif outputFormat == "graphml":
                        if dataType=='Authority': self.writeGraphml(self.entityDataSelection())
                        if dataType=='Bibliographic': self.writeGraphml(self.resourceDataSelection())
                                    

                if elem.tag == '{http://www.loc.gov/MARC21/slim}controlfield':
                    self.record[self.currentTag] = elem.text
                    

                if elem.tag in ['{http://www.loc.gov/MARC21/slim}datafield']:
                    if self.currentDatafield not in self.record[self.currentTag]:
                        self.record[self.currentTag].append(self.currentDatafield)
                    
                    
                if elem.tag in '{http://www.loc.gov/MARC21/slim}subfield':
                    if self.normalizeName(elem.text) not in self.currentDatafield[self.currentCode]:
                        self.currentDatafield[self.currentCode].append(self.normalizeName(elem.text))

                elem.clear()

        if outputFormat == "graphml": 
            print('Transforms {} nodes, {} edges to graphml'.format(self.nodes, self.relations))
            print('Processed {} records'.format(self.recs))
            
#             print('Transforms {} nodes, {} edges to graphml\nFound {} relations with old id\nFound {} relations without id\nFound {} relations to Tn authority files'.format(self.nodes, self.relations, self.relationWithOldId, self.relationWithoutId, self.relationToTn))

        
            
    ##############################################################################################################        
    # Hilffunktionen für Sammeln der Informationen aus einem Record
    ##############################################################################################################        

    
    # für Normdaten
    def entityDataSelection(self):
        """Transformation der Normdaten gemäß Datenmodell, das entsprechende Felder und Unterfelder berücksichtigt.
        Für jedes Merkmal wird eine aussagekräftige Benennung gewählt, die seinen Inhalt widerspiegelt. 
        Bennenungen für Entitäten beginnen mit "Entity".
        
        :return: ausgewählte Informationen aus einem Record, der eine Entität beschreibt
        :rtype: dict
        """
        
        # leeres Dict als default
        selectedData = dict()
        
        
        # Merkmale von Entitäten        
#        selectedData['EntityType'] = self.EntityType
        selectedData['Id'] = self.getEntityFeature( tag='035', code='a', condition='(DE-588)')
        self.Id = selectedData['Id']
        self.Uri = 'http://d-nb.info/gnd/' + selectedData['Id'].replace('(DE-588)', '')
        selectedData['Uri'] = self.Uri
        selectedData['Isil'] = self.getEntityFeature( tag='035', code='a', repeatable=True)
        selectedData['OldId'] =  self.getEntityFeature(tag = '035', code = 'z', condition = '(DE-588)', repeatable=True)
        selectedData['GenType'] = self.getEntityFeature(tag = '075', code = 'b', addCode = '2', addCondition='gndgen').lower()
        selectedData['SpecType'] = [code.lower() for code in self.getEntityFeature(tag = '075', code = 'b', addCode = '2', addCondition='gndspec', repeatable=True)]
        

        # Extraktion spezifischer Features
        if self.EntityType == 'PerName':
            selectedData['Name'] = self.getEntityFeature(tag = '100', code = 'a')
            selectedData['VariantName'] = self.getEntityFeature(tag = '400', code = 'a', repeatable=True) 
            selectedData['Gender'] = self.getEntityFeature(tag = '375', code = 'a', repeatable=True)
            selectedData['DateStrictOriginal'] = self.getEntityFeature(tag = '548', code = 'a', addCode = '4', addCondition='datx')
            selectedData['DateStrictBegin'], selectedData['DateStrictEnd'] = self.normalizeDate(self.getEntityFeature(tag = '548', code = 'a', addCode = '4', addCondition='datx'), self.EntityType)
            selectedData['DateApproxOriginal'] = self.getEntityFeature(tag = '548', code = 'a', addCode = '4', addCondition='datl')
            selectedData['DateApproxBegin'], selectedData['DateApproxEnd'] = self.normalizeDate(self.getEntityFeature(tag = '548', code = 'a', addCode = '4', addCondition='datl'), self.EntityType)

        if self.EntityType == 'CorpName':
            selectedData['Name'] = self.getEntityFeature(tag = '110', code = 'a')
            selectedData['VariantName'] = self.getEntityFeature(tag = '410', code = 'a', repeatable=True) 
            selectedData['Info'] = self.getEntityFeature(tag = '110', code = 'g', repeatable=True) 
            selectedData['SubUnit'] = self.getEntityFeature(tag = '110', code = 'b', repeatable=True)
            
            # datb beschreibt zwei Arten von Zeitangaben, hier werden diese entsprechend gefiltert
            selectedData['DateOriginal'] = self.getEntityFeature(tag = '548', code = 'a', addCode = '4', addCondition='datb')
            selectedData['DateApproxBegin'], selectedData['DateApproxEnd'], selectedData['DateStrictBegin'], selectedData['DateStrictEnd'] = self.normalizeDate(self.getEntityFeature(tag = '548', code = 'a', addCode = '4', addCondition='datb'), self.EntityType)

        if self.EntityType == 'MeetName':
            selectedData['Name'] = self.getEntityFeature(tag = '111', code = 'a')
            selectedData['VariantName'] = self.getEntityFeature(tag = '411', code = 'a', repeatable=True)
            selectedData['Place'] = self.getEntityFeature(tag = '111', code = 'c')
#            selectedData['MeetDate'] = self.getEntityFeature(tag = '111', code = 'd')
            selectedData['Info'] = self.getEntityFeature(tag = '111', code = 'g', repeatable=True) 
            selectedData['SubUnit'] = self.getEntityFeature(tag = '111', code = 'e', repeatable=True)
            selectedData['DateOriginal'] = self.getEntityFeature(tag = '111', code = 'd')
            selectedData['DateApproxBegin'], selectedData['DateApproxEnd'], selectedData['DateStrictBegin'], selectedData['DateStrictEnd'] = self.normalizeDate(self.getEntityFeature(tag = '111', code = 'd'), self.EntityType)
            
        if self.EntityType == 'UniTitle':
            selectedData['Name'] = self.getEntityFeature(tag = '130', code = 'a') + self.getEntityFeature(tag = '100', code = 't') + self.getEntityFeature(tag = '110', code = 't') + self.getEntityFeature(tag = '111', code = 't')
            selectedData['VariantName'] = self.getEntityFeature(tag = '430', code = 'a', repeatable=True) + self.getEntityFeature(tag = '400', code = 't', repeatable=True) + self.getEntityFeature(tag = '410', code = 't', repeatable=True) + self.getEntityFeature(tag = '411', code = 't', repeatable=True)
            selectedData['Creator'] = self.getEntityFeature(tag = '100', code = 'a', repeatable=True) + self.getEntityFeature(tag = '110', code = 'a', repeatable=True) + self.getEntityFeature(tag = '111', code = 'a', repeatable=True)
            selectedData['Medium'] = self.getEntityFeature(tag = '130', code = 'm', repeatable=True) + self.getEntityFeature(tag = '100', code = 'm', repeatable=True)
            selectedData['Medium'] += [i for i in [self.getEntityFeature(tag = '130', code = 'h'), self.getEntityFeature(tag = '100', code = 'h')] if i != '']
            selectedData['Lang'] = self.getEntityFeature(tag = '130', code = 'l') + self.getEntityFeature(tag = '100', code = 'l')
            date = self.getEntityFeature(tag = '130', code = 'f') +  self.getEntityFeature(tag = '100', code = 'f') + self.getEntityFeature(tag = '110', code = 'f') + self.getEntityFeature(tag = '111', code = 'f')
            selectedData['DateOriginal'] = date
            selectedData['DateApproxBegin'], selectedData['DateApproxEnd'], selectedData['DateStrictBegin'], selectedData['DateStrictEnd'] = self.normalizeDate(date, self.EntityType)
#            print(selectedData['Uri'], selectedData['DateApproxBegin'], selectedData['DateApproxEnd'], selectedData['DateStrictBegin'], selectedData['DateStrictEnd'])

            
        if self.EntityType == 'TopicTerm':
            selectedData['Name'] = self.getEntityFeature(tag = '150', code = 'a')
            selectedData['VariantName'] = self.getEntityFeature(tag = '450', code = 'a', repeatable=True)
            selectedData['Info'] = self.getEntityFeature(tag = '150', code = 'g', repeatable=True)
            selectedData['GenSubdiv'] = self.getEntityFeature(tag = '150', code = 'x', repeatable=True)
                
        if self.EntityType == 'GeoName':
            selectedData['Name'] = self.getEntityFeature(tag = '151', code = 'a')
            selectedData['VariantName'] = self.getEntityFeature(tag = '451', code = 'a', repeatable=True) 
            selectedData['Info'] = self.getEntityFeature(tag = '151', code = 'g', repeatable=True)
            selectedData['GenSubdiv'] = self.getEntityFeature(tag = '151', code = 'x', repeatable=True)
            selectedData['Coordinates'] = self.getEntityFeature(tag = '034', code = 'f', addCode = '9', addCondition='A:dgx') + ' ' + self.getEntityFeature(tag = '034', code = 'd', addCode = '9', addCondition='A:dgx')
            selectedData['GeoArea'] = self.getEntityFeature(tag = '043', code = 'c', repeatable=True)
            selectedData['IdGeonames'] = self.getEntityFeature(tag = '034', code = '0', addCode = '9', addCondition='A:dgx')


        # Fehlermeldungen
        if selectedData['Id'] == '': self.logfile.write('ValueError: Id not found in EntityType - {}, Name - {}\n'.format(self.EntityType, self.Name))
        if selectedData['Name'] == '': self.logfile.write('ValueError: Name not found in EntityType - {}, Uri - {}\n'.format(self.EntityType, self.Uri))
        if selectedData['GenType'] not in self.EntityGenCodes:
            self.logfile.write('CodeError: invalide GenType {} found in EntityType - {}, Uri - {}\n'.format(selectedData['GenType'], self.EntityType, self.Uri))
        for spec in selectedData['SpecType']:
            if spec not in self.EntitySpecCodes: self.logfile.write('CodeError: invalide SpecType {} found in EntityType - {}, Uri - {}\n'.format(spec, self.EntityType, self.Uri))
        if self.EntityType == 'GeoName':
            for geo in selectedData['GeoArea']:
                if geo not in self.GeoAreaCodes: self.logfile.write('CodeError: invalide GeoArea {} found in EntityType - {}, Uri - {}\n'.format(geo, self.EntityType, self.Uri))

        self.Name = selectedData['Name']
                    
        # Relationen
        selectedData['RelationList']= self.getEntityRelation()

        
        return selectedData

    
    
    # für Titeldaten
    def resourceDataSelection(self):
        """Transformation der Titeldaten gemäß Datenmodell, das entsprechende Felder und Unterfelder berücksichtigt.
        Bennenungen für Ressourcen beginnen mit "Resource".


        :return: ausgewählte Informationen aus einem Record, der eine Resource beschreibt
        :rtype: dict
        """
        
        # leeres Dict als default
        selectedData = dict()
        
        
        # Merkmale von Entitäten        
        if self.EntityType[:3] == 'Sbb': self.Id = self.getEntityFeature( tag='035', code='a', condition='DE-599')
        else: self.Id = '(DE-101)' + self.getEntityFeature( tag='016', code='a', addCode = '2', addCondition='DE-101')
        selectedData['Id'] = self.Id
        selectedData['Isil'] = self.getEntityFeature( tag='035', code='a', repeatable=True)
#        self.sources.add(selectedData['Id'].replace('(DE-588)', '').replace("-", "_"))
        if self.EntityType == "Zdb": self.Uri = 'https://zdb-katalog.de/title.xhtml?idn={}&amp;view=full'.format(selectedData['Id'].replace('(DE-101)', ''))
        elif self.EntityType[:3] == "Sbb": self.Uri = ''
        else: self.Uri = 'http://d-nb.info/' + selectedData['Id'].replace('(DE-101)', '')
        selectedData['Uri'] = self.Uri
        # in Titeldaten gibt es keine veraltete Ids
#        selectedData['ResourceOldId'] =  self.getEntityFeature(tag = '035', code = 'z', condition = '(DE-101)', repeatable=True)
        selectedData['Name'] = self.getEntityFeature(tag = '245', code = 'a')
        self.Name =  selectedData['Name']        
        selectedData['Creator'] = self.getEntityFeature(tag = '100', code = 'a', repeatable=True) + self.getEntityFeature(tag = '110', code = 'a', repeatable=True) + self.getEntityFeature(tag = '111', code = 'a', repeatable=True)
        date = self.getEntityFeature(tag = '264', code = 'c', repeatable=True)
        selectedData['DateOriginal'] = date
        selectedData['DateApproxBegin'], selectedData['DateApproxEnd'], selectedData['DateStrictBegin'], selectedData['DateStrictEnd'] = self.normalizeDate(';;;'.join(date), self.EntityType)
        selectedData['Place'] = self.getEntityFeature(tag = '264', code = 'a', repeatable=True)
        selectedData['Lang'] = self.getEntityFeature(tag = '041', code = 'a', repeatable=True)
        selectedData['Genre'] = self.getEntityFeature(tag = '655', code = 'a', repeatable=True)
        

        # FEHLERMELDUNGEN
        if selectedData['Id'] == '': self.logfile.write('ValueError: Id not found in Name - {}\n'.format(self.Name))
        if selectedData['Name'] == '': self.logfile.write('ValueError: Name not found in Id - {}\n'.format(self.Id))

            
        # Relationen
        selectedData['RelationList']= self.getEntityRelation()

        
        return selectedData

    
    
    ##############################################################################################################        
    # Hilffunktionen für Transformation der gesammelten Informationen aus einem Record
    ##############################################################################################################        

    
    # GRAPHML
    def writeGraphml(self, selectedData):
        """Transformiert gesammelte Informationen zu GRAPHML,
        also Entitäten oder Ressourcen werden zu Knoten und Referenzen zu Kanten umgewandelt.
        Zu GRAPHML kann man nur ausgewählte Informationen transformieren. 

        :param selectedData: gesammelte Informationen aus einem Record
        :type filecontent: dict
        
        :return: void-Funktion
        :rtype: none
        """

        
        # Vorkommen der Duplikate aus der DNB ausschließen
        if self.DataType == "Bibliographic" and self.EntityType in ["Dnb1", "Dnb2", "Dnb3", "Dnb4"] and self.Id in self.duplicateIdsList: 
            notDuble = False
        else: notDuble = True
            
            
        chronTerms = ''

        # Id für Knoten bestimmen, Präfixe hinzufügen
        # Aut für Authority files
        # Bib für Bibliographic files
        if self.DataType == "Authority":
            NodeId = "Aut" + self.Id.replace("(DE-588)", "").replace("-", "_")
        else:
            NodeId = "Bib" + self.Id.replace("(DE-101)", "").replace("(DE-599)", "").replace("-", "_")

            
        if notDuble:
            # Knoten nach Type initialisieren
            if self.DataType == "Bibliographic":
                self.gnodes.write('<node id="' + NodeId + '" labels=":Resource"><data key="labels">:Resource</data>')
            else:
                self.gnodes.write('<node id="' + NodeId + '" labels=":' + self.EntityType + '"><data key="labels">:' + self.EntityType + '</data>')
                
            self.nodes += 1

            # Informationen aus einem Datensatz (= record) transformieren
            for key in sorted(selectedData):
                # Attribute für Knoten transformieren
                if key != "RelationList" and key != 'Isil':
                    if type(selectedData[key]) == str and selectedData[key] != '':
                        self.gnodes.write('<data key="' + key + '">' + selectedData[key] + '</data>')
                    elif type(selectedData[key]) == list and selectedData[key] != []:
                        self.gnodes.write('<data key="' + key + '">' + ';;;'.join(selectedData[key]) + '</data>')

                # Verknüpfungen zu ISILs herstellen
                elif key != "RelationList" and key == 'Isil':
                    for isilId in selectedData[key]:
                        isil = isilId[isilId.find("(") +1:isilId.find(")")].replace('-', '_')
                        entityId = isilId[isilId.find(")") + 1:]
                        if isil in self.val_isils:
                            self.gedges.write('<edge id="From' + NodeId + 'ToIsilTerm' + isil + '" source="' + NodeId + '" target="IsilTerm' + isil + '" label="RelationToIsilTerm"><data key="label">RelationToIsilTerm</data><data key="TypeAddInfo">' + entityId + '</data></edge>\n')
                            
###################################################################################                            
#                            self.relations += 1

                else:
                    
                    # Relationen transformieren
                    for relation in selectedData["RelationList"]:
                        
                        # Identifikator für einen Ausgangsknoten
                        source = NodeId
                       
                        
                        # Entitäten mit Zeitausdrücken gesondert verknüpfen
                        if relation["RelationType"] == "RelationToChronTerm":
                            # Identifikator für einen Zeitausdruck automatisch zuweisen
                            # s. Funktion getChronTermId
                            target = 'ChronTerm' + self.getChronTermId(relation["Id"])
                            
                            # Relationen mit Entitäten ohne Identifikatoren ausfiltern
                            # bzw. checken, dass ein Identifikator existiert
                            if relation["Id"] != '':
                                self.nodes += 1
                                chronTerms += '<node id="' + target + '" labels=":ChronTerm"><data key="labels">:ChronTerm</data><data key="Name">' + relation["Id"] + '</data></node>\n'
                                # Relation initialisieren
                                self.gedges.write('<edge id="From' + source + 'To' + target + '" source="' + source + 
                                                  '" target="' + target + '" label="' + relation["RelationType"] + '"><data key="label">' + relation["RelationType"] + '</data>')
                                # Attribute für Relation transformieren
                                for key in relation:
                                    if key not in ["RelationType", "Id"] and relation[key] != '':
                                        self.gedges.write('<data key="' + key + '">' + relation[key] + '</data>')
                                self.gedges.write('</edge>\n')
                                
                        else: 
                            
                            target = self.checkId(relation["Id"], relation["RelationType"])

                            
                            if target != '':
                                # Relation initialisieren
                                self.gedges.write('<edge id="From' + source + 'To' + target + '" source="' + source + 
                                                  '" target="' + target + '" label="' + relation["RelationType"] + '"><data key="label">' + relation["RelationType"] + '</data>')
                                # Attribute für Relation transformieren
                                for key in relation:
                                    if key not in ["RelationType", "Id"] and relation[key] != '':
                                        self.gedges.write('<data key="' + key + '">' + relation[key] + '</data>')
                                self.gedges.write('</edge>\n')
            self.gnodes.write('</node>\n')
            
            # Knoten für gefundene Zeitausdrücke erzeugen
            if self.DataType == "Authority": self.chronTerms.write(chronTerms)

        # Soziale Relationen extrahieren
        socialRelationList = self.extractSocialRelations(selectedData)
        for relation in socialRelationList:
            source = self.checkId(relation["SourceId"], relation["RelationType"])
            target = self.checkId(relation["TargetId"], relation["RelationType"])
            if source != '' and target != '':
                # Relation initialisieren
                self.gedges.write('<edge id="From' + source + 'To' + target + '" source="' + source + 
                                  '" target="' + target + '" label="' + relation["RelationType"] + '"><data key="label">' + relation["RelationType"] + '</data>')
                # Attribute für Relation transformieren
                for key in relation:
                    if key not in ["RelationType", "SourceId", "TargetId"] and relation[key] != '':
                        self.gedges.write('<data key="' + key + '">' + relation[key] + '</data>')
                self.gedges.write('</edge>\n')
            
            

    def checkId(self, Id, RelationType):
        if RelationType == "RelationToResource":
            # Identifikator für einen Zielknoten
            # einige Ids haben "Fehler" ==> normalisieren
            target = 'Bib' + Id.replace("(DE-101)", "").replace("(DE-599)", "").replace("-", "_").replace(" ", "").upper()
        else:
            # Identifikator für einen Zielknoten
            target = 'Aut' + Id.replace("(DE-588)", "").replace("-", "_")

        # Checken der Tn-Datensätzen
        if target.replace("Aut", "").replace("Bib", "") in self.nonIdsList: 
            self.relationToTn += 1
            value = False

        else: value = True

        # Relationen mit Entitäten ohne Identifikatoren oder
        # mit Tn-Entitäten ausfiltern                
        if Id == '': self.relationWithoutId += 1
        if value and Id != '':
            self.relations += 1

            # Checken der veralteten Identifikatoren
            if target.replace("Aut", "") in self.OldIdsList: 
                self.relationWithOldId += 1
                # Vorkommen der veralteten Identifikatoren in log schreiben
                if self.DataType == "Authority": self.logfile.write('ValueError: old Id (DE-588){} found in relation from a entity with EntityType - {}, Uri - {}\n'.format(target.replace("Aut", "").replace('_','-'), self.EntityType, self.Uri))
                else: self.logfile.write('ValueError: old Id (DE-588){} found in relation from a entity with Uri - {}\n'.format(target.replace("Aut", "").replace('_','-'), self.Uri))


                # einen veralteten Identifikator ersetzen
                target = "Aut" + self.OldIdsList[target.replace("Aut", "")]
                
            # ZielIds ausgeben, wenn einen Namen nicht leer ist oder nicht zu Tn gehört
            # ZielIds sind "normale" Ids und veraltete, die durch aktuelle ersezt wurden
            return target
        
        # Sonst default value ausgeben
        return ""    

        
    # JSON
    def writeJson(self, selectedData):
        """Transformiert gesammelte Informationen zu JSON.
        Zu JSON kann man alle oder ausgewählte Informationen transformieren. 

        :param selectedData: gesammelte Informationen aus einem Record
        :type filecontent: dict
        
        :return: void-Funktion
        :rtype: none
        """

        
        if self.jsonBegin:
            self.json.write('[')
            self.json.write(str(json.dumps(selectedData, ensure_ascii=False, indent=4, sort_keys=True)))
            self.jsonBegin = False
        else: 
            self.json.write(',\n')
            self.json.write(str(json.dumps(selectedData, ensure_ascii=False, indent=4, sort_keys=True)))

            
            
    ##############################################################################################################        
    # Hilffunktionen für Sammeln der Informationen aus einem Feld
    ##############################################################################################################        

    # für Entitäten, Ressourcen und ihre Merkmale
    def getEntityFeature(self, tag=None, code=None, condition=None, addCode=None, addCondition=None, repeatable=False):
        """Sammelt Informationen aus Feldern und Unterfeldern.

        :param tag: ein betroffener Tag, wo gesuchte Information befindet
        :type tag: string
        :param code: ein betroffener Code, wo gesuchte Information befindet
        :type code: string
        :param condition: Bedingung (genannt Präfix in MARC21) für Auswahl eines richtigen Unterfeldes in einem Feld
        :type condition: string
        :param addCode: ein Unterfeld, wo zusätzliche Informationen über gesuchte Information enthalten sind
        :type addCode: string
        :param addCondition: Wert aus einem zusätzlichen Unterfeld
        :type addCondition: string
        :param repeatable: Art des betroffenen Unterfeldes, also wiederholbar bzw. nicht wiederholbar
        :type repeatable: Boolean
        
        :return: void-Funktion
        :rtype: none
        """
        
        values = []

        
        # Für alle tags in record
        if tag in self.record:
            for datafield in self.record[tag]:
                
                # Für alle codes in record
                if code in datafield:
                    
                    for value in datafield[code]:

                        # Bedingungen mit code prüfen
                        # z.B. (DE-101) in ID, nämlich condition = '(DE-101)'
                        if condition != None and addCode == None and addCondition == None:
                            if condition in value: values.append(value)                                
                        # z.B. gndgen in $2, also addCode = '2', addCondition='gndgen'        
                        if condition == None and addCode != None and addCondition != None:
                            
                            if addCode in datafield and addCondition in datafield[addCode]:
                                values.append(value)
                                   
                        # Wenn keine Bedingungen sind
                        if condition == None and addCode == None and addCondition == None: values.append(value)
        
        if condition == 'DE-599' and values == []: print(self.record['035'])                    
        # Wenn field wiederholbar ist
        if not repeatable:
            if len(values) > 1: 
                
                # überflüssige Fehlermeldungen
#                if self.EntityType == 'Resource': self.logfile.write('TypeError: not repeatable field {}${} is repeated in EntityType - {}, Uri - {}\n'.format(tag, code, self.EntityType, self.Uri))
#                else: self.logfile.write('TypeError: not repeatable field {}${} is repeated in EntityType - {}, Uri - {}\n'.format(tag, code, self.EntityType, self.Uri))

                return ';;;'.join(values)
            elif len(values) == 1: return values[0]
            else: return ''
        
        return values
    
    
    # für Relationen
    def getEntityRelation(self):
        """Sammelt Verknüpfungen aus einem Record, die in MARC21Codes.relationTypeListAut bzw. 
        MARC21Codes.relationTypeListBib definiert sind.
       
        :return: Verknüpfungen, die Informationen über Identifikator einer referenzierten Entität bzw. Ressource,
        Verknüpfungstyp, Verknüpfungsquelle, authentischen Verknüpfungstyp, zusätzliche Information und 
        zeitliche Gültigkeit
        :rtype: dict
        """

        # default-Wert
        RelationList = []
        
        for tag in self.RelationTypeList:
            
            
            
            if tag in self.record:
                for features in self.record[tag]:
                    
                        
                    Id = ''
                    
                    # RelationToEntities
                    if '0' in features:
                        for ids in features['0']:
                            if '(DE-588)' in ids: Id = ids
                                
                    # RelationToResource 
                    elif 'w' in features:
                        for ids in features['w']:
                            if '(DE-101)' in ids and ids.replace('(DE-101)', '').replace('(DE-599)', '') != '': Id = ids
                            elif '(DE-599)' in ids and ids.replace('(DE-101)', '').replace('(DE-599)', '') != '': Id = ids
#                             elif '(DE-599)' in ids and Id == '': Id = ids

                    if tag == "548":
                        if 'a' in features:
                            for ids in features['a']:
                                Id = ids

                    SourceType = ''
                    
                    if tag[:2] in ['77', '78']:
                        RelationType = self.RelationTypeList[tag][0]
                        SourceType = self.RelationTypeList[tag][1]
                        Source = self.addSource()
                        TypeAddInfo = ''
                        TempValidity = ''
                        
                        
                        if tag[:2] == '77' and 'a' in features: TypeAddInfo = ';;;'.join([ids for ids in features['a']])
                        elif tag[:2] == '78' and 'i' in features: TypeAddInfo = ';;;'.join([ids for ids in features['i']])
                            
                        if tag in ['770','772'] and 'b' in features: TempValidity =  ';;;'.join([ids for ids in features['b']])
                        elif tag in ['775','776'] and 'n' in features: TempValidity =  ';;;'.join([ids for ids in features['n']])
                        
                    elif tag[:1] == '6':
                        RelationType = self.RelationTypeList[tag][0]
                        SourceType = self.RelationTypeList[tag][1]
                        Source = self.addSource()
                        TypeAddInfo = ''
                        TempValidity = ''
                        
                    else:
                        RelationType = self.RelationTypeList[tag]
                        SourceType = ''
                        Source = self.addSource()
                        TypeAddInfo = ''
                        TempValidity = ''
                        
                        if self.DataType == "Authority":
                            if '4' in features:
                                for ids in features['4']:
                                    SourceType = ids
                                    if 'http://d-nb.info/standards/elementset/gnd#' in ids: 
                                        if ids.replace('http://d-nb.info/standards/elementset/gnd#','') in self.RelationGndTypeList:
                                            SourceType = ids.replace('http://d-nb.info/standards/elementset/gnd#','')
                                        else: self.logfile.write('CodeError: invalide SourceType {} found in field {} EntityType - {}, Uri - {}\n'.format(ids, tag, self.EntityType, self.Uri))


                            # Für GND typische codes 9v: und 9Z:
                            if '9' in features: TypeAddInfo = ';;;'.join([ids.replace('v:','') for ids in features['9'] if 'v:' in ids]) 
                            if '9' in features: TempValidity =  ';;;'.join([ids.replace('Z:','') for ids in features['9'] if 'Z:' in ids])

                        else:
                            if '4' in features: 
                                for code in features['4']:
                                    if code not in self.RelationBibTypeList:
                                        self.logfile.write('CodeError: invalide SourceType {} found in field {}, EntityType - {}, Uri - {}\n'.format(code, tag, self.EntityType, self.Uri))
                                SourceType = ';;;'.join(sorted(features['4']))

                    # Gefundene Relationen zur Liste hinzufügen    
                    RelationList.append({"Id": Id, "RelationType": RelationType, 
                                      "Source": Source, "SourceType": SourceType, 
                                      "TypeAddInfo": TypeAddInfo, 
                                      "TempValidity": TempValidity})

        return RelationList
    

        
    def extractSocialRelations(self, selectedData):
        """Findet implizite Relationen für eine Ressource 
       
        :param selectedData: Relationen inkl. ihre Merkmale für einen Knoten (Ressource)
        :type selectedData: dict

        :return: Zusätzliche soziale implizite Beziehungen (Relationen), die anhand Regeln gefunden werden
        :rtype: dict
        """
        
        socialRelationList = []
        NodeId = "Bib" + self.Id.replace("(DE-101)", "").replace("(DE-599)", "").replace("-", "_")
        
        # R1 „Folgerung“ sozialer Beziehungen
        associatedRelation = [i for i in selectedData['RelationList'] if i['RelationType'] in ['RelationToPerName', 'RelationToCorpName']]

        if len(associatedRelation) > 1:
            for onePart in associatedRelation:
                for otherPart in associatedRelation:
                    if onePart['Id'] != otherPart['Id']:
                        socialRelationList.append({'SourceId': onePart['Id'], 'TargetId': otherPart['Id'], 'RelationType':'SocialRelation', 'SourceType':'associatedRelation', 'Source': NodeId, 'TypeAddInfo':'undirected'})

        # R2 Sekundärquellen
        associatedRelation = [i for i in selectedData['RelationList'] if i['RelationType'] in ['RelationToPerName', 'RelationToCorpName']]

        if len(associatedRelation) > 1:
            for onePart in associatedRelation:
                if onePart['SourceType'] == "cre":
                    for otherPart in associatedRelation:
                        if otherPart['SourceType'] != "cre": continue
                        else: 
                            if onePart['Id'] != otherPart['Id']:
                                socialRelationList.append({'SourceId': onePart['Id'], 'TargetId': otherPart['Id'], 'RelationType':'SocialRelation', 'SourceType':'areCoAuthors', 'Source': NodeId, 'TypeAddInfo':'undirected'})  
                                socialRelationList.append({'SourceId': otherPart['Id'], 'TargetId': onePart['Id'], 'RelationType':'SocialRelation', 'SourceType':'areCoAuthors', 'Source': NodeId, 'TypeAddInfo':'undirected'})                        
        
        # R3 Sekundärquellen
        associatedRelation = [i for i in selectedData['RelationList'] if i['RelationType'] in ['RelationToPerName', 'RelationToCorpName']]

        if len(associatedRelation) > 1:
            for onePart in associatedRelation:
                if onePart['SourceType'] == "isb":
                    for otherPart in associatedRelation:
                        if otherPart['SourceType'] != "isb": continue
                        else: 
                            if onePart['Id'] != otherPart['Id']:
                                socialRelationList.append({'SourceId': onePart['Id'], 'TargetId': otherPart['Id'], 'RelationType':'SocialRelation', 'SourceType':'areCoEditors', 'Source': NodeId, 'TypeAddInfo':'undirected'})  
                                socialRelationList.append({'SourceId': otherPart['Id'], 'TargetId': onePart['Id'], 'RelationType':'SocialRelation', 'SourceType':'areCoEditors', 'Source': NodeId, 'TypeAddInfo':'undirected'})                        
                        
        # R4 Affiliationen
        associatedRelation_PerName = [i for i in selectedData['RelationList'] if i['RelationType']=='RelationToPerName']
        associatedRelation_CorpName = [i for i in selectedData['RelationList'] if i['RelationType']=='RelationToCorpName']

        if len(associatedRelation_PerName) > 0 and len(associatedRelation_CorpName) > 0:
            for onePart in associatedRelation_PerName:
                if onePart['SourceType'] == "cre":
                    for otherPart in associatedRelation_CorpName:
                        if onePart['SourceType'] != "isb": continue
                        else: 
                            socialRelationList.append({'SourceId': onePart['Id'], 'TargetId': otherPart['Id'], 'RelationType':'SocialRelation', 'SourceType':'affiliatedRelation', 'Source': NodeId, 'TypeAddInfo':'undirected'})  
                            socialRelationList.append({'SourceId': otherPart['Id'], 'TargetId': onePart['Id'], 'RelationType':'SocialRelation', 'SourceType':'affiliatedRelation', 'Source': NodeId, 'TypeAddInfo':'undirected'})                        
        
                else: continue
                
        return socialRelationList
                
        
    
    ##############################################################################################################        
    # Normalisierungsfunktionen für Zeitausdrücke und Namen
    ##############################################################################################################        

    def getChronTermId(self, ChronTerm):
        """Generiert einen Identifikator für Zeitausdrücke automatisch 
       
        :param ChronTerm: ein Zeitausdruck
        :type ChronTerm: string

        :return: Identifikator für einen zeitausdruck mit erlaublen Zeichen
        :rtype: string
        """

        
        valid = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        newChronTerm = ChronTerm
        for char in ChronTerm:

            if char == '-': newChronTerm = newChronTerm.replace(char, 'To')
            if char == '–': newChronTerm = newChronTerm.replace(char, 'To')
            if char == '–': newChronTerm = newChronTerm.replace(char, 'To')
            if char == '.': newChronTerm = newChronTerm.replace(char, 'Dot')
            if char == ':': newChronTerm = newChronTerm.replace(char, 'Colon')
            if char == ';': newChronTerm = newChronTerm.replace(char, 'Semicolon')
            if char == ',': newChronTerm = newChronTerm.replace(char, 'Comma')
            if char == ' ': newChronTerm = newChronTerm.replace(char, 'Space')
            if char == '|': newChronTerm = newChronTerm.replace(char, 'Pipe')
            if char == '/': newChronTerm = newChronTerm.replace(char, 'Slash')
            if char == '\\': newChronTerm = newChronTerm.replace(char, 'Backslash')
            if char == '?': newChronTerm = newChronTerm.replace(char, 'QuestionMark')
            if char == '!': newChronTerm = newChronTerm.replace(char, 'ExclamationMark')
            if char == '*': newChronTerm = newChronTerm.replace(char, 'Asterics')
            if char == '(': newChronTerm = newChronTerm.replace(char, 'BracketOn')
            if char == ')': newChronTerm = newChronTerm.replace(char, 'BracketOff')
            if char == '[': newChronTerm = newChronTerm.replace(char, 'SquareBracketOn')
            if char == ']': newChronTerm = newChronTerm.replace(char, 'SquareBracketOff')
            if char == '{': newChronTerm = newChronTerm.replace(char, 'CurlyBracketOn')
            if char == '}': newChronTerm = newChronTerm.replace(char, 'CurlyBracketOff')
            if char not in valid: newChronTerm = newChronTerm.replace(char, '')
                
        return newChronTerm
    
    def normalizeName(self, Name):
        """Normalisiert einen Namen 
       
        :param Name: ein Name
        :type Name: string

        :return: Name mit erlaubten Zeichen
        :rtype: string
        """
        
        
        # Problem in <subfield code="a"/>
        if type(Name) == str: Name = Name.replace('', '').replace('', '').replace('', '')
        else: Name = ''
            
        if self.OutputFormat == "graphml":
            newName = ''
            for i in Name:
                if i == '&': newName += '&amp;'
                elif i == '<': newName += '&lt;'
                elif i == '>': newName += '&gt;'
                else: newName += i
        else: newName = Name

        return newName

    def normalizeDate(self, Date, entityType):
        """Normalisiert und trennt eine Datumsangabe
       
        :param Name: eine Datumsangabe
        :type Name: string

        :return: zwei Datumsangaben, die Anfang und Ende beschreiben
        :rtype: list of strings
        """
        
        DateApproxBegin = []
        DateApproxEnd = []
        DateStrictBegin = []
        DateStrictEnd = []
        
        # Bei Personen Namen unterscheiden sich Zeitangaben
        # nach exakten und nicht-exakten
        if entityType == "PerName":
            for oneDate in Date.split(';;;'):
                if '-' in oneDate: 
                    DateApproxBegin.append(oneDate.split('-')[0])
                    DateApproxEnd.append(oneDate.split('-')[1])
                else: DateApproxBegin.append(oneDate)
            return ';;;'.join(DateApproxBegin), ';;;'.join(DateApproxEnd)
        
        else:
            for oneDate in Date.split(';;;'):
                if '-' in oneDate: 
                    if '.' in oneDate and oneDate.split('-')[0].replace('.','').replace('X','').isnumeric() and  oneDate.split('-')[1].replace('.','').replace('X','').isnumeric():
                        DateStrictBegin.append(oneDate.split('-')[0])
                        DateStrictEnd.append(oneDate.split('-')[1])
                    else:
                        DateApproxBegin.append(oneDate.split('-')[0])
                        DateApproxEnd.append(oneDate.split('-')[1])
                else: 
                    if '.' in oneDate and oneDate.replace('.','').replace('X','').isnumeric(): DateStrictBegin.append(oneDate)
                    else: DateApproxBegin.append(oneDate)
            return ';;;'.join(DateApproxBegin), ';;;'.join( DateApproxEnd), ';;;'.join(DateStrictBegin), ';;;'.join( DateStrictEnd)
        
    def addSource(self):
        if self.EntityType in ["PerName", "CorpName", "MeetName", "UniTitle", "TopicTerm", "GeoName"] : return 'GND'
        elif self.EntityType in ["Dnb1", "Dnb2", "Dnb3", "Dnb4"]: return 'DNB'
        elif self.EntityType == "Zdb": return 'ZDB'
        elif self.EntityType[:3] == "Sbb": return 'SBB'
        else: raise Exception('InputError: invalide entity type "{}".'.format(self.entityType)) 


    def readList(self, filename):
        f = open(filename, 'r', encoding='utf-8')
        ids = set()
        for line in f.readlines():
            line = line.strip()
            ids.add(line)
        f.close()
        return ids
