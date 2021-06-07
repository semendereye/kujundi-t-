import os.path
import random
import pickle
#Alexandr Klis
#it20
#07.06.21
#seiklusmang
#Mängus valid punktid ja võitled gobliniga


Ehp = 0
Eat = 0
hp = 0
p = 10
health = 0
attack = 0
defence = 0

def main():
    print ("Vajuta number 1, et mängu alustada")
    option = input(' ')
    if option == "1":
        punktid()
    

#küsib kasutaja nime
name = input("Sisesta kasutajanimi: ")
def punktid():
    global health, p, attack, defence
    p = 10
    #otsib kas kasutaja on juba olemas
    if os.path.isfile(name)==True:
        print("Kasutaja on juba olemas")
        main1()
    #küsib mis oskustele punktid lisada

    else:
        print("Sul on 10 punkti jaga need 3 oskuse vahel")
        health = int(input("Palju punkte Healthile: "))
        while health >= p:
            health = int(input("Palju punkte Healthile: "))
            if health >=p:
                print("Sul ei ole piisavalt punkte")
        p = p-health
        print(f"Sul on alles {p} punkti")
        attack = int(input("Palju punkte attackile: "))
        while attack >= p:
            attack = int(input("Palju punkte attackile: "))
            if attack >=p:
                print("Sul ei ole piisavalt punkte")
        p = p-attack
        print(f"Sul on alles {p} punkti")
        defence = int(input("Palju punkte defencile: "))
        while defence > p:
            defence = int(input("Palju punkte defencile: "))
            print("Sul ei ole piisavalt punkte")
        p = p-defence
        main1()
    while p > 0:
        print(f"Sul jäi {p} punkte üle kasuta need ära")
        punktid()
      
        
def main1():
    global playa
    print ("1. Lae mäng")
    print ("2. salvesta mäng")
    option = input(' ')
    if option == "2":
        os.system('clear')
        with open(name , 'wb') as f:
            pickle.dump(playa, f)
            print ("\nMäng on salvestatut!\n")
            voitlus()
        option = input(' ')
    elif option == "1":
        if os.path.exists(name) == True:
            os.system('clear')
            with open(name , 'rb') as f:
                playa = pickle.load(f)
            print ("Save file on laaditud")
            option = input(' ')
            voitlus()
        else:
            print ("Mäng pole salvestatud")
            option = input(' ')
            main1()

class playa:
    def __init__(self, name):
        global health, attack, defence
        self.hp = 20 + health
        self.attack = 3 + attack
        self.defence = 2 + defence
        self.hp = self.hp + defence
player = playa("playa")
class vastane:
    def __init__(self, name):
        self.Ehp = 10
        self.Eat = random.randrange(15)
    
vastanee = vastane("vastane")
def voitlus():
    option = input(' ')
    global Ehp, hp, attack, defence, Eat, vastanee, player
    print ("vastu tuleb goblin")
    print (" 1. löö goblinit")
    print (" 2. seisa")
    if option == "1":
        vastanee.Ehp = vastanee.Ehp - player.attack
        print (f" Goblinil jäi {vastanee.Ehp} elu")
    
    if vastanee.Ehp <=0:
        voit()
    if option == "2":
        player.hp = player.hp - vastanee.Ehp
        print (f"sa seisid ühe koha peal ja goblin lõi sind sul on alles {player.hp}elu")
    if player.hp <=0:
        surnud()
    else:
        voitlus()
    


def voit():
    print ("Sa võitsid!")

def surnud():
    print(" Sa kaotasid")


main()