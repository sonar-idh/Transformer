# coding: utf-8

import os
import zipfile
import xml.etree.ElementTree as etree
import src.MARC21Codes as codes
import src.AllOldAuthorityIdentifier as oldIds
from src.ValidIsilTerms import val_isils

class EAD:
    def __init__(self, dataSelection=True, outputFormat = 'graphml', filename = ''):
        
        dataType = 'Bibliographic'
        entityType ='Kpe'
                
        # LOGFILE: für Fehler, befindet sich im gleichen Ordner mit diesem Skript
        # z.B. unter errorsAuthorityGeoName...
        filename = 'log/errors' + dataType + entityType + '.txt' #time.strftime("%Y-%m-%dT%H%M%S%z", time.localtime()) + '.txt'
        self.logfile = open(filename, 'w', encoding="utf8")

        self.DataType = dataType
        self.EntityType = entityType
        self.OutputFormat = outputFormat
        self.Path = []
        self.rootPath = []
        
        
        # GRAPHML Format           
        if self.OutputFormat ==  'graphml':
            self.gnodes = open('data/graphml/{}{}Nodes.graphml'.format(dataType, entityType), 'w', encoding="utf8")
            self.gedges = open('data/graphml/{}{}Edges.graphml'.format(dataType, entityType), 'w', encoding="utf8")
        if self.OutputFormat ==  'json':
            self.jsonBegin = True
            self.json = open('data/json/{}{}.json'.format(dataType, entityType), 'w', encoding="utf8")

        
        # LISTEN
        self.RelationTypeList = codes.relationTypeListBib
        self.RelationBibTypeList = codes.relationBibTypeList
        self.OldIdsList = oldIds.EntityOldIds
        self.val_isils = val_isils
        self.nonIdsList = self.readNonIds()
        
        self.nodes = 0
        self.relations = 0
        # STATISTIKEN ZU RELATIONEN
        self.relationWithoutId = 0
        self.relationOldId = 0
        self.relationToTn = 0
        self.relationToNotGnd = 0

        
        
        ##################################################################################################################
        # FIX: mit Var filename kam zu Fehler, dass es kein zipfile ist. Wurde durch string(=path) ersetzt
        zfile = zipfile.ZipFile('C:/Users/elle01/Documents/SoNAR/sonar/Metadaten/KPE_EADXML_20190701.zip', mode='r')

        for name in zfile.namelist():

            if '.xml' in name:               
                fn = zfile.open(name)              
                root = etree.parse(fn)
                root = root.getroot()

                self.bestandsbildner = []
                selectedData = {'RelationList': []}

                # Merkmale von Ressourcen
                selectedData['Id'] = root.find('{urn:isbn:1-931666-22-9}archdesc').attrib['id']
                selectedData['Isil'] = ';;;'.join([self.normalizeText(i.attrib['authfilenumber']) for i in root.findall('{urn:isbn:1-931666-22-9}archdesc/{urn:isbn:1-931666-22-9}did/{urn:isbn:1-931666-22-9}repository/{urn:isbn:1-931666-22-9}corpname') if 'source' in i.attrib and i.attrib['source'] == 'ISIL' and 'authfilenumber' in i.attrib])
                selectedData['Title'] = ';;;'.join([self.normalizeText(i.text) for i in root.findall('{urn:isbn:1-931666-22-9}archdesc/{urn:isbn:1-931666-22-9}did/{urn:isbn:1-931666-22-9}unittitle') if i.text != None])
                selectedData['Creator'] = ';;;'.join([self.normalizeText(i.attrib['normal']) for i in root.findall('{urn:isbn:1-931666-22-9}archdesc/{urn:isbn:1-931666-22-9}did/{urn:isbn:1-931666-22-9}origination/{urn:isbn:1-931666-22-9}persname[@normal]')] + [self.normalizeText(i.attrib['normal']) for i in root.findall('{urn:isbn:1-931666-22-9}archdesc/{urn:isbn:1-931666-22-9}did/{urn:isbn:1-931666-22-9}origination/{urn:isbn:1-931666-22-9}corpname[@normal]')])
                self.bestandsbildner = [self.normalizeId(i.attrib['authfilenumber']) for i in root.findall('{urn:isbn:1-931666-22-9}archdesc/{urn:isbn:1-931666-22-9}did/{urn:isbn:1-931666-22-9}origination/{urn:isbn:1-931666-22-9}persname[@authfilenumber]') if i.attrib['source'] == 'GND' and  self.normalizeText(i.attrib['authfilenumber']) not in self.nonIdsList] + [self.normalizeId(i.attrib['authfilenumber']) for i in root.findall('{urn:isbn:1-931666-22-9}archdesc/{urn:isbn:1-931666-22-9}did/{urn:isbn:1-931666-22-9}origination/{urn:isbn:1-931666-22-9}corpname[@authfilenumber]') if i.attrib['source'] == 'GND' and self.normalizeText(i.attrib['authfilenumber']) not in self.nonIdsList]
                date = ';;;'.join([self.normalizeText(i.attrib['normal']) for i in root.findall('{urn:isbn:1-931666-22-9}archdesc/{urn:isbn:1-931666-22-9}did/{urn:isbn:1-931666-22-9}unitdate[@normal]')])
                selectedData['DateOriginal'] = date
                selectedData['DateApproxBegin'], selectedData['DateApproxEnd'], selectedData['DateStrictBegin'], selectedData['DateStrictEnd'] = self.normalizeDate(date)
                
                selectedData['Place'] = ';;;'.join([self.normalizeText(i.text) for i in root.findall('{urn:isbn:1-931666-22-9}controlaccess/{urn:isbn:1-931666-22-9}geogname[@role]') if i.attrib['role'] in ["PlaceOfOrigin", "Entstehungsort"] and i.text != None])
                selectedData['Lang'] = ';;;'.join([self.normalizeText(i.text) for i in root.findall('{urn:isbn:1-931666-22-9}archdesc/{urn:isbn:1-931666-22-9}did/{urn:isbn:1-931666-22-9}langmaterial/{urn:isbn:1-931666-22-9}language') if i.text != None])
                selectedData['Genre'] = ';;;'.join([self.normalizeText(i.text) for i in root.findall('{urn:isbn:1-931666-22-9}archdesc/{urn:isbn:1-931666-22-9}controlaccess/{urn:isbn:1-931666-22-9}genreform') if i.text != None])
                selectedData['Uri'] = 'http://kalliope-verbund.info/{}'.format(self.normalizeText(root.find('{urn:isbn:1-931666-22-9}archdesc').attrib['id']))
                self.Uri = selectedData['Uri']
                selectedData['SourcePath'] = "root"
