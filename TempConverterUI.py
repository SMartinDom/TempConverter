from tkinter import *

def on_enter(event):
    value = eingabe.get()
    eingabe.delete(0,END)
    return value

master=Tk()
master.geometry('400x300')

Titel = Label(master, 
                   font= ('verdana', 10, 'bold'),
                   width=40,
                   text = 'Temperaturwandler 0.3')
Titel.place(x = 4, y =10)
mAuswahl = Label(master, 
                    justify= 'l',
                    text = '(1) Umrechnung von Celsius nach Kelvin\n'
                    '(2) Umrechnung von Celsius nach Fahrenheit\n'
                    '(3) Umrechnung von Kelvin nach Celsius\n'
                    '(4) Umrechnung von Kelvin nach Fahrenhei\n'
                    '(5) Umrechnung von Fahrenheit nach Celsius\n'
                    '(6) Umrechnung von Fahrenheit nach Kelvin')
mAuswahl.place(x = 4, y = 50)

beenden = Button(master, 
                    text = 'Beenden',
                    width=10,
                    command= master.destroy)
beenden.place(x = 4, y = 160)

anweisung = Label(master, 
                   text = 'Dummytext für Anweisung')
anweisung.place(x=4, y=200)

eingabe = Entry(master, 
                    background='lightblue',
                    relief=SOLID,
                    borderwidth= 1,
                    )
eingabe.place(x=70, y=230)
eingabe.bind('<Return>', on_enter)


eingabeText = Label(master, text='Eingabe: ')
eingabeText.place(x=4, y=230)

ausErg = Label(master, 
                   font= ('verdana', 8, 'bold'),
                   text = 'Dummytext für Ausgabe des Ergebnisses')
ausErg.place(x=4, y=260)

master.mainloop()
