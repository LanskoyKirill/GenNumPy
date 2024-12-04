import numpy as np
import random
import main as anp
import pygame as pg
import sys
from pygame.locals import *
import numpy as np
pg.init()
listNet = {}
NewNet = []
pg.init()
listNet = {}
NewNet = []
goodNet = []
timeNN = 0
showNN = False
moveRight = False
moveLeft = False
epoch = 0
pg.init()
mainClock = pg.time.Clock()
WINDOWWIDTH = 551
WINDOWHEIGHT = 720
windowSurface = pg.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pg.display.set_caption('ANN Bird')
def sigmoid(x):
    return 1/(1 + np.exp(-x))

class Network():
    def __init__(self):
        self.H1 = np.random.randn(4, 12)
        self.H2 = np.random.randn(12, 6)
        self.O1 = np.random.randn(6, 2)
        self.BH1 = np.random.randn(12)
        self.BH2 = np.random.randn(6)
        self.BO1 = np.random.randn(2)
        self.epoch = 0

    def predict(self, x):
        nas = x @ self.H1 + self.BH1
        nas = sigmoid(nas)
        nas = nas @ self.H2 + self.BH2
        nas = sigmoid(nas)
        nas = nas @ self.O1 + self.BO1
        nas = sigmoid(nas)
        if nas[0] >= nas[1]:
            return True
        else:
            return False
        def epoch(self, a):
            return 0
            

class Network1():
    def __init__(self, H1, H2, O1, BH1, BH2, BO1, ep):
        self.H1 = H1
        self.H2 = H2
        self.O1 = O1
        self.BH1 = BH1
        self.BH2 = BH2
        self.BO1 = BO1
        self.epoch = ep

    def predict(self, x):
        nas = x @ self.H1 + self.BH1
        nas = sigmoid(nas)
        nas = nas @ self.H2 + self.BH2
        nas = sigmoid(nas)
        nas = nas @ self.O1 + self.BO1
        nas = sigmoid(nas)
        if nas[0] >= nas[1]:
            return True
        else:
            return False

for s in range (1000):
    s = Network()
    timeNN = anp.NPong(s, False, 0, 0)
    listNet.update({
        s : timeNN
    })
    
listNet = dict(sorted(listNet.items(), key=lambda item: item[1]))
NewNet = listNet.keys()
goodNet = list(NewNet)
NewNet = goodNet[:10]
listNet = {}
goodNet = NewNet
print(str(epoch) + " epoch")
anp.NPong(NewNet[0], True, 0, 0)
print(NewNet[0].epoch)
print('next')
anp.NPong(NewNet[1], True, 0, 0)
print(NewNet[1].epoch)
print('next')
anp.NPong(NewNet[2], True, 0, 0)
print(NewNet[2].epoch)
print('next')

anp.NPong(NewNet[3], True, 0, 0)
print(NewNet[3].epoch)
print('next')
anp.NPong(NewNet[4], True, 0, 0)
print(NewNet[4].epoch)
print('next')
anp.NPong(NewNet[5], True, 0, 0)
print(NewNet[5].epoch)
print('next')
anp.NPong(NewNet[6], True, 0, 0)
print(NewNet[6].epoch)
print('next')
anp.NPong(NewNet[7], True, 0, 0)
print(NewNet[7].epoch)
print('next')
anp.NPong(NewNet[8], True, 0, 0)
print(NewNet[8].epoch)
print('next')
anp.NPong(NewNet[9], True, 0, 0)
print(NewNet[9].epoch)
print('that is all')
for g in range(990):
    parent1 = random.choice(NewNet)
    parent2 = random.choice(NewNet)
    ch1H = np.vstack((parent1.H1[:2], parent2.H1[2:])) * random.uniform(-2, 2)
    ch2H = np.vstack((parent1.H2[:6], parent2.H2[6:])) * random.uniform(-2, 2)
    ch1O = np.vstack((parent1.O1[:3], parent2.O1[3:])) * random.uniform(-2, 2)
    chB1 = parent1.BH1 * random.uniform(-2, 2)
    chB2 = parent2.BH2 * random.uniform(-2, 2)
    chB3 = parent2.BO1 * random.uniform(-2, 2)
    g = Network1(ch1H, ch2H, ch1O, chB1, chB2, chB3, 1)
    goodNet.append(g)
NewNet = []
while True:
    epoch += 1
    print(str(epoch) + " epoch")
    if epoch < 10:
        for s in goodNet:
            timeNN = anp.NPong(s, False, 0, 0)
            listNet.update({
                s : timeNN
            })
    if epoch >= 10:
        for s in goodNet:
            timeNN = anp.NPong(s, False, 0, 1)
            listNet.update({
                s : timeNN
            })
    goodNet =[]
    listNet = dict(sorted(listNet.items(), key=lambda item: item[1], reverse = True))
    goodNet = list(listNet.keys())
    NewNet.append(goodNet[0])
    goodNet = list(listNet.values())
    for i in listNet:
        a = goodNet[0]
        if listNet.get(i) == a:
            NewNet.append(i)
    goodNet = list(NewNet)
    listNet = {}
    if epoch > 0:
        try:
            print(NewNet[0].epoch)
            anp.NPong(NewNet[0], True, 0, 1)
            print('next')
            print(NewNet[1].epoch)
            anp.NPong(NewNet[1], True, 0, 1)
            print('next')
            print(NewNet[2].epoch)
            anp.NPong(NewNet[2], True, 0, 1)
            print('next')
            print(NewNet[3].epoch)
            anp.NPong(NewNet[3], True, 0, 1)
            print('next')
            print(NewNet[4].epoch)
            anp.NPong(NewNet[4], True, 0, 1)
            print('next')
            
            print(NewNet[5].epoch)
            anp.NPong(NewNet[5], True, 0, 1)
            print('next')
            print(NewNet[6].epoch)
            anp.NPong(NewNet[6], True, 0, 1)
            print('next')
            print(NewNet[7].epoch)
            anp.NPong(NewNet[7], True, 0, 1)
            print('next')
        except IndexError:
            print('that is all')
    howALot = 1000 - len(NewNet)
    if howALot < 40:
        howALot = 40
    for g in range(howALot):
        parent1 = random.choice(NewNet)
        parent2 = random.choice(NewNet)
        ch1H = np.vstack((parent1.H1[:2], parent2.H1[2:])) * random.uniform(-2, 2)
        ch2H = np.vstack((parent1.H2[:6], parent2.H2[6:])) * random.uniform(-2, 2)
        ch1O = np.vstack((parent1.O1[:3], parent2.O1[3:])) * random.uniform(-2, 2)
        chB1 = parent1.BH1 * random.uniform(-2, 2)
        chB2 = parent2.BH2 * random.uniform(-2, 2)
        chB3 = parent2.BO1 * random.uniform(-2, 2)
        g = Network1(ch1H, ch2H, ch1O, chB1, chB2, chB3, epoch)
        goodNet.append(g)
    print(len(NewNet))
    print(len(goodNet))
    NewNet = []


