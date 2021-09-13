# coding: utf-8
"""
@author: melina
"""

from enrich.enrich_data import search_doublette, wd_id_to_gnd, enrich_entity
from os import listdir
from os.path import isfile, join
import pandas as pd
import json
import re
import fire

def process_tsv(inpath, outfile):
    """
    Proceses the ocr .tsv files and
    returns the file 'entities-dict.json'
    ---------
    
    inpath : str
        Path to directory which contains
        the .tsv files.
    outfile : str
        entities-dict.json
        
    Returns
    -----------
    None.
    """
    filelist = [f for f in listdir(inpath) if isfile(join(inpath, f))]
    print(filelist)
    results = {}
    for x in filelist:
        file = open(inpath + x, 'r', encoding='utf8')
        lines = file.readlines()
        url = lines[1].strip("# ")
        if url.endswith("\n"):
            url = url.rstrip("\n")
        splitted = url.split("SNP")
        meta = splitted[1].split("-")
        zdb_id = meta[0]
        date = meta[1]
        issue = meta[2]
        page = meta[3]
        article = meta[4]
        version = re.sub("/left,top,width,height/full/0/default.jpg","", meta[5])
        url = re.sub("left,top,width,height", "full", url)
        meta = {'IdZDB': zdb_id, 'date': date, 'issue': issue, 'page': page, 'article': article, 'version': version, 'url': url}
        file.close()
        filex = open(inpath + x, 'r', encoding='utf8')      
        group_df = pd.read_csv(filex, sep='\t', names=['sent', 'token', 'ne_tag', 'ne_emb', 'wd_id', 'url', 'left', 'top', 'width', 'height'], encoding='utf8', error_bad_lines=False, engine="python")
        sents = group_df['sent'].tolist()
        tokens = group_df['token'].tolist()
        tags = group_df['ne_tag'].tolist()
        embs = group_df['ne_emb'].tolist()
        wd_ids = group_df['wd_id'].tolist()
        lefts = group_df['left'].tolist()
        tops = group_df['top'].tolist()
        widths = group_df['width'].tolist()
        heights = group_df['height'].tolist()
        multient = False
        entities = []
        for sent, token, tag, nexttag, emb, nextemb, wd_id, left, top, width, height in zip(sents[2:], tokens[2:], tags[2:], tags[3:], embs[2:], embs[3:], wd_ids[2:], lefts[2:], tops[2:], widths[2:], heights[2:]):
            if not tag == 'O' and multient == False:
                if nexttag == 'O': # named entities with only one token
                    entity = {"entity":{"Sent": sent, "Token": token, "Tag": tag, "Emb": emb, "Wd_Id": wd_id.split('|')[0], "Left": left, "Top": top, "Width": width, "Height": height}}
                    entities.append(entity)
                elif nexttag.startswith('B-'):
                    entity = {"entity":{"Sent": sent, "Token": token, "Tag": tag, "Emb": emb, "Wd_Id": wd_id.split('|')[0], "Left": left, "Top": top, "Width": width, "Height": height}}
                    entities.append(entity)
            if tag.startswith('B-') and nexttag.startswith('I-'):
                multient = True
                entity_mult = token
                multitags, multiemb, multileft, multitop, multiwidth, multiheight = [], [], [], [], [], []
                multiemb.append(emb)
                multitags.append(tag)
                multileft.append(left)
                multitop.append(top)
                multiwidth.append(width)
                multiheight.append(height)
            if multient and tag.startswith('I-') and not nexttag == 'O':
                entity_mult += " " + token
                multitags.append(tag)
                multiemb.append(emb)
                multileft.append(left)
                multitop.append(top)
                multiwidth.append(width)
                multiheight.append(height)
            if multient and nexttag == 'O':
                entity_mult += " " + token 
                multitags.append(tag)
                multiemb.append(emb)
                multileft.append(left)
                multitop.append(top)
                multiwidth.append(width)
                multiheight.append(height)
                print("Multi Entity: ", entity_mult, wd_id.split('|')[0])
                entity = {"entity":{"Sent": sent, "Token": entity_mult, "Tag": multitags, "Emb": multiemb, "Wd_Id": wd_id.split('|')[0], "Left": multileft, "Top": multitop, "Width": multiwidth, "Height": multiheight}}
                entities.append(entity)
                entity_mult = ""
                multient = False
            print(entities)
        results[x]= {"meta": meta, "entities": entities}
        json.dump(results, open(outfile, 'w', encoding='utf8'), indent=4)

