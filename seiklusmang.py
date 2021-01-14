import os.path
#Alexandr Klis
#it20
#11.01.21
#seiklusmang

#def createplayer
#karakterid


p = 10
health = 0
attack = 0
defence = 0




#küsib kasutaja nime
name = input("Sisesta kasutajanimi: ")
def punktid():
    p = 10
    #otsib kas kasutaja on juba olemas
    if os.path.isfile(name+".txt")==True:
        print("Kasutaja on juba olemas")

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
    while p > 0:
        print(f"Sul jäi {p} punkte üle kasuta need ära")
        punktid()
      
        
hp = health
at = attack
df = defence


    
    

    


punktid()