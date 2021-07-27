# -*- coding: utf-8 -*-
"""
@author: melina
"""

from os import listdir
from os.path import isfile, join
import fire

def merge_ocr_files(outfile, ocr_data_path):
    """
    WORKS ONLY FOR THE FIRST FILE OF THE OCR BATCH3. GND ENTITIES HAVE BEEN ADDED
    MANUALLY.
    
    Merges all ocr files into one graphml file.
    ---------
    outfile : str
        Name of output file. Needs to end in .graphml .
    ocr_data_path : name of directory which contains the 
        ocr .graphml files
        
    Returns
    -----------
    None.
    """
    with open(outfile, 'w', encoding='utf8') as out:
        out.write("""<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">
<key id="id" for="node" attr.name="id" attr.type="string"/>
<key id="IdGND" for="node" attr.name="IdGND" attr.type="string"/>
<key id="IdWikidata" for="node" attr.name="IdWikidata" attr.type="string"/>
<key id="OldId" for="node" attr.name="OldId" attr.type="string"/>
<key id="Uri" for="node" attr.name="Uri" attr.type="string"/>
<key id="GenType" for="node" attr.name="GenType" attr.type="string"/>
<key id="SpecType" for="node" attr.name="SpecType" attr.type="string"/>
<key id="Type" for="node" attr.name="Type" attr.type="string"/>
<key id="Name" for="node" attr.name="Name" attr.type="string"/>
<key id="IdZDB" for="node" attr.name="IdZDB" attr.type="string"/>
<key id="DateApproxBegin" for="node" attr.name="DateApproxBegin" attr.type="string"/>
<key id="DateStrictBegin" for="node" attr.name="DateStrictBegin" attr.type="string"/>
<key id="VariantName" for="node" attr.name="VariantName" attr.type="string"/>
<key id="Gender" for="node" attr.name="Gender" attr.type="string"/>
<key id="DateOriginal" for="node" attr.name="DateOriginal" attr.type="string"/>
<key id="DateApproxOriginal" for="node" attr.name="DateApproxOriginal" attr.type="string"/>
<key id="DateApproxEnd" for="node" attr.name="DateApproxEnd" attr.type="string"/>
<key id="DateStrictOriginal" for="node" attr.name="DateStrictOriginal" attr.type="string"/>
<key id="DateStrictEnd" for="node" attr.name="DateStrictEnd" attr.type="string"/>
<key id="SubUnit" for="node" attr.name="SubUnit" attr.type="string"/>
<key id="Info" for="node" attr.name="Info" attr.type="string"/>
<key id="Place" for="node" attr.name="Place" attr.type="string"/>
<key id="Date" for="node" attr.name="Date" attr.type="string"/>
<key id="Creator" for="node" attr.name="Creator" attr.type="string"/>
<key id="Medium" for="node" attr.name="Medium" attr.type="string"/>
<key id="Lang" for="node" attr.name="Lang" attr.type="string"/>
<key id="GenSubdiv" for="node" attr.name="GenSubdiv" attr.type="string"/>
<key id="GeoArea" for="node" attr.name="GeoArea" attr.type="string"/>
<key id="Coordinates" for="node" attr.name="Coordinates" attr.type="string"/>
<key id="UriGeonames" for="node" attr.name="UriGeonames" attr.type="string"/>
<key id="Title" for="node" attr.name="Title" attr.type="string"/>
<key id="Genre" for="node" attr.name="Genre" attr.type="string"/>
<key id="labels" for="node" attr.name="labels" attr.type="string"/>
<key id="issue" for="node" attr.name="issue" attr.type="string"/>
<key id="page" for="node" attr.name="page" attr.type="string"/>
<key id="article" for="node" attr.name="article" attr.type="string"/>
<key id="version" for="node" attr.name="version" attr.type="string"/>
<key id="url" for="node" attr.name="url" attr.type="string"/>
<key id="id" for="edge" attr.name="id" attr.type="string"/>
<key id="source" for="edge" attr.name="source" attr.type="string"/>
<key id="target" for="edge" attr.name="target" attr.type="string"/>
<key id="label" for="edge" attr.name="label" attr.type="string"/>
<key id="TypeAddInfo" for="edge" attr.name="TypeAddInfo" attr.type="string"/>
<key id="Sent" for="edge" attr.name="Sent" attr.type="string"/>
<key id="Name" for="edge" attr.name="Name" attr.type="string"/>
<key id="Emb" for="edge" attr.name="Emb" attr.type="string"/>
<key id="Left" for="edge" attr.name="Left" attr.type="string"/>
<key id="Top" for="edge" attr.name="Top" attr.type="string"/>
<key id="Width" for="edge" attr.name="Width" attr.type="string"/>
<key id="Height" for="edge" attr.name="Height" attr.type="string"/>
<key id="WdDateApproxBegin" for="node" attr.name="WdDateApproxBegin" attr.type="string"/>
<key id="WdDateStrictBegin" for="node" attr.name="WdDateStrictBegin" attr.type="string"/>
<key id="WdDateApproxOriginal" for="node" attr.name="WdDateApproxOriginal" attr.type="string"/>
<key id="WdDateStrictOriginal" for="node" attr.name="WdDateStrictOriginal" attr.type="string"/>
<key id="WdDateApproxEnd" for="node" attr.name="WdDateApproxEnd" attr.type="string"/>
<key id="WdDateStrictEnd" for="node" attr.name="WdDateStrictEnd" attr.type="string"/>
<key id="WdGender" for="node" attr.name="WdGender" attr.type="string"/>
<key id="WdPlaceOfBirth" for="node" attr.name="WdPlaceOfBirth" attr.type="string"/>
<key id="WdPlaceOfBirthId" for="node" attr.name="WdPlaceOfBirthId" attr.type="string"/>
<key id="WdPlaceOfDeath" for="node" attr.name="WdPlaceOfDeath" attr.type="string"/>
<key id="WdPlaceOfDeathId" for="node" attr.name="WdPlaceOfDeathId" attr.type="string"/>
<key id="SourceType" for="edge" attr.name="SourceType" attr.type="string"/>
<key id="TempValidity" for="edge" attr.name="TempValidity" attr.type="string"/>
<key id="Source" for="edge" attr.name="Source" attr.type="string"/>
<graph id="G" edgedefault="directed">
""")
        with open(ocr_data_path +'/'+ 'OCRDocumentNodes.graphml', 'r', encoding='utf8') as file:
            for line in file.readlines():
                out.write(line)
        with open(ocr_data_path +'/'+ 'WikiNodes.graphml', 'r', encoding='utf8') as file:
            for line in file.readlines():
                out.write(line)
        out.write("""<node id="Aut4005728_8" labels=":GeoName"><data key="labels">:GeoName</data><data key="Coordinates">N052.500000 E013.416669</data><data key="GenType">g</data><data key="GeoArea">XA-DE-BE</data><data key="Id">(DE-588)4005728-8</data><data key="IdGeonames">http://sws.geonames.org/2950157</data><data key="Name">Berlin</data><data key="OldId">(DE-588)7761961-4;;;(DE-588)2004272-3</data><data key="SpecType">gik;;;gif</data><data key="Uri">http://d-nb.info/gnd/4005728-8</data><data key="VariantName">Großberlin;;;Groß-Berlin;;;Haupt- und Residenz-Stadt Berlin;;;Reichshauptstadt Berlin;;;Berlino;;;Berolino;;;Stadtgemeinde Berlin;;;Hauptstadt Berlin;;;Birlīn;;;Barlīn;;;Berolinon;;;Land Berlin;;;Coloniae Brandenburgicae;;;Berlinum;;;Verolino;;;Berolinum;;;Cölln an der Spree;;;Colonia Brandenburgica;;;Colonia Marchica;;;Cöln an der Spree;;;Berlin;;;"Besonderes Gebiet" Berlin;;;Gross-Berlin</data></node> 
<node id="Aut5006371_6" labels=":CorpName"><data key="labels">:CorpName</data><data key="DateApproxBegin">1861</data><data key="DateApproxEnd">1884</data><data key="DateOriginal">1861-1884</data><data key="GenType">b</data><data key="Id">(DE-588)5006371-6</data><data key="Name">Deutsche Fortschrittspartei</data><data key="OldId">(DE-588)4011640-2</data><data key="SpecType">kiz</data><data key="Uri">http://d-nb.info/gnd/5006371-6</data><data key="VariantName">Fortschrittspartei;;;DFP</data></node>
<node id="Aut4047194_9" labels=":GeoName"><data key="labels">:GeoName</data><data key="Coordinates"> </data><data key="GenType">g</data><data key="GeoArea">XA-DXDE;;;XA-DE</data><data key="Id">(DE-588)4047194-9</data><data key="Name">Preußen</data><data key="OldId">(DE-588)1086116984;;;(DE-588)35060-6</data><data key="SpecType">gik</data><data key="Uri">http://d-nb.info/gnd/4047194-9</data><data key="VariantName">Brandenburg-Preußen;;;Königreich Preußen;;;Preußische Staaten;;;Preußischer Staat;;;Der Preußische Staat;;;Königlich Preußische Staaten;;;Prusy Królewskie;;;Königlich Preußen;;;Prussia</data></node>
<node id="Aut42375_0" labels=":CorpName"><data key="labels">:CorpName</data><data key="DateApproxBegin">1844</data><data key="DateOriginal">1844-</data><data key="GenType">b</data><data key="Id">(DE-588)42375-0</data><data key="Name">Centralverein für das Wohl der Arbeitenden Klassen</data><data key="OldId">(DE-588)1089039174</data><data key="SpecType">kiz</data><data key="Uri">http://d-nb.info/gnd/42375-0</data><data key="VariantName">Zentralverein für das Wohl der Arbeitenden Klassen;;;Centralverein zum Wohl der Arbeitenden Klassen</data></node>
""")
        with open(ocr_data_path +'/'+ 'DocContainsEntEdges.graphml', 'r', encoding='utf8') as file:
            for line in file.readlines():
                out.write(line)
        with open(ocr_data_path +'/'+ 'SameAsEdges.graphml', 'r', encoding='utf8') as file:
            for line in file.readlines():
                out.write(line)
            out.write("""</graph>
</graphml>""")
            

