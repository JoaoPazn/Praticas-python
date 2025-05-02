produtosavenda = []
ProtagonistaDaJornadaDeRevendas = "Ventilador"
def venderprodutos():
    continuarvendas = "0"
    while continuarvendas == "0":
        meuprodutoavender = input("Digite o nome do produto que você irá vender : ")
        meuprodutoavenderpreco = input("Digite o preço apropiado do produto que você vai vender : ")
        meuprodutoavenderpreco = int(meuprodutoavenderpreco)
        produtosavenda.append([ProtagonistaDaJornadaDeRevendas, meuprodutoavender, meuprodutoavenderpreco])

        continuarvendas = input("Deseja continuar vendendo outros produtos? 0 - Sim / 1 - Não : ")
        if continuarvendas == "0":
            pass
        else:
            break

    print(produtosavenda)


venderprodutos()