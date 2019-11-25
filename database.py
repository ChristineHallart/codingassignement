# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:51:38 2019

@author: chris
"""
import copy

class Database:
    def __init__(self, corename):
        self.graph={corename:{"parent":None, "sons":[], "g_cov":False}}
        self.extract=[]
     
    @staticmethod
    def create_node(parent):
        return {"parent":parent,
                "sons":[],
                "c_cov":False}
             
    def add_nodes(self,nodelist):
        oldtree=copy.deepcopy(self.graph)
        for elements in nodelist:
            if (elements[1] in self.graph) and (elements[0] not in self.graph): #not adding nodes without a parent and existing nodes 

                #Add son to existing node
                sons=self.graph.get(elements[1]).get("sons")
                sons.append(elements[0])
                self.graph[elements[1]]["sons"]=sons
                
                #Change cov of brothers
                if elements[1] in oldtree:
                    exsons=oldtree.get(elements[1]).get("sons") #get node's sons before update
                    for bro in exsons:
                        self.graph[bro]["c_cov"]=True
                
                #Add newnode
                newnode=self.create_node(elements[1])
                self.graph[elements[0]]=newnode
            else :
                print("a node couldn't have been had to the graph")
        
#                     
    def add_extract(self,extract):
        self.extract=extract
      
    def get_extract_status(self):
        status= {}
        print(self.extract.keys())
        for key in list(self.extract.keys()): #key=img00x...
            
            labels=self.extract[key] #label=[...]
            print("labels",labels)
            if labels==[]: #if there's no label, dont go further
                status[key]="valid"
                continue
            else:
                stats=[]
                statu=["valid","granularity_staged","coverage_staged","invalid"] #different status, sort by priority
                for label in labels:
                    #invalid case
                    if label not in self.graph:
                        stats.append(3)
                        continue #no need to search further in that case
                    #coverage staged case
                    if self.graph.get(label).get("c_cov")==True:
                        stats.append(2)
                        continue #idem
                    #granularity staged case
                    if self.graph.get(label).get("sons"):
                        stats.append(1)
                    else:
                    #valid case
                        stats.append(0)
                status[key]=statu[max(stats)]
                    
    
        return status
            
            