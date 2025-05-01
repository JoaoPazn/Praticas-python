import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg as tkagg

# Criação do gráfico
plt.plot([1, 2, 3], [1, 4, 3,])

#Acessando a janela Tkinter
fig = plt.gcf()
canvas = fig.canvas

# Alterando o título da janela
canvas.manager.window.title("HAHHAHAHAHAHHAHAHAHHA")
# Mostra o gráficoq
plt.show()