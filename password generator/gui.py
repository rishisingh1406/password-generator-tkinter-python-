import tkinter 
from tkinter.font import Font
import random


class Homescreen():
    def __init__(self) :
        
        # creating the basic window 
        self.window = tkinter.Tk()
        self.window.title("password generator")
        self.window.maxsize(300,500)
        self.window.minsize(300,500)
        self.bgimg = tkinter.PhotoImage(file="bgimg.png")
        self.canvas = tkinter.Canvas(width=300,height=500,background="white")
        self.canvas.create_image(150,250,image=self.bgimg)
        self.canvas.pack()


        
        # creating the input box 
        self.entboxfont = Font(weight="bold")
        self.entbox = tkinter.Entry(width=8,font=self.entboxfont,highlightthickness=0,borderwidth=0)
        self.entbox.place(x=105,y=220)
        # creating the password funtion for genearting the code 
        def password():
            passlen = int(self.entbox.get())
            num = ["1","2","3","4","5","6","7","8","9"]
            lettrs =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            symbol = ['!',"@","#","$","]","&","*","%","["]
            value = [num,lettrs,symbol]
            realpas = []
            for x in range(passlen):
             chr1 = random.choice(value[random.randint(0,2)])
             realpas.append(chr1)
            finpass = ''.join(realpas)
            
         # creating the password box 
            self.txtfont = Font(weight="bold")
            self.textbox = tkinter.Label(text=finpass,width=20,height=1,background="#ffffff",font=self.txtfont)
            self.textbox.place(x=30,y=140)
        # creating the generate button 
        self.btnfont =Font(weight="bold") 
        self.genbtn = tkinter.Button(width=8,height=1,text="Generate",bg="#7ED957",fg="white",font=self.btnfont,command=password)
        self.genbtn.place(x=105,y=280)

        

        self.window.mainloop()