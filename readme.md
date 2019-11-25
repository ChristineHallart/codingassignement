# Foodvisor Coding assignement

Dans ce répertoire se trouve le rendu pour le coding assignement de foodvior

## Getting Started

### Prerequisites

Python3


## Running the tests

Le fichier test.py execute importe les données fournies dans l'énoncé (les chemins sont à changer pour correspondre au chemin de vos fichiers json) 

```
with open(path+'graph_build.json','r') as json_file:
   build = json.load(json_file)
with open(path+'img_extract.json','r') as json_file:
   extract = json.load(json_file)
with open(path+'graph_edits.json','r') as json_file:
   edits = json.load(json_file)
with open(path+'expected_status.json','r') as json_file:
   res = json.load(json_file)
```

Le test ensuite effectué est celui présent dans l'énoncé:

```
status = {}
if len(build) > 0:
    # Build graph
    db = Database(build[0][0])
    if len(build) > 1:
    	db.add_nodes(build[1:])
    # Add extract
    db.add_extract(extract)
    # Graph edits
    db.add_nodes(edits)
    # Update status
    status = db.get_extract_status()
print(status)

```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Author

* **Christine Hallart**



