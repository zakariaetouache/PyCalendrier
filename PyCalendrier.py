import pandas as pd
import numpy as np

mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

lst = ["lu", "ma", "me", "je", "ve", "sa", "di"]


def jour(j, m, a):
    _M = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
    return ((j+(a-1900)+((a-1900)//4)+_M[m-1]) % 7)


def afficheMoi(m, a):

    dictMoi = {"lu": [], "ma": [], "me": [],
               "je": [], "ve": [], "sa": [], "di": []}

    jj = 1

    j = int(jour(jj, m, a))

    if (((a % 4 == 0 and a % 100 != 0) | (a % 400 == 0)) & (m == 2)):
        mois[1] = 29
        j -= 1

    zz = (mois[m-1]+j-1) % 7
    z = (j-1) % 7

    while (z):
        z -= 1
        dictMoi[lst[z]].append(np.nan)

    for i in range(j, mois[m-1]+j):
        dictMoi[lst[(i-1) % 7]].append(i-j+1)

    while ((zz < 7) & (zz != 0)):
        dictMoi[lst[zz]].append(np.nan)
        zz += 1
    df = pd.DataFrame(dictMoi)
    print(df)
    print("\n")


d = input("saisie une date ")

dat = d.split("/")

if (len(dat) > 1):
    m = int(dat[0])
    a = int(dat[1])
    afficheMoi(m, a)
else:
    a = int(dat[0])
    for m in range(1, 13):
        afficheMoi(m, a)