#                 self.rootPath = [selectedData['Uri']]
                self.rootPath = [selectedData['Id']]
                
                # Relation
                perName = root.findall('{urn:isbn:1-931666-22-9}archdesc/{urn:isbn:1-931666-22-9}did/{urn:isbn:1-931666-22-9}origination/{urn:isbn:1-931666-22-9}persname')
                selectedData['RelationList'] += self.findRelation(perName, 'RelationToPerName')

                corpName = root.findall('{urn:isbn:1-931666-22-9}corpname')
                selectedData['RelationList'] += self.findRelation(corpName, 'RelationToCorpName')

                geoName = root.findall('{urn:isbn:1-931666-22-9}geogname')
                selectedData['RelationList'] += self.findRelation(geoName, 'RelationToGeoName')
                            
                topicTerm = root.findall('{urn:isbn:1-931666-22-9}subject')
                selectedData['RelationList'] += self.findRelation(topicTerm, 'RelationToTopicTerm')
                            
                
                # Level Collection
                if self.OutputFormat ==  'graphml': self.writeGraphml(selectedData)
                if self.OutputFormat ==  'json': self.writeJson(selectedData)
            
                for archdesc in root.iter('{urn:isbn:1-931666-22-9}dsc'):
                    # Level Class, File, Item...
                    data = self.recurse(archdesc, root.find('{urn:isbn:1-931666-22-9}archdesc').attrib)
                    if data != {'RelationList': []}: 
                        if self.OutputFormat ==  'graphml': self.writeGraphml(data)
                        if self.OutputFormat ==  'json': self.writeJson(data)
        if self.OutputFormat ==  'graphml':
            self.gnodes.close()
            self.gedges.close()
        if self.OutputFormat ==  'json': self.json.close()
        self.logfile.close()
