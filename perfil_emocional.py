# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:45:23 2023

@author: jason
"""

# Define a função para fazer a pergunta e obter a resposta do usuário
def fazer_pergunta(pergunta):
    while True:
        resposta = input(pergunta)
        if resposta.isdigit() and 1 <= int(resposta) <= 5:
            return int(resposta)
        print("A resposta deve ser um número inteiro entre 1 e 5.")
        
# Define a função para somar as respostas A e B

def somar_respostas_a_b():
    soma_a = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 + a11
    soma_b = b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9 + b10 + b11
    return soma_a, soma_b



# Define a função para somar as respostas a(n) e b(n)
def somar2_respostas_a_b():
    soma_a = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 + a11
    soma_b = b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9 + b10 + b11
    return (soma_a, soma_b)

# Faz a primeira pergunta e obtém as respostas
a1 = fazer_pergunta("1a) Você pensaria: “Eu não tenho consideração pelos outros”. ____\n")
b1 = fazer_pergunta("1b) Você pensaria que precisa fazer algo para compensar seu amigo o mais brevemente possível. ____\n")
a2 = fazer_pergunta("2a) Você pensaria em pedir demissão. ____\n")
b2 = fazer_pergunta("2b) Você pensaria: “Isso está me deixando aflito. Preciso consertar ou pedir para alguém consertar”. ____\n")
a3 = fazer_pergunta("3a) Você se sentiria incompetente. ____\n")
b3 = fazer_pergunta("3b) Você pensaria: “Eu mereço ser repreendido por ter feito mal o projeto”. ____\n")
a4 = fazer_pergunta("4a) Você ficaria quieto e evitaria o colega de trabalho. ____\n")
b4 = fazer_pergunta("4b) Você se sentiria infeliz e ansioso para corrigir a situação. ____\n")



a5 = fazer_pergunta("5a) Você se sentiria um incompetente por não saber nem lançar uma bola. ____\n")
b5 = fazer_pergunta("5b) Você pediria desculpas e faria questão de consolar seu amigo. ____\n")
a6 = fazer_pergunta("6a) Você pensaria: “Eu sou uma pessoa péssima”. ____\n")
b6 = fazer_pergunta("6b) Você se sentiria mal por não estar mais alerta ao dirigir numa estrada. ____\n")
a7 = fazer_pergunta("7a) Você se sentiria burro. ____\n")
b7 = fazer_pergunta("7b) Você pensaria: “Eu deveria ter estudado mais”. ____\n")
a8 = fazer_pergunta("8a) Você se sentiria pequeno… como um rato. ____\n")
b8 = fazer_pergunta("8b) Você pediria desculpas e falaria sobre os pontos positivos desse amigo. ____\n")
a9 = fazer_pergunta("9a) Você sentiria vontade de se esconder. ____\n")
b9 = fazer_pergunta("9b) Você pensaria: “Eu deveria ter reconhecido o problema e feito um trabalho melhor”. ____\n")
a10 = fazer_pergunta("10a) Você pensaria: “Sou um irresponsável e incompetente”. ____\n")
b10 = fazer_pergunta("10b) Você juraria ter mais cuidado da próxima vez. ____\n")
a11 = fazer_pergunta("11a) Você gostaria de estar em qualquer lugar menos naquela festa. ____\n")
b11 = fazer_pergunta("11b) Você ficaria até mais tarde para ajudar a limpar a mancha. ____\n")


# Chamar a funçao de soma

soma_respostas_a_b = somar_respostas_a_b()
print("Soma das respostas para a):", soma_respostas_a_b[0])
print("Soma das respostas para b):", soma_respostas_a_b[1])




