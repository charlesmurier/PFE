import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import random
import time
import pandas as pd
from scipy.io.wavfile import read
from pylab import specgram
from os import path
import pydub


global ypage_piano
ypage_piano = 0
global ypage_tab
ypage_tab = 0
global x_tab
x_tab = 200
x = 200
global xnext_tab
xnext_tab = 0
global compt
compt = 0
global test
test = False

# Partition
img = mpimg.imread("part.png")
part = np.copy(img)

# Simples
img = mpimg.imread("Notes/Simples/1.png")
S1 = np.copy(img)
img = mpimg.imread("Notes/Simples/1D.png")
S1D = np.copy(img)
img = mpimg.imread("Notes/Simples/1.1.png")
S11 = np.copy(img)
img = mpimg.imread("Notes/Simples/1.1D.png")
S11D = np.copy(img)
img = mpimg.imread("Notes/Simples/1.2.png")
S12 = np.copy(img)
img = mpimg.imread("Notes/Simples/1.2D.png")
S12D = np.copy(img)
img = mpimg.imread("Notes/Simples/1.3.png")
S13 = np.copy(img)
img = mpimg.imread("Notes/Simples/1.3D.png")
S13D = np.copy(img)
img = mpimg.imread("Notes/Simples/1.4.png")
S14 = np.copy(img)
img = mpimg.imread("Notes/Simples/1.4D.png")
S14D = np.copy(img)
img = mpimg.imread("Notes/Simples/1B.png")
S1B = np.copy(img)
img = mpimg.imread("Notes/Simples/1BD.png")
S1BD = np.copy(img)

# Simples Reverses
img = mpimg.imread("Notes/Simples Reverses/1R.png")
S1R = np.copy(img)
img = mpimg.imread("Notes/Simples Reverses/1DR.png")
S1DR = np.copy(img)
img = mpimg.imread("Notes/Simples Reverses/1BR.png")
S1BR = np.copy(img)
img = mpimg.imread("Notes/Simples Reverses/1BDR.png")
S1BDR = np.copy(img)
img = mpimg.imread("Notes/Simples Reverses/1.1R.png")
S11R = np.copy(img)
img = mpimg.imread("Notes/Simples Reverses/1.1DR.png")
S11DR = np.copy(img)
img = mpimg.imread("Notes/Simples Reverses/1.2R.png")
S12R = np.copy(img)
img = mpimg.imread("Notes/Simples Reverses/1.2DR.png")
S12DR = np.copy(img)
img = mpimg.imread("Notes/Simples Reverses/1.3R.png")
S13R = np.copy(img)
img = mpimg.imread("Notes/Simples Reverses/1.3DR.png")
S13DR = np.copy(img)
img = mpimg.imread("Notes/Simples Reverses/1.4R.png")
S14R = np.copy(img)
img = mpimg.imread("Notes/Simples Reverses/1.4DR.png")
S14DR = np.copy(img)

# Rondes
img = mpimg.imread("Notes/Rondes/Ronde.png")
R = np.copy(img)
img = mpimg.imread("Notes/Rondes/RondeD.png")
RD = np.copy(img)

# Alterations
img = mpimg.imread("Notes/Alterations/Becarre.png")
Becarre = np.copy(img)
img = mpimg.imread("Notes/Alterations/Becarre2.png")
Becarre2 = np.copy(img)
img = mpimg.imread("Notes/Alterations/BecarreBemol.png")
BecarreBemol = np.copy(img)
img = mpimg.imread("Notes/Alterations/BecarreDiese.png")
BecarreDiese = np.copy(img)
img = mpimg.imread("Notes/Alterations/Bemol.png")
Bemol = np.copy(img)
img = mpimg.imread("Notes/Alterations/Bemol2.png")
Bemol2 = np.copy(img)
img = mpimg.imread("Notes/Alterations/Diese.png")
Diese = np.copy(img)

# Tablature
img = mpimg.imread("tab.png")
tab = np.copy(img)