def write_enriched_graphml(result_file, path_to_ocr, output_format): 
    """
    Use to integrate ocr files. Writes enriched .graphml files . 
    ---------
    result_file : str
        'entities-dict.json', output of process_tsv method.
    output_format : str
        Currently 'graphml' supported.
    path_to_ocr : str
        Path to the place where the ocr files should be written to
        
    Returns
    -----------
    str.
    """
    with open(result_file, 'r') as inp:
        if output_format ==  'graphml':
            doc_nodes = open(path_to_ocr +'OCRDocumentNodes.graphml', 'w', encoding="utf8")
            wiki_nodes = open(path_to_ocr +'WikiNodes.graphml', 'w', encoding="utf8")
            same_edges = open(path_to_ocr +'SameAsEdges.graphml', 'w', encoding="utf8")
            contains_edges = open(path_to_ocr +'DocContainsEntEdges.graphml', 'w', encoding="utf8")
            docs = json.load(inp)
            doc_node_count = 0
            wiki_node_count = 0
            unknown_count = 0
            contains_edges_count = 0
            attribute_list = ["Sent", "Token", "Emb", "Left", "Top", "Width", "Height"]
            id_dict = {}
            for doc in docs:
#                if doc_node_count == 1:
#                    break
                meta = docs[doc]['meta']
                node_id = "OCR" + meta["IdZDB"] + meta["date"]
                doc_nodes.write('<node id="' + node_id + '" labels=":OCRDocument"><data key="labels">:OCRDocument</data>')
                doc_nodes.write('<data key="' + 'Name' +'">' + doc.strip(".tsv") + '</data>')
                for ele in meta:
                    if ele == "date":
                        time = meta[ele]
                        year = time[0:4]
                        month = time[4:6] 
                        day = time[6:]
