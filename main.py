#!/usr/bin/env python
# coding: utf8
import csv
import os

"""
os.mkdir("D:\\France")

"""

fichier = open("departements-france.csv", "r")
parent_dir = "D:\\France"
readerRegion = csv.DictReader(fichier)
readerDepart = csv.DictReader(fichier)
for row in readerRegion:
	dirNomRegion = row['nom_region']
	path = os.path.join(parent_dir, dirNomRegion) # chemin acces + nom region
	if not os.path.exists(path):
		os.mkdir(path) 
		print("repertoire region '% s' créé" % path ) 
	




"""

	dirNomDep = row['nom_departement']
	
		
	
			for row in readerDepart:
				parent_dir = path
				path = os.path.join(parent_dir, dirNomRegion)
				if not os.path.exists(path):




	
	subpath = os.path.join(path, dirNomDep) #chemin acces(region) + nom depart
	if not os.path.exists(subpath):
			# creation du dossier "directory"(=nom du departement) dans repertoire "parent_dir"(=chemin acces)
			#os.mkdir(path, mode) 
			print("repertoire departement '% s' créé" % dirNomDep ) 



	# mode 
	mode = 0o666
	par defaut 0o777
"""	 
"""Lecture
fichier = open("departements-france.csv", "r")
lecteurCSV = csv.reader(fichier, delimiter=",")
for ligne in lecteurCSV:
	print(ligne)	# Exemple avec la 1e ligne du fichier d'exemple : ['departement', 'numero', 'region']
fichier.close()
"""

"""creation
 solution n°1
	if not os.path.exists(path):
		#creation du dossier "directory"(=nom du departement) dans repertoire "parent_dir"(=chemin acces)
		os.mkdir(path, mode) 
	 	print("repertoire '% s' créé" % directory) 

	#solution n°2:
	try: 
	os.makedirs(path)
	except OSError:
	if not os.path.isdir(path):
	Raise
"""
