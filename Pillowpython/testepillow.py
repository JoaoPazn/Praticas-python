# rodar no centro de comandos : pip3 install pillow
from PIL import Image
from PIL import features
from tkinter import Tk, Label
from PIL import Image, ImageTk


imagem = Image.open("HQ_Pearto.png") # copiar caminho relativo na mesma pasta


janela = Tk()
janela.title("Pera")

janela.geometry(f"{imagem.width}x{imagem.height}")

imagem_tk = ImageTk.PhotoImage(imagem)

label = Label(janela, image=imagem_tk)
label.pack()

janela.mainloop()