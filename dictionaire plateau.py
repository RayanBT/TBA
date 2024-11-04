dictionaire_plateau = {
#niveaux 0
"entée" : ["jardin" , "dépot afaire" , "escalier entée"] , 
"cour botanique" : ["jardin","bureau du professeur de botanique"] , 
"jardin" : ["entée" , "cour botanique"] ,
"dépot afaire" : ["entée"],
"bureau du professeur de botanique" : ["cour botanique"],
#niveaux 1
"couloir etage 1" : ["escalier niveau 1", "sale comune" , "cour magie" ,"dortoire grifondore"],
"sale comune" : ["couloir etage 1"],
"cour magie" : ["couloir etage 1" , "bureau du professeur de magie"],
"bureau du professeur de magie" : ["cour magie"],
"dortoire grifondore" : ["couloir etage 1"],
#niveaux 2
"couloir etage 2" : ["escalier niveau 2" , "cour animeaux magique" , "toilette" , "dortoire serpentard","cour de potion"],
"cour animeaux magique" : ["couloir etage 2","bureau du professeur des annimeaux magique"],
"bureau du professeur des annimeaux magique" : ["cour animeaux magique"],
"toilette" : ["couloir etage 2"],
"dortoire serpentard" : ["couloir etage 2"],
"cour de potion" : ["couloir etage 2", "bureau du professeur des potion"],
"bureau du professeur des potion" : ["cour de potion"],
#niveau 3
"couloir etage 3" : ["escalier niveau 3","dortoire ser d'aigle", "dortoire poufesoufle" , "cour de défance"],
"dortoire ser d'aigle" : ["couloir etage 3"],
"dortoire poufesoufle" : ["couloir etage 3"],
"cour de défance" : ["couloir etage 3" , "bureau du professeur de défance"],
"bureau du professeur de défance" : ["cour de défance"],
#escalier
"escalier entée" : ["entée" ,"escalier niveau 1" ,"escalier niveau 2" ,"escalier niveau 3"] , 
"escalier niveau 1" : ["escalier entée", "couloir etage 1" ,"escalier niveau 2" ,"escalier niveau 3"] , 
"escalier niveau 2" : ["escalier entée", "couloir etage 2" ,"escalier niveau 1" ,"escalier niveau 3"] , 
"escalier niveau 3" : ["escalier entée", "couloir etage 3" ,"escalier niveau 1" ,"escalier niveau 2"] , 
}