# Chiffres
img = mpimg.imread("Chiffres/C0.png")
C0 = np.copy(img)
img = mpimg.imread("Chiffres/C1.png")
C1 = np.copy(img)
img = mpimg.imread("Chiffres/C2.png")
C2 = np.copy(img)
img = mpimg.imread("Chiffres/C3.png")
C3 = np.copy(img)
img = mpimg.imread("Chiffres/C4.png")
C4 = np.copy(img)
img = mpimg.imread("Chiffres/C5.png")
C5 = np.copy(img)
img = mpimg.imread("Chiffres/C6.png")
C6 = np.copy(img)
img = mpimg.imread("Chiffres/C7.png")
C7 = np.copy(img)
img = mpimg.imread("Chiffres/C8.png")
C8 = np.copy(img)
img = mpimg.imread("Chiffres/C9.png")
C9 = np.copy(img)
img = mpimg.imread("Chiffres/C10.png")
C10 = np.copy(img)
img = mpimg.imread("Chiffres/C11.png")
C11 = np.copy(img)
img = mpimg.imread("Chiffres/C12.png")
C12 = np.copy(img)


def aleatoire_both(nb):
    freq = []
    for i in range(nb):
        choix = random.randint(1, 5)
        if choix == 1:
            freq.append(random.randint(131, 261))
        elif choix == 2:
            freq.append(random.randint(261, 523))
        elif choix == 3:
            freq.append(random.randint(523, 1046))
        elif choix == 4:
            freq.append(random.randint(1046, 1975))
    return (freq)


def aleatoire_piano(nb):
    note = ["A", "B", "C", "D", "E", "F", "G"]
    octave = ["inf", "sup"]
    genre = ["Noire"]
    alteration = ["Becarre", "Double Becarre", "Becarre Bemol", "Becarre Diese", "Bemol", "Double Bemol", "Diese",
                  "Double Diese", "None"]
    ListeNotes = []
    for i in range(0, nb):
        L = []
        L.append(note[random.randint(0, len(note) - 1)])
        L.append(octave[random.randint(0, len(octave) - 1)])
        L.append(genre[random.randint(0, len(genre) - 1)])
        if random.randint(0, 2) == 0:
            L.append(alteration[random.randint(0, len(alteration) - 2)])
        else:
            L.append(alteration[8])

        same = random.randint(2, 8)
        if (same == 2) and (nb - i < 3):
            same = 8
        if same > 2:  # 1
            L.append(1)
        elif same == 2:
            L.append(same)
            ListeNotes.append(L)
            L = []
            L.append(note[random.randint(0, len(note) - 1)])
            L.append(octave[random.randint(0, len(octave) - 1)])
            L.append(genre[random.randint(0, len(genre) - 1)])
            if random.randint(0, 2) == 0:
                L.append(alteration[random.randint(0, len(alteration) - 2)])
            else:
                L.append(alteration[8])
            L.append(same)
            i = i + 1
        ListeNotes.append(L)
    return (ListeNotes)


def aleatoire_tab(nb):
    note = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    octave = ["1", "2", "3", "4"]
    ListeNotes = []
    while (len(ListeNotes) < nb):
        rand_note = note[random.randint(0, len(note) - 1)]
        rand_octave = octave[random.randint(0, len(octave) - 1)]
        if not ((rand_octave == "4" and (
                rand_note == "F" or rand_note == "F#" or rand_note == "G" or rand_note == "G#" or rand_note == "A" or rand_note == "A#" or rand_note == "B"))
                or (rand_octave == "1" and (
                        rand_note == "A" or rand_note == "A#" or rand_note == "B" or rand_note == "C" or rand_note == "C#" or rand_note == "D" or rand_note == "D#"))):
            ListeNotes.append(rand_note + rand_octave)
    return (ListeNotes)


def matrice_tab():
    List = [[], [], [], [], [], []]
    List[0] = ["E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4"]
    List[1] = ["B2", "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3"]
    List[2] = ["G2", "G#2", "A2", "A#2", "B2", "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3"]
    List[3] = ["D2", "D#2", "E2", "F2", "F#2", "G2", "G#2", "A2", "A#2", "B2", "C3", "C#3", "D3"]
    List[4] = ["A1", "A#1", "B1", "C2", "C#2", "D2", "D#2", "E2", "F2", "F#2", "G2", "G#2", "A2"]
    List[5] = ["E1", "F1", "F#1", "G1", "G#1", "A1", "A#1", "B1", "C2", "C#2", "D2", "D#2", "E2"]
    tab = np.asarray(List)
    return (tab)


