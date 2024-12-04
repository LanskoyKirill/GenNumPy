import numpy as np
import random
import ANNPong as anp
import pygame as pg
import sys
from pygame.locals import *
pg.init()
listNet = {}
NewNet = []
goodNet = []
timeNN = 0
moveRight = False
moveLeft = False
epoch = 0
mainClock = pg.time.Clock()
WINDOWWIDTH = 800
WINDOWHEIGHT = 500
windowSurface = pg.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pg.display.set_caption('ANN Pong')
def sigmoid(x):
    return 1/(1 + np.exp(-x))

class Network():
    def __init__(self):
        self.H1 = np.random.randn(6, 12)
        self.H2 = np.random.randn(12, 6)
        self.O1 = np.random.randn(6, 3)
        self.BH1 = np.random.randn(12)
        self.BH2 = np.random.randn(6)
        self.BO1 = np.random.randn(3)
        self.epoch = 0

    def predict(self, x, first, second):
        nas = x @ self.H1 + self.BH1
        nas = sigmoid(nas)
        nas = nas @ self.H2 + self.BH2
        nas = sigmoid(nas)
        nas = nas @ self.O1  + self.BO1
        nas = sigmoid(nas)
        if nas[0] > nas[1] and nas[0] > nas[2]:
            first = True
            second = False
            return first, second
        elif nas[1] > nas[0] and nas[1] > nas[2]:
            first = False
            second = True
            return first, second
        elif nas[2] > nas[0] and nas[2] > nas[1]:
            first = False
            second = False
            return first, second
        else:
            first = False
            second = False
            return first, second
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

    def predict(self, x, first, second):
        nas = x @ self.H1 + self.BH1
        nas = sigmoid(nas)
        nas = nas @ self.H2 + self.BH2
        nas = sigmoid(nas)
        nas = nas @ self.O1 + self.BO1
        nas = sigmoid(nas)
        if nas[0] > nas[1] and nas[0] > nas[2]:
            first = True
            second = False
            return first, second
        elif nas[1] > nas[0] and nas[1] > nas[2]:
            first = False
            second = True
            return first, second
        elif nas[2] > nas[0] and nas[2] > nas[1]:
            first = False
            second = False
            return first, second
        else:
            first = False
            second = False
            return first, second

for s in range (1000):
    s = Network()
    timeNN = anp.NNPong(s)
    listNet.update({
        s : timeNN
    })
    
listNet = dict(sorted(listNet.items(), key=lambda item: item[1]))
NewNet = listNet.keys()
goodNet = list(NewNet)
NewNet = goodNet[:10]
listNet = {}
goodNet = NewNet
#NewNet = list(listNet.keys())
anp.NPong(NewNet[0])
print(str(epoch) + " epoch")
print(NewNet[0].epoch)
print('next')
anp.NPong(NewNet[1])
print(NewNet[1].epoch)
print('next')
anp.NPong(NewNet[2])
print(NewNet[2].epoch)
print('next')
anp.NPong(NewNet[3])
print(NewNet[3].epoch)
print('next')
anp.NPong(NewNet[4])
print(NewNet[4].epoch)
print('next')
anp.NPong(NewNet[5])
print(NewNet[5].epoch)
print('next')
anp.NPong(NewNet[6])
print(NewNet[6].epoch)
print('next')
anp.NPong(NewNet[7])
print(NewNet[7].epoch)
print('next')
anp.NPong(NewNet[8])
print(NewNet[8].epoch)
print('next')
anp.NPong(NewNet[9])
print(NewNet[9].epoch)
print('that is all')
for g in range(990):
    parent1 = random.choice(NewNet)
    parent2 = random.choice(NewNet)
    ch1H = np.vstack((parent1.H1[:3], parent2.H1[3:])) * random.uniform(-2, 2)
    ch2H = np.vstack((parent1.H2[:6], parent2.H2[6:])) * random.uniform(-2, 2)
    ch1O = np.vstack((parent1. O1[:3], parent2. O1[3:])) * random.uniform(-2, 2)
    chB1 = parent1.BH1 * random.uniform(-2, 2)
    chB2 = parent2.BH2 * random.uniform(-2, 2)
    chB3 = parent2.BO1 * random.uniform(-2, 2)
    g = Network1(ch1H, ch2H, ch1O, chB1, chB2, chB3, 1)
    goodNet.append(g)
NewNet = []
while True:
    epoch += 1
    print(str(epoch) + " epoch")
    for s in goodNet:
        timeNN = anp.NNPong(s)
        listNet.update({
            s : timeNN
        })
    goodNet =[]
    listNet = dict(sorted(listNet.items(), key=lambda item: item[1], reverse=True))
    goodNet = list(listNet.keys())
    NewNet.append(goodNet[0])
    goodNet = list(listNet.values())
    for i in listNet:
        a = goodNet[0]
        if listNet.get(i) == a:
            NewNet.append(i)
    goodNet = list(NewNet)
    listNet = {}
    try:
        print(NewNet[0].epoch)
        anp.NPong(NewNet[0])
        print('next')
        print(NewNet[1].epoch)
        anp.NPong(NewNet[1])
        print('next')
        print(NewNet[2].epoch)
        anp.NPong(NewNet[2])
        print('next')
        print(NewNet[3].epoch)
        anp.NPong(NewNet[3])
        print('next')
        print(NewNet[4].epoch)
        anp.NPong(NewNet[4])
        print('next')
            
        print(NewNet[5].epoch)
        anp.NPong(NewNet[5])
        print('next')
        print(NewNet[6].epoch)
        anp.NPong(NewNet[6])
        print('next')
        print(NewNet[7].epoch)
        anp.NPong(NewNet[7])
        print('next')
    except IndexError:
        print('that is all')
        
    for g in range(1000 - len(NewNet)):
        parent1 = random.choice(NewNet)
        parent2 = random.choice(NewNet)
        ch1H = np.vstack((parent1.H1[:3], parent2.H1[3:])) * random.uniform(-2, 2)
        ch2H = np.vstack((parent1.H2[:6], parent2.H2[6:])) * random.uniform(-2, 2)
        ch1O = np.vstack((parent1. O1[:3], parent2. O1[3:])) * random.uniform(-2, 2)
        chB1 = parent1.BH1 * random.uniform(-2, 2)
        chB2 = parent2.BH2 * random.uniform(-2, 2)
        chB3 = parent2.BO1 * random.uniform(-2, 2)
        g = Network1(ch1H, ch2H, ch1O, chB1, chB2, chB3, epoch)
        goodNet.append(g)
    print(len(NewNet))
    print(len(goodNet))
    NewNet = []



