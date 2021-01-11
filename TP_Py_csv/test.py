import csv
import os.path

mode=0o777
parent_dir = "C:\test"
# Directory 
#
#print(row['nom_departement'])
dirNomRegion = "test"


path = os.path.join(parent_dir, dirNomRegion)
    #chemin acces + nom region	
if not os.path.exists(path):
	#creation du dossier "dirNomRegion"(=nom de la region) dans repertoire "parent_dir"(=chemin acces)
	os.mkdir(path) 