#Jogo feito por Ryan Costa com o intuito de simular um jogo de par ou impar

#importações
from random import randint
from time import sleep

#funções
def robotchoice(user):
    cpu = randint(0,10)
    print("Computador: Eu escolho {}".format(cpu))
    print("Jogador:Eu escolho {}".format(user))
    print("somando...")
    sleep(0.8)
    return cpu
def vitoria():
    print("-" * len("Você Venceu!"))
    print("Você Venceu!")
    print("-" * len("Você Venceu!"))
def derrota():
    print("-" * len("Você Perdeu!"))
    print("Você Perdeu!")
    print("-" * len("Você Perdeu!"))
def intro():
    frase = "Bem vindo ao PAR OU ÍMPAR"
    print("-" * len(frase))
    print(frase)
    print("-" * len(frase))
def escolha():
    choice = input("par ou impar?[P/I]").strip().upper()
    return choice
def number():
    user = int(input("Digite um número entre 0 e 10: "))
    return user


#exibição inicial
intro()
sleep (1)

#interativo
choice = escolha()

#condicional

#caso par
if choice == "P": 
    user = number()#escolher número
    
    #randomiza jogada do computador
    cpu = robotchoice(user) 
    sleep(1)

    #verificador par 
    if (user + cpu) % 2== 0:
        vitoria()
    else:
        derrota()

#caso impar
elif choice == "I": 
    user = number() #escolher número
    
    #randomiza jogada do computador
    cpu = robotchoice(user) 
    sleep(1)

    #verificador par
    if (user + cpu) % 2== 0:
        derrota()
    else:
        vitoria()

#caso jogador não digite par ou ímpar
else: 
    while choice != "P" and choice != "I": #repeat até escolha funcionável
        print("Você não digitou P nem I")
        choice = escolha()
    user = number() #escolher número novamente
    cpu = robotchoice(user) #randomiza novamente
    sleep(1)
    
    #condicional novamente
    
    #caso par
    if choice=="P":
        #verificador par
        if (user+cpu) % 2 == 0:
            vitoria()
        else:
            derrota()
    
    #caso impar
    else:
        #verificador par
        if (user + cpu) %2 == 0:
            derrota()
        else:                 
            vitoria()    
#fim