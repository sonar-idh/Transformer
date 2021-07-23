# -*- coding: utf-8 -*-

import requests
from enrich.queries import per_wd
import re
import time
from enrich.sonar_server import Neo4jConnection



def wd_id_to_gnd(wd_id):
    url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql'
    try:
        time.sleep(2.0)
        data = requests.get(url, params={'query': "SELECT ?Entity WHERE {wd:%s wdt:P227 ?Entity.}" % (wd_id),
                                         'format': 'json'}).json()
        gnd_id = []
        for item in data['results']['bindings']:
            if gnd_id == []:
                gnd_id.append(item['Entity']['value'])
        return gnd_id[0]
    except:
        return "-"

#print(wd_id_to_gnd('Q5879'))

def gnd_to_wd_id(gnd_id):
    url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql'
    try:
        time.sleep(2.0)
        data = requests.get(url, params={'query': "SELECT ?Entity WHERE {?Entity wdt:P227 '%s'.}" % (gnd_id),
                                         'format': 'json'}).json()
        result = []
        for item in data['results']['bindings']:
            if result == []:
                result.append(item['Entity']['value'])
                wd_id= re.findall("[Q]\d*",str(result))
        return wd_id[0]
    except:
        return "Exception"
#print(gnd_to_wd_id('118540238'))

def get_wd_result(data, query):
    result = []
    date_list = ["Todestag", "Geburtsdatum"]
    query_var= re.findall("SELECT \?[a-zA-Z]*\s", query)
    query_var = query_var[0].split('?')
    query_var = query_var[1].strip(" ")
    if "Label" in query_var or query_var in date_list and not len(query_var)<2:
        if not "skos:altLabel" in query:
            for item in data['results']['bindings']:
                if result == []:
                    result.append(item[query_var]['value'])
            return result[0]
    elif not "Label" in query_var and not len(query_var)<2 :
        for item in data['results']['bindings']:
            if result == []:
                result.append(item[query_var]['value'])
                wd_id= re.findall("[Q]\d*",str(result))   
        return wd_id[0]
        
def search_doublette(gnd_id, ent_type):
    try:
        if ent_type == "LOC" or "B-LOC" or "I-LOC":
            ent_type = "GeoName OR n:CorpName"
        elif ent_type == "PER" or "B-PER" or "I-PER":
            ent_type = "PerName"
        elif ent_type == "ORG" or "B-ORG" or "I-ORG":
            ent_type = "CorpName OR n:GeoName"
        conn = Neo4jConnection(uri="bolt+ssc://h2918680.stratoserver.net:7687", user="sonar", pwd="sonar2021")
        query_string = "MATCH (n) WHERE (n:%s) AND n.Id ENDS WITH '%s' RETURN n.id" % (ent_type, gnd_id)
        result = conn.query(query_string)  
        for record in result:
            new_result = record[0]
            print(new_result)
            break
        return str(new_result)
    except:
        new_result = "-"
        return str(new_result)
    
def add_label(wd_id):
    url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql'
    try:
        label = wd_queries['Label'] % (wd_id)
        time.sleep(2.0)
        label_data = requests.get(url, params={'query': label, 'format': 'json'}).json()
        label_result = get_wd_result(label_data, label)
        return label_result            
    except:
        label_result = "-"
        return label_result 


