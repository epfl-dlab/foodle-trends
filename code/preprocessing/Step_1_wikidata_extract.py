from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
import time
sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
freebase_foods = pd.read_csv('data/freebase_foods.tsv',sep = "\t")

MIDs = freebase_foods['mid'].values
names = freebase_foods['name'].values
types = freebase_foods['types'].values

list_entries = []

not_found = 0
for cnt,MID in enumerate(MIDs):
    if cnt %10 == 0:
        print('done:',cnt,'/',len(freebase_foods))
        print('not found:',not_found)
        print('\n')
    
    ### Step 1: Find the entity
    
    time.sleep(1)
    
    query = """PREFIX wd: <http://www.wikidata.org/entity/>
    PREFIX wdt: <http://www.wikidata.org/prop/direct/>
    PREFIX wikibase: <http://wikiba.se/ontology#>

    SELECT  DISTINCT  ?s   WHERE {
     ?s wdt:P646 """ + '"' + MID+'"' + """ .
       SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
     }""";

    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    
    try:
        results = sparql.query().convert()
    except:
        print(cnt,'blocked. Backing off 10 min.')
        time.sleep(10*60)
        try:
            results = sparql.query().convert()
        except:
            continue
        
    
    #not found based on mid. 
    if len(results['results']['bindings']) == 0:
        not_found +=1
        continue
        
    ID = results['results']['bindings'][0]['s']['value'].split('/')[-1]

    
    ### Step 2: Get metadata

    time.sleep(1)

    query = """
    
    PREFIX wd: <http://www.wikidata.org/entity/>
    PREFIX wdt: <http://www.wikidata.org/prop/direct/>
    PREFIX wikibase: <http://wikiba.se/ontology#>
    
    SELECT ?wdLabel ?ps_Label  {
      VALUES (?company) {(wd:""" + ID + """)}
      ?company ?p ?statement .
      ?statement ?ps ?ps_ .
      ?wd wikibase:claim ?p.
      ?wd wikibase:statementProperty ?ps.

      OPTIONAL {
      ?statement ?pq ?pq_ .
      ?wdpq wikibase:qualifier ?pq .
      }
      SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" }
    } ORDER BY ?wd ?statement ?ps_
    """
    
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    try:
        results = sparql.query().convert()
    except:
        print(cnt,'blocked. Backing off 10 min.')
        time.sleep(10*60)
        
        try:
            results = sparql.query().convert()
        except:
            continue
    
    ### Save result
    
    entry = {}
    entry['mid'] = MID
    entry['qid'] = ID
    entry['name'] = names[cnt]
    entry['mid_types'] = types[cnt]
    for feature in results['results']['bindings']:
        entry[feature['wdLabel']['value']] = feature['ps_Label']['value']
        
    list_entries.append(entry)
    
pd.DataFrame(list_entries).to_csv('wikidata_info_entities.csv', index = False)