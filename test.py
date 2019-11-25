# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:23:35 2019

@author: chris
"""
#
from database import Database
import json

path='C:\\Users\\chris\\Downloads\\'
with open(path+'graph_build.json','r') as json_file:
   build = json.load(json_file)
with open(path+'img_extract.json','r') as json_file:
   extract = json.load(json_file)
with open(path+'graph_edits.json','r') as json_file:
   edits = json.load(json_file)
with open(path+'expected_status.json','r') as json_file:
   res = json.load(json_file)

# Get status (this is only an example, test your code as you please as long as it works)
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