def merge_all_files(outfile, ocr_data_path, all_data_path):
    """
    Merges all files into one graphml file.
    ---------
    outfile : str
        Name of output file. Needs to end in .graphml .
    ocr_data_path : str
        Name of directory which contains the 
        ocr .graphml files
    all_data_path : str
        Name of directory which contains all .graphml
        files (except the ocr .graphml files)
        
    Returns
    -----------
    None.
    """
    allfiles = [f for f in listdir(all_data_path) if isfile(join(all_data_path, f))]
    with open(outfile, 'w', encoding='utf8') as out:
        out.write("""<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">
<key id="id" for="node" attr.name="id" attr.type="string"/>
<key id="Id" for="node" attr.name="Id" attr.type="string"/>
<key id="IdGND" for="node" attr.name="IdGND" attr.type="string"/>
<key id="IdWikidata" for="node" attr.name="IdWikidata" attr.type="string"/>
<key id="OldId" for="node" attr.name="OldId" attr.type="string"/>
<key id="Uri" for="node" attr.name="Uri" attr.type="string"/>
<key id="GenType" for="node" attr.name="GenType" attr.type="string"/>
<key id="SpecType" for="node" attr.name="SpecType" attr.type="string"/>
<key id="Type" for="node" attr.name="Type" attr.type="string"/>
<key id="Name" for="node" attr.name="Name" attr.type="string"/>
<key id="IdZDB" for="node" attr.name="IdZDB" attr.type="string"/>
<key id="DateApproxBegin" for="node" attr.name="DateApproxBegin" attr.type="string"/>
<key id="DateStrictBegin" for="node" attr.name="DateStrictBegin" attr.type="string"/>
<key id="VariantName" for="node" attr.name="VariantName" attr.type="string"/>
<key id="Gender" for="node" attr.name="Gender" attr.type="string"/>
<key id="DateOriginal" for="node" attr.name="DateOriginal" attr.type="string"/>
<key id="DateApproxOriginal" for="node" attr.name="DateApproxOriginal" attr.type="string"/>
<key id="DateApproxEnd" for="node" attr.name="DateApproxEnd" attr.type="string"/>
<key id="DateStrictOriginal" for="node" attr.name="DateStrictOriginal" attr.type="string"/>
<key id="DateStrictEnd" for="node" attr.name="DateStrictEnd" attr.type="string"/>
<key id="SubUnit" for="node" attr.name="SubUnit" attr.type="string"/>
<key id="Info" for="node" attr.name="Info" attr.type="string"/>
<key id="Place" for="node" attr.name="Place" attr.type="string"/>
<key id="Date" for="node" attr.name="Date" attr.type="string"/>
<key id="Creator" for="node" attr.name="Creator" attr.type="string"/>
<key id="Medium" for="node" attr.name="Medium" attr.type="string"/>
<key id="Lang" for="node" attr.name="Lang" attr.type="string"/>
<key id="GenSubdiv" for="node" attr.name="GenSubdiv" attr.type="string"/>
<key id="GeoArea" for="node" attr.name="GeoArea" attr.type="string"/>
<key id="Coordinates" for="node" attr.name="Coordinates" attr.type="string"/>
<key id="UriGeonames" for="node" attr.name="UriGeonames" attr.type="string"/>
<key id="Title" for="node" attr.name="Title" attr.type="string"/>
<key id="Genre" for="node" attr.name="Genre" attr.type="string"/>
<key id="labels" for="node" attr.name="labels" attr.type="string"/>
<key id="issue" for="node" attr.name="issue" attr.type="string"/>
<key id="page" for="node" attr.name="page" attr.type="string"/>
<key id="article" for="node" attr.name="article" attr.type="string"/>
<key id="version" for="node" attr.name="version" attr.type="string"/>
<key id="url" for="node" attr.name="url" attr.type="string"/>
<key id="id" for="edge" attr.name="id" attr.type="string"/>
<key id="source" for="edge" attr.name="source" attr.type="string"/>
<key id="target" for="edge" attr.name="target" attr.type="string"/>
<key id="label" for="edge" attr.name="label" attr.type="string"/>
<key id="TypeAddInfo" for="edge" attr.name="TypeAddInfo" attr.type="string"/>
<key id="Sent" for="edge" attr.name="Sent" attr.type="string"/>
<key id="Name" for="edge" attr.name="Name" attr.type="string"/>
<key id="Emb" for="edge" attr.name="Emb" attr.type="string"/>
<key id="Left" for="edge" attr.name="Left" attr.type="string"/>
<key id="Top" for="edge" attr.name="Top" attr.type="string"/>
<key id="Width" for="edge" attr.name="Width" attr.type="string"/>
<key id="Height" for="edge" attr.name="Height" attr.type="string"/>
<key id="WdDateApproxBegin" for="node" attr.name="WdDateApproxBegin" attr.type="string"/>
<key id="WdDateStrictBegin" for="node" attr.name="WdDateStrictBegin" attr.type="string"/>
<key id="WdDateApproxOriginal" for="node" attr.name="WdDateApproxOriginal" attr.type="string"/>
<key id="WdDateStrictOriginal" for="node" attr.name="WdDateStrictOriginal" attr.type="string"/>
<key id="WdDateApproxEnd" for="node" attr.name="WdDateApproxEnd" attr.type="string"/>
<key id="WdDateStrictEnd" for="node" attr.name="WdDateStrictEnd" attr.type="string"/>
<key id="WdGender" for="node" attr.name="WdGender" attr.type="string"/>
<key id="WdPlaceOfBirth" for="node" attr.name="WdPlaceOfBirth" attr.type="string"/>
<key id="WdPlaceOfBirthId" for="node" attr.name="WdPlaceOfBirthId" attr.type="string"/>
<key id="WdPlaceOfDeath" for="node" attr.name="WdPlaceOfDeath" attr.type="string"/>
<key id="WdPlaceOfDeathId" for="node" attr.name="WdPlaceOfDeathId" attr.type="string"/>
<key id="SourceType" for="edge" attr.name="SourceType" attr.type="string"/>
<key id="TempValidity" for="edge" attr.name="TempValidity" attr.type="string"/>
<key id="Source" for="edge" attr.name="Source" attr.type="string"/>
<key id="SourceType" for="edge" attr.name="SourceType" attr.type="string"/>
<graph id="G" edgedefault="directed">
""")
        ######## ADD NODES #############
        with open(ocr_data_path +'/'+ 'OCRDocumentNodes.graphml', 'r', encoding='utf8') as file:
            for line in file.readlines():
                out.write(line)
        with open(ocr_data_path +'/'+ 'WikiNodes.graphml', 'r', encoding='utf8') as file:
            for line in file.readlines():
                out.write(line)
       ######## ADD ISIL NODES ###########
        with open("data/IsilNodes.graphml", 'r', encoding='utf8') as file:
            for line in file.readlines():
                out.write(line)
        for f in allfiles:
            if "Nodes" in f:
                print(f)
                file = open('graphml/'+ f, 'r', encoding='utf8')
                for line in file.readlines():
                    out.write(line)
                file.close()
        ####### ADD ALL EDGES #############
        for f in allfiles:
            if "Edges" in f:
                print(f)
                file = open('graphml/'+ f, 'r', encoding='utf8')
                for line in file.readlines():
                    out.write(line)
                file.close()
        with open(ocr_data_path +'/'+ 'DocContainsEntEdges.graphml', 'r', encoding='utf8') as file:
            for line in file.readlines():
                out.write(line)
        with open(ocr_data_path +'/'+ 'SameAsEdges.graphml', 'r', encoding='utf8') as file:
            for line in file.readlines():
                out.write(line)
            out.write("""</graph>
</graphml>""")
            
