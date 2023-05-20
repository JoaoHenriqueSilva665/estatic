import numpy as np
import math as mt
def TypeQuest(tipo, arm1):
    f = np.array(eval(input(f"Insira os valores {tipo} (x,y,z): ")))
    np.copyto(arm1, f)

def decompor_forca(forca, tetaz_xy, teta_xy):
    fz = forca * (mt.sin(mt.radians(tetaz_xy)))
    fxy = forca*(mt.cos(mt.radians(tetaz_xy)))
    fx = fxy * (mt.cos(mt.radians(teta_xy)))
    fy = fxy * (mt.sin(mt.radians(teta_xy)))

    list_auxiliar = []
    array_forca = np.array([fx, fy, fz])
    for i in range(np.size(array_forca)):
        quest = input(f"Componente {round(array_forca[i], 6)} [positivo/negativo] P/N : ")
        if quest == "p" or quest == "P":
            b = (array_forca[i]) * (1)
            list_auxiliar.append(b)
        elif quest == "n" or quest == "N":
            b = (array_forca[i]) * (-1)
            list_auxiliar.append(b)
    np.copyto(array_forca, list_auxiliar)
    return array_forca


vetor_Forca = np.empty(3)
vetor_direcao = np.empty(3)
eixo = np.zeros(3)
vetor_ab = np.empty(3)

print("================== escolha a opção =======================\n")
while True:
    quest = input("força[F], distancia[D], eixo[E], momento no ponto e no eixo[M], sair[S]: ")
    if quest == "F" or quest == "f":
        forca_quest = input("a força é: conhecida? [c], por dois pontos? [p], por dois angulos [a]: ")
        if forca_quest == "c" or forca_quest == "C":
            TypeQuest("Força", vetor_Forca)
            continue

        elif forca_quest == "p" or forca_quest == "P":
           a = np.array(eval(input("A: ")))
           b = np.array(eval(input("B: ")))
           sub_ab = (b - a)
           np.append(vetor_ab, sub_ab)

        elif forca_quest == "A" or forca_quest == "a":
            forca_escalar = float(input("insira a força: "))
            angalfa = float(input("angulo alfa: "))
            angbeta = float(input("angulo em beta: "))
            vetor_angulo = decompor_forca(forca_escalar, angalfa, angbeta)
            np.copyto(vetor_Forca, vetor_angulo)

            continue

    elif quest == "D" or quest == "d":
        TypeQuest("Distancia", vetor_direcao)
        continue

    elif quest == "E" or quest == "e":
        TypeQuest("eixo", eixo)
        continue

    elif quest == "M" or quest == "m":
        momento = np.cross(vetor_direcao, vetor_Forca)
        result = 0
        if np.size(eixo) == 0:
            print("vazio, somente o momento")
            print(f" o momento {momento}")
        if np.size(eixo) != 0:
            for k in range(3):
                result += eixo[k] * momento[k]
            print(f" o momento {momento}")
            print(np.dot(result, eixo))
        break

    elif quest == "s" or quest == "S":
        break

    else:
        print("digite uma opção valida!\n")
        continue

