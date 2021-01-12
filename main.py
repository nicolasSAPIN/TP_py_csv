#!/usr/bin/env python
# coding: utf8

import json
import yaml
import csv
import os
import re

def isRoi(string):
	str = string
	match = re.search( 'Hugues|Robert|Henri|Philippe|Louis|Jean|Charles', str)
	if match:
		result = True
	else:
		result = False
	return result

fichierRegion = open("departements-france.csv", "r")
fichMonument =  open("liste-des-immeubles-proteges-au-titre-des-monuments-historiques.csv", "r")

with open('liste-des-immeubles-proteges-au-titre-des-monuments-historiques.json', encoding='utf8') as json_data:
    data_dict = json.load(json_data)

data_str = json.dumps(data_dict)

parent_dir = "D:\\France"
#parent_dir = " D:\\_FICHIERS\\_COURSetFORMATIONS\\2020 - EPSI RENNES\\_Formation\\_COURS\\_03_PYTHON\Workspace\\TP_Py_csv\\France"
readerRegion = csv.DictReader(fichierRegion)
readerMonument =  csv.DictReader(fichMonument)

for row in readerRegion:

	dirNumRegion = row['code_region']
	dirNomRegion = row['nom_region']
	dirNumDepartement = row['code_departement']
	dirNomDep = row['nom_departement']
	DirRegion= dirNumRegion + "_" + dirNomRegion
	DirDepart = dirNumDepartement + " - " + dirNomDep
	path = os.path.join(parent_dir, DirRegion) # chemin acces + nom region
	if not os.path.exists(path):
		os.mkdir(path) 
		print("repertoire region '% s' créé" % path ) 
	subpath = os.path.join(path, DirDepart) #chemin acces(region) + nom depart
	if not os.path.exists(subpath):
		os.mkdir(subpath) 
		print("repertoire departement '% s' créé" % dirNomDep )
		for monument in data_dict:
			monuCodeDept = monument['fields']['code_departement']

			monuNom = monument['fields']['tico']
			
			if "hist" in monument['fields']:
				monuDesc = monument['fields']['hist']
			else:
				 monuDesc = ""	
			
			monuCommune = monument['fields']['commune']

			if "sclx" in  monument['fields']:
				monuLatitude = monument['fields']['sclx']
			else:
				monuLatitude = ""

			if "coordonnees_ban" in monument['fields']:
				monuLongitude = monument['fields']['coordonnees_ban']
			else:
				monuLongitude = ""	

			if (monuCodeDept == dirNumDepartement):
				print("creation d'un fichier")

			if(isRoi(monuNom) | isRoi(monuDesc)):
				ymlfile = [{'nom': monuNom},{'description' : monuDesc},{'commune': monuCommune},{'localisation': {'latitude ':  monuLatitude, 'longitude' : monuLongitude }}]
				
				monumFichnom = subpath + "\\monument.yaml"
				monumFichCree = open( monumFichnom , 'w')
				yaml.dump(ymlfile, monumFichCree)
				monumFichCree.close()
				print("Fichier  '% s' créé" % dirNomDep)

fichierRegion.close()

