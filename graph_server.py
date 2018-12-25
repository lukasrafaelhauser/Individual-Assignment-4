#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 14:20:34 2018

@author: l-r-h
"""

#%%

  #  In this exercise we will create an HTTP server to which we can upload a
  # graph and in which we can get the degrees of separation between two nodes
  #in the graph.
  #1. Create a route in the server to which the user can upload a graph using
  # JSON and using the POST http method. The JSON data should be
#passed as part of the request body, not in the URL.
#2. Create a route to get the degrees of separation between two nodes in
#the previously uploaded graph.
#localhost:5000/degrees_of_separation/<origin>/<destination>.
#You can use any code we want from the exercises we’ve done in class
#related to graphs.
  
#%%


from flask import Flask, jsonify, request

server = Flask("Graph Server")

@server.route('/home')
def home_fct():
    return "Hi Pepe - Merry Christmas"

@server.route('/upload-graph', methods=['POST'])
def upload_graph():
    body = request.get_json()
    return jsonify(body)

@server.route('/degrees-of-separation/<origin>/<destination>', methods=['GET'])
def find_path(origin, destination, graph='', path=[]):
        
    graph = request.get_json()
    
    path = path + [origin]
    
    if origin == destination:
        return jsonify(len(path)-1)
    
    if origin not in graph:
        return jsonify("Origin not in graph")
    
    for node in graph[origin]:
        if node not in path:
            newpath = find_path(node, destination, graph, path)
            if newpath is not None:
                return newpath
  
    return jsonify(None)
                
server.run()