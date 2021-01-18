#Alexandr Klis IT20
#iseseisvad tööd
#18.01.21
import random

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