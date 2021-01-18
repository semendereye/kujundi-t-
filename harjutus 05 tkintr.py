#Alexandr Klis
#IT20 18.01.21

from tkinter import *
aken = Tk()
aken.title('Käibemaksukalkulaator')
aken.iconbitmap('favicon.ico')
aken.geometry("250x150")


#funktsioonid
#silt
silt = Label(aken, text="Hind käibemaksuta:")
silt.grid(row=0,column=0)
#sisestus
sisestus = Entry(aken)
sisestus.grid(row=0,column=1)

#silt2
silt2 = Label(aken, text="Käibemaksumäär:")
silt2.grid(row=1,column=0, sticky= W)
#valik

    
var = IntVar()
valikukast = Radiobutton(aken,text="9%", variable=var, value=9)
valikukast.grid(row=1,column=1)
valikukast = Radiobutton(aken,text="20%", variable=var, value=20)
valikukast.grid(row=2,column=1)

#arvutus
#silt3
silt3 = Label(aken, text="Käibemaks:")
silt3.grid(row=3,column=0, sticky = W)

#silt4
silt4 = Label(aken, text="Hind käibemaksuga:")
silt4.grid(row=4,column=0)

#käibemaks arvutus
def Käibemaks():
    km = float(sisestus.get())
    lp = float(var.get() / 100)
    km1 = km * lp
    km2 = km1 + km
    vastus.config(text=km1)
    vastus2.config(text=km2)
    
#vastus
vastus = Label(aken, text="€")
vastus.grid(row=3,column=1)

vastus2 = Label(aken, text="€")
vastus2.grid(row=4,column=1)


#nupp
nupp1 = Button(aken, text="OK", width=10, command=Käibemaks)
nupp1.grid(row=5,column=1)

