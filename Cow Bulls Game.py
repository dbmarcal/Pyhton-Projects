# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 13:34:51 2020

@author: Daniel Marçal
"""

from random import randint
r = 0
def numb():
    for i in range (1) :
        global r
        global r1
        global r2
        global r3
        global r4
        r= randint(0000,9999)
        r4 = r%10
        r3 = (r%100-r4) // 10
        r2 = ((r%1000) - (r%100 - r4) - r4 ) // 100
        r1 = int((r/1000) - (r%1000 / 1000))
#        print(r)

    while r > 1000 and (r1!=r2) and (r1!=r3) and (r1!=r4) and (r2!= r3) and (r2!=r4) and (r3!=r4):
        
        r4 = r%10
        r3 = (r%100-r4) // 10
        r2 = ((r%1000) - (r%100 - r4) - r4 ) // 100
        r1 = int((r/1000) - (r%1000 / 1000))
#        print(r)
        break
    
    else :
        numb()


contagem = 1



def main() :
    touros = 0
    vacas = 0
    n = int(input("Qual é o número: "))
    while n < 1000 or n > 9999 :
        print("O número tem de ter 4 dígitos!")
        n = int(input("Qual é o número: "))
    
   
    global contagem


    n4 = n%10 
    n3 = (n%100 - n4) // 10
    n2 = ((n%1000) - (n%100 - n4) - n4 ) // 100
    n1 = int((n/1000) - (n%1000 / 1000))


    
    if n1 == r1 :
        vacas += 1
    if n2 == r2 :
            vacas += 1
    if n3 == r3 :
        vacas += 1
    if n4 == r4 :
        vacas += 1

    if (n1 == r2):
        touros +=1
    if (n1 == r3):
        touros +=1
    if (n1 == r4):
        touros +=1
    
    if (n2 == r1):
        touros +=1
    if (n2 == r3):
        touros +=1
    if (n2 == r4):
        touros +=1  
    
    if (n3 == r1):
        touros +=1
    if (n3 == r2):
        touros +=1
    if (n3 == r4):
        touros +=1
    
    if (n4 == r1):
        touros +=1
    if (n4 == r2):
        touros +=1
    if (n4 == r3):
        touros +=1


    if vacas == 4:
        print("ganhou em ",contagem," tentativas")
    else:
        print("Tem ",vacas,"vacas e " ,touros, "touros")
        contagem=contagem + 1
        main()

print("Bem vindo ao jogo das vacas e touros! Neste jogo terás de tentar acertar nos 4 dígitos mágicos!")
print("Se acertares um dígito exato, na posição exata ganhas uma vaca")
print("Se acertares um dígito mas não o colocaste na posição certa, ganhas um touro")
print("O Objetivo é conseguires ficar com 4 vacas, ou seja acertares todos os números!" )
print("PS: Não há números repetidos!")
print("Achas que estás à altura!? Não te esqueças que eu vou contar o teu número de tentativas!")    

numb()
main()
        

    
