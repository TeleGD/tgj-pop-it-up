from numpy import *
from random import *

with open("verbes.txt") as fv:
    verbes = fv.read().splitlines()


with open("mots.txt") as fm:
    mots = fm.read().splitlines()

N = 20
for k in range(N):
    verbe = choice(verbes)
    mot1 = choice(mots)
    mot2 = choice(mots)
    print("%s %s %s" %(verbe, mot1, mot2))
