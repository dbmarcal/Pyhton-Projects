# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 17:04:14 2020

@author: Daniel Marçal

"""
import sys

print("Vamos calcular a tua média da faculdade!")
print("Caso não tenhas feito uma cadeira preenche com 00")

creditos=0
notas = 0
cadeiras = 0

def contagem() :
    media = (notas * creditos) / (creditos * cadeiras)
    print("A tua média é de ",(media),  ", tens um total de " ,(cadeiras), " cadeiras feitas e neste momento tens ",(creditos)," créditos!")


def continuar() :
    x = int(input("Próximo semestre?(1-sim 2-não): "))
    if x == 2:
        contagem()
        sys.exit()
    elif x !=1:
        print("Erro tente de novo (1-sim ou 2-não)")
        continuar()

    
        
                    ##### Primeiro Ano - Primeiro Semestre #####

AM1 = (int(input("ANÁLISE MATEMÁTICA 1: ")))        
while  AM1 != 00 and AM1 < 10 or AM1 > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        AM1 = (int(input("ANÁLISE MATEMÁTICA 1: ")))
if AM1 != 00 :
        creditos = creditos + 6
        notas = notas + AM1
        cadeiras = cadeiras + 1
else :
    creditos = creditos

BG = int(input("BIOLOGIA GERAL: "))
while  BG != 00 and BG < 10 or BG > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        BG = int(input("BIOLOGIA GERAL: "))
if BG != 00 :
        creditos =creditos + 5
        notas=notas = notas + BG
        cadeiras = cadeiras + 1
else :
        creditos = creditos

FSI = int(input("FUNDAMENTOS DE SISTEMAS DE INFORMAÇÃO: "))
while  FSI != 00 and FSI < 10 or FSI > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        FSI = int(input("FUNDAMENTOS DE SISTEMAS DE INFORMAÇÃO: "))
if FSI != 00 :
        creditos =creditos + 5
        notas = notas + FSI
        cadeiras = cadeiras + 1
else :
        creditos = creditos

PB = int(input("PRESPETIVAS EM BIOINFORMÁTICA: "))
while  PB != 00 and PB < 10 or PB > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        PB = int(input("PRESPETIVAS EM BIOINFORMÁTICA: "))
if PB != 00 :
        creditos =creditos + 3.5
        notas = notas + PB
        cadeiras = cadeiras + 1
else :
        creditos = creditos

QG = int(input("QUÍMICA GERAL: "))
while  QG != 00 and QG < 10 or QG > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        QG = int(input("QUÍMICA GERAL: "))
if QG != 00 :
        creditos = creditos + 5.5
        notas = notas + QG
        cadeiras = cadeiras + 1
else :
        creditos = creditos

AL = int(input("ÁLGEBRA LINEAR: "))
while  AL != 00 and AL < 10 or AL > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        AL = int(input("ÁLGEBRA LINEAR: "))
if AL != 00 :
        creditos = creditos + 5
        notas = notas + AL
        cadeiras = cadeiras + 1
else :
        creditos = creditos


                    ##### Primeiro Ano - Segundo Semestre #####

continuar()

AM2 = int(input("ANÁLISE MATEMÁTICA 2: "))
while  AM2 != 00 and AM2 < 10 or AM2 > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        AM2 = int(input("ANÁLISE MATEMÁTICA 2: "))
if AM2 != 00 :
        creditos = creditos + 6
        notas = notas + AM2
        cadeiras = cadeiras + 1
else :
        creditos = creditos

BDD = int(input("BASES DE DADOS: "))
while  BDD != 00 and BDD < 10 or BDD > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        BDD = int(input("BASES DE DADOS: "))
if BDD != 00 :
        creditos =creditos + 5
        notas=notas = notas + BDD
        cadeiras = cadeiras + 1
else :
        creditos = creditos

BMC = int(input("BIOLOGIA MOLECULAR E CELULAR: "))
while  BMC != 00 and BMC < 10 or BMC > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        BMC = int(input("BIOLOGIA MOLECULAR E CELULAR: "))
if BMC != 00 :
        creditos =creditos + 5
        notas = notas + BMC
        cadeiras = cadeiras + 1
else :
        creditos = creditos

IE = int(input("INTRODUÇÃO À ESTATÍSTICA: "))
while  IE != 00 and IE < 10 or IE > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        IE = int(input("INTRODUÇÃO À ESTATÍSTICA: "))
if IE != 00 :
        creditos =creditos + 4
        notas = notas + IE
        cadeiras = cadeiras + 1
else :
        creditos = creditos

LP1 = int(input("lINGUAGENS DE PROGRAMAÇÃO 1: "))
while  LP1 != 00 and LP1 < 10 or LP1 > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        LP1 = int(input("LINGUAGENS DE PROGRAMAÇÃO 1: "))
if LP1 != 00 :
        creditos = creditos + 5
        notas = notas + LP1
        cadeiras = cadeiras + 1
else :
        creditos = creditos

QO = int(input("QUÍMICA ORGÂNICA: "))
while  QO != 00 and QO < 10 or QO > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        QO = int(input("QUÍMICA ORGÂNICA: "))
if QO != 00 :
        creditos = creditos + 5
        notas = notas + QO
        cadeiras = cadeiras + 1
else :
        creditos = creditos


                    ##### Segundo Ano - Primeiro Semestre #####

continuar()

ATDM = int(input("ANÁLISE E TRATAMENTO DE DADOS MULTIVARIADOS: "))
while  ATDM != 00 and ATDM < 10 or ATDM > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        ATDM = int(input("ANÁLISE E TRATAMENTO DE DADOS MULTIVARIADOS: "))
if ATDM != 00 :
        creditos = creditos + 5.5
        notas = notas + ATDM
        cadeiras = cadeiras + 1
else :
        creditos = creditos

BQ = int(input("BIOQUÍMICA: "))
while  BQ != 00 and BQ < 10 or BQ > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        BQ = int(input("BIOQUÍMICA: "))
if BQ != 00 :
        creditos =creditos + 4.5
        notas=notas = notas + BQ
        cadeiras = cadeiras + 1
else :
        creditos = creditos

DW = int(input("DATA WAREHOUSING: "))
while  DW != 00 and DW < 10 or DW > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        DW = int(input("DATA WAREHOUSING: "))
if DW != 00 :
        creditos =creditos + 5
        notas = notas + DW
        cadeiras = cadeiras + 1
else :
        creditos = creditos
        
EM = int(input("ESPETROESCOPIA MOLECULAR: "))
while  EM != 00 and EM < 10 or EM > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        EM = int(input("ESPETROESCOPIA MOLECULAR: "))
if EM != 00 :
        creditos = creditos + 5
        notas = notas + EM
        cadeiras = cadeiras + 1
else :
        creditos = creditos


GE = int(input("GENÓMICA ESTRUTURAL E EVOLUTIVA: "))
while  GE != 00 and GE < 10 or GE > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        GE = int(input("GENÓMICA ESTRUTURAL E EVOLUTIVA: "))
if GE != 00 :
        creditos = creditos + 5
        notas = notas + GE
        cadeiras = cadeiras + 1
else :
        creditos = creditos
        

LP2 = int(input("LINGUAGENS DE PROGRAMAÇÃO 2: "))
while  LP2 != 00 and LP2 < 10 or LP2 > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        LP2 = int(input("LINGUAGENS DE PROGRAMAÇÃO 2: "))
if LP2 != 00 :
        creditos =creditos + 5
        notas = notas + LP2
        cadeiras = cadeiras + 1
else :
        creditos = creditos
        

                    ##### Segundo Ano - Segundo Semestre #####

continuar()

ASB = int(input("ANÁLISE DE SEQUÊNCIAS BIOLÓGICAS: "))
while  ASB != 00 and ASB < 10 or ASB > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        ASB = int(input("ANÁLISE DE SEQUÊNCIAS BIOLÓGICAS: "))
if ASB != 00 :
        creditos = creditos + 5
        notas = notas + ASB
        cadeiras = cadeiras + 1
else :
        creditos = creditos

AA = int(input("APRENDIZAGEM AUTOMÁTICA: "))
while  AA != 00 and AA < 10 or AA > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        AA = int(input("APRENDIZAGEM AUTOMÁTICA: "))
if AA != 00 :
        creditos =creditos + 5
        notas=notas = notas + AA
        cadeiras = cadeiras + 1
else :
        creditos = creditos

CAD = int(input("COMPUTAÇÃO DE ALTO DESEMPENHO: "))
while  CAD != 00 and CAD < 10 or CAD > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        CAD = int(input("COMPUTAÇÃO DE ALTO DESEMPENHO: "))
if CAD != 00 :
        creditos =creditos + 5
        notas = notas + CAD
        cadeiras = cadeiras + 1
else :
        creditos = creditos

DM = int(input("DATA MINING: "))
while  DM != 00 and DM < 10 or DM > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        DM = int(input("DATA MINING: "))
if DM != 00 :
        creditos =creditos + 5
        notas = notas + DM
        cadeiras = cadeiras + 1
else :
        creditos = creditos

MERE = int(input("METABOLISMO E REGULAÇÃO: "))
while  MERE != 00 and MERE < 10 or MERE > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        MERE = int(input("METABOLISMO E REGULAÇÃO: "))
if MERE != 00 :
        creditos = creditos + 5
        notas = notas + MERE
        cadeiras = cadeiras + 1
else :
        creditos = creditos

ESI = int(input("ÉTICA E SISTEMAS DA INFORMAÇÃO: "))
while  ESI != 00 and ESI < 10 or ESI > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        ESI = int(input("ÉTICA E SISTEMAS DA INFORMAÇÃO: "))
if ESI != 00 :
        creditos = creditos + 5
        notas = notas + ESI
        cadeiras = cadeiras + 1
else :
        creditos = creditos
        

                    ##### Terceiro Ano - Primeiro Semestre #####

continuar()

BGD = int(input("BIG DATA: "))
while  BGD != 00 and BGD < 10 or BGD > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        BGD = int(input("BIG DATA: "))
if BGD != 00 :
        creditos = creditos + 5
        notas = notas + BGD
        cadeiras = cadeiras + 1
else :
        creditos = creditos

BC = int(input("BIOQUÍMICA COMPUTACIONAL: "))
while  BC != 00 and BC < 10 or BC > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        BC = int(input("BIOQUÍMICA COMPUTACIONAL: "))
if BC != 00 :
        creditos =creditos + 5.5
        notas=notas = notas + BC
        cadeiras = cadeiras + 1
else :
        creditos = creditos

E = int(input("EMPREENDEDORISMO: "))
while  E != 00 and E < 10 or E > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        E = int(input("EMPREENDEDORISMO: "))
if E != 00 :
        creditos =creditos + 4.5
        notas = notas + E
        cadeiras = cadeiras + 1
else :
        creditos = creditos

LBI = int(input("LABORATÓRIO DE BIOINFORMÁTICA: "))
while  LBI != 00 and LBI < 10 or LBI > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        LBI = int(input("LABORATÓRIO DE BIOINFORMÁTICA: "))
if LBI != 00 :
        creditos =creditos + 10
        notas = notas + LBI
        cadeiras = cadeiras + 1
else :
        creditos = creditos

MPB = int(input("MODELAÇÃO DE PROCESSOS BIOLÓGICOS: "))
while  MPB != 00 and MPB < 10 or MPB > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        MPB = int(input("MODELAÇÃO DE PROCESSOS BIOLÓGICOS: "))
if MPB != 00 :
        creditos = creditos + 5
        notas = notas + MPB
        cadeiras = cadeiras + 1
else :
        creditos = creditos


                    ##### Estágio #####
                        
continuar()                

EST = int(input("ESTÁGIO: "))
while  EST != 00 and EST < 10 or EST > 20:
        print ("Se passaste a esta cadeira seleciona uma nota entre 10 e 20, caso não tenhas feito a cadeira preenche com 00")
        EST = int(input("ESTÁGIO: "))
if EST != 00 :
        creditos = creditos + 30
        notas = notas + EST
        cadeiras = cadeiras + 1
else :
        creditos = creditos
        
if cadeiras == 30 and creditos == 180 :
    media = (notas * creditos) / (creditos * cadeiras)
    print("Parabéns estás licenciado!!!")
    print("A tua média é de ",media)
else:
    contagem()
 

        
















    