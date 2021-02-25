import pygame
import time
from fonctions_tom_salle import *


pygame.init()

def fenetre():
    #Crée une fenêtre vierge
    global ecran, icone, largeur_ecran,hauteur_ecran
    
    #taille de l'écran au format 16/9
    largeur_ecran=pygame.display.Info().current_w -pygame.display.Info().current_w%16
    hauteur_ecran=pygame.display.Info().current_h - pygame.display.Info().current_h%9
    
    #Surface écran pour pygame
    ecran = pygame.display.set_mode((largeur_ecran,hauteur_ecran), pygame.RESIZABLE)
    
    #icone et titre de la fenetre
    icone = pygame.image.load("Isaac.png").convert_alpha()
    pygame.display.set_icon(icone)
    pygame.display.set_caption("Roguelike Project")

class Personnage:
    #Crée une instance personnage avec son image et sa position
    def __init__ (self,image, x=0,y=0):
        self.image=pygame.image.load(image).convert_alpha()
        self.x=x
        self.y=y
        self.emplacement_niveau= (6,3)
    
    def hitbox(self):
        #Return le Rect du personnage
        return pygame.Rect((self.x,self.y),(self.image.get_size()))

    def setX(self,x):
        #change la position x du personnage
        self.x=x
    
    def setY(self,y):
        #change la position y du personnage
        self.y=y
    
    def getPos(self):
        #Récupère la position sur l'écran du personnage
        return self.x,self.y
    
    def getImage(self):
        #Récupère l'image du personnage
        return self.image
    
    def setEmplacementNiveau(self,salle):
        #Récupère la position (dans quel salle) est le personnage dans le niveau
        self.emplacement=salle.getEmplacement()
        salle.passage()
        
    def redimensionner(self):
        #redimensionne la taille du personnage pour qu'il rentre dans une case de jeu
        self.image=pygame.transform.scale(self.image,(int((largeur_ecran/16)),int((hauteur_ecran/9))))
        
    def afficher(self):
        #affiche le personnage sur l'écran
        perso=ecran.blit(self.image,(self.x,self.y))
    
    #Méthodes de déplacement du personnage
    def haut(self):
        #Le personnage monte et s'affiche
        self.y-=20
        self.afficher()
        
    def bas(self):
        #Le personnage descend et s'affiche
        self.y+=20
        self.afficher()
        
    def gauche(self):
        #Le personnage va à gauche et s'affiche
        self.x-=20
        self.afficher()
        
    def droite(self):
        #Le personnage va à droite et s'affiche
        self.x+=20
        self.afficher()
        
class Collision:
    #Classe à utiliser pour gérer les collisions (entre le joueur, son attaque, les obstacles...)
    def __init__(self,x,y,Salle,liste_rect=[]):
        self.x=x
        self.y=y
        self.coord=(self.x,self.y)
        self.liste_rect=liste_rect
        self.tolerance=100
        self.liste_collision=Salle.getListe_collision()
    
    def setListe_rect(self,pos,largeur_ecran,hauteur_ecran):
        #Récupère les hitbox(=rect) des obstacles autour de l'élément
        x =pos[0]
        y=pos[1]
        c= max(0,int(x/(largeur_ecran/15)))
        l=max(0,int(y/(hauteur_ecran/9)))
        case=(c,l)
        self.liste_rect=[]
        for rect in self.liste_collision:
            if rect[1]["pos_grille"]==case:
                self.liste_rect.append((rect[0],rect[1]["id"]))
                
            elif rect[1]["pos_grille"]==(case[0]+1,case[1]):
                self.liste_rect.append((rect[0],rect[1]["id"]))
                
            elif rect[1]["pos_grille"]==(case[0],case[1]+1):
                self.liste_rect.append((rect[0],rect[1]["id"]))
                
            elif rect[1]["pos_grille"]== (case[0]+1,case[1]+1):
                self.liste_rect.append((rect[0],rect[1]["id"]))
        return self.liste_rect
    
    def testCollision(self,hitbox_element,element,pos,largeur_ecran,hauteur_ecran,ecran):
        #test si il y a une collision et renvoie l'intersection si il y en a une
        self.setListe_rect(pos,largeur_ecran,hauteur_ecran)
        
        for obstacle in self.liste_rect:
            rect2=obstacle[0]
            #pygame.draw.rect(ecran,(255,0,0),rect2)
            #pygame.draw.rect(ecran,(255,0,0),hitbox_element)
            if hitbox_element.colliderect(rect2):
                if obstacle[1]==3:
                    #Changement de salle
                    print("porte")
                else:
                    self.deplacementCorrection(rect2,hitbox_element,element)
            
    def deplacementCorrection(self,rect2,hitbox_element,element):
            x1=0
            y1=0
            if abs(rect2.top - hitbox_element.bottom) < self.tolerance:
                    y1-=abs(rect2.top - hitbox_element.bottom)
                
            if abs(rect2.left - hitbox_element.right) < self.tolerance:
                    x1-=abs(rect2.left - hitbox_element.right)
                
            if abs(rect2.bottom - hitbox_element.top) < self.tolerance:
                    y1+=(rect2.bottom - hitbox_element.top)
                
            if abs(rect2.right - hitbox_element.left) < self.tolerance:
                    x1+=(rect2.right - hitbox_element.left)
                    
            if isinstance(element,Personnage):
                element.setX(element.getPos()[0]+x1)
                element.setY(element.getPos()[1]+y1)
            