#        print('Transforms {} nodes, {} edges to graphml\nFound {} relations with old GND id\nFound {} relations to other sources (not GND)\nFound {} relations without id\nFound {} relations to Tn authority files\n'.format(self.nodes, self.relations, self.relationOldId, self.relationToNotGnd, self.relationWithoutId, self.relationToTn))        
        print('Transforms {} nodes, {} edges to graphml\n'.format(self.nodes, self.relations))


    def recurse(self, element, previos_attrib):
        

        selectedData = {'RelationList': []}


        if 'level' in element.attrib:
            
            # RelationToResource
            selectedData['RelationList'].append({"Id": previos_attrib['id'], 
                                                 "RelationType": 'RelationToResource', 
                                                 "Source": 'KPE', 
                                                 "SourceType": previos_attrib['level'].capitalize() + 'To' + element.attrib['level'].capitalize()})


            # Merkmale von Ressourcen sammeln
            # ResourceId
            selectedData['Id'] = self.normalizeText(element.attrib['id'])
            # ISIL
            selectedData['Isil'] = ';;;'.join([self.normalizeText(i.attrib['authfilenumber']) for i in element.findall('{urn:isbn:1-931666-22-9}did/{urn:isbn:1-931666-22-9}repository/{urn:isbn:1-931666-22-9}corpname') if 'source' in i.attrib and i.attrib['source'] == 'ISIL' and 'authfilenumber' in i.attrib])
            # ResourceTitle
            selectedData['Title'] = ';;;'.join([self.normalizeText(i.text) for i in element.findall('{urn:isbn:1-931666-22-9}did/{urn:isbn:1-931666-22-9}unittitle') if i.text != None])          
            
            
