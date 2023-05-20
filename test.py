import numpy as np

def TypeQuest(tipo, arm1):
    f = np.array(eval(input(f"Insira os valores {tipo} (x,y,z): ")))
    vet = np.copyto(arm1, f)
    return vet

vetor_Forca = np.zeros(3)

TypeQuest("Força", vetor_Forca)

print(vetor_Forca)