class Attaque:
    def __init__(self, joueur ,image_atq_perso):
        self.image_atq_perso=pygame.image.load(image_atq_perso).convert_alpha()
        self.x=joueur.getPos()[0]
        self.y=joueur.getPos()[1]
        self.atqx=self.x
        self.atqy=self.y
        
    def attaque1(self,salle):
        
        salle.afficherDecor(niveau1,ecran,fond_jeu,largeur_ecran,hauteur_ecran)
        self.atqx+=20
        ecran.blit(self.image_atq_perso, (self.atqx, self.atqy))
            
        
            
    def refresh(self,joueur,actif):
        if actif==False:
            self.atqx=joueur.getPos()[0]
            self.atqy=joueur.getPos()[1]
        if self.atqx>1920:
            self.x=joueur.getPos()[0]
            self.y=joueur.getPos()[1]
            self.atqx=self.x
            self.atqy=self.y
            actif=False
        
            
def jeu():
    #Fonction principale du jeu
    global pos_perso_x, pos_perso_y,fond_jeu,ecran
    pygame.init()
    fenetre()
    fond_jeu = pygame.image.load("fond_jeu.png").convert_alpha()
    fond_jeu=pygame.transform.scale(fond_jeu,ecran.get_size())
    ecran.blit(fond_jeu,(0,0))
    progression=1
    tableau,niveau1=niveaux(progression)
    ListeS=listeSalles(tableau,largeur_ecran,hauteur_ecran)
    ListeS.setEmplacementSalles(progression,largeur_ecran,hauteur_ecran)
    ListeS.getListe()[0].creationDecors(niveau1,ecran,fond_jeu,largeur_ecran,hauteur_ecran)
    joueur=Personnage("Isaac.png")
    joueur.redimensionner()
    pos_perso_x=(int(largeur_ecran/2)-((joueur.getImage()).get_width()/2))
    pos_perso_y= ((hauteur_ecran/2)-((joueur.getImage()).get_height()/2))
    joueur.setX(pos_perso_x)
    joueur.setY(pos_perso_y)
    joueur.afficher()
    salle_actuelle=ListeS.getListe()[1]
    attaque=Attaque(joueur,"atq_perso.jpg")
    actif=False
    #Boucle de jeu
    continuer=True
    pygame.key.set_repeat(5,50)
    while continuer:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #Mouvements et attaque du joueur
                if event.unicode=="a":
                    attaque.refresh(joueur,actif)
                    actif=True
                    attaque.attaque1(salle_actuelle)
                if event.unicode=="s":
                    #Test des changements de salles en faisant bougeant le personnage (a retirer et ré-intégrer lorsqu'il touche une porte)
                    #ListeS.getListe()[0].creationDecors(niveau1,ecran,fond_jeu,largeur_ecran,hauteur_ecran)
                    
                    salle_actuelle.afficherDecor(niveau1,ecran,fond_jeu,largeur_ecran,hauteur_ecran)
                    actif=False
                    joueur.bas()
                    Collision(joueur.getPos()[0],joueur.getPos()[1],salle_actuelle).testCollision(joueur.hitbox(),joueur,joueur.getPos(),largeur_ecran,hauteur_ecran,ecran)
                    attaque.refresh(joueur,actif)
                    
                if event.unicode=="z":
                    salle_actuelle.afficherDecor(niveau1,ecran,fond_jeu,largeur_ecran,hauteur_ecran)
                    actif=False
                    joueur.haut()
                    Collision(joueur.getPos()[0],joueur.getPos()[1],salle_actuelle).testCollision(joueur.hitbox(),joueur,joueur.getPos(),largeur_ecran,hauteur_ecran,ecran)
                    attaque.refresh(joueur,actif)
                    
                if event.unicode=="q":
                    #ListeS.getListe()[2].creationDecors(niveau1,ecran,fond_jeu,largeur_ecran,hauteur_ecran)
                    
                    salle_actuelle.afficherDecor(niveau1,ecran,fond_jeu,largeur_ecran,hauteur_ecran)
                    actif=False
                    joueur.gauche()
                    Collision(joueur.getPos()[0],joueur.getPos()[1],ListeS.getListe()[1]).testCollision(joueur.hitbox(),joueur,joueur.getPos(),largeur_ecran,hauteur_ecran,ecran)
                    attaque.refresh(joueur,actif)
                    
                if event.unicode=="d":
                    #ListeS.getListe()[3].creationDecors(niveau1,ecran,fond_jeu,largeur_ecran,hauteur_ecran)
                    
                    salle_actuelle.afficherDecor(niveau1,ecran,fond_jeu,largeur_ecran,hauteur_ecran)
                    actif=False
                    joueur.droite()
                    Collision(joueur.getPos()[0],joueur.getPos()[1],ListeS.getListe()[1]).testCollision(joueur.hitbox(),joueur,joueur.getPos(),largeur_ecran,hauteur_ecran,ecran)
                    attaque.refresh(joueur,actif)
                    
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                continuer=ecranfin()
                
            if event.type ==pygame.QUIT:
                continuer = False
                
        if actif==True:
            attaque.attaque1(salle_actuelle)
            joueur.afficher()
    pygame.quit()


