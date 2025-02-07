import os
from tkinter import filedialog
from tkinter import messagebox

def question():
    return messagebox.askyesno(
        title="Adicionar linha?", 
        message="Gostaria de incluir um novo par de origem e destino?"
    )

with open(os.path.join('input', 'diretorios.csv'), 'w') as dircsv:
    continuar = question()
    dircsv.write('origem,destino\n')
    while continuar:
        origem = filedialog.askdirectory()
        destino = filedialog.askdirectory()
        dircsv.write(f'{origem}, {destino}\n')
        continuar = question()
