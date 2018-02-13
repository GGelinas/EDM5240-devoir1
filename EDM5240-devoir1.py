'''
Script Python sur les posts de médias québécois
Titre: EDM5240-devoir1
Réalisé par Geneviève Gélinas / GELG19608607 dans le cadre du cours EDM5240 - Technologie de l'information appliquée au journalisme
Date de réalisation: Samedi 10 février 2017

Description général du script: 
Écrire un script qui calcule l'engagement total(partages, réactions et commentaires) de tous les médias québécois présents dans la liste et ensuite le calculer pour chaque média et en donner les détails.
'''


#coding: utf-8

liste=[] #Création/ouverture de listes pour venir y positionner notre premier élément, dans ce cas-ci, le nom du média.
tamponliste=[]
listeref=[]
j=0

boiteA=publications[0][0] #Positionnement du premier index (nom du média) de notre fichier source dans une variable.
tamponliste.append(boiteA)
liste.append(tamponliste)
listeref.append(boiteA) #Création d'une liste référence qui permettra la comparaison entre les noms des médias.


#Première boucle avec condition d'une différence qui permet de lire le fichier source au complet et de créer des listes avec les différents noms des médias.
for publication in publications: 
	boiteB=publications[j][0]
	
	if boiteB != boiteA:
		tamponliste=[]
		tamponliste.append(boiteB)
		liste.append(tamponliste)
		listeref.append(boiteB)
		boiteA=boiteB
	j+=1

	
#Deuxième boucle avec trois conditions intégrées qui permet de calculer le nombre de posts par média.
boiteA=publications[0][0]
j=0
g=0
publicationstotal=0
listemedia=[]

for publication in publications:
	boiteB=publications[j][0]
	test=len(publications)-1

	if boiteB==boiteA: 	#1ere condition sert à comparer les pareils et les compiler.
		publicationstotal+=1
		
	if boiteB != boiteA:	#2e condition sert à détecter les différents.
		liste[g].append(publicationstotal)
		publicationstotal=0
		boiteA=boiteB
		g+=1

	if j==test:		#3e condition assure qu'il compte tous les posts, même le dernier.
		liste[g].append(publicationstotal)
	j+=1

	
#Troisième boucle sert à calculer le nombre de partages total, le nombre de réactions total et le nombre de commentaires total pour l'ensemble des médias
# et ainsi calculer l'engagement total de tous les médias.
e=0
grandtotal=0
partagestotal=0
reactionstotal=0
commentairestotal=0
for publication in publications:
	partagestotal+=publications[e][3]
	reactionstotal+=publications[e][4]
	commentairestotal+=publications[e][5]
	grandtotal+=publications[e][3]+publications[e][4]+publications[e][5]
	e+=1
print ("Pour l'ensemble des 101 médias de cet échantillon, on compte",partagestotal,"partages,",reactionstotal,"réactions,",commentairestotal,"commentaires ainsi qu'un engagement total de",grandtotal,"en 2017.")


#Quatrième boucle contient deux boucles dont une avec deux conditions. Elles servent à calculer par média le nombre de partages, réactions, commentaires et son engagement.
#Chaque nombre calculé sera ensuite ajouté comme élément à la liste[].
k=0
for i in liste:
	n=0
	total=0
	partages=0
	reactions=0
	commentaires=0

	for publication in publications:
			if listeref[k]==publications[n][0]:
				partages+=publications[n][3]
				reactions+=publications[n][4]
				commentaires+=publications[n][5]
				total+=publications[n][3]+publications[n][4]+publications[n][5]
				n+=1
			else:
				n+=1
		
	liste[k].append(partages)
	liste[k].append(reactions)
	liste[k].append(commentaires)
	liste[k].append(total)
	k+=1

#Cinquième boucle qui insère un compteur et permet de placer un élément de la liste[] par ligne.
#Permet de peaufiner l'affichage en y insérant les index de la liste[] à la bonne place dans une phrase.
n=0
for lettre in liste:
	n+=1
	print (n,"-",lettre[0],"- Les",lettre[1],"publications du média", lettre[0],"ont été partagées", lettre[2], "fois, ont provoqué", lettre[3],"réactions et ont généré", lettre[4], "commentaires, pour un engagement total de", lettre[5], "en 2017.")

