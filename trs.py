# coding: utf-8

import gzip
import zipfile
import time
import datetime
from src.MarcTransform import MARC21
from src.EadTransform import EAD



# PARAMETER
of = 'graphml'
dataSel=True


# Daten aus der GND
dt="Authority"
for filename, entity in [("Personen", "PerName"),
                         ("Sachbegriffe", "TopicTerm"),
                         ("Werke", "UniTitle"), 
                         ("Geografikum", "GeoName"), 
                         ("Koerperschaften", "CorpName"),
                         ("Kongresse", "MeetName")
]:
    fn = 'C:/Users/elle01/Documents/SoNAR/sonar/Normdaten/GND_{}_MARC21XML_20190613.mrc.xml.gz'.format(filename)

    print('Prozess {}'.format(entity))
    
    # Laufzeit messen
    startTime = time.time()
    with gzip.open(fn, 'rt', encoding='utf-8') as f:
        gr = MARC21(f, dataType=dt, entityType=entity, outputFormat=of, dataSelection=dataSel)
        elapsedTime = time.time() - startTime

        # Report
        print('{} files converted in {} h {} min {} s\n'.format(entity, str(datetime.timedelta(seconds=int(elapsedTime))).split(':')[0], str(datetime.timedelta(seconds=int(elapsedTime))).split(':')[1], str(datetime.timedelta(seconds=int(elapsedTime))).split(':')[2]))
        

        
# Daten aus der ZDB, DNB
dt="Bibliographic"     
for filename, entity in [("ZDB_MARC21_20190305", "Zdb"), 
                         ("DNB_MARC21_20190613-1", "Dnb1"),
                         ("DNB_MARC21_20190613-2", "Dnb2"), 
                         ("DNB_MARC21_20190613-3", "Dnb3"), 
                         ("DNB_MARC21_20190613-4", "Dnb4")
                        ]:
    fn = 'C:/Users/elle01/Documents/SoNAR/sonar/Metadaten/{}.mrc.xml.gz'.format(filename)
    
    print('Prozess {}'.format(entity))
    
    # Laufzeit messen
    startTime = time.time()
    with gzip.open(fn, 'rt', encoding='utf-8') as f:
        gr = MARC21(f, dataType=dt, entityType=entity, outputFormat=of, dataSelection=dataSel)
        elapsedTime = time.time() - startTime

        # Report
        print('{} files converted in {} h {} min {} s\n'.format(entity, str(datetime.timedelta(seconds=int(elapsedTime))).split(':')[0], str(datetime.timedelta(seconds=int(elapsedTime))).split(':')[1], str(datetime.timedelta(seconds=int(elapsedTime))).split(':')[2]))


# Daten aus der SBB
zfile = zipfile.ZipFile('C:/Users/elle01/Documents/SoNAR/sonar/Metadaten/sbb_titel_2019-06-20_marcxml.zip', mode='r')
count = 1
for fn in zfile.namelist():

    if '.xml' in fn and count in range(0,51):
        entity = "Sbb{}".format(count)
        
        print('Prozess {}'.format(fn))

        # Laufzeit messen
        startTime = time.time()
        with zfile.open(fn) as f:
            gr = MARC21(f, dataType=dt, entityType=entity, outputFormat=of, dataSelection=dataSel)
            elapsedTime = time.time() - startTime

            # Report
            print('{} files converted in {} h {} min {} s\n'.format(entity, str(datetime.timedelta(seconds=int(elapsedTime))).split(':')[0], str(datetime.timedelta(seconds=int(elapsedTime))).split(':')[1], str(datetime.timedelta(seconds=int(elapsedTime))).split(':')[2]))
    count += 1
    
# Daten aus der Kalliope
print('Prozess Kpe'.format(fn))
gr=EAD(filename = 'C:/Users/elle01/Documents/SoNAR/sonar/Metadaten/KPE_EADXML_20190701.zip')