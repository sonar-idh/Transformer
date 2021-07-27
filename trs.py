# coding: utf-8

import gzip
import zipfile
import time
import datetime
from src.marcTransform import MARC21
from src.eadTransform import EAD
from enrich.transform_ocr import write_enriched_graphml, process_tsv
from enrich.merge import merge_all_files
import fire

if __name__=='__main__': 
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
    #    fn = 'C:/Users/elle01/Documents/SoNAR/sonar/Normdaten/GND_{}_MARC21XML_20190613.mrc.xml.gz'.format(filename)
        fn = 'D:/Datendump/GND_{}_MARC21XML_20190613.mrc.xml.gz'.format(filename)
        print('Process {}'.format(entity))
        
        # Laufzeit messen
        startTime = time.time()
        with gzip.open(fn, 'rt', encoding='utf-8') as f:
            gr = MARC21(f, dataType=dt, entityType=entity, outputFormat=of, dataSelection=dataSel)
            elapsedTime = time.time() - startTime
    
            # Report
            print('{} files converted in {} h {} min {} s\n'.format(entity, str(datetime.timedelta(seconds=int(elapsedTime))).split(':')[0], str(datetime.timedelta(seconds=int(elapsedTime))).split(':')[1], str(datetime.timedelta(seconds=int(elapsedTime))).split(':')[2]))
            
    
            
#    # Daten aus der ZDB, DNB
    dt="Bibliographic"     
    for filename, entity in [("ZDB_MARC21_20190305", "Zdb"), 
                             ("DNB_MARC21_20190613-1", "Dnb1"),
                             ("DNB_MARC21_20190613-2", "Dnb2"), 
                             ("DNB_MARC21_20190613-3", "Dnb3"), 
                             ("DNB_MARC21_20190613-4", "Dnb4")
                            ]:
        fn = 'Datendump/{}.mrc.xml.gz'.format(filename)
        
        print('Process {}'.format(entity))
        
        # Laufzeit messen
        startTime = time.time()
        with gzip.open(fn, 'rt', encoding='utf-8') as f:
            gr = MARC21(f, dataType=dt, entityType=entity, outputFormat=of, dataSelection=dataSel)
            elapsedTime = time.time() - startTime
    
            # Report
            print('{} files converted in {} h {} min {} s\n'.format(entity, str(datetime.timedelta(seconds=int(elapsedTime))).split(':')[0], str(datetime.timedelta(seconds=int(elapsedTime))).split(':')[1], str(datetime.timedelta(seconds=int(elapsedTime))).split(':')[2]))
    
    
    # Daten aus der SBB
    zfile = zipfile.ZipFile('Datendump/sbb_titel_2019-06-20_marcxml.zip', mode='r')
    count = 1
    for fn in zfile.namelist():
    
        if '.xml' in fn and count in range(0,51):
            entity = "Sbb{}".format(count)
            
            print('Process {}'.format(fn))
    
            # Laufzeit messen
            startTime = time.time()
            with zfile.open(fn) as f:
                gr = MARC21(f, dataType=dt, entityType=entity, outputFormat=of, dataSelection=dataSel)
                elapsedTime = time.time() - startTime
    
                # Report
                print('{} files converted in {} h {} min {} s\n'.format(entity, str(datetime.timedelta(seconds=int(elapsedTime))).split(':')[0], str(datetime.timedelta(seconds=int(elapsedTime))).split(':')[1], str(datetime.timedelta(seconds=int(elapsedTime))).split(':')[2]))
        count += 1
        
    # Daten aus der Kalliope
        
    print('Process Kpe'.format(fn))
    
    gr=EAD(filename = 'Datendump/KPE_EADXML_20190701.zip')
    
    def integrate_ocr(tsv_files, merged_file, ocr_data_path, all_data_path):
        """
        Use to process OCR files and merge all files
        into one .graphml file.
    
        Parameters
        ----------
        
        tsv_files : str
            Path to directory which contains ocr files in tsv format 
        merged_file : str
            Name and path of output file, name needs to end in '.graphml'
        ocr_data_path : str
            Name of directory which contains the 
            ocr .graphml files 
        all_data_path : str
            Name of directory which contains all .graphml
            files (except the ocr .graphml files), 
            should be in data/graphml/
            
        Returns
        -------
        None.
        """
        process_tsv(tsv_files, 'data/entities-dict.json')
        write_enriched_graphml("data/entities-dict.json", "data/ocr/", "graphml")
        merge_all_files(merged_file, ocr_data_path, all_data_path)
        
    #integrate_ocr('D:/SoNAR/Enrich/batch3/', 'data/merged/v_27072021.graphml', 'D:/SoNAR/Transformers/data/ocr/', 'D:/SoNAR/Transformers/data/graphml/' )
    fire.Fire()