def coord_tab(n):  # NN
    mat = matrice_tab()
    coord = []
    test = False
    for j in range(13):
        if test:
            break
        for i in range(6):
            if n == mat[i][j]:
                coord.append(i + 1)
                coord.append(j)
                test = True
                break
    return (coord)


def position_piano(note, octave, cle, lastx):
    global ypage_piano
    espace = 38
    x = lastx + espace
    if x > 1150:
        ypage_piano = ypage_piano + 272
        x = 150
    if octave == "inf":
        y = 89 + ypage_piano  # DO
        sens = "N"
        if note == "C":
            y = y
            trait(x, octave, ypage_piano)
        elif note == "D":
            y = y - 6
        elif note == "E":
            y = y - (6 + 7)
        elif note == "F":
            y = y - (6 + 7 + 6)
        elif note == "G":
            y = y - (6 + 7 + 6 + 7)
        elif note == "A":
            y = y - (6 + 7 + 6 + 7 + 6)
        elif note == "B":
            y = y - (6 + 7 + 6 + 7 + 6 + 7 + 10)  # +10 car Reverse
            sens = "R"
    elif octave == "sup":
        y = 34 + ypage_piano  # DO
        sens = "R"
        if note == "C":
            y = y
        elif note == "D":
            y = y - 7
        elif note == "E":
            y = y - (7 + 7)
        elif note == "F":
            y = y - (7 + 7 + 6)
        elif note == "G":
            y = y - (7 + 7 + 6 + 6)
        elif note == "A":
            y = y - (7 + 7 + 6 + 6 + 6)
        elif note == "B":
            y = y - (7 + 7 + 6 + 6 + 6 + 6)
        if note == "A" or note == "B":
            trait(x, octave, ypage_piano)
    if cle == "fa":
        y = y + 136
    return ([x, y, sens, ypage_piano])


def position_tab(coord, tab):
    global x_tab
    global xnext_tab
    x_tab += 50 + xnext_tab
    xnext_tab = 0
    global ypage_tab
    if x_tab > 2200:
        ypage_tab += 290
        x_tab = 250
    y = 206
    yspace = 31
    image = C0
    if coord[0] == 1:
        y += ypage_tab
    elif coord[0] == 2:
        y += yspace + ypage_tab
    elif coord[0] == 3:
        y += yspace * 2 + ypage_tab
    elif coord[0] == 4:
        y += yspace * 3 + ypage_tab
    elif coord[0] == 5:
        y += yspace * 4 + ypage_tab
    elif coord[0] == 6:
        y += yspace * 5 + ypage_tab

    if coord[1] == 0:
        image = C0
    elif coord[1] == 1:
        image = C1
    elif coord[1] == 2:
        image = C2
    elif coord[1] == 3:
        image = C3
    elif coord[1] == 4:
        image = C4
    elif coord[1] == 5:
        image = C5
    elif coord[1] == 6:
        image = C6
    elif coord[1] == 7:
        image = C7
    elif coord[1] == 8:
        image = C8
    elif coord[1] == 9:
        image = C9
    elif coord[1] == 10:
        image = C10
        xnext_tab += 15
    elif coord[1] == 11:
        image = C11
        xnext_tab += 15
    elif coord[1] == 12:
        image = C12
        xnext_tab += 15
    tab = remplacement_tab(x_tab, y, image, tab)
    return (tab)


def trait(x, octave, ypage_piano):
    if octave == "inf":
        a = 84 + ypage_piano
    elif octave == "sup":
        a = 6 + ypage_piano
    for i in range(x - 5, x + 13 + 7):
        part[a, i] = [0.2, 0.2, 0.2, 1]
        part[a + 1, i] = [0.2, 0.2, 0.2, 1]


