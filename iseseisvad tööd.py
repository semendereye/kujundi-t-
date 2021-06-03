#Alexandr Klis IT20
#iseseisvad tööd
#18.01.21
import random
import re

#lisa 8
    #Vaatab kas email on õige
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

def check(email):
    if(re.search(regex, email)):
        enimi,pnimi,domeen,com = re.split(".|@", email)
        
        print("Tere"+ enimi +", sinu email on "+ domeen +"serveris ja domeeniks on sul"+com)
 
    else:
        print("Vale email")
 
# Põhi kood
if __name__ == '__main__':
 
    # emaili lisamine
    email = input(print("Lisa oma Email: "))
    
    check(email)








input()
#lisa 7
mangija2 = 0
mangija = 0
arvuti = 0
arvuti2 = 0

    #korda kõike selles plokis 10 korda
for i in range(10):

    # genereerim täringu numbri
    mangija = random.randint(1, 6)
    mangija2 = random.randint(1, 6)
    arvuti = random.randint(1, 6)
    arvuti2 = random.randint(1, 6)

    # kuvab täringu numbri
    print("Mängija sai: ", mangija+mangija2)
    print("Arvuti sai: ", arvuti+arvuti2)
    
    mangija = mangija + mangija2
    arvuti = arvuti + arvuti2

    if mangija > arvuti:
        print("Mängija võitis")
        arvuti = mangija + 1 
    elif arvuti > mangija:
        print("Arvuti võitis")
        arvuti = mangija + 1
    else:
        print("VIIK")

    input("Vajuta Enterit, et edasi liikuda.") 

print("### Game Over ###")
print("Mängija skoor:", mangija)
print("Arvuti skoor:", arvuti)





#6 lisa
rahad = {
    "EEK":"(Eesti kroon)",
    "EUR":"(Euro)",    
}
#küsib valikud
print ("Võimalikud valikud:")
for raha in rahad:
    print (raha + " " + rahad[raha])
    
user_choice1 = input("Millest: ")
user_choice2 = input("Millsesse: ")
#küsib palju soovid vahetada
def lisa():
    kasutajainput = input("Kui palju soovite vahetada? ")
    amount = float(kasutajainput)
    conversion = amount / 15.6466
    print( str(kasutajainput) + "Krooni on väärt " + str(conversion) + " Eurot.")


def euro_to_eek():
    kasutajainput = input("Kui palju soovite vahetada? ")
    amount = float(kasutajainput)
    conversion = amount * 15.6466
    print( str(kasutajainput) + "Eurot on väärt " + str(conversion) + " Krooni.")

#näitab vahetatud vastust
if user_choice1 == "EEK" and user_choice2 == "EUR":
    print ("EEK to EUR.")
    print(lisa())

elif user_choice1 == "EUR" and user_choice2 == "EEK":
    print ("Euro to EEK.")
    print(euro_to_eek())
    



#5 lisa
shopping_list = []

print("Mida me võiks poest osta?")
print("Kirjuta Tehtud kui list on valmis")

while True:
    new_item = input("> ")
    if new_item == 'Tehtud':
        break
    shopping_list.append(new_item)

print("Siin on sinu list:")

for item in shopping_list:
    print(item)




#4 lisa
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)
        



#3 lisa
uus_loend = []
uus_loend2 = []
for i in range(5):
    sisend = int(input('Lisa arv loenditesse: '))
    if sisend>0:
        uus_loend.append(sisend)
    else:
        uus_loend2.append(sisend)
    
    
print(uus_loend)
print(uus_loend2)


input()
#2 lisa

vanused = [15,16,17,18,19,20,21,30,50,32,60,11,1,5,100]
print(f"Suurim arv: {max(vanused)}")
print(f"Väikseim arv: {min(vanused)}")
print(f"Summa: {sum(vanused)}")
print(f"Keskmine: {round(sum(vanused)/len(vanused),2)} ")

#1 lisa

for j in range(10):
    suv = random.randint(0,10)
    suv2 = random.randint(0,10)
    print(f"{suv}*{suv2}")
    vastus = int(input("Sisesta vastus:"))
    summa = suv * suv2
    if vastus==summa:
        print("Õige vastus!")
    else:
        print("Vale vastus")


#2
for j in range(1):
    suv = random.randint(0,6)
    print(suv, end="")


print("\n","_"*20)
#10
for i in range(1,67):
    print(f"{i}", end="")
    if i%5==0:
        print("",end="\n")
    
print("\n","_"*20)
#7
sona = input("Sisesta palindroom: ")
print(sona == sona[::-1])

print("\n","_"*20)
#11
for i in range(1,66):
    if i%3==0:
        print(i, end=" ")
print("\n","_"*20)
#3
print('"jutumärgid"')
print("Kaldu\//")
print('Kas \'"kirjutad' "\" samamoodi?")