#            if '&#xD;&#xA;' in selectedData['ResourceTitle']: print(selectedData['ResourceTitle'] )   
                
                
                
            # ResourceCreator, @role='Verfasser'
            selectedData['Creator'] = ';;;'.join([self.normalizeText(i.attrib['normal']) for i in element.findall('{urn:isbn:1-931666-22-9}controlaccess/{urn:isbn:1-931666-22-9}persname[@normal]') if 'role' in i.attrib and i.attrib['role']=="Verfasser"] + [self.normalizeText(i.attrib['normal']) for i in element.findall('{urn:isbn:1-931666-22-9}controlaccess/{urn:isbn:1-931666-22-9}corpname[@normal]') if 'role' in i.attrib and i.attrib['role']=="Verfasser"]).replace('\n', ' ')
            # ResourcePublDate
            date = ';;;'.join([self.normalizeText(i.attrib['normal']) for i in element.findall('{urn:isbn:1-931666-22-9}did/{urn:isbn:1-931666-22-9}unitdate[@normal]')])
            selectedData['DateOriginal'] = date
            selectedData['DateApproxBegin'], selectedData['DateApproxEnd'], selectedData['DateStrictBegin'], selectedData['DateStrictEnd'] = self.normalizeDate(date)
            # ResourcePublPlace
            selectedData['Place'] = ';;;'.join([self.normalizeText(i.text) for i in element.findall('{urn:isbn:1-931666-22-9}controlaccess/{urn:isbn:1-931666-22-9}geogname[@role]') if i.attrib['role'] in ["PlaceOfOrigin", "Entstehungsort"] and i.text != None])
            # ResourceLang
            selectedData['Lang'] = ';;;'.join([self.normalizeText(i.text) for i in element.findall('{urn:isbn:1-931666-22-9}did/{urn:isbn:1-931666-22-9}langmaterial/{urn:isbn:1-931666-22-9}language') if i.text != None])
            # ResourceGenre
            selectedData['Genre'] = ';;;'.join([self.normalizeText(i.text) for i in element.findall('{urn:isbn:1-931666-22-9}controlaccess/{urn:isbn:1-931666-22-9}genreform') if i.text != None])
            # ResourceUri
            selectedData['Uri'] = 'http://kalliope-verbund.info/{}'.format(self.normalizeText(element.attrib['id']))
            self.Uri = selectedData['Uri']
            self.Path.append(selectedData['Id'])
            
            # SourcePath
            selectedData['SourcePath'] = ''
            

            # Relation
            perName = element.findall('{urn:isbn:1-931666-22-9}controlaccess/{urn:isbn:1-931666-22-9}persname')
            selectedData['RelationList'] += self.findRelation(perName, 'RelationToPerName')

            corpName = element.findall('{urn:isbn:1-931666-22-9}controlaccess/{urn:isbn:1-931666-22-9}corpname')
            selectedData['RelationList'] += self.findRelation(corpName, 'RelationToCorpName')

            geoName = element.findall('{urn:isbn:1-931666-22-9}controlaccess/{urn:isbn:1-931666-22-9}geogname')
            selectedData['RelationList'] += self.findRelation(geoName, 'RelationToGeoName')

            topicTerm = element.findall('{urn:isbn:1-931666-22-9}controlaccess/{urn:isbn:1-931666-22-9}subject')
            selectedData['RelationList'] += self.findRelation(topicTerm, 'RelationToTopicTerm')

            
            # FEHLERMELDUNGEN
            if selectedData['Id'] == '': self.logfile.write('ValueError: Id not found in Title - {}\n'.format(selectedData['Title']))
            if selectedData['Title'] == '': self.logfile.write('ValueError: Title not found in Id - {}\n'.format(selectedData['Id']))

            new_attrib = element.attrib
        else: new_attrib = previos_attrib
        for c in element:
            if c.tag == '{urn:isbn:1-931666-22-9}c' and 'level' in c.attrib:
                data = self.recurse(c, new_attrib)
                if data != {'RelationList': []}: 
                    if self.OutputFormat ==  'graphml': self.writeGraphml(data)
                    if self.OutputFormat ==  'json': self.writeJson(data)

        return selectedData

    
    def readNonIds(self):
        f = open('src/nonEntities.txt', 'r', encoding='utf-8')
        nonIds = set()
        for line in f.readlines():
            line = line.strip()
            nonIds.add(line)
        f.close()
        return nonIds


    def writeGraphml(self, selectedData):
        
#        print(self.rootPath, self.Path, selectedData['Uri'])
        self.Path = self.Path[:-1]
        if selectedData['SourcePath'] != 'root': selectedData['SourcePath'] = '|'.join(self.rootPath) + '|' + '|'.join(self.Path)
#        print('path', selectedData['SourcePath'])
        
        #self.extractSocialRelations(selectedData)
        
        
        NodeId = "Bib" + selectedData["Id"].replace("-", "_")
        self.nodes += 1

        # Relation zu ISIL
        entityId = selectedData["Id"].replace(selectedData['Isil']+'-', '').replace("-", "_")
        for isil in selectedData['Isil'].split(';;;'):
            isil = isil.replace("-", "_")
            if isil in self.val_isils:
                self.gedges.write('<edge id="From' + NodeId + 'ToIsilTerm' + isil + '" source="' + NodeId + '" target="IsilTerm' + isil + '" label="RelationToIsilTerm"><data key="label">RelationToIsilTerm</data><data key="TypeAddInfo">' + entityId + '</data></edge>\n')
                self.relations +=1 

        # Knoteninformationen 
        self.gnodes.write('<node id="' + NodeId + '" labels=":Resource"><data key="labels">:Resource</data>')
        for key in sorted(selectedData):
            if key != "RelationList" and key != 'Isil':
                if type(selectedData[key]) == str and selectedData[key] != '':
                    self.gnodes.write('<data key="' + key + '">' + selectedData[key].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('\n', ' ') + '</data>')
                elif type(selectedData[key]) == list and selectedData[key] != []:
                    self.gnodes.write('<data key="' + key + '">' + ';;;'.join(selectedData[key]).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('\n', ' ') + '</data>')

            # Relationen
            if key == "RelationList" and key != 'Isil':
                for relation in selectedData["RelationList"]:
                    source = NodeId