def forme(genre, sens):
    if sens == 'N':
        if genre == "Noire":
            fig = S1
        elif genre == "Noire Pointee":
            fig = S1D
        elif genre == "Croche":
            fig = S11
        elif genre == "Croche Pointee":
            fig = S11D
        elif genre == "Double Croche":
            fig = S12
        elif genre == "Double Croche Pointee":
            fig = S12D
        elif genre == "Triple Croche":
            fig = S13
        elif genre == "Triple Croche Pointee":
            fig = S13D
        elif genre == "Quadruple Croche":
            fig = S14
        elif genre == "Quadruple Croche Pointee":
            fig = S14D
        elif genre == "Blanche":
            fig = S1B
        elif genre == "Blanche Pointee":
            fig = S1BD
        elif genre == "Ronde":
            fig = R
        elif genre == "Ronde Pointee":
            fig = RD
    elif sens == 'R':
        if genre == "Noire":
            fig = S1R
        elif genre == "Noire Pointee":
            fig = S1DR
        elif genre == "Croche":
            fig = S11R
        elif genre == "Croche Pointee":
            fig = S11DR
        elif genre == "Double Croche":
            fig = S12R
        elif genre == "Double Croche Pointee":
            fig = S12DR
        elif genre == "Triple Croche":
            fig = S13R
        elif genre == "Triple Croche Pointee":
            fig = S13DR
        elif genre == "Quadruple Croche":
            fig = S14R
        elif genre == "Quadruple Croche Pointee":
            fig = S14DR
        elif genre == "Blanche":
            fig = S1BR
        elif genre == "Blanche Pointee":
            fig = S1BDR
        elif genre == "Ronde":
            fig = R
        elif genre == "Ronde Pointee":
            fig = RD
    return (fig)


def forme_alteration(L, alteration):  # L=[x,y,sens,ypage_piano]
    x = L[0]
    y = L[1]
    fig = Becarre
    xgap = 5
    ygap = 5
    if alteration == "Becarre":
        fig = Becarre
        ygap = 5
    elif alteration == "Double Becarre":
        fig = Becarre2
        ygap = 5
    elif alteration == "Becarre Bemol":
        fig = BecarreBemol
        ygap = 5
    elif alteration == "Becarre Diese":
        fig = BecarreDiese
        ygap = 5
    elif alteration == "Bemol":
        fig = Bemol
        ygap = 0
    elif alteration == "Double Bemol":
        fig = Bemol2
        ygap = 0
    elif alteration == "Diese":
        fig = Diese
        ygap = 7

    if L[2] == "R":  # decalage entre HG et BG
        y = y + 13

    for i in range(0, fig.shape[0]):  # hauteur
        for j in range(0, fig.shape[1]):  # largeur
            for k in range(0, fig.shape[2]):  # profondeur
                if fig[fig.shape[0] - 1 - i, j, 0] < 0.3 and fig[fig.shape[0] - 1 - i, j, 1] < 0.3 and fig[
                    fig.shape[0] - 1 - i, j, 2] < 0.3 and fig[fig.shape[0] - 1 - i, j, 3] > 0.3:
                    part[L[1] - i + ygap + 13, L[0] + j - (xgap + fig.shape[1]), k] = fig[fig.shape[0] - 1 - i, j, k]
    return ()


