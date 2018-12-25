#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 15:06:18 2018

@author: l-r-h
"""

#%%

import requests

graph = {
    "a": ["b"],
    "b": ["d", "c"],
    "c": ["d", "e"],
    "d": ["e"],
    "e": [],
    "f": []
}

def upload_graph_client(graph): 
    data = graph
    request = requests.post("http://127.0.0.1:5000/upload-graph", json=data)
    return request.json()

def degrees_separation_client(origin, destination): 
    data = graph
    request = requests.get('http://127.0.0.1:5000/degrees-of-separation/{}/{}'.format(origin, destination), json=data)
    
    return request.json()