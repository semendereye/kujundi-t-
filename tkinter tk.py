#Alexandr Klis
#it20 25.01.21
#tkinter kt
import random
from tkinter import *
aken = Tk()
aken.title('matemaatika')
aken.iconbitmap('favicon.ico')
aken.geometry("250x150")


oige = 0
vale = 0
#funktsioonid
#silt
silt = Label(aken, text="Sisesta vastus:")
silt.grid(row=0,column=0)
#sisestus
sisestus = Entry(aken)
sisestus.grid(row=0,column=1)

#silt2
silt2 = Label(aken, text="Tehe:")
silt2.grid(row=1,column=0, sticky= W)

tehe = Label(aken, text="Alustamiseks vajuta arvuta")  
tehe.grid(row=1,column=1)


def arvutus():
    suv = random.randint(0,10)
    suv2 = random.randint(0,10)
    summa = suv * suv2
    tehe.config(text=f"{suv}*{suv2}")
    km = sisestus.get()
    print(summa)
    if km==summa:
        oige =+ 1
        vastus.config(text=oige)
    else:
        vale =+ 1
        vastus2.config(text=vale)
    
#vastused
vastus = Label(aken, text=oige)
vastus.grid(row=3,column=1)

vastus2 = Label(aken, text=vale)
vastus2.grid(row=4,column=1)



#arvutus
#silt3
silt3 = Label(aken, text="Õigeid vastuseid:")
silt3.grid(row=3,column=0, sticky = W)

#silt4
silt4 = Label(aken, text="Valesi vastuseid:")
silt4.grid(row=4,column=0)


#nupp
nupp1 = Button(aken, text="Arvuta", width=10, command=arvutus)
nupp1.grid(row=5,column=1)