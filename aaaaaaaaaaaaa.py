import numpy as np #pip3 install numpy
import random
import time
import matplotlib.pyplot as plt #pip3 install matplotlib
import matplotlib.backends.backend_tkagg as tkagg

Nomes = [
    "Dr. Eggman",
    "Sam, O Gato",
    "Irvine, O Rato",
    "Fortune, Grande Mestre Do Horizonte",
    "Marisa",
    "Reimu",
    "Morgana",
    "Red",
    "Pink",
    "Blue",
    "Bong-Bong",
    "Yesod, Sephiroth",
    "Netzach, Sephiroth",
    "Malkuth, Sephiroth",
    "Binah, Sephiroth",
    "Chesed, Sephiroth",
    "Angela, Bibliotecária Patrono",
    "Roland",
    "Kingaleppu",
    "Lucy, A Slime",
    "Artoria Pendagron",
    "Luana",
    "João P.",
    "João G.",
    "Tomé",
    "Renan",
    "Amanda",
    "Cecilia",
    "Gleristone",
    "Marcelino",
    "Feliciano",
    "Luciano",
    "Romulo",
    "Félix",
    "Pedro",
    "Paulistaaaaaaaaaaaaaaaa",
    "Jack Black",
    "Pablo",
    "Marciano",
    "Omni-Man"
]

itens = [
    "Metal Sonic",
    "Kit de Abrir Fechaduras",
    "Óculos Irado",
    "Pelúcia de Raposa Kitsune",
    "Mini Hakkero",
    "Gohei de 3 Metros",
    "Pente para Gatos",
    "Braço de um Boneco de Madeira",
    "Bandana Vermelha",
    "Braço de um Boneco de Madeira (Roubado)",
    "Mini Metralhadora",
    "Livro “Python para Iniciantes”",
    "Livro “Como Usar Ataques de Penetração 101”",
    "Livro “Botei Fogo no Meu Colega, e Agora?”",
    "Livro “História da Floresta Escura e os 3 Pássaros”",
    "Livro “Para os Viciados em Café”",
    "Miniatura de Biblioteca",
    "Livro “Como Lidar com a Morte da Minha Esposa”",
    "Mimicry",
    "Talismã com um Rosto Familiar",
    "Saber",
    "Enxada (Deluxe, Usada pelo Deus do Capino dos Lotes)",
    "Cópia Física de “Everhood 2”",
    "Manga “Call of the Night”",
    "Mangá “Jujutsu Kaizen 0”",
    "Partes de Carro",
    "Dicionário da Língua Espanhola",
    "Cópia Física de “A Night in the Woods”",
    "Coleção de Mangá da Série Jojo",
    "Cópia Física de “Anno Mutationem”",
    "10000 Jades Estelares",
    "Cópia Digital de “Terraria” (2000 Horas)",
    "Kit de Poker",
    "Bola de Futebol Assinada",
    "Kit de Chapéus",
    "Livro “Como Fazer Agachamento”",
    "Jockey de Galinha",
    "Doutorado",
    "Máquina de Contato Extraterrestre",
    "“Are You Sure?”"
]

precos = [
    15000,
    120,
    250,
    340,
    800,
    2000,
    90,
    130,
    100,
    300,
    1800,
    60,
    120,
    75,
    110,
    50,
    400,
    95,
    2000,
    600,
    1000,
    3500,
    300,
    45,
    60,
    800,
    70,
    250,
    900,
    220,
    10000,
    80,
    150,
    500,
    220,
    65,
    700,
    5000,
    15000,
    1
]


valordiario = 0
produtosavenda = []
vendadias = []
dias = 1
diaspassados = []



def adicionarprodutosnaloja():
    repet = random.randint(1,3)
    while repet > 0:
        nomesnaloja = random.randint(0,80)
        if nomesnaloja < len(Nomes):
            produtosnaloja = random.randint(0,len(itens) - 1)
            produtosavenda.append([Nomes[nomesnaloja], itens[produtosnaloja], precos[produtosnaloja]])
        repet -= 1
        
        #5. Função que calcula o fim do dia
def Fimdedia():
    global valordiario, dias
# calcula a renda diaria
    for k in produtosavenda:
        valordiario += k[2]

    resumo = np.array(produtosavenda)
    print('''#
#''')
    print('Relátorio do que foi vendido hoje (dia {}) : \n {}'.format(dias, resumo))

#envia o valor das vendas diarias 
    vendadias.append(valordiario)
# zera o valor diario
    valordiario = 0
# array de dias
    diaspassados.append(dias)


    if dias == 1:
        print("Gráfico não dísponivel")
    else:
        # Criação do gráfico
        # primeiro array = Y no gráfico, segundo array = X no gráfico
        # obs, o primeiro e segundo array devem ter o a mesma quantidade de valores
        plt.plot(diaspassados ,  vendadias)

        #Acessando a janela Tkinter
        # pega a atual figura
        fig = plt.gcf()
        # chama o canvas
        canvas = fig.canvas

        # Alterando o título da janela usando o canvas
        canvas.manager.window.title("resumo diário")
        # Mostra o gráfico
        plt.show()

    del produtosavenda[:]

        # para rodar o código dennovo feche a janela do gráfico atual.
    # dias passados
    dias += 1
for i in range(10): 
    adicionarprodutosnaloja()
    Fimdedia()