def remplacement_piano(note, octave, cle, genre, alteration, same, L):
    fig = 0
    fig = forme(genre, L[2])

    if L[2] == "N":
        for i in range(0, fig.shape[0]):  # hauteur
            for j in range(0, fig.shape[1]):  # largeur
                for k in range(0, fig.shape[2]):  # profondeur
                    if fig[fig.shape[0] - 1 - i, j, 0] < 0.3 and fig[fig.shape[0] - 1 - i, j, 1] < 0.3 and fig[
                        fig.shape[0] - 1 - i, j, 2] < 0.3 and fig[fig.shape[0] - 1 - i, j, 3] > 0.3:
                        part[L[1] - i, L[0] + j, k] = fig[fig.shape[0] - 1 - i, j, k]

    elif L[2] == "R":
        for i in range(0, fig.shape[0]):  # hauteur
            for j in range(0, fig.shape[1]):  # largeur
                for k in range(0, fig.shape[2]):  # profondeur
                    if fig[i, j, 0] < 0.3 and fig[i, j, 1] < 0.3 and fig[i, j, 2] < 0.3 and fig[i, j, 3] > 0.3:
                        part[L[1] + i, L[0] + j, k] = fig[i, j, k]

    if alteration != "None":
        forme_alteration(L, alteration)
    if same == 1:
        return (L[0] + fig.shape[1])
    else:
        global compt
        compt = compt + 1
        if compt < same:
            return (L[0] - 38)
        elif compt == same:
            compt = 0
            return (L[0] + fig.shape[1])


def remplacement_tab(x, y, image, tab):
    for i in range(0, image.shape[0]):  # hauteur
        for j in range(0, image.shape[1]):  # largeur
            for k in range(0, image.shape[2]):  # profondeur
                tab[i + y, j + x, k] = image[i, j, k]
    return (tab)


def remplacement_all_piano(L):
    lastx = 200 - 38  # start
    ListeNotes = L
    for i in range(0, len(ListeNotes)):
        lastx = remplacement_piano(ListeNotes[i][0], ListeNotes[i][1], ListeNotes[i][2], ListeNotes[i][3],
                                   ListeNotes[i][4], ListeNotes[i][5],
                                   position_piano(ListeNotes[i][0], ListeNotes[i][1], ListeNotes[i][2], lastx))


def remplacement_all_tab(L, tab):
    coord = []
    for i in range(0, len(L)):
        coord = coord_tab(L[i])
        tab = position_tab(coord, tab)


def transposer_piano(L):
    test1 = True
    test2 = True
    test3 = True
    for x in L:
        if x < 130 or x > 1976:
            test1 = False
        if x < 261 or x > 3952:
            test2 = False
        if x < 523 or x > 7903:
            test3 = False
    if test1:
        trans = -1
    elif test2:
        trans = 1
    elif test3:
        trans = 2
    else:
        return (None)
    L_new = []
    for i in range(len(L)):
        L_new.append(L[i] * (1 / 2 ** trans))
    return (L_new)


def transposer_tab(L):
    test1 = True
    test2 = True
    test3 = True
    for x in L:
        if x < 41 or x > 330:
            test1 = False
        if x < 164 or x > 1320:
            test2 = False
        if x < 330 or x > 2640:
            test3 = False
    if test1:
        trans = -1
    elif test2:
        trans = 1
    elif test3:
        trans = 2
    else:
        return (None)
    L_new = []
    for i in range(len(L)):
        L_new.append(L[i] * (1 / 2 ** trans))
    return (L_new)


def octave(f):
    octave = "";
    if f < 15 or f > 16274:
        octave = "erreur";
    elif f < 31.75:
        octave = -1;
    elif f < 63.5:
        octave = 0;
    elif f < 127:
        octave = 1;
    elif f < 254.5:
        octave = 2;
    elif f < 508.5:
        octave = 3;
    elif f < 1017.25:
        octave = 4;
    elif f < 2034:
        octave = 5;
    elif f < 4068.5:
        octave = 6;
    elif f < 8137:
        octave = 7;
    elif f <= 16274:
        octave = 8;
    return octave;


