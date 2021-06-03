#Alexandr Klis
#it20 25.01.21
#tkinter kt
import random
from tkinter import *

aken = Tk()
aken.title('matemaatika')
aken.iconbitmap('favicon.ico')
aken.geometry("250x150")
question = ["4 * 4","2 * 4","15 * 0","5 * 5","Test sooritatud.\n Vajuta arvuta et naha tulemusi"]

q = 0
vastused = ["16","8","0","25",""]
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

tehe = Label(aken, text= question[0])  
tehe.grid(row=1,column=1)


def arvutus():
    global oige,vale,q,question,vastused
    km = sisestus.get()    
    print(km)
    if q < 4:
        if vastused[q] == km:
            sisestus.delete(0, END)
            q += 1
            oige = oige + 1           
            tehe.config(text= question[q])
        else:
            sisestus.delete(0, END)
            q += 1
            vale = vale + 1
            tehe.config(text= question[q])
            
    else:
        sisestus.delete(0, END)
        tehe.config(text = "Oigeid: "+str(oige) + " Valesi:   "+str(vale))


        

#nupp
nupp1 = Button(aken, text="Arvuta", width=10, command=arvutus)
nupp1.grid(row=5,column=1)
aken.mainloop()