def merge_except_ocr(outfile, all_data_path):
    """
    Merges all files into one graphml file.
    ---------
    outfile : str
        Name of output file. Needs to end in .graphml .
    all_data_path : str
        Name of directory which contains all .graphml
        files (except the ocr .graphml files)
        
    Returns
    -----------
    None.
    """
    allfiles = [f for f in listdir(all_data_path) if isfile(join(all_data_path, f))]
    with open(outfile, 'w', encoding='utf8') as out:
        out.write("""<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">
<key id="id" for="node" attr.name="id" attr.type="string"/>
<key id="Id" for="node" attr.name="Id" attr.type="string"/>
<key id="OldId" for="node" attr.name="OldId" attr.type="string"/>
<key id="Uri" for="node" attr.name="Uri" attr.type="string"/>
<key id="GenType" for="node" attr.name="GenType" attr.type="string"/>
<key id="SpecType" for="node" attr.name="SpecType" attr.type="string"/>
<key id="Name" for="node" attr.name="Name" attr.type="string"/>
<key id="VariantName" for="node" attr.name="VariantName" attr.type="string"/>
<key id="Gender" for="node" attr.name="Gender" attr.type="string"/>
<key id="DateOriginal" for="node" attr.name="DateOriginal" attr.type="string"/>
<key id="DateApproxOriginal" for="node" attr.name="DateApproxOriginal" attr.type="string"/>
<key id="DateApproxBegin" for="node" attr.name="DateApproxBegin" attr.type="string"/>
<key id="DateApproxEnd" for="node" attr.name="DateApproxEnd" attr.type="string"/>
<key id="DateStrictOriginal" for="node" attr.name="DateStrictOriginal" attr.type="string"/>
<key id="DateStrictBegin" for="node" attr.name="DateStrictBegin" attr.type="string"/>
<key id="DateStrictEnd" for="node" attr.name="DateStrictEnd" attr.type="string"/>
<key id="SubUnit" for="node" attr.name="SubUnit" attr.type="string"/>
<key id="Info" for="node" attr.name="Info" attr.type="string"/>
<key id="Place" for="node" attr.name="Place" attr.type="string"/>
<key id="Date" for="node" attr.name="Date" attr.type="string"/>
<key id="Creator" for="node" attr.name="Creator" attr.type="string"/>
<key id="Medium" for="node" attr.name="Medium" attr.type="string"/>
<key id="Lang" for="node" attr.name="Lang" attr.type="string"/>
<key id="GenSubdiv" for="node" attr.name="GenSubdiv" attr.type="string"/>
<key id="GeoArea" for="node" attr.name="GeoArea" attr.type="string"/>
<key id="Coordinates" for="node" attr.name="Coordinates" attr.type="string"/>
<key id="UriGeonames" for="node" attr.name="UriGeonames" attr.type="string"/>
<key id="Title" for="node" attr.name="Title" attr.type="string"/>
<key id="Genre" for="node" attr.name="Genre" attr.type="string"/>
<key id="labels" for="node" attr.name="labels" attr.type="string"/>
<key id="label" for="edge" attr.name="label" attr.type="string"/>
<key id="id" for="edge" attr.name="id" attr.type="string"/>
<key id="SourceType" for="edge" attr.name="SourceType" attr.type="string"/>
<key id="TypeAddInfo" for="edge" attr.name="TypeAddInfo" attr.type="string"/>
<key id="TempValidity" for="edge" attr.name="TempValidity" attr.type="string"/>
<key id="Source" for="edge" attr.name="Source" attr.type="string"/>
<graph id="G" edgedefault="directed">
""")
       ######## ADD NODES ###########
        with open("data/IsilNodes.graphml", 'r', encoding='utf8') as file:
            for line in file.readlines():
                out.write(line)
        for f in allfiles:
            if "Nodes" in f:
                print(f)
                file = open('graphml/'+ f, 'r', encoding='utf8')
                for line in file.readlines():
                    out.write(line)
                file.close()
        ####### ADD EDGES #############
        for f in allfiles:
            if "Edges" in f:
                print(f)
                file = open('graphml/'+ f, 'r', encoding='utf8')
                for line in file.readlines():
                    out.write(line)
                file.close()
        out.write("""</graph>
</graphml>""")    
    
if __name__=='__main__': 
    fire.Fire()    
#merge_ocr_files("D:/SoNAR/Transformers/data/merged/version_23-07-21.graphml", "D:/SoNAR/Transformers/data/graphml/")