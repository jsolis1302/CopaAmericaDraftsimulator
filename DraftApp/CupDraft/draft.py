import random
from CupDraft.models import Country


class Draft:

    def __init__(self,pot1,pot2,pot3,pot4) -> None:
        self.pot1 = pot1
        self.pot2 = pot2
        self.pot3 = pot3
        self.pot4 = pot4

        #init groups and numbers
        self.GA = [None,None,None,None]
        self.GB = [None,None,None,None]
        self.GC = [None,None,None,None]
        self.GD = [None,None,None,None]

        self.GAn = [1,2,3]
        self.GBn = [1,2,3]
        self.GCn = [1,2,3]
        self.GDn = [1,2,3]

    def getRandHeads(self,b):  
        gpNbr = []
        while b:
            chNmbr = random.choice(b)
            gpNbr.append(chNmbr)
            b.remove(chNmbr)
        return gpNbr
    
    def getHeads(self,b1):
        self.GA[0]=b1[0]
        self.GB[0]=b1[1]
        self.GC[0]=b1[2]
        self.GD[0]=b1[3]

    def getSecond(self,b2):
        runUp = self.getRandHeads(b2)
        randPos = random.choice(self.GAn)
        self.GA[randPos]=runUp[0]
        self.GAn.remove(randPos)
        randPos = random.choice(self.GBn)
        self.GB[randPos]=runUp[1]
        self.GBn.remove(randPos)
        randPos = random.choice(self.GCn)
        self.GC[randPos]=runUp[2]
        self.GCn.remove(randPos)
        randPos = random.choice(self.GDn)
        self.GD[randPos]=runUp[3]
        self.GDn.remove(randPos)
        
    def getThird(self,b3):

        pot3 = self.getRandHeads(b3)
        randPos = random.choice(self.GAn)
        self.GA[randPos] = pot3[0]
        self.GAn.remove(randPos)
        randPos = random.choice(self.GBn)
        self.GB[randPos] = pot3[1]
        self.GBn.remove(randPos)  
        randPos = random.choice(self.GCn)
        self.GC[randPos] = pot3[2]
        self.GCn.remove(randPos)
        randPos = random.choice(self.GDn)
        self.GD[randPos] = pot3[3]
        self.GDn.remove(randPos)
        
    def getLast(self,b4):
        pot4 = self.getRandHeads(b4)
        self.GA[self.GAn[0]] = pot4[0]
        self.GB[self.GBn[0]] = pot4[1]
        self.GC[self.GCn[0]] = pot4[2]
        self.GD[self.GDn[0]] = pot4[3]
    
    def sorteoCA(self,b1,b2,b3,b4):
        self.getHeads(b1)
        self.getSecond(b2)
        self.getThird(b3)
        self.getLast(b4)

        #return [self.GA,self.GB,self.GC,self.GD]
    
    def resetAll(self):
            
        #init groups and numbers
        self.GA = [None,None,None,None]
        self.GB = [None,None,None,None]
        self.GC = [None,None,None,None]
        self.GD = [None,None,None,None]

        self.GAn = [1,2,3]
        self.GBn = [1,2,3]
        self.GCn = [1,2,3]
        self.GDn = [1,2,3]

    def getConfCount(self,Group):
        concaCount = 0
        conmeCount = 0
        for item in Group:
            if item is not None:
                if item.CountryConf == 'CONCACAF':
                    concaCount+=1

        for item in Group:
            if item is not None:
                if item.CountryConf == 'CONMEBOL':
                    conmeCount+=1
        return concaCount,conmeCount
    
    def isValid(self):
        groups = [self.GA,self.GB, self.GC, self.GD]
        valid=[]
        #validsort = False
        conca =0
        conme = 0
        for item in groups:
            conca =self.getConfCount(item)[0]
            conme = self.getConfCount(item)[1]
            if conca<=2 and conme <=3:
                valid.append(1)
            else:
                valid.append(0)
        return all(valid)
        









    
