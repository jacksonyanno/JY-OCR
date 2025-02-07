from tkinter import *
import _thread
import threading


def atualizarInterface(atoa):
    while True:
        root.update_idletasks()
        root.update()


def iniciarThreadAtualizar():
    _thread.start_new_thread(atualizarInterface, tuple([1]))


class InterfaceGrafica:
    def __init__(self, master=None):
        self.corVerde = "color-" + 'green'
        self.corAzul = "color-" + 'blue'
        self.corCinza= "color-" + 'grey'

        self.fontePadrao = ("Arial", "12")
        self.fonteTitulos = ("Arial", "12", "bold")

        self.containerGeral = Frame(master)
        self.containerGeral.pack(fill=BOTH, expand=YES)

        self.containerMenu = Frame(self.containerGeral, bg='#cbccc6', width=100)
        self.containerMenu.pack(side=LEFT, anchor='nw', fill=Y, expand=YES)

        self.containerCanvas = Frame(self.containerGeral, bg='black', width=100, height=100)
        self.containerCanvas.pack(side=LEFT, anchor='nw', fill=BOTH, expand=YES)

        self.containerBotoes = Frame(self.containerMenu, bg='#cbccc6')
        self.containerBotoes.pack(fill=X, anchor='nw')

        self.botaoTranslacao = Button(self.containerBotoes, text="Translação", bd=2, font=self.fonteTitulos)

        self.botaoRotacao = Button(self.containerBotoes, text="Rotação", bd=2, font=self.fonteTitulos)

        self.botaoEscala = Button(self.containerBotoes, text="Escala", bd=2, font=self.fonteTitulos)

        self.botaoReflexao = Button(self.containerBotoes, text="Reflexões", bd=2, font=self.fonteTitulos)

        self.botaoTranslacao.pack(side=LEFT, expand=YES)
        self.botaoRotacao.pack(side=LEFT, expand=YES)
        self.botaoEscala.pack(side=LEFT, expand=YES)
        self.botaoReflexao.pack(side=LEFT, expand=YES)

        self.containerAzul = Frame(self.containerMenu, bg='blue')
        self.containerAzul.pack(anchor='nw', fill=BOTH, expand=YES)


root = Tk()
root.title("Trabalho Computação Gráfica")
root.geometry("800x480")
interface = InterfaceGrafica(root)
root.after(100, iniciarThreadAtualizar)
root.mainloop()