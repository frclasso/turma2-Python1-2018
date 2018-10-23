from tkinter import *

class calculadora_JCAVI:
    def __init__(self, calc):
        self.calc = calc
        self.calc.title("Calculadora - JCAVI")
        self.calc.geometry('188x195')
        self.calc.resizable(height=FALSE,width=FALSE)

        self.valores = Entry(self.calc, bg='Gray', font=('Tahoma', 22))
        self.valores.grid(row=0,sticky=W, ipadx=93, ipady=9, pady=3)

        self.sete = Button(self.calc, relief=GROOVE, activebackground='Red', activeforeground='White')
        self.sete['text'] = '7'
        self.sete.grid(row=1, column=0, sticky=W, ipadx=15, pady=3)

        self.quatro = Button(self.calc, relief=GROOVE, activebackground='Red', activeforeground='White')
        self.quatro['text'] = '4'
        self.quatro.grid(row=2, column=0, sticky=W, ipadx=15, pady=3)

        self.um = Button(self.calc, relief=GROOVE, activebackground='Red', activeforeground='White')
        self.um['text'] = '1'
        self.um.grid(row=3, column=0, sticky=W, ipadx=15, pady=3)

        self.zero = Button(self.calc, relief=GROOVE, activebackground='Red', activeforeground='White')
        self.zero['text'] = '0'
        self.zero.grid(row=4, sticky=W, ipadx=39, pady=3, padx=0)

        self.oito = Button(self.calc, relief=GROOVE, activebackground='Red', activeforeground='White')
        self.oito['text'] = '8'
        self.oito.grid(row=1, sticky=W, ipadx=15, pady=2, padx=49)

        self.cinco = Button(self.calc, relief=GROOVE, activebackground='Red', activeforeground='White')
        self.cinco['text'] = '5'
        self.cinco.grid(row=2,sticky=W, ipadx=15, pady=3, padx=49)

        self.dois = Button(self.calc, relief=GROOVE, activebackground='Red', activeforeground='White')
        self.dois['text'] = '2'
        self.dois.grid(row=3, sticky=W, ipadx=15, pady=3, padx=49)

        self.nove = Button(self.calc, relief=GROOVE, activebackground='Red', activeforeground='White')
        self.nove['text'] = '9'
        self.nove.grid(row=1, sticky=W, ipadx=15, pady=2, padx=98)

        self.seis = Button(self.calc, relief=GROOVE, activebackground='Red', activeforeground='White')
        self.seis['text'] = '6'
        self.seis.grid(row=2,sticky=W, ipadx=15, pady=3, padx=98)

        self.tres = Button(self.calc, relief=GROOVE, activebackground='Red', activeforeground='White')
        self.tres['text'] = '3'
        self.tres.grid(row=3,sticky=W, ipadx=15, pady=3, padx=98)

        self.igual = Button(self.calc, relief=GROOVE, activebackground='Red', activeforeground='White')
        self.igual['text'] = '='
        self.igual.grid(row=4, sticky=W, ipadx=14, pady=3, padx=98)

        self.adicao = Button(self.calc, relief=GROOVE, activebackground='Red', activeforeground='White')
        self.adicao['text'] = '+'

        self.adicao.grid(row=1,sticky=W, ipadx=11, padx=146)

        self.sub = Button(self.calc, relief=GROOVE, activebackground='Red', activeforeground='White')
        self.sub['text'] = '-'
        self.sub.grid(row=2,sticky=W, ipadx=13, padx=146)

        self.mul = Button(self.calc, relief=GROOVE, activebackground='Red', activeforeground='White')
        self.mul['text'] = '*'
        self.mul.grid(row=3,sticky=W, ipadx=13, padx=146)

        self.divi = Button(self.calc, relief=GROOVE, activebackground='Red', activeforeground='White')
        self.divi['text'] = '÷'
        self.divi.grid(row=4,sticky=W, ipadx=11, padx=146)

calc = Tk()
calculadora_JCAVI(calc)
calc.mainloop()
