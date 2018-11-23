#!/usr/bin/env python3

"""
Exemplo de interface para um sistema de login com Tkinter
By Júlio Schoenardie
"""
from tkinter import *
import shelve

"""Criando o shelve"""
db = shelve.open("login.db")
db['login'] = "admin"
db['senha'] = "admin"


"""Criando as funções utilizadas para validar o login"""

def logar():
    form1 = ent1.get()
    form2 = ent2.get()

    if form1 == db['login'] and form2 == db['senha']:
        text3['text'] = "Bem vindo {}!".format(db['login'])
        text3['fg'] = "blue"
    else:
        text3['text'] = "Senha ou usuário não coferem!"
        text3['fg'] = "red"


"""Iniciando a interface gráfica"""

i = Tk()
i.title("Login")
i.geometry("250x140")

text1 = Label(i, text="Email")
text1.pack()

ent1 = Entry(i)
ent1.pack()

text2 = Label(i, text="Senha")
text2.pack()

ent2 = Entry(i)
ent2.pack()

botao = Button(i, text="Login", command=logar)
botao.pack()

text3 = Label(i, text="")
text3.pack()


i.mainloop()
db.close()