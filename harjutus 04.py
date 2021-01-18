#Alexandr Klis
#It20 18.01.21
from tkinter import *
#aknaseaded
aken = Tk()
aken.title('Kalkulaator')
aken.iconbitmap('favicon.ico')
aken.geometry("200x200")

#tekst
ebat = 'Siia Kunagi vastus!'
tekst = Label(aken, text=ebat, justify=CENTER, font="Tahoma 12")
tekst.grid(row=0, columnspan=4, column=0)



laius=5

#nupud
nupp1 = Button(aken, text="7", height=2, width=4, padx=laius)
nupp1.grid(row=1, column=0, padx=2, pady=2)
nupp2 = Button(aken, text="4", height=2, width=4, padx=laius)
nupp2.grid(row=2, column=0, padx=2, pady=2)
nupp3 = Button(aken, text="1", height=2, width=4, padx=laius)
nupp3.grid(row=3, column=0, padx=2, pady=2)
nupp4 = Button(aken, text="0", height=2, width=4, padx=laius)
nupp4.grid(row=4, column=0, padx=2, pady=2)
nupp1 = Button(aken, text="8", height=2, width=4, padx=laius)
nupp1.grid(row=1, column=1, padx=2, pady=2)
nupp2 = Button(aken, text="5", height=2, width=4, padx=laius)
nupp2.grid(row=2, column=1, padx=2, pady=2)
nupp3 = Button(aken, text="2", height=2, width=4, padx=laius)
nupp3.grid(row=3, column=1, padx=2, pady=2)
nupp4 = Button(aken, text=",", height=2, width=4, padx=laius)
nupp4.grid(row=4, column=1, padx=2, pady=2)
nupp1 = Button(aken, text="9", height=2, width=4, padx=laius)
nupp1.grid(row=1, column=2, padx=2, pady=2)
nupp2 = Button(aken, text="6", height=2, width=4, padx=laius)
nupp2.grid(row=2, column=2, padx=2, pady=2)
nupp3 = Button(aken, text="3", height=2, width=4, padx=laius)
nupp3.grid(row=3, column=2, padx=2, pady=2)
nupp4 = Button(aken, text="=", height=2, width=4, padx=laius)
nupp4.grid(row=4, column=2, padx=2, pady=2)
nupp1 = Button(aken, text="/", height=2, width=4, padx=laius)
nupp1.grid(row=1, column=3, padx=2, pady=2)
nupp2 = Button(aken, text="*", height=2, width=4, padx=laius)
nupp2.grid(row=2, column=3, padx=2, pady=2)
nupp3 = Button(aken, text="-", height=2, width=4, padx=laius)
nupp3.grid(row=3, column=3, padx=2, pady=2)
nupp4 = Button(aken, text="+", height=2, width=4, padx=laius)
nupp4.grid(row=4, column=3, padx=2, pady=2)

aken.mainloop()