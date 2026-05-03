import random

comprehension_regle=0
print("LA JUSTE CASE")
input("Êtes vous prêt à jouer ?")
regle=input("Connaissez vous les règles du jeu ? (0:si oui)(1:si c'est non)")
while not regle.isdigit() or not int(regle) in [0, 1]:
        regle=input("Connaissez vous les règles du jeu ? (0:si oui)(1:si c'est non)")
if int(regle)==1:
    print("Voici les règles :")
    print("Le principe est simple : il suffit d'estimer la place de la juste case choisie dans une grille. Cette case est choisie aléatoirement à chaque nouvelle partie et chaque nouveau niveau ! ")
    comprehension_regle=input("Vous avez tout compris ? (si oui: écrire 0, sinon écrire 1)")
    while not comprehension_regle.isdigit() or not int(comprehension_regle) in [0, 1]:
        comprehension_regle=input("Vous avez tout compris ? (si oui: écrire 0, sinon écrire 1)")
if int(comprehension_regle)==1:
    print("Ce n'est pas grave vous allez comprendre en jouant !")
niveau=0
piège=0
for nombre_niveau in range (5,11):
    niveau=nombre_niveau
    numero_niveau=niveau-4
    print()
    print("vous etes au niveau",numero_niveau)
    if numero_niveau==1:
        print("voici la grille, la juste case est caché dedans")
        print("La distance se calcule par la moyenne des distances pour vous compliquer la tache, Bonne chance")


    def creer_grille(lignes, colonnes, valeur_initiale=None):
        return [[valeur_initiale for _ in range(colonnes)] for _ in range(lignes)]

    def remplir_grille(grille, valeur):
        lignes = len(grille)
        colonnes = len(grille[0]) if grille else 0
        for i in range(lignes):
            for j in range(colonnes):
                 grille[i][j] = valeur
        for ligne in grille:
            print(" ".join(str(val) for val in ligne))
            print()

    grille= creer_grille(niveau,niveau)
    remplir_grille(grille, 0)  
    a=0
    ordo_alea=random.randint(0,niveau-1)
    absci_alea=random.randint(0,niveau-1)
    grille[ordo_alea-1][absci_alea-1]=1
    print()
    ordo_piege=random.randint(0,niveau-1)
    absci_piege=random.randint(0,niveau-1)
    if ordo_alea==ordo_piege and absci_alea==absci_piege :
        ordo_piege=random.randint(0,niveau-1)
        absci_piege=random.randint(0,niveau-1)
    case_trouver=1
    while case_trouver!=0:
        ordo_case=input("quelle est l’ordonnée de la juste case ? (pour toi)")
        while not ordo_case.isdigit(): 
            ordo_case=input("DONNEZ UN CHIFFRE !!!")
        absci_case=input("quelle est l'abscisse de la juste case ? (pour toi)")
        while not absci_case.isdigit():  
            absci_case=input("DONNEZ UN CHIFFRE !!!")
        ordo_case=int(ordo_case)
        absci_case=int(absci_case)
        if ordo_case<0 or absci_case<0 or ordo_case>len(grille) or absci_case>len(grille):
            print()
            print("Vous etes pas dans la grille")
        else:
            if ordo_case==ordo_piege and absci_case==absci_piege and nombre_niveau!=10 :
                case_trouver=0
                piège=(-1)+piège
                print()
                print("Vous êtes tombés sur la case piège, il faut recommencer le niveau !")
                print()
                a=1
                while a!=0:
                    print("vous etes au niveau",numero_niveau)
                    remplir_grille(grille, 0)  
                    ordo_alea=random.randint(0,niveau-1)
                    absci_alea=random.randint(0,niveau-1)
                    grille[ordo_alea-1][absci_alea-1]=1
                    print()
                    ordo_piege=random.randint(0,niveau-1)
                    absci_piege=random.randint(0,niveau-1)
                    if ordo_alea==ordo_piege and absci_alea==absci_piege :
                        ordo_piege=random.randint(0,niveau-1)
                        absci_piege=random.randint(0,niveau-1)
                    case_trouver=1
                    while case_trouver!=0:
                        ordo_case=input("quelle est l’ordonnée de la juste case ? (pour toi)")
                        while not ordo_case.isdigit(): 
                            ordo_case=input("DONNEZ UN CHIFFRE !!!")
                        absci_case=input("quelle est l'abscisse de la juste case ? (pour toi)")
                        while not absci_case.isdigit():  
                            absci_case=input("DONNEZ UN CHIFFRE !!!")
                        ordo_case=int(ordo_case)
                        absci_case=int(absci_case)
                        if ordo_case<0 or absci_case<0 or ordo_case>len(grille) or absci_case>len(grille):
                            print()
                            print("Vous etes pas dans la grille")
                        else:
                            if ordo_case==ordo_piege and absci_case==absci_piege and nombre_niveau!=10 :
                                case_trouver=0
                                piège=(-1)+piège
                                print()
                                print("Vous êtes tombés sur la case piège, il faut recommencer le niveau !")
                                print()
                                a=1
                            else:
                                result_x=ordo_alea-ordo_case
                                result_y=absci_alea-absci_case
                                moyenne_distance=int(abs(result_x)+abs(result_y)//2)
                                if result_x==0 and result_y==0:
                                    case_trouver=0
                                    print()
                                    print("Bravo vous avez trouvé la solution ")
                                    a=0
                                else :
                                    if moyenne_distance==1 or moyenne_distance==0:
                                        print("tu y es presque, trop proche pour que je donne des indices")
                                    else :
                                        print("tu y es presque")
                                        print("tu es au alentour de",moyenne_distance,"cases")    
            else:
                result_x=ordo_alea-ordo_case
                result_y=absci_alea-absci_case
                moyenne_distance=int(abs(result_x)+abs(result_y)//2)
                if result_x==0 and result_y==0:
                    case_trouver=0
                    print()
                    print("Bravo vous avez trouvé la solution ")
                else :
                    if moyenne_distance==1 or moyenne_distance==0:
                        print("tu y es presque, trop proche pour que je donne des indices")
                    else :
                        print("tu y es presque")
                        print("tu es au alentour de",moyenne_distance,"cases!") 
                
    if nombre_niveau == 10 and a==0:
        piège=0
        a=1
        difficulté=input("Combien de difficulté voulait vous ? (de 1 à 10)")
        while not difficulté.isdigit():
            difficulté=input("Combien de difficulté voulait vous ? (de 1 à 10)")
        difficulté=int(difficulté)
        
        for nombre_de_piege in range (1,difficulté+1):
            ordo_alea=random.randint(0,niveau-1)
            absci_alea=random.randint(0,niveau-1)
            grille[ordo_alea-1][absci_alea-1]=1
            print()  
            print("Vous etes a la difficulté", nombre_de_piege)
            remplir_grille(grille, 0)
            for y in range (1,nombre_de_piege+1):
                ordo_piege=random.randint(0,niveau-1)
                absci_piege=random.randint(0,niveau-1)
                if ordo_alea==ordo_piege and absci_alea==absci_piege :
                    ordo_piege=random.randint(0,niveau-1)
                    absci_piege=random.randint(0,niveau-1)
                liste_ordo_piege=[]
                liste_ordo_piege.append(ordo_piege)
                liste_absci_piege=[]
                liste_absci_piege.append(absci_piege)
            case_trouver=1
            while case_trouver!=0:
                ordo_case=input("quelle est l’ordonnée de la juste case ? (pour toi)")
                while not ordo_case.isdigit(): 
                    ordo_case=input("DONNEZ UN CHIFFRE !!!")
                absci_case=input("quelle est l'abscisse de la juste case ? (pour toi)")
                while not absci_case.isdigit():  
                    absci_case=input("DONNEZ UN CHIFFRE !!!")
                ordo_case=int(ordo_case)
                absci_case=int(absci_case)
                if ordo_case<0 or absci_case<0 or ordo_case>len(grille) or absci_case>len(grille):
                    print()
                    print("Vous etes pas dans la grille")
                else:
                    i=0
                    for i in range (0,len(liste_ordo_piege)):
                        if ordo_case==liste_ordo_piege[i] and absci_case==liste_absci_piege[i] and nombre_niveau!=5:
                            case_trouver=0
                            piège=(-1)+piège
                            print()
                            print("Vous êtes tombés sur la case piège, il faut recommencer le niveau !")
                            print()
                            a=1
                            while a!=0:
                                print("vous etes au niveau",nombre_de_piege)
                                remplir_grille(grille, 0)  
                                ordo_alea=random.randint(0,niveau-1)
                                absci_alea=random.randint(0,niveau-1)
                                grille[ordo_alea-1][absci_alea-1]=1
                                print()
                                for y in range (0,nombre_de_piege):
                                    ordo_piege=random.randint(0,niveau-1)
                                    absci_piege=random.randint(0,niveau-1)
                                    if ordo_alea==ordo_piege and absci_alea==absci_piege :
                                        ordo_piege=random.randint(0,niveau-1)
                                        absci_piege=random.randint(0,niveau-1)
                                    liste_ordo_piege=[]
                                    liste_ordo_piege.append(ordo_piege)
                                    liste_absci_piege=[]
                                    liste_absci_piege.append(absci_piege)
                                case_trouver=1
                                while case_trouver!=0:
                                    ordo_case=input("quelle est l’ordonnée de la juste case ? (pour toi)")
                                    while not ordo_case.isdigit(): 
                                        ordo_case=input("DONNEZ UN CHIFFRE !!!")
                                    absci_case=input("quelle est l'abscisse de la juste case ? (pour toi)")
                                    while not absci_case.isdigit():  
                                        absci_case=input("DONNEZ UN CHIFFRE !!!")
                                    ordo_case=int(ordo_case)
                                    absci_case=int(absci_case)
                                    if ordo_case<0 or absci_case<0 or ordo_case>len(grille) or absci_case>len(grille):
                                        print()
                                        print("Vous etes pas dans la grille")
                                    else:
                                        if ordo_case==liste_ordo_piege[i] and absci_case==liste_absci_piege[i] and nombre_niveau!=5 :
                                            case_trouver=0
                                            piège=(-1)+piège
                                            print()
                                            print("Vous êtes tombés sur la case piège, il faut recommencer le niveau !")
                                            print()
                                            a=1
                                        else:
                                            result_x=ordo_alea-ordo_case
                                            result_y=absci_alea-absci_case
                                            moyenne_distance=int(abs(result_x)+abs(result_y)//2)
                                            if result_x==0 and result_y==0:
                                                case_trouver=0
                                                print("Bravo vous avez trouvé la solution ")
                                                a=0
                                            else :
                                                print("tu y es presque")
                                                print("tu es au alentour de",moyenne_distance,"cases") 
                        else:
                            result_x=ordo_alea-ordo_case
                            result_y=absci_alea-absci_case
                            moyenne_distance=int(abs(result_x)+abs(result_y)//2)
                            if result_x==0 and result_y==0:
                                case_trouver=0
                                print()
                                print("Bravo vous avez trouvé la solution ")
                            else :
                               print("tu y es presque")
                               print("tu es au alentour de",moyenne_distance,"cases")
print()
print("Vous avez fini le jeu, vous etes un genie")
print()
print("Merci d'avoir jouer !")
print()
input("Avez-vous aimé ?")
