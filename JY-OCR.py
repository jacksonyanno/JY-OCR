import os
from time import sleep
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
from tkinter import ttk
from PIL import Image
from pytesseract import pytesseract


WORKING_DIR = os.path.dirname(os.path.realpath(__file__)) # Diretório atual
custom_config = r'--oem 3 --psm 6'


class Application:
    def __init__(self, master=None):
        # Inicializando o Tesseract-OCR #
        path_to_tesseract = f"{WORKING_DIR}\\tesseract-ocr\\tesseract.exe"
        pytesseract.tesseract_cmd = path_to_tesseract

        self.standardFont = ("Arial", "12")
        self.titlesFont = ("Calibri", "8", "bold")

        self.titleContainer = Frame(master)
        self.titleContainer["pady"] = 10
        self.titleContainer.pack()

        self.title = Label(self.titleContainer, text="Gerador de OCR de images JPG/JPEG/PNG")
        self.title["font"] = ("Arial", "10", "bold")
        self.title.pack()

        self.targetPathContainer = Frame(master)
        self.targetPathContainer["padx"] = 20
        self.targetPathContainer.pack()

        self.targetPathLabel = Label(self.targetPathContainer,text="Caminho", font=self.standardFont)
        self.targetPathLabel.pack(side=LEFT)

        self.targetPath = Entry(self.targetPathContainer)
        self.targetPath["width"] = 30
        self.targetPath["font"] = self.titlesFont
        self.targetPath.pack(side=LEFT)

        self.buttonsContainer = Frame(master)
        self.buttonsContainer["pady"] = 20
        self.buttonsContainer.pack(fill=X, anchor='nw')
        self.buttonsContainer.pack()
        
        self.researchButton = Button(self.buttonsContainer, text="...", bd=2, font=self.titlesFont)
        self.researchButton["width"] = 20
        self.researchButton["command"] = self.getDirectoryPath
        self.researchButton.pack(side=LEFT, expand=YES)
        
        self.generateOcrButton = Button(self.buttonsContainer, text="Gerar OCR", bd=2, font=self.titlesFont)
        self.generateOcrButton["width"] = 20
        self.generateOcrButton["command"] = self.generateOcrFromFiles
        self.generateOcrButton.pack(side=LEFT, expand=YES)

    def getDirectoryPath(self):
        self.targetPath.delete(0,END)
        self.targetPath.insert(0,filedialog.askdirectory())

    def generateOcrFromFiles(self):
        count = 0
        folder_path = self.targetPath.get()

        if not folder_path:
            showinfo(
                title="Entrada inválida",
                message="O caminho do diretório insereido é inválido. Favor, insira um caminho válido e tente novamente."
            )
            return

        all_imgs_path = [os.path.join(folder_path, file_name) for file_name in os.listdir(folder_path) \
                         if file_name.lower().endswith(".jpg") or \
                            file_name.lower().endswith(".jpeg") or \
                            file_name.lower().endswith(".png")]
        imgs_path = [img for img in all_imgs_path if not os.path.exists(img[:-4] + ".ocr.txt")]
        
        if len(all_imgs_path) == 0:
            showinfo(
                title="Aquivos de imagem JPG/JPEG/PNG - não encontrados",
                message="A pasta selecionada não contem arquivos \nem formato de imagem permitido (.jpg/.jpeg/.png)!"
            )
            return
        elif len(imgs_path) == 0:
            showinfo(
                title="Imagens já possuem OCR",
                message="Todas as imagens desta pasta já possuem um OCR associado!"
            )
            return

        popup = Toplevel()
        popup.geometry("400x200")
        Label(popup, text=f"Gerando o OCR de {len(imgs_path)} arquivos...").place(x=0, y=0)
        
        progress = 0
        progress_var = DoubleVar()
        progress_bar = ttk.Progressbar(popup, variable=progress_var, maximum=100)
        progress_bar.place(x=0, y=40, width=400, height=40)
        popup.pack_slaves()

        progress_step = float(100.0/len(imgs_path))
        for img_path in imgs_path:
            popup.update()
            texts = str(((
                pytesseract.image_to_string(
                    Image.open(img_path), 
                    config=custom_config,                            
                )
            )))
            with open(img_path[:-4] + ".ocr.txt", "w+") as f:
                f.write(texts)
            count += 1
            progress += progress_step
            progress_var.set(progress)
        
        if showinfo("JY-OCR", f"Foram gerados {count} novos OCRs!") == "ok":
            popup.quit()


app = Tk()
app.title("JY-OCR")
app.geometry("400x200")
Application(app)
app.mainloop()