def convert_note(f):
    octa = octave(f);
    if octa == "erreur":
        return ("erreur");
    elif octa == -1:
        L = [16.3, 17.3, 18.3, 19.4, 20.5, 21.8, 23.1, 24.5, 26.0, 27.5, 29.1, 30.8];
    elif octave == 0:
        L = [32.7, 34.6, 36.7, 38.9, 41.2, 43.6, 46.2, 49.0, 51.9, 55.0, 58.0, 62.0];
    elif octa == 1:
        L = [65, 69, 74, 78, 83, 87, 92.5, 98, 104, 110, 117, 123];
    elif octa == 2:
        L = [131, 139, 147, 156, 165, 175, 185, 196, 208, 220, 233, 247];
    elif octa == 3:
        L = [262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494];
    elif octa == 4:
        L = [523, 554, 587, 622, 659, 698.5, 740, 784, 831, 880, 932, 988];
    elif octa == 5:
        L = [1046.5, 1109, 1175, 1244.5, 1318.5, 1397, 1480, 1568, 1661, 1760, 1865, 1975];
    elif octa == 6:
        L = [2093, 2217, 2349, 2489, 2637, 2794, 2960, 3136, 3322, 3520, 3729, 3951];
    elif octa == 7:
        L = [4186, 4435, 4698, 4978, 5274, 5588, 5920, 6272, 6645, 7040, 7458, 7902];
    elif octa == 8:
        L = [8372, 8870, 9396, 9956, 10548, 11176, 11840, 12544, 13290, 14080, 14918, 15804];

    ind = 0;
    minimum = abs(L[0] - f);
    for i in range(1, len(L)):
        if minimum > abs(L[i] - f):
            minimum = abs(L[i] - f);
            ind = i;

    if ind == 0:
        return (["C", str(octa)]);
    if ind == 1:
        return (["C#", str(octa)]);
    if ind == 2:
        return (["D", str(octa)]);
    if ind == 3:
        return (["D#", str(octa)]);
    if ind == 4:
        return (["E", str(octa)]);
    if ind == 5:
        return (["F", str(octa)]);
    if ind == 6:
        return (["F#", str(octa)]);
    if ind == 7:
        return (["G", str(octa)]);
    if ind == 8:
        return (["G#", str(octa)]);
    if ind == 9:
        return (["A", str(octa)]);
    if ind == 10:
        return (["A#", str(octa)]);
    if ind == 11:
        return (["B", str(octa)]);


def octave_max_search(freq):
    L = []
    for i in range(len(freq)):
        L.append(freq[i])
    L_test = []
    for i in range(len(L)):
        if L[i] not in L_test:
            L_test.append(L[i])
    max_freq = max(L_test)
    return (convert_note(max_freq)[1])


def octave_min_search(freq):
    L = []
    for i in range(len(freq)):
        L.append(freq[i])
    L_test = []
    for i in range(len(L)):
        if L[i] not in L_test:
            L_test.append(L[i])
    min_freq = min(L_test)
    return (convert_note(min_freq)[1])


def adapt_piano(freq):
    if not (test_freq_piano(freq)):  ##############
        freq = transposer_piano(freq)
        if freq == None:
            return (None)
    ListeNotes = []
    octave_min = octave_min_search(freq)
    alteration = ""
    for i in range(len(freq)):
        L = convert_note(freq[i])
        if freq[i] < 523:
            cle = "fa"
        else:
            cle = "sol"
        if len(L[0]) == 2:
            note = L[0][0]
            if L[0][1] == "#":
                alteration = "Diese"
        else:
            note = L[0]
            alteration = "None"
        if L[1] == octave_min:
            octave = "inf"
        else:
            octave = "sup"
        genre = "Noire"  # a modifier
        same = 1  # a modifier
        ListeNotes.append([note, octave, cle, genre, alteration, same])
    return (ListeNotes)


def adapt_tab(freq):
    if not (test_freq_tab(freq)):
        freq = transposer_tab(freq)
        if freq == None:
            return (None)
    ListeNotes = []
    alteration = ""
    for i in range(len(freq)):
        L = convert_note(freq[i])
        ListeNotes.append(L[0] + L[1])
    return (ListeNotes)


def test_freq_piano(L):
    for x in L:
        if x < 130 or x > 1976:
            return (False)
    return (True)


def test_freq_tab(L):
    for x in L:
        if x < 82 or x > 660:
            return (False)
    return (True)