def options():
    #Menu options du menu principal
    fenetre()
    BLUE = (40, 120, 230)
    GREEN = (40, 230, 120)
    #Créations des textes et importations des images
    font = pygame.font.SysFont('Arial', 24)
    prompt = font.render('Réglez le volume, de 0 pour couper le son à 1 (Utilisez . comme virgule) : ', True, BLUE)
    prompt_rect = prompt.get_rect(center=(ecran.get_rect().center))
    boutonv= pygame.image.load("bouton_volume.png").convert_alpha()
    boutonv_p =pygame.image.load("bouton_volumep.png").convert_alpha()
    bouton_volume=boutonv.get_rect()
    bouton_volume.center=ecran.get_rect().center
    bouton_volume=ecran.blit(boutonv,((bouton_volume.x),(bouton_volume.y)-150))
     
    volume = ""
    user_input = font.render(volume, True, GREEN)
    user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)
   
    continuer = True
     
    while continuer:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                menu(False)
                continuer = False
            x,y = pygame.mouse.get_pos()
            collide_v= bouton_volume.collidepoint(x,y)
            if event.type ==pygame.MOUSEBUTTONDOWN :
                if collide_v:
                    ecran.blit(boutonv_p,bouton_volume)
                    pressed=pygame.mouse.get_pressed()
            if event.type ==pygame.MOUSEBUTTONUP:
                if collide_v and pressed[0]==1:
                    continuer2=True
                    while continuer2:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                                    try:
                                        volume = float(volume)
                                        pygame.mixer.music.set_volume(volume)
                                    except ValueError:
                                        text=font.render('Veuillez entrer un nombre valide', True, BLUE)
                                        text_rect=text.get_rect(center=(ecran.get_rect().center))
                                        ecran.blit(text,((text_rect.x),(text_rect.y)+50))
                                        pygame.display.flip()
                                        time.sleep(1.5)
                                    options()
                                    continuer2 = False
                                elif event.key == pygame.K_BACKSPACE:
                                    volume = volume[:-1]
                                elif event.key == pygame.K_ESCAPE:
                                    options()
                                    continuer2= False
                                else:
                                    volume += event.unicode
                                user_input = font.render(volume, True, GREEN)
                                user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)
         
                        ecran.fill(0)
                        ecran.blit(prompt, prompt_rect)
                        ecran.blit(user_input, user_input_rect)
                        pygame.display.flip()
            pygame.display.flip()
                 

