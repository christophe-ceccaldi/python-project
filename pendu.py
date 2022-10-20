
from random import randrange
# choisir un mot de façon aléatoire dans dico
opendic =open ("dico_france.txt", "r", encoding="iso-8859-1")
#var pour ouvrir le dico
fichier = opendic.read().splitlines()
opendic.close
#lire toute les lignes du dico et fermer
chw = fichier[randrange(len(fichier))]
# pacourir tout le fichier juqu'a la fin et choisir un mot aléatoire
displayw = "_" * (len(chw))
# pour afficher autant de _ que de lettre dans le mot choisi

deflevel = int(input("Bonjour, quelle niveau voulez-vous choisir 1 2 ou 3 ? :"))
print ("Vous avez choisi " , deflevel)
# demander quel niveau choisir
if deflevel == 1:
    chance = 10
    usedl = []
      # definir les niveaux et leurs options

    print("débutant")
    while  chance>0 and chw != displayw:
        lettre = (input("choisir une lettre :"))
        usedl.append(lettre)
        if lettre in chw:
            for i in range (len(chw)):
                if chw[i] == lettre:
                    displayw = displayw[:i] + lettre + displayw[i+1:]
        else: 
            print ("pas la bonne lettre", lettre) 
            chance=chance-1
        print ("il vous reste", chance)
        print ("les lettres déja utilisés", usedl)
        print (displayw)
        #boucle de jeux


elif deflevel == 2:
    chance = 7
    usedl = []
      # definir les niveaux et leurs options

    print("intermédiare")
    while  chance>0 and chw != displayw:
        lettre = (input("choisir une lettre :"))
        usedl.append(lettre)
        if lettre in chw:
            for i in range (len(chw)):
                if chw[i] == lettre:
                    displayw = displayw[:i] + lettre + displayw[i+1:]
        else: 
            print ("pas la bonne lettre", lettre) 
            chance=chance-1
        print ("il vous reste", chance)
        print ("les lettres déja utilisés", usedl)
        print (displayw)
         #boucle de jeux
   
elif deflevel == 3:
    chance = 5
    usedl = []
      # definir les niveaux et leurs options

    print("expert")
    while  chance>0 and chw != displayw:
        lettre = (input("choisir une lettre :"))
        usedl.append(lettre)
        if lettre in chw:
            for i in range (len(chw)):
                if chw[i] == lettre:
                    displayw = displayw[:i] + lettre + displayw[i+1:]
        else: 
            print ("pas la bonne lettre", lettre) 
            chance=chance-1
        print ("il vous reste", chance)
        print (displayw)
         #boucle de jeux
    if displayw == chw:
        print("Vous avez gagné")
    else:
        print("Vous avez perdu ! same player shoot again !")
    
     
  














#gameon = True
#while gameon == True:
 #   niv1 = 
 #  age = int(input("> whats your age? "))

    #if age == 50:
       # gameon = False
    #else:
       # print("woow, you are %d years old" % age)


