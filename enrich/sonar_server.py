
# -*- coding: utf-8 -*-

from neo4j import GraphDatabase
import re
import requests
import time
import json
import csv
#from collect_data import Entity

class Neo4jConnection:
    
    def __init__(self, uri, user, pwd):
        self.__uri = uri
        self.__user = user
        self.__pwd = pwd
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__pwd))
        except Exception as e:
            print("Failed to create the driver:", e)
        
    def close(self):
        if self.__driver is not None:
            self.__driver.close()
        
    def query(self, query, db=None):
        assert self.__driver is not None, "Driver not initialized!"
        session = None
        response = None
        try: 
            session = self.__driver.session(database=db) if db is not None else self.__driver.session() 
            response = list(session.run(query))
        except Exception as e:
            print("Query failed:", e)
        finally: 
            if session is not None:
                session.close()
        return response


#def write_matches_to_tsv(ent_type, outfile, result):
#    with open(outfile, 'w', encoding="utf8", newline="") as n:
#        if ent_type == "PerName":     
#            human = Entity(ent_type="PerName")
#            per_list = []
#            tsv_output = csv.writer(n, delimiter='\t')
#            tsv_output.writerow(["GND-ID", "Wikidata-ID"])
#            for record in result:
#                gnd_id = record.get('n.Id')
#                gnd_id = gnd_id.replace("(DE-588)", "")
#                per_list.append(gnd_id)
#            for per in per_list:
#                time.sleep(3.0)
#                wd_id = human.gnd_to_wd_id(per)
#                print(per)
#                tsv_output.writerow([per, wd_id])
#        elif ent_type == "CorpName":
#            organisation = Entity(ent_type="CorpName")
#            #print(result)
#            org_list = []
#            tsv_output = csv.writer(n, delimiter='\t')
#            tsv_output.writerow(["GND-ID", "Wikidata-ID"])
#            for record in result:
#                print(record)
#                gnd_id = record.get('n.Id')
#                gnd_id = gnd_id.replace("(DE-588)", "")
#                org_list.append(gnd_id)
#            for org in org_list:
#                print(org)
#                time.sleep(3.0)
#                wd_id = organisation.gnd_to_wd_id(org)
##                print(wd_id)
##                print(gnd_id)
#                tsv_output.writerow([org, wd_id])
          
        
    

#if __name__=='__main__':
#    conn = Neo4jConnection(uri="bolt+ssc://h2918680.stratoserver.net:7687", user="sonar", pwd="sonar2021")
##    query_string = "MATCH (n:PerName) RETURN n.Name, n.Id LIMIT 1000"
###    query_string = """MATCH (n:PerName)-[r]-()
###    RETURN n.Name, count(r) AS num
###    ORDER BY num desc LIMIT 15"""
#    query_string = "MATCH (n:CorpName) RETURN n.Name, n.Id LIMIT 20"
#    result = conn.query(query_string)  
#    print(result)
#    #write_matches_to_tsv("PerName", "statistics/gnd_to_wd_per1000.tsv", result)
    

        