def menu(premierTour):
    #Menu principal
    pygame.mixer.init()
    fenetre()
    #Fond menu
    fond_menu = pygame.image.load("fond_menu2.png").convert_alpha()
    fond_menu=pygame.transform.scale(fond_menu,ecran.get_size())
    ecran.blit(fond_menu,(0,0))

    #boutons menu
    bouton= pygame.image.load("bouton1.png").convert_alpha()
    bouton_p =pygame.image.load("bouton2.png").convert_alpha()
    boutonq=pygame.image.load("boutonq.png").convert_alpha()
    boutonq_p=pygame.image.load("boutonq2.png").convert_alpha()
    boutono=pygame.image.load("boutono.png").convert_alpha()
    boutono_p=pygame.image.load("boutono2.png").convert_alpha()
    bouton_start=bouton.get_rect()
    bouton_start.center=ecran.get_rect().center
    bouton_start=ecran.blit(bouton,(bouton_start))
    bouton_option=ecran.blit(boutono,((bouton_start.x),(bouton_start.y)+150))
    bouton_quit=ecran.blit(boutonq,((bouton_start.x),(bouton_start.y)+300))
    #Permet de démarrer la musique au lancement
    if pygame.mixer.get_busy()==False and premierTour==True:
        pygame.mixer_music.load("background.mp3")
        pygame.mixer_music.play(-1,0)
        pygame.mixer.music.set_volume(0.03)
    


    continuer = True

    while continuer:
        pygame.display.flip()
        for event in pygame.event.get():
            #Arrêt
            if event.type ==pygame.QUIT:
                continuer = False
            
            #Boutons
            x,y = pygame.mouse.get_pos()
            collide_s= bouton_start.collidepoint(x,y)
            collide_o= bouton_option.collidepoint(x,y)
            collide_q= bouton_quit.collidepoint(x,y)
            if event.type ==pygame.MOUSEBUTTONDOWN :
                if collide_s:
                    ecran.blit(bouton_p,bouton_start)
                    pressed=pygame.mouse.get_pressed()
                if collide_o:
                    ecran.blit(boutono_p,(bouton_option))
                    pressed=pygame.mouse.get_pressed()
                if collide_q:
                    ecran.blit(boutonq_p,(bouton_quit))
                    pressed=pygame.mouse.get_pressed()
            if event.type ==pygame.MOUSEBUTTONUP:
                if collide_s and pressed[0]==1:
                    jeu()
                    continuer=False
                if collide_o and pressed[0]==1:
                    options()
                    continuer=False
                if collide_q and pressed[0]==1:
                    continuer=False
                else :
                    ecran.blit(bouton,bouton_start)
                    ecran.blit(boutono,(bouton_option))
                    ecran.blit(boutonq,(bouton_quit))
     
    pygame.quit()

def ecranfin():
    #Menu qui permet d'arrêter de jouer ou de reprendre
    fenetre()
    hauteur =100
    largeur=200
    couleur=(0,0, 255)
    vert=(0,255,0)
    lancmt=pygame.draw.rect(ecran, couleur, ((largeur_ecran/2)-(largeur/2), hauteur_ecran/2-(hauteur), largeur, hauteur))
    fin=pygame.draw.rect(ecran, vert, ((largeur_ecran/2)-(largeur/2), (hauteur_ecran/2)+(hauteur-50), largeur, hauteur))


    continuer = True
    print("presse une touche pour lancer le jeu")

    while continuer:
        pygame.display.flip()
        for event in pygame.event.get():
            x, y =pygame.mouse.get_pos()
            collide=lancmt.collidepoint(x, y)
            collide_2=fin.collidepoint(x, y)
            if collide :
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return True
                    pygame.display.update()
                
            if collide_2:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("le jeu va être fermé")
                    return False
           
    pygame.quit()
                

menu(True)
 
pygame.quit()



        