def enrich_entity(wd_id, ent_type):
    url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql'
    if ent_type == "PER" or "B-PER" or "I-PER":
        properties = {}
        birthdate = per_wd['DateOfBirth'] % (wd_id)
        deathdate = per_wd['DateOfDeath'] % (wd_id)
        gender = per_wd['Gender'] % (wd_id)
        birthplace = per_wd['PlaceOfBirthName'] % (wd_id)
        deathplace = per_wd['PlaceOfDeathName'] % (wd_id)
        birthplaceid = per_wd['PlaceOfBirth'] % (wd_id)
        deathplaceid = per_wd['PlaceOfDeath'] % (wd_id)
        time.sleep(2.0)
        try:
            birth_data = requests.get(url, params={'query': birthdate, 'format': 'json'}).json()
    #            print(birth_data)
            birth_result = get_wd_result(birth_data, birthdate)
            birth_list = normalize_data(birth_result, "birthdate")
            dateApproxBegin = birth_list[0]
            dateStrictBegin = birth_list[2] + "." + birth_list[1] + "." + birth_list[0]
            properties["WdDateApproxBegin"] = dateApproxBegin
            properties["WdDateStrictBegin"] = dateStrictBegin
            properties["WdDateApproxOriginal"] = dateApproxBegin + "-" 
            properties["WdDateStrictOriginal"] = dateStrictBegin + "-"
        except:
            properties["WdDateApproxBegin"] = "-"
            properties["WdDateStrictBegin"] = "-"
            properties["WdDateApproxOriginal"] = "-" 
            properties["WdDateStrictOriginal"] = "-"
        time.sleep(2.0)
        try:
            death_data = requests.get(url, params={'query': deathdate, 'format': 'json'}).json()
    #            print(birth_data)
            death_result = get_wd_result(death_data, deathdate)
            death_list = normalize_data(death_result, "deathdate")
            dateApproxEnd = death_list[0]
            dateStrictEnd = death_list[2] + "." + death_list[1] + "." + death_list[0]
            properties["WdDateApproxEnd"] = dateApproxEnd
            properties["WdDateStrictEnd"] = dateStrictEnd
            properties["WdDateApproxOriginal"] = properties["WdDateApproxBegin"] + "-" + dateApproxEnd
            properties["WdDateStrictOriginal"] = properties["WdDateStrictBegin"] + "-" + dateStrictEnd
        except:
            properties["WdDateApproxEnd"] = "-"
            properties["WdDateStrictEnd"] = "-"
        time.sleep(2.0)
        try:
            gender_data = requests.get(url, params={'query': gender, 'format': 'json'}).json()
            #print(gender_data)
            gender_result = get_wd_result(gender_data, gender)
            #print(gender_result)
            if gender_result == "female" or "weiblich":
                gender_value = "0"
            elif gender_result == "male" or "männlich" or "maennlich": 
                gender_value = "1"
            properties["WdGender"] = gender_value
        except:
            properties["WdGender"] = "-"
        time.sleep(2.0)
        try:
            deathplace_data = requests.get(url, params={'query': deathplace, 'format': 'json'}).json()
            #print(deathplace_data)
            deathplace_result = get_wd_result(deathplace_data, deathplace)
            #print(deathplace_result)
            deathplace_result = re.sub("&", "&#38;", deathplace_result)
            properties["WdPlaceOfDeath"] = deathplace_result
        except:
            properties["WdPlaceOfDeath"] = "-"   
        time.sleep(2.0)
        try:
            birthplace_data = requests.get(url, params={'query': birthplace, 'format': 'json'}).json()
            #print(birthplace_data)
            birthplace_result = get_wd_result(birthplace_data, birthplace)
            #print(birthplace_result)
            birthplace_result = re.sub("&", "&#38;", birthplace_result)
            properties["WdPlaceOfBirth"] = birthplace_result
        except:
            properties["WdPlaceOfBirth"] = "-" 
        time.sleep(2.0)
        try:
            deathplaceid_data = requests.get(url, params={'query': deathplaceid, 'format': 'json'}).json()
            #print(deathplaceid_data)
            deathplaceid_result = get_wd_result(deathplaceid_data, deathplaceid)
            #print(deathplaceid_result)
            properties["WdPlaceOfDeathId"] = deathplaceid_result
        except:
            properties["WdPlaceOfDeathId"] = "-"   
        time.sleep(2.0)
        try:
            birthplaceid_data = requests.get(url, params={'query': birthplaceid, 'format': 'json'}).json()
            #print(birthplaceid_data)
            birthplaceid_result = get_wd_result(birthplaceid_data, birthplaceid)
            #print(birthplaceid_result)
            properties["WdPlaceOfBirthId"] = birthplaceid_result
        except:
            properties["WdPlaceOfBirthId"] = "-" 
            
        return properties
#            death_data =
#            time.sleep(2.0)
#            gender_data =

#            data = requests.get(url, params={query, 'format': 'json'}).json()
#        elif ent_type == "CorpOCR":
def normalize_data(indata, prop):
    """
    Transforms Wikidata results into the neccessary format
    to be added to SoNAR
    ---------
    indata : str
        result of query
    prop : str
        type of property (birthdate, deathdate etc.)
    """
    if prop == "birthdate" or "deathdate":
        result = indata.strip("T00:00:00Z")
        result = result.split("-") # format: yyyy-mm-dd
        return result
            
#if __name__ == '__main__':
    #search_per_props("Q5879", "118584596") # für Namen nicht name in native language nehmen, sondern label bei Tabelle
#    print(enrich_entity("Q5879", "PER"))
#    print(enrich_entity("Q70532", "PER"))
#     props = enrich_entity("Q567", "PER")
#     for prop in props:
#         print(prop)
#         print(props[prop])
