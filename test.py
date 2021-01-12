#import yaml
import csv
import os
import re
import json




depatement="35"


with open('liste-des-immeubles-proteges-au-titre-des-monuments-historiques.json') as json_data:
    data_dict = json.load(json_data)

data_str = json.dumps(data_dict)

for monument in data_dict:
	print (monument['fields']['code_departement'])








"""



with open('liste-des-immeubles-proteges-au-titre-des-monuments-historiques.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';')
	for row in spamreader:
		print(row['code_departement'])




ymlfile = [{'nom': 'test'},{'description' :  'test'},{'commune':  'test'},{'localisation': {'latitude ':  'test', 'longitude' : 'test' }}]
monumFichnom = "D:\\France\\monument.yaml"
monumFichCree = open( monumFichnom , 'w')
yaml.dump(ymlfile, monumFichCree)
monumFichCree.close()
print("Fichier  '% s' créé" % monumFichnom ) 












String="Ler roi Robert"
ymlfile = [{'nom': 'test'},{'description' :  'test'},{'commune':  'test'},{'localisation': {'latitude ':  'test', 'longitude' : 'test' }}]
print(ymlfile)

,
monumFichnom = subpath + "\monument.yaml"]
monumFichCree = open( monumFichnom , 'w')
yaml.dump(ymlfile, monumFichCree)
monumFichCree.close()
print("Fichier  '% s' créé" % dirNomDep ) 

def isRoi(string):
	str = String
	match = re.search( 'Hugues|Robert|Henri|Philippe|Louis|Jean|Charles', str)
	if match:
		result = True
	else:
		result = False
	return result




m = re.search('(?<=abc)def', 'abcdef')
m.group(0)

regex = r"^Alors"
test_str = "Alors on danse !!!"
matches = re.finditer(regex, test_str)
for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

string = "Le roi Robert"


if(isRoi(string)):
	print ("OK")
else:
	print ("NON")

def isRoi(string):
		
	mon_tab = ["Hugues", "Robert", "Henri", "Philippe", "Louis", "Jean", "Charles"]
	for element in mon_tab:
		regex = r"^"+ element +" \" "
		test_str = string
		regex = r"^test"
		matches = re.finditer(regex, test_str)
		for matchNum, match in enumerate(matches):
    		matchNum = matchNum + 1
			if(matchNum)>0:
			result = True
		else
			result = False
	return result

"""

"""

for row in readerDepart:
				parent_dir = path
				path = os.path.join(parent_dir, dirNomRegion)
				if not os.path.exists(path):




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