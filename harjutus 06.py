#Alexandr Klis
#It20 18.01.21
from tkinter import *
#aknaseaded
aken = Tk()
aken.title('taani lipp')
aken.iconbitmap('favicon.ico')

#löendi loomine

louend = Canvas(aken, width=500, height=500)
louend.pack()

#lipu loomine

louend.create_rectangle(10, 10, 400, 250, fill="#C60C30", outline='#C60C30')
louend.create_rectangle(10, 115, 400, 145, fill="#FFFFFF", outline='#FFFFFF')
louend.create_rectangle(110, 10, 140, 250, fill="#FFFFFF", outline='#FFFFFF')

#pildi lisamine


minu_pilt = PhotoImage(file='m.png')
louend.create_image(0, 260, anchor=NW, image=minu_pilt)