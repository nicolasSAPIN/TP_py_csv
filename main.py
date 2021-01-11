

import csv
#!/usr/bin/env python
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

fichier = open("departements-france.csv", "r")
reader = csv.DictReader(fichier)

for row in reader:
	"""
	# mode 
	mode = 0o666
	par defaut 0o777
	"""
	mode=0o777

	# Parent Directory path 
	parent_dir ="D:\_FICHIERS\_COURSetFORMATIONS\2020 - EPSI RENNES\_Formation\_COURS\_03_PYTHON\Workspace\TP_Py_csv"
	# Directory 
	#
	#print(row['nom_departement'])
	dirNomRegion=row['nom_region']
	dirNomDep = "row['nom_departement']"
	# Path 
	path = os.path.join(parent_dir, dirNomRegion) #chemin acces + nom region	

	if not os.path.exists(path):
			#creation du dossier "dirNomRegion"(=nom de la region) dans repertoire "parent_dir"(=chemin acces)
			os.mkdir(path, mode) 

	
	subpath = os.path.join(path, dirNomDep) #chemin acces(region) + nom depart

	if not os.path.exists(subpath):
			#creation du dossier "directory"(=nom du departement) dans repertoire "parent_dir"(=chemin acces)
			os.mkdir(path, mode) 
			print("repertoire departement '% s' créé" % directory) 

	 
	
	
	
	
	
	
	



		
	
