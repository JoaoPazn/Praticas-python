import random
Erro = 0
Selecionamento = input('''
Selecione um personagem :    

1.Anne Jane (F)
Vida : 10 
Ataque : 5 
Velocidade : 3 
passiva : devolver 1 ponto de dano recebido
   
2.Belshazzar agapeteus (F)
Vida : 8
Ataque : 7
Velocidade : X
passiva : sempre agir primeiro

3.Roland Loland (M)
Vida : 14
Ataque : 4
Velocidade : 1
passiva : aumenta o ataque em 1 a cada ataque recebido, recupera 1 de vida no ataque
                       
                       SELECIONE O PERSONAGEM : ''')

if Selecionamento == "1":
    nome = "Anne jane"
    Vida = 10 
    Ataque = 5 
    Velocidade = 3 
    Passiva = "devolverDano"
elif Selecionamento == "2":
    nome = "Belshazzar agapeteus"
    Vida = 8 
    Ataque = 7
    Velocidade = "X"
    Passiva = "ataquePrimeiro"
elif Selecionamento == "3":
    nome = "Roland Loland"
    Vida = 14 
    Ataque = 4
    Velocidade = 1
    Passiva = "Tanque"
else : 
    Erro = 1
    print("VALOR DE PERSONAGEM INVALIDO, PORFAVOR REINICIE O CÓDIGO")

while Erro != 1: 
    Erro = 1
    numero_aleatorio = random.randint(1, 3)

    print("Instancia de Batalha :", numero_aleatorio)

    if numero_aleatorio == 1:
        print('''
        Lobo branco Ataca!
        vida : 4     
        Ataque : 3        
        velocidade : 10      
            ''')
        inimigo_vida = 4
        inimigo_Ataque = 3
        inimigo_Velocidade = 10

    if numero_aleatorio == 2:
        print('''
        Corvo Doente Ataca!
        vida : 2     
        Ataque : 1        
        velocidade : 1      
            ''')
        inimigo_vida = 2
        inimigo_Ataque = 1
        inimigo_Velocidade = 1

    if numero_aleatorio == 3:
        print('''
        Galho louco Ataca!
        vida : 7     
        Ataque : 1        
        velocidade : 2     
            ''')
        inimigo_vida = 7
        inimigo_Ataque = 1
        inimigo_Velocidade = 2

turno = 0
    
def testeVelocidade(suavel, inimigovel):
        if suavel == "X" :
            print("Seu turno!")
            turno = 0
        elif suavel < inimigovel:
            print("Turno do inimigo!")
            turno = 1
        elif suavel == inimigovel:
            print("Turno do Inimigo!")
            turno = 1
        else:
            print("Seu turno!")
            turno = 0

testeVelocidade(Velocidade, inimigo_Velocidade)