#                        doc_nodes.write('<data key="' + 'year' + '">' +  year + '</data>')
#                        doc_nodes.write('<data key="' + 'month' + '">' +  month + '</data>')
#                        doc_nodes.write('<data key="' + 'day' + '">' +  day + '</data>')
#                        doc_nodes.write('<data key="' + ele + '">' +  meta[ele] + '</data>')
                        doc_nodes.write('<data key="' + 'DateStrictBegin' + '">' +  day + "." + month + "." + year + '</data>')
                        doc_nodes.write('<data key="' + 'DateApproxBegin' + '">' + year + '</data>')
                    else:
                        doc_nodes.write('<data key="' + ele + '">' + meta[ele] + '</data>')                       
                doc_node_count += 1
                doc_nodes.write('</node>\n')
                entities = docs[doc]['entities']
                for ele in entities: # iterate through entities in doc
                    for entity in ele:
                        whole_entity = ele[entity]
                        wd_id = ele[entity]['Wd_Id']
                        ne_tag = ele[entity]['Tag'] # get entity type
                        if type(ne_tag) == list:
                            ne_tag = ne_tag[0]
                        ne_tag = ne_tag.strip('I-').strip('B-')
                        if wd_id in id_dict and ne_tag in id_dict[wd_id]:
                            contains_edges.write('<edge id="From' + node_id + 'ToWiki' + ne_tag + "_" + wd_id + "_" + str(contains_edges_count) + '" source="' + node_id + '" target="Wiki_'+ wd_id + '" label="DocContainsEnt"><data key="label">DocContainsEnt</data><data key="TypeAddInfo">' + 'directed' + '</data>')
                            for attribute in whole_entity:
                                if attribute in attribute_list:
                                    if not type(whole_entity[attribute]) == list:
                                        if attribute == "Token":
                                            token = whole_entity[attribute]
                                            token = re.sub("&", "&#38;", token)
                                            contains_edges.write('<data key="' + "Name" + '">' + token  + '</data>')
                                        else:
                                            contains_edges.write('<data key="' + attribute + '">' + whole_entity[attribute]  + '</data>')
                                    else: 
                                        contains_edges.write('<data key="' + attribute + '">' + ';;;'.join(x for x in whole_entity[attribute])  + '</data>')
                            contains_edges.write('</edge>\n')
                            contains_edges_count += 1
                            continue
                        elif wd_id in id_dict:
                            if not ne_tag in id_dict[wd_id]:  
                                # Wenn zwar Wd ID vorhanden, aber
                                # mit anderem Entitätstypen     
                                tags = []
                                if not type(id_dict[wd_id]) == list:
                                    tags.append(id_dict[wd_id])
                                    tags.append(ne_tag)
                                else:
                                    for tag in id_dict[wd_id]:
                                        tags.append(tag)
                                    tags.append(ne_tag)
                                id_dict[wd_id] = tags # Trotzdem neuen Node erstellen, da neuer Typ
                                name = ele[entity]['Token']
                                name = re.sub("&", "&#38;", name)
                                gnd_id = wd_id_to_gnd(wd_id)
                                if "PER" in ne_tag:
                                    wiki_nodes.write('<node id="' + 'Wiki_' + wd_id + '" labels=":PerName"><data key="labels">:PerName</data>')
                                elif "LOC" in ne_tag:
                                    wiki_nodes.write('<node id="' + 'Wiki_' + wd_id + '" labels=":GeoName"><data key="labels">:GeoName</data>')
                                elif "ORG" in ne_tag:
                                    wiki_nodes.write('<node id="' + 'Wiki_' + wd_id + '" labels=":CorpName"><data key="labels">:CorpName</data>')
                               # wiki_nodes.write('<node id="' + 'Wiki_' + wd_id + '" labels=":WikiName"><data key="labels">:WikiName</data>')
                                if len(gnd_id) >= 3:
                                    wiki_nodes.write('<data key="' + 'IdGND' + '">' + gnd_id  + '</data>') 
                                    sonar_equivalent = search_doublette(gnd_id, ne_tag)
                                    if len(sonar_equivalent) >= 4:
                                        same_edges.write('<edge id="From' + sonar_equivalent + 'ToWiki' + ne_tag + "_" + wd_id + '" source="' + sonar_equivalent + '" target="Wiki_'+ wd_id + '" label="SameAs" directed="false"><data key="label">SameAs</data><data key="TypeAddInfo">' + 'undirected' + '</data></edge>\n')
                                else:
                                    print("Goes to enrich entities!")
                                    properties = enrich_entity(wd_id, ele[entity]['Tag'] )
                                    for prop in properties:
                                        if properties[prop] == "-":
                                            continue
                                        else:
                                            wiki_nodes.write('<data key="' + prop + '">' + properties[prop] + '</data>')                                            
                                wiki_nodes.write('<data key="' + 'IdWikidata' + '">' + wd_id  + '</data>') 
                                wiki_nodes.write('<data key="' + 'Name' + '">' + name  + '</data>')
                                wiki_nodes.write('<data key="' + 'Source' + '">' + 'Wikidata'  + '</data>')
                               # wiki_nodes.write('<data key="' + 'Type' + '">' + ne_tag  + '</data>')
                                wiki_nodes.write('</node>\n')
                                wiki_node_count += 1
                                print("NE_Tag2: ", ne_tag, wd_id)
                                contains_edges.write('<edge id="From' + node_id + 'ToWiki' + ne_tag + "_" + wd_id + "_" + str(contains_edges_count) + '" source="' + node_id + '" target="Wiki_'+ wd_id + '" label="DocContainsEnt"><data key="label">DocContainsEnt</data><data key="TypeAddInfo">' + 'directed' + '</data>')
                                for attribute in whole_entity:
                                    if attribute in attribute_list:
                                        if not type(whole_entity[attribute]) == list:
                                            if attribute == "Token":
                                                token = whole_entity[attribute]
                                                token = re.sub("&", "&#38;", token)
                                                contains_edges.write('<data key="' + "Name" + '">' + token  + '</data>')
                                            else:
                                                contains_edges.write('<data key="' + attribute + '">' + whole_entity[attribute]  + '</data>')
                                        else: 
                                            contains_edges.write('<data key="' + attribute + '">' + ';;;'.join(x for x in whole_entity[attribute])  + '</data>')
                                contains_edges.write('</edge>\n')
                                contains_edges_count += 1
                        elif not wd_id in id_dict:  #  Neue WikiName entity wird hinzugefügt
                            if not wd_id == "-":
                                id_dict[wd_id] = ne_tag
                                name = ele[entity]['Token']
                                name = re.sub("&", "&#38;", name)
                                gnd_id = wd_id_to_gnd(wd_id)
                                if "PER" in ne_tag:
                                    wiki_nodes.write('<node id="' + 'Wiki_' + wd_id + '" labels=":PerName"><data key="labels">:PerName</data>')
                                elif "LOC" in ne_tag:
                                    wiki_nodes.write('<node id="' + 'Wiki_' + wd_id + '" labels=":GeoName"><data key="labels">:GeoName</data>')
                                elif "ORG" in ne_tag:
                                    wiki_nodes.write('<node id="' + 'Wiki_' + wd_id + '" labels=":CorpName"><data key="labels">:CorpName</data>')
                               # wiki_nodes.write('<node id="' + 'Wiki_' + wd_id + '" labels=":WikiName"><data key="labels">:WikiName</data>')
                                if len(gnd_id) >= 3:
                                    wiki_nodes.write('<data key="' + 'IdGND' + '">' + gnd_id  + '</data>')
                                    sonar_equivalent = search_doublette(gnd_id, ne_tag)
                                    if len(sonar_equivalent) >= 4:
                                        same_edges.write('<edge id="From' + sonar_equivalent + 'ToWiki' + ne_tag + "_" + wd_id + '" source="' + sonar_equivalent + '" target="Wiki_'+ wd_id + '" label="SameAs" directed="false"><data key="label">SameAs</data><data key="TypeAddInfo">' + 'undirected' + '</data></edge>\n')                                       
                                else:
                                    print("Goes to enrich entities!")
                                    properties = enrich_entity(wd_id, ele[entity]['Tag'] )
                                    for prop in properties:
                                        if properties[prop] == "-":
                                            continue
                                        else:
                                            wiki_nodes.write('<data key="' + prop + '">' + properties[prop] + '</data>')                                 
                                wiki_nodes.write('<data key="' + 'IdWikidata' + '">' + wd_id  + '</data>') 
                                wiki_nodes.write('<data key="' + 'Name' + '">' + name  + '</data>')
                                wiki_nodes.write('<data key="' + 'Source' + '">' + 'Wikidata'  + '</data>')
                            elif wd_id == "-":
                                unknown_count += 1
                                wd_id = "Unknown" + str(unknown_count)
                               # wiki_nodes.write('<node id="' + 'Wiki_' + wd_id + '" labels=":WikiName"><data key="labels">:WikiName</data>')
                                if "PER" in ne_tag:
                                    wiki_nodes.write('<node id="' + 'Wiki_' + wd_id + '" labels=":PerName"><data key="labels">:PerName</data>')
                                elif "LOC" in ne_tag:
                                    wiki_nodes.write('<node id="' + 'Wiki_' + wd_id + '" labels=":GeoName"><data key="labels">:GeoName</data>')
                                elif "ORG" in ne_tag:
                                    wiki_nodes.write('<node id="' + 'Wiki_' + wd_id + '" labels=":CorpName"><data key="labels">:CorpName</data>') 
                                wiki_nodes.write('<data key="' + 'IdWikidata' + '">' + 'Unknown'  + '</data>')
                                wiki_nodes.write('<data key="' + 'Name' + '">' + ele[entity]['Token']  + '</data>')
                                wiki_nodes.write('<data key="' + 'Source' + '">' + 'Wikidata'  + '</data>')
                           # wiki_nodes.write('<data key="' + 'Type' + '">' + ne_tag  + '</data>')
                            wiki_nodes.write('</node>\n')
                            wiki_node_count += 1
                            contains_edges.write('<edge id="From' + node_id + 'ToWiki' + ne_tag + "_" + wd_id + "_" + str(contains_edges_count) + '" source="' + node_id + '" target="Wiki_'+ wd_id + '" label="DocContainsEnt"><data key="label">DocContainsEnt</data><data key="TypeAddInfo">' + 'directed' + '</data>')
                            for attribute in whole_entity:
                                if attribute in attribute_list:
                                    if not type(whole_entity[attribute]) == list:                                
                                        contains_edges.write('<data key="' + attribute + '">' + whole_entity[attribute]  + '</data>')
                                    else: 
                                        contains_edges.write('<data key="' + attribute + '">' + ';;;'.join(x for x in whole_entity[attribute])  + '</data>')
                            contains_edges.write('</edge>\n')
                            contains_edges_count += 1
                            
if __name__=='__main__': 
    fire.Fire()
#    process_tsv('D:/SoNAR/Enrich/batch3/', 'D:/SoNAR/Transformers/data/entities-dict.json')
#    write_enriched_graphml('D:/SoNAR/Transformers/data/entities-dict.json', 'D:/SoNAR/Transformers/data/ocr/', 'graphml')