#                    target = relation["Id"]
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


    def writeJson(self, selectedData):
        if self.jsonBegin:
            self.json.write('[')
            self.json.write(str(json.dumps(selectedData, ensure_ascii=False, indent=4, sort_keys=True)))
            self.jsonBegin = False
        else: 
            self.json.write(',\n')
            self.json.write(str(json.dumps(selectedData, ensure_ascii=False, indent=4, sort_keys=True)))
            
            
    def extractSocialRelations(self, selectedData):
        """Findet implizite Relationen für eine Ressource 
       
        :param selectedData: Relationen inkl. ihre Merkmale für einen Knoten (Ressource)
        :type selectedData: dict

        :return: Zusätzliche soziale implizite Beziehungen (Relationen), die anhand Regeln gefunden werden
        :rtype: dict
        """
        
        socialRelationList = []
        NodeId = "Bib" + selectedData["Id"].replace("-", "_")
    
        # soziale Beziehungen extrahieren
        # R1 „Folgerung“ sozialer Beziehungen
        associatedRelation = [i for i in selectedData['RelationList'] if i['RelationType'] in ['RelationToPerName', 'RelationToCorpName']]

        if len(associatedRelation) > 1:
            for onePart in associatedRelation:
                if onePart['TypeAddInfo'] in ['dokumentiert', 'behandelt', 'nicht-definiert']:
                    continue
                for otherPart in associatedRelation:
                    if otherPart['TypeAddInfo'] in ['dokumentiert', 'behandelt', 'nicht-definiert']:
                        continue
                    if onePart['Id'] != otherPart['Id']:
                        socialRelationList.append({'SourceId': onePart['Id'], 'TargetId': otherPart['Id'], 'RelationType':'SocialRelation', 'SourceType':'associatedRelation', 'Source': NodeId, 'TypeAddInfo':'undirected'})

                        
        # R4 Affiliationen
        associatedRelation_PerName = [i for i in selectedData['RelationList'] if i['RelationType']=='RelationToPerName']
        associatedRelation_CorpName = [i for i in selectedData['RelationList'] if i['RelationType']=='RelationToCorpName']

        if len(associatedRelation_PerName) > 0 and len(associatedRelation_CorpName) > 0:
            for onePart in associatedRelation_PerName:
                if onePart['TypeAddInfo'] == "Verfasser":
                    for otherPart in associatedRelation_CorpName:
                        if otherPart['TypeAddInfo'] != "Verfasser": continue
                        else: 
                            socialRelationList.append({'SourceId': onePart['Id'], 'TargetId': otherPart['Id'], 'RelationType':'SocialRelation', 'SourceType':'affiliatedRelation', 'Source': NodeId, 'TypeAddInfo':'undirected'})  
                            socialRelationList.append({'SourceId': otherPart['Id'], 'TargetId': onePart['Id'], 'RelationType':'SocialRelation', 'SourceType':'affiliatedRelation', 'Source': NodeId, 'TypeAddInfo':'undirected'})                        
        
                elif onePart['TypeAddInfo'] == "Adressat":
                    for otherPart in associatedRelation_CorpName:
                        if otherPart['TypeAddInfo'] != "Adressat": continue
                        else: 
                            socialRelationList.append({'SourceId': onePart['Id'], 'TargetId': otherPart['Id'], 'RelationType':'SocialRelation', 'SourceType':'affiliatedRelation', 'Source': NodeId, 'TypeAddInfo':'undirected'})  
                            socialRelationList.append({'SourceId': otherPart['Id'], 'TargetId': onePart['Id'], 'RelationType':'SocialRelation', 'SourceType':'affiliatedRelation', 'Source': NodeId, 'TypeAddInfo':'undirected'})
                else: continue

        # R5 Korrespondenz
        correspondedRelation_uni = []
        correspondedRelation_bi = []
        if selectedData['Genre'] == "Briefe": correspondedRelation_uni = [i for i in selectedData['RelationList'] if i['RelationType'] in ['RelationToPerName', 'RelationToCorpName'] and i['TypeAddInfo'] in ['Adressat', 'Verfasser']]
        if selectedData['Genre'] == "Briefwechsel": correspondedRelation_bi = [i for i in selectedData['RelationList'] if i['RelationType'] in ['RelationToPerName', 'RelationToCorpName'] and i['TypeAddInfo'] in ['Adressat', 'Verfasser', 'Korrespondenzpartner']]

        if len(correspondedRelation_uni) > 1:
            for onePart in correspondedRelation_uni:
                if onePart['TypeAddInfo'] == "Verfasser":
                    for otherPart in correspondedRelation_uni:
                        if otherPart['TypeAddInfo'] == "Adressat" and onePart['Id'] != otherPart['Id']: socialRelationList.append({'SourceId': onePart['Id'], 'TargetId': otherPart['Id'], 'RelationType':'SocialRelation', 'SourceType':'correspondedRelation', 'Source': NodeId, 'TypeAddInfo':'directed'})  

        if len(correspondedRelation_bi) > 1:
            for onePart in correspondedRelation_bi:
                if onePart['TypeAddInfo'] in ["Verfasser", 'Korrespondenzpartner']:
                    for otherPart in correspondedRelation_bi:
                        if onePart['TypeAddInfo'] == "Verfasser" and otherPart['TypeAddInfo'] == "Adressat" and onePart['Id'] != otherPart['Id']: 
                            socialRelationList.append({'SourceId': onePart['Id'], 'TargetId': otherPart['Id'], 'RelationType':'SocialRelation', 'SourceType':'correspondedRelation', 'Source': NodeId, 'TypeAddInfo':'directed'})
                            socialRelationList.append({'SourceId': otherPart['Id'],  'TargetId': onePart['Id'], 'RelationType':'SocialRelation', 'SourceType':'correspondedRelation', 'Source': NodeId, 'TypeAddInfo':'directed'})
                            
                        elif onePart['TypeAddInfo'] == "Korrespondenzpartner" and otherPart['TypeAddInfo'] == "Korrespondenzpartner" and onePart['Id'] != otherPart['Id']:
                            socialRelationList.append({'SourceId': onePart['Id'], 'TargetId': otherPart['Id'], 'RelationType':'SocialRelation', 'SourceType':'correspondedRelation', 'Source': NodeId, 'TypeAddInfo':'directed'})
                            socialRelationList.append({'SourceId': otherPart['Id'],  'TargetId': onePart['Id'], 'RelationType':'SocialRelation', 'SourceType':'correspondedRelation', 'Source': NodeId, 'TypeAddInfo':'directed'})
                                    
        # R6 Tagebücher
        knows_onePart = []
        knows_otherPart = []
        if "Tagebuch" in selectedData['Genre']: 
            knows_onePart = [i for i in selectedData['RelationList'] if i['RelationType'] in ['RelationToPerName', 'RelationToCorpName'] and i['TypeAddInfo'] == 'Verfasser']
            knows_otherPart = [i for i in selectedData['RelationList'] if i['RelationType'] in ['RelationToPerName', 'RelationToCorpName'] and i['TypeAddInfo'] in ["Behandelt", "Erwähnt", "Erwähnte Person", "Behandelte Person", "Erwähnte Körperschaft", "Behandelte Körperschaft"]]

        if len(knows_onePart) > 0 and len(knows_otherPart) > 0:
            for onePart in knows_onePart:
                for otherPart in knows_otherPart:
                    if onePart['Id'] != otherPart['Id']:
                        socialRelationList.append({'SourceId': onePart['Id'], 'TargetId': otherPart['Id'], 'RelationType':'SocialRelation', 'SourceType':'knows', 'Source': NodeId, 'TypeAddInfo':'directed'})
                    
        # R7 Stammbücher / Stammbucheintrag, Alben 
        knows_onePart = []
        knows_otherPart = []
        if "Stammbuchblatt" in selectedData['Genre']: 
            knows_onePart = [i for i in selectedData['RelationList'] if i['RelationType'] in ['RelationToPerName', 'RelationToCorpName'] and i['TypeAddInfo'] in ['Verfasser', "Schreiber"]]
            knows_otherPart = [i for i in selectedData['RelationList'] if i['RelationType'] in ['RelationToPerName', 'RelationToCorpName'] and i['TypeAddInfo'] == "Adressat"]

        if len(knows_onePart) > 0 and len(knows_otherPart) > 0:
            for onePart in knows_onePart:
                for otherPart in knows_otherPart:
                    if onePart['Id'] != otherPart['Id']:
                        socialRelationList.append({'SourceId': onePart['Id'], 'TargetId': otherPart['Id'], 'RelationType':'SocialRelation', 'SourceType':'knows', 'Source': NodeId, 'TypeAddInfo':'undirected'})
                        socialRelationList.append({'SourceId': otherPart['Id'], 'TargetId': onePart['Id'], 'RelationType':'SocialRelation', 'SourceType':'knows', 'Source': NodeId, 'TypeAddInfo':'undirected'})
        
        # R8 Protokoll
        knows_onePart = []
        if "Protokoll" in selectedData['Genre']: 
            knows_onePart = [i for i in selectedData['RelationList'] if i['RelationType'] == 'RelationToPerName' and i['TypeAddInfo'] == "Dokumentiert"]

        if len(knows_onePart) > 1:
            for onePart in knows_onePart:
                for otherPart in knows_onePart:
                    if onePart['Id'] != otherPart['Id']:
                        socialRelationList.append({'SourceId': onePart['Id'], 'TargetId': otherPart['Id'], 'RelationType':'SocialRelation', 'SourceType':'knows', 'Source': NodeId, 'TypeAddInfo':'undirected'})
                        socialRelationList.append({'SourceId': otherPart['Id'], 'TargetId': onePart['Id'], 'RelationType':'SocialRelation', 'SourceType':'knows', 'Source': NodeId, 'TypeAddInfo':'undirected'})
                        
        # R9 Archivbestände / Findbücher 
        associatedRelation = []
        if selectedData['SourcePath'] != "root" and self.bestandsbildner != [] and selectedData['Genre'] != "Sammlung": associatedRelation = [i for i in selectedData['RelationList'] if i['RelationType'] in ['RelationToPerName', 'RelationToCorpName'] and i['TypeAddInfo'] in ['Adressat', 'Verfasser', 'Schreiber']]
        for onePart in associatedRelation:
            for otherPart in self.bestandsbildner:
                if onePart['Id'] != otherPart:
                    socialRelationList.append({'SourceId': onePart['Id'], 'TargetId': otherPart, 'RelationType':'SocialRelation', 'SourceType':'associatedRelation', 'Source': NodeId, 'TypeAddInfo':'undirected'})
        
#         knows = self.bestandsbildner
#         if selectedData['SourcePath'] == "root" and len(knows) > 1:
#             print(selectedData, self.bestandsbildner, self.Uri, self.rootPath, self.Path)
#             for onePart in knows:
#                 for otherPart in knows:
#                     if onePart != otherPart:
#                         print({'SourceId': onePart, 'TargetId': otherPart, 'RelationType':'SocialRelation', 'SourceType':'knows', 'Source': NodeId, 'TypeAddInfo':'undirected'})
                        
        knows = [i for i in selectedData['RelationList'] if i['RelationType'] in ['RelationToPerName', 'RelationToCorpName']]
        if selectedData['SourcePath'] == "root" and len(knows) > 1:
            for onePart in knows:
                for otherPart in knows:
                    if onePart['Id'] != otherPart['Id']:
                        socialRelationList.append({'SourceId': onePart['Id'], 'TargetId': otherPart['Id'], 'RelationType':'SocialRelation', 'SourceType':'knows', 'Source': NodeId, 'TypeAddInfo':'undirected'})


        return socialRelationList
        
#################################################################################################################        


    def checkId(self, Id, RelationType):
        if RelationType == "RelationToResource":
            # Identifikator für einen Zielknoten
            # einige Ids haben "Fehler" ==> normalisieren
            target = 'Bib' + Id.replace("(DE-101)", "").replace("(DE-599)", "").replace("-", "_").replace(" ", "")#.upper()
        else:
            # Identifikator für einen Zielknoten
            target = 'Aut' + Id.replace("(DE-588)", "").replace("-", "_")

        # Checken der Tn-Datensätzen
        if target.replace("Aut", "").replace("Bib", "").replace("_", "-") in self.nonIdsList: 
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
    
    
    def normalizeDate(self, date):
        
        DateApproxBegin = []
        DateApproxEnd = []
        DateStrictBegin = []
        DateStrictEnd = []
                        
                
                
        for oneDate in date.split(';;;'):
            if '/' in oneDate: 
                if '-' in oneDate and oneDate.split('/')[0].replace('-','').replace('X','').isnumeric() and  oneDate.split('/')[1].replace('-','').replace('X','').isnumeric():
                    
                    # Zeitangaben normalisieren wie bei der GND
                    # Zeitangaben, die KPE-Zeitform nicht entsprechen, werden nicht normalisiert
                    DateStrictBegin.append('.'.join(reversed(oneDate.split('/')[0].split('-'))))
                    DateStrictEnd.append('.'.join(reversed(oneDate.split('/')[1].split('-'))))
                else:
                    DateApproxBegin.append(oneDate.split('/')[0])
                    DateApproxEnd.append(oneDate.split('/')[1])
            else: 
                if '-' in oneDate and oneDate.replace('-','').replace('X','').isnumeric(): DateStrictBegin.append('.'.join(reversed(oneDate.split('-'))))
                else: DateApproxBegin.append(oneDate)
        return ';;;'.join(DateApproxBegin), ';;;'.join(DateApproxEnd), ';;;'.join(DateStrictBegin), ';;;'.join( DateStrictEnd)

    
    # für fehlerhafte Ids
    def normalizeId(self, string):
