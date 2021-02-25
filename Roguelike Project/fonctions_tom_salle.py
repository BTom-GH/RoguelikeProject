import pygame
import copy
from random import *

pygame.init()

#Dictionnaire répertoriant tous les types de salles
salles={1:[[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
         ,[2,1,1,0,0,1,1,0,1,1,0,0,1,1,2]
         ,[2,1,0,0,0,0,0,0,0,0,0,0,0,1,2]
         ,[2,0,0,0,0,0,1,1,1,0,0,0,0,0,2]
         ,[2,0,1,0,0,1,1,1,1,1,0,0,1,0,2]
         ,[2,0,0,0,0,0,1,1,1,0,0,0,0,0,2]
         ,[2,1,0,0,0,0,0,0,0,0,0,0,0,1,2]
         ,[2,1,1,0,0,1,1,0,1,1,0,0,1,1,2]
         ,[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]],
        
        2:[[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
         ,[2,1,0,0,0,0,0,0,0,0,1,1,1,0,2]
         ,[2,0,1,0,0,0,0,0,0,0,0,0,0,0,2]
         ,[2,0,0,0,0,0,1,1,1,0,0,0,0,0,2]
         ,[2,0,0,0,1,1,0,0,0,1,1,0,0,0,2]
         ,[2,0,0,0,0,0,1,1,1,0,0,0,0,0,2]
         ,[2,0,0,0,0,0,0,0,0,0,0,0,0,0,2]
         ,[2,0,1,1,1,0,0,0,0,0,1,1,1,0,2]
         ,[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]],
        
        3:[[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
         ,[2,0,0,0,0,0,0,0,0,0,0,0,0,0,2]
         ,[2,0,0,0,0,0,0,1,0,0,0,0,0,0,2]
         ,[2,0,0,1,0,0,0,1,0,0,0,1,0,0,2]
         ,[2,0,0,1,0,0,0,1,0,0,0,1,0,0,2]
         ,[2,0,0,1,0,0,0,1,0,0,0,1,0,0,2]
         ,[2,0,0,0,0,0,0,1,0,0,0,0,0,0,2]
         ,[2,0,0,0,0,0,0,0,0,0,0,0,0,0,2]
         ,[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]],
        
        4:[[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
         ,[2,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
         ,[2,1,0,0,0,0,0,0,0,0,0,0,0,1,2]
         ,[2,1,0,0,0,0,0,0,0,0,0,0,0,1,2]
         ,[2,1,0,0,0,0,0,0,0,0,0,0,0,1,2]
         ,[2,1,0,0,0,0,0,0,0,0,0,0,0,1,2]
         ,[2,1,0,0,0,0,0,0,0,0,0,0,0,1,2]
         ,[2,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
         ,[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]],
        
        5:[[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
         ,[2,0,0,0,0,0,0,0,0,0,0,0,0,0,2]
         ,[2,0,0,0,0,0,0,0,0,0,0,0,0,0,2]
         ,[2,0,0,0,0,0,0,0,0,0,0,0,0,0,2]
         ,[2,0,0,0,0,0,0,0,0,0,0,0,0,0,2]
         ,[2,0,0,0,0,0,0,0,0,0,0,0,0,0,2]
         ,[2,0,0,0,0,0,0,0,0,0,0,0,0,0,2]
         ,[2,0,0,0,0,0,0,0,0,0,0,0,0,0,2]
         ,[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]}

#Modèle pour le niveau 1
niveau1=[[0,0,0,0,0,0,0,0,0,0,0,0,0]
        ,[0,0,0,0,0,0,0,0,0,0,0,0,0]
        ,[0,0,0,0,0,0,0,0,0,0,0,0,0]
        ,[0,0,0,0,0,0,0,0,0,0,0,0,0]
        ,[0,0,0,0,0,0,0,0,0,0,0,0,0]
        ,[0,0,0,0,0,0,0,0,0,0,0,0,0]
        ,[0,0,0,0,0,0,0,0,0,0,0,0,0]]

#Création des niveaux en ajoutant au hasard un nombre de salle définit en fonction de la progression
def niveaux(progression):
    global niveau1, salles,tableau
    l=[]
    #Change la taille du niveau et le nombre de salle en fonction de la progression (nombre de boss battus)
    if progression>2:
        for loop in range(progression):
            niveau1.append([0,0,0,0,0,0,0,0,0,0,0,0,0])
        if progression%2!=0:
            niveau1.append([0,0,0,0,0,0,0,0,0,0,0,0,0])
        if progression<6:
            for loop in range(int(progression**2)):
                l.append(randint(1,4))
        else:
            for loop in range(int(progression**1.9)):
                l.append(randint(1,4))
    
    for loop in range(3+int(progression*2)):
        l.append(randint(1,4))
    #récupère les coordonnées du point d'apparition (=spawn)   
    y=int(len(niveau1)/2)
    x=6
    n=-1
    
    #Réserve la place du niveau pour le spawn    
    if niveau1[y][x]==0:
        niveau1[y][x]=5
    #Ajoute les places des salles aléatoirement dans le niveau, tout en les gardant liées    
    while n<(len(l)-1):
        k=randint(1,4)
        if k==1 and x<12:
            x=x+1
        if k==2 and y<(len(niveau1))-1:
            y=y+1
        if k==3 and x>0:
            x=x-1
        if k==4 and y>0:
            y=y-1
                
        if niveau1[y][x]==0:
            n+=1
            niveau1[y][x]=l[n]
    
    #Remplace les places réservées par les salles par leurs équivalents dans le dictionnaire répertoriant les salles, et garde une copie avec uniquement leurs places (tableau)            
    tableau=copy.deepcopy(niveau1)
    for i in range(len(niveau1)):
        for u in range(12):
            if niveau1[i][u]!=0:
                try:
                    if niveau1[i+1][u]!=0:
                        if type(niveau1[i][u])!=list:
                            niveau1[i][u]=copy.deepcopy(salles[niveau1[i][u]])
                        niveau1[i][u][8][7]=3
                        niveau1[i][u][7][7]=0
                        if type(niveau1[i+1][u])!=list:
                            niveau1[i+1][u]=copy.deepcopy(salles[niveau1[i+1][u]])
                        niveau1[i+1][u][0][7]=3
                        niveau1[i+1][u][1][7]=0
                        if (i+1)==int(len(niveau1)/2) and u==6:
                            pass
                        else:
                            tableau[i+1][u]=1
                except:
                    pass
                try:
                    if niveau1[i][u+1]!=0:
                        if type(niveau1[i][u])!=list:
                            niveau1[i][u]=copy.deepcopy(salles[niveau1[i][u]])
                        niveau1[i][u][4][14]=3
                        niveau1[i][u][4][13]=0
                        if type(niveau1[i][u+1])!=list:
                            niveau1[i][u+1]=copy.deepcopy(salles[niveau1[i][u+1]])
                        niveau1[i][u+1][4][0]=3
                        niveau1[i][u+1][4][1]=0
                        if i==int(len(niveau1)/2) and (u+1)==6:
                            pass
                        else:
                            tableau[i][u+1]=1
                except:
                    pass
                if i==int(len(niveau1)/2) and u==6:
                    pass
                else:
                    tableau[i][u]=1
    
    return tableau, niveau1

class Salle:
    #Classe pour chaques salles d'un niveau
    def __init__(self,num,largeur_ecran,hauteur_ecran):
        self.num=num
        self.visite=0
        self.emplacement=None
        self.grille=None
        self.liste_collision=[]
        self.charge=False
        self.mur=pygame.transform.scale((pygame.image.load("mur.png").convert_alpha()),(int((largeur_ecran/16))+10,int((hauteur_ecran/9))))
        self.murg=pygame.transform.scale((pygame.transform.rotate(self.mur,90)),(int((largeur_ecran/16))+10,int((hauteur_ecran/9)+10)))
        self.murd=pygame.transform.scale((pygame.transform.rotate(self.mur,270)),(int((largeur_ecran/16))+5,int((hauteur_ecran/9)+10)))
        self.murb=pygame.transform.scale((pygame.transform.rotate(self.mur,180)),(int((largeur_ecran/16))+10,int((hauteur_ecran/9))))
        self.porte=pygame.transform.scale((pygame.image.load("porte_fermé.png").convert_alpha()),(int((largeur_ecran/16))+10,int((hauteur_ecran/9))))
        self.porteg=pygame.transform.scale((pygame.transform.rotate(self.porte,90)),(int((largeur_ecran/16))+10,int((hauteur_ecran/9)+10)))
        self.ported=pygame.transform.scale((pygame.transform.rotate(self.porte,270)),(int((largeur_ecran/16))+5,int((hauteur_ecran/9)+10)))
        self.porteb=pygame.transform.scale((pygame.transform.rotate(self.porte,180)),(int((largeur_ecran/16))+10,int((hauteur_ecran/9))))
        self.coin_hg=pygame.transform.scale((pygame.image.load("coin.png").convert_alpha()),(int((largeur_ecran/16))+10,int((hauteur_ecran/9))))
        self.coin_bg=pygame.transform.scale((pygame.transform.rotate(self.coin_hg,90)),(int((largeur_ecran/16))+10,int((hauteur_ecran/9)+10)))
        self.coin_bd=pygame.transform.scale((pygame.transform.rotate(self.coin_hg,180)),(int((largeur_ecran/16))+10,int((hauteur_ecran/9)+10)))
        self.coin_hd=pygame.transform.scale((pygame.transform.rotate(self.coin_hg,270)),(int((largeur_ecran/16))+10,int((hauteur_ecran/9)+10)))
        self.decor=pygame.transform.scale((pygame.image.load("rocher.png").convert_alpha()),(int((largeur_ecran/16)),int((hauteur_ecran/9))))
    
    def __str__(self):
        return f"Numéro de salle :{self.num}, Emplacement : {self.emplacement}, passage : {self.visite}"
    
    def setEmplacement(self,tableau,progression):
        #Récupère l'emplacement de la salle dans le niveau
        n=1
        
        if progression==1:
            if self.num=="spawn":
                self.emplacement=(6,3)
                self.passage()
            continuer=True
            while continuer==True:
                for l in range(7):
                    for c in range(12):
                        if tableau[l][c]==1:
                            if n==self.num:
                                self.emplacement=(c,l)
                                continuer=False
                            n+=1
                continuer=False
    
    def getEmplacement(self):
        #Renvoie l'emplacement de la salle
        return self.emplacement
    
    def recupGrille(self,niveau):
        #Récupère la grille(=liste avec les obstacles..) de la salle
        self.grille=niveau[self.emplacement[1]][self.emplacement[0]]

    
    def creationDecors(self,niveau,ecran,fond_jeu,largeur_ecran,hauteur_ecran):
        #Affiche les décors et obstacles de la salle, et récupère leurs hitbox et emplacements
        self.recupGrille(niveau)
        posx_case=largeur_ecran/15
        posy_case=hauteur_ecran/9
        for l in range(9):
            for c in range(15):
                #Affichage des portes
                if self.grille[l][c]==3:
                    pos={"pos_grille":(c,l), "pos_ecran":(posx_case*c,posy_case*l),"id":3}
                    self.liste_collision.append((pygame.Rect((posx_case*c,posy_case*l),(self.decor.get_size())),pos))
                #Affichage des murs et des coins
                if self.grille[l][c]==2:
                    pos={"pos_grille":(c,l), "pos_ecran":(posx_case*c,posy_case*l),"id":2}
                    self.liste_collision.append((pygame.Rect((posx_case*c,posy_case*l),(self.decor.get_size())),pos))
                #affichage des obstacles
                if self.grille[l][c]==1:
                    pos={"pos_grille":(c,l), "pos_ecran":(posx_case*c,posy_case*l),"id":1}
                    self.liste_collision.append((pygame.Rect((posx_case*c,posy_case*l),(self.decor.get_size())),pos))
        self.charge=True
        return self.liste_collision
        
    
    def afficherDecor(self,niveau,ecran,fond_jeu,largeur_ecran,hauteur_ecran):
        #Ré-affiche ou créé puis affiche les décors
        if self.charge==False:
            self.creationDecors(niveau,ecran,fond_jeu,largeur_ecran,hauteur_ecran)
        ecran.blit(fond_jeu,(0,0))
        for obstacle in self.liste_collision:
            
            if obstacle[1]["id"]==3:
                if obstacle[1]["pos_ecran"][1]/(hauteur_ecran/9)==0:
                    ecran.blit(self.porte,(obstacle[1]["pos_ecran"]))
                
                if obstacle[1]["pos_ecran"][1]/(hauteur_ecran/9)==8:
                    ecran.blit(self.porteb,(obstacle[1]["pos_ecran"]))

                if obstacle[1]["pos_ecran"][0]/(largeur_ecran/15)==0:
                    ecran.blit(self.porteg,(obstacle[1]["pos_ecran"]))
            
                if obstacle[1]["pos_ecran"][0]/(largeur_ecran/15)==14:
                    ecran.blit(self.ported,(obstacle[1]["pos_ecran"]))
        
                
            if obstacle[1]["id"]==2:
                
                if obstacle[1]["pos_ecran"][1]/(hauteur_ecran/9)==0:
                    if obstacle[1]["pos_ecran"][0]/(largeur_ecran/15)==0:
                        ecran.blit(self.coin_hg,(0,0))
                    elif obstacle[1]["pos_ecran"][0]/(largeur_ecran/15)==14:
                        ecran.blit(self.coin_hd,(obstacle[1]["pos_ecran"]))
                    else:
                        ecran.blit(self.mur,(obstacle[1]["pos_ecran"]))
                
                if obstacle[1]["pos_ecran"][1]/(hauteur_ecran/9)==8:
                    if obstacle[1]["pos_ecran"][0]/(largeur_ecran/15)==0:
                        ecran.blit(self.coin_bg,(obstacle[1]["pos_ecran"]))
                    elif obstacle[1]["pos_ecran"][0]/(largeur_ecran/15)==14:
                        ecran.blit(self.coin_bd,(obstacle[1]["pos_ecran"]))
                    else:
                        ecran.blit(self.murb,(obstacle[1]["pos_ecran"]))
                
                if obstacle[1]["pos_ecran"][0]/(largeur_ecran/15)==0 and obstacle[1]["pos_ecran"][1]/(hauteur_ecran/9)!=0 and obstacle[1]["pos_ecran"][1]/(hauteur_ecran/9)!=8:
                    ecran.blit(self.murg,(obstacle[1]["pos_ecran"]))
                
                if obstacle[1]["pos_ecran"][0]/(largeur_ecran/15)==14 and obstacle[1]["pos_ecran"][1]/(hauteur_ecran/9)!=0 and obstacle[1]["pos_ecran"][1]/(hauteur_ecran/9)!=8:
                    ecran.blit(self.murd,(obstacle[1]["pos_ecran"]))
            
            if obstacle[1]["id"]==1:
                ecran.blit(self.decor,(obstacle[1]["pos_ecran"]))
        pygame.display.flip()
    
    def getListe_collision(self):
        return self.liste_collision
                
                    
    def passage(self):
        #Méthode a utiliser lorsque le joueur est passé dans celle-ci
        self.visite=1

class listeSalles:
    #Classe listant toutes les salles du niveau
    def __init__(self,tableau,largeur_ecran,hauteur_ecran):
        self.nombre_salle=0
        self.tableau=tableau
        self.liste=[Salle("spawn",largeur_ecran,hauteur_ecran)]
    
    def compterSalles(self,progression):
        #Compte le nombre de salles en fonction de la progression (en accord avec la création du niveau cf ligne 72)
        if progression>2:
            if progression<6:
                self.nombre_salle=int(progression**2)
            else:
                self.nombre_salle=10+int(progression**1.9)
        self.nombre_salle=3+int(progression*2)
    
    def listerSalles(self,largeur_ecran,hauteur_ecran):
        #Liste et crée toutes les salles en leur attribuant un numéro 
        for loop in range(1,self.nombre_salle+1):
            self.liste.append(Salle(loop,largeur_ecran,hauteur_ecran))
    
    def setEmplacementSalles(self,progression,largeur_ecran,hauteur_ecran):
        #Ajoute les emplacements aux salles créés
        self.compterSalles(progression)
        self.listerSalles(largeur_ecran,hauteur_ecran)
        for loop in range (len(self.liste)):
            self.liste[loop].setEmplacement(self.tableau,progression)
    
    def afficherListe(self):
        #Affiche la liste de salles
        print(self.liste)
    
    def getListe(self):
        #Récupère la liste de salles
        return self.liste