def analyse_freq(path):
    rate, data = read(path)  # Openning The file
    print(data)
    #data = data[:, 1]  # Converting the sond to a mono signal

    spectrum, freqs, t, im = specgram(data, NFFT=1024, Fs=rate, noverlap=0)
    SpactrogramData = pd.DataFrame(spectrum, freqs, t)  # Converting the spectrogram data into a pandas Dataframe

    # Show the fondamental Frequency
    HighestFrequency = SpactrogramData.idxmax().to_frame()
    HighestFrequency.columns = ['FoundamentalFrequency']

    ExtractedData = SpactrogramData.mean().to_frame()
    ExtractedData.columns = ['Mean_Intensity']

    periods = 10
    ExtractedData['RolledMean'] = ExtractedData['Mean_Intensity'].rolling(periods, min_periods=1).mean()
    ExtractedData['RolledSTD'] = ExtractedData['Mean_Intensity'].rolling(periods, min_periods=1).std()
    ExtractedData['UP'] = ExtractedData['RolledMean'] + ExtractedData['RolledSTD']
    ExtractedData['DOWN'] = ExtractedData['RolledMean'] - ExtractedData['RolledSTD']

    Time = ExtractedData.index.values
    result = []
    resultIndex = []

    for i in range(0, len(ExtractedData)):
        if (ExtractedData.iloc[i]['Mean_Intensity'] > ExtractedData.iloc[i]['UP']):
            result.append(ExtractedData.iloc[i]['Mean_Intensity'])
            resultIndex.append(Time[i])

    Result = pd.DataFrame(result, resultIndex, ['Mean_Intensity'])

    Time = ExtractedData.index.values
    result = []
    resultIndex = []
    last_spotted = 0

    for i in range(0, len(ExtractedData)):
        if (ExtractedData.iloc[i]['Mean_Intensity'] > ExtractedData.iloc[i]['UP']):
            if (len(resultIndex) > 0 and Time[i - 1] == resultIndex[-1]):
                result[-1] = ExtractedData.iloc[i]['Mean_Intensity']
                resultIndex[-1] = Time[i]
                last_spotted = ExtractedData.iloc[i]['Mean_Intensity']
            elif (last_spotted < ExtractedData.iloc[i]['Mean_Intensity']):
                result.append(ExtractedData.iloc[i]['Mean_Intensity'])
                resultIndex.append(Time[i])
                last_spotted = ExtractedData.iloc[i]['Mean_Intensity']
            else:
                last_spotted = ExtractedData.iloc[i]['Mean_Intensity']

    Result = pd.DataFrame(result, resultIndex, ['Mean_Intensity'])

    Result = Result.join(HighestFrequency, how='left')

    i = 1
    while (i < len(Result)):
        if (Result.iloc[i]['FoundamentalFrequency'] == Result.iloc[i - 1]['FoundamentalFrequency']):
            Result.drop(Result.index[i], inplace=True)
        else:
            i += 1

    ratio = len(data) / len(HighestFrequency)
    result_list = []

    for index, row in Result.iterrows():
        note_frequency = row['FoundamentalFrequency']
        position_deb = np.where(HighestFrequency.index == index)[0][0] * ratio
        position_fin = position_deb + 30000

        w = np.fft.fft(data[int(position_deb):int(position_fin)])

        freqs = np.fft.fftfreq(len(w))
        idx = np.argmax(np.abs(w))
        freq = freqs[idx]
        freq_in_hertz = abs(freq * rate)

        result_list.append(freq_in_hertz)

    return result_list


def affichage_piano(part):
    fig = plt.imshow(part)
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.savefig('result.png', dpi=300, bbox_inches='tight')


def affichage_tab(tab):
    fig = plt.imshow(tab)
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.show()

# files
#sound = pydub.AudioSegment.from_mp3("essai2.mp4a")
#sound.export("essai.wav", format="wav")
freq = analyse_freq("original.wav")
# freq=[258,350,190,650,502,404,440,256,258,350,190,650,502,404,440,256,1000]

# freq=aleatoire_both(80)

L_piano = adapt_piano(freq)
L_tab = adapt_tab(freq)

if L_piano != None:
    remplacement_all_piano(L_piano)
    affichage_piano(part)
else:
    print("Impossible d'afficher la partition")
"""
if L_tab!=None:
	remplacement_all_tab(L_tab,tab)
	affichage_tab(tab)
else:
	print("Impossible d'afficher la tablature")
    """