#         for i in string:
#             if i not in ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "X", "Y", "-"]:
#                 print('Invalide character "{}" from EntityId {} in {}'.format(i, string, self.ResourceUri))
#                 break

        string = string.replace('x', 'X')
        string = string.replace('028C', '')
        string = string.replace(';LoC', '')
        string = string.replace('gnd/', '')
        string = string.replace('n', '')
        string = string.replace(';GKD', '')
        string = string.replace(';PND', '')
        string = string.replace('$eor', '')
        string = string.replace('$eAutor', '')  
        string = string.replace('(DE-588)', '')
        string = string.replace('/', '')
        string = string.replace(' g', '')
        string = string.replace('geloescht', '')
        string = string.replace(' (Fehler:0001)', '')
        string = string.replace('er', '')
        if len(string) > 0 and string[-1] == 'H': string = string[:-1]

        string = string.strip()
#         for i in string:
#             if i not in ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "X", "Y", "-"]:
#                 print('Invalide character "{}" from EntityId {} in {}'.format(i, string, self.ResourceUri))
#                 break
        return string


    def findRelation(self, elements, entityType):
        relations = []

        for i in elements:
            relation = {}
            if 'source' in i.attrib and 'authfilenumber' in i.attrib and i.attrib['source'] == 'GND':
                

#                 if i.attrib['authfilenumber'] not in self.nonIdsList:
                entityId = self.normalizeId(i.attrib['authfilenumber'])
#                self.foundIds.add(entityId)

                if 'role' in i.attrib: role = self.normalizeText(i.attrib['role'])
                else: role = ''

                relation = {"Id": entityId,
                            "RelationType": entityType, 
                            "Source": 'KPE', "SourceType": '', 
                            "TypeAddInfo": role, 
                            "TempValidity": ''}
                                        
#                 # Tn-Datensätze zählen
#                 else: self.relationToTn += 1
                    
            if relation != {}: relations.append(relation)

                    
            elif 'source' in i.attrib and 'authfilenumber' in i.attrib and i.attrib['source'] != 'GND':
                # Relationen zu Nicht-GND zählen
                self.relationToNotGnd += 1
                
        return relations

    def normalizeText(self, text):
        text = text.strip().replace('\n', ' ').replace('\r', ' ')
        return text

