# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 10:19:23 2020

@author: trist
"""
'''
NEW

TODO
_ !bankrupcy!
_ add monopoly chance cards
_ throw exceptions
_ thorough security - either use boolean returns or throw exceptions
_ number to player, number to property (for interaction)
_ printing at all transactions
'''


#GLOBAL VARS
pi = []
prop = [0]*23

#CLASSES
class Player(object):
    
    def __init__(self,playerNum,playerName):
        self.num = playerNum
        self.name = playerName
        self.properties = [0]*23
        self.savings = 1500
    
    def pay(self,n):
        if n<0:
            print('invalid number')
        elif self.savings-n < 0:
            print('cannot make payment')
        else:
            self.savings -= n
            
    def receive(self,n):
        if n<0:
            print('invalid number')
        else:
            self.savings += n
    
    def addProperty(self,p):
        if p in range(1,23):
            self.properties[p] = 1
        else:
            print('invalid property number')
            
    def getPropertyList(self):
        propList = []
        for p in range(1,22):
            if self.properties[p] == 1:
                propList.append(prop[p].name)
        return propList
    
    def getNetWorth(self):
        worth = self.savings
        for p in range(1,22):
            if self.properties[p] == 1:
                worth += prop[p].cost
        return worth

class Property(object):
    
    houseCost = [50,100,150,200]
    
    def __init__(self,num,pName,ownedBy,value,cost,rent):
        self.num = num
        self.name = pName
        self.owner = ownedBy
        self.val = value
        self.cost = cost
        self.rent = rent
    
    def changeVal(self,n):
        if 0 <= self.val+n and self.val+n <= 4:
            self.val += n
        else:
            print('invalid property value')
            
    def setVal(self,n):
        if 0 <= n and n <= 4: 
            self.val = n
        else:
            print('invalid property value')
    
    def getRent(self):
        return self.rent[self.val]
	
    def getInfo(self):
        info = self.name +' is owned by '+ pi[self.owner].name
        if self.owner == 0:
            return info + '\nBuy for $'+ str(self.cost)
        else:
            return info + '\nRent is $'+ str(self.getRent())

#METHODS
def initProperties():
    prop[1] = Property( 1, 'Mediterranean Avenue',  0, 0,  60, [ 70,130,220,370, 750])
    prop[2] = Property( 2, 'Baltic Avenue',         0, 0,  60, [ 70,130,220,370, 750])
    prop[3] = Property( 3, 'Oriental Avenue',       0, 0, 100, [ 80,140,240,410, 800])
    prop[4] = Property( 4, 'Vermont Avenue',        0, 0, 100, [ 80,140,240,410, 800])
    prop[5] = Property( 5, 'Connecticut Avenue',    0, 0, 120, [100,160,260,440, 860])
    prop[6] = Property( 6, 'St. Charles Place',     0, 0, 140, [110,180,290,460, 900])
    prop[7] = Property( 7, 'States Avenue',         0, 0, 140, [110,180,290,460, 900])
    prop[8] = Property( 8, 'Virginia Avenue',       0, 0, 160, [130,200,310,490, 980])
    prop[9] = Property( 9, 'St. James Place',       0, 0, 180, [140,210,330,520,1000])
    prop[10]= Property(10, 'Tennessee Avenue',      0, 0, 180, [140,210,330,520,1000])
    prop[11]= Property(11, 'New York Avenue',       0, 0, 200, [160,230,350,550,1100])
    prop[12]= Property(12, 'Kentucky Avenue',       0, 0, 220, [170,250,380,580,1160])
    prop[13]= Property(13, 'Indiana Avenue',        0, 0, 220, [170,250,380,580,1160])
    prop[14]= Property(14, 'Illinois Avenue',       0, 0, 240, [190,270,400,610,1200])
    prop[15]= Property(15, 'Atlantic Avenue',       0, 0, 260, [200,280,420,640,1300])
    prop[16]= Property(16, 'Ventnor Avenue',        0, 0, 260, [200,280,420,640,1300])
    prop[17]= Property(17, 'Marvin Gardens',        0, 0, 280, [220,300,440,670,1340])
    prop[18]= Property(18, 'Pacific Avenue',        0, 0, 300, [230,320,460,700,1400])
    prop[19]= Property(19, 'North Carolina Avenue', 0, 0, 300, [230,320,460,700,1400])
    prop[20]= Property(20, 'Pennsylvania Avenue',   0, 0, 320, [250,340,480,730,1440])
    prop[21]= Property(21, 'Park Place',            0, 0, 350, [270,360,510,740,1500])
    prop[22]= Property(22, 'Boardwalk',             0, 0, 400, [300,400,560,810,1600])

def initGame():
    initProperties()
    addPlayer('the Bank')	

def addPlayer(name):
    k = len(pi)
    pi.append(Player(k,name))
    print(name + ' is player ' + str(k))

def displayPlayers():
    print('---------------------------------')
    print('_________________________________')
    print('Name\t'+'Number\t'+'Savings\t'+'Net Worth')
    for i in range(1,len(pi)):
        print(pi[i].name +'\t'+ str(pi[i].num) +'\t$'+ str(pi[i].savings) +'\t$'+ str(pi[i].getNetWorth()))
    print('---------------------------------')

def displayProperties():
    print('---------------------------------')
    for i in range(1,23):
        print(prop[i].getInfo())
    print('---------------------------------')

def displayPropertiesOf(p1):
    plist = p1.getPropertyList()
    print(p1.name +' owns:')
    for i in range(len(plist)):
        print(plist[i])

def payPlayer(p1,n,p2):
    p1.pay(n)
    p2.receive(n)

def receiveFromBank(p1,n):
    p1.receive(n)

def payToBank(p1,n):
    p1.pay(n)


def buyProperty(p1,prop):
    if prop.owner == 0:
        payToBank(p1,prop.cost)
        prop.owner = p1.num
        p1.addProperty(prop.num)
        print(p1.name + ' bought ' + prop.name)
    else:
        print('someone already owns that!')

def payRent(p1,prop):
    if prop.owner == 0:
        print('no one owns this property')
    else:
        payPlayer(p1,prop.getRent(),pi[prop.owner])
        print(p1.name + ' paid $' + str(prop.getRent()) + ' to ' + pi[prop.owner].name)

def mortgage(prop):
	if prop.owner < 0:
		print('property already mortgaged')
	elif prop.owner == 0:
		print('no one owns this property')
	else:
		receiveFromBank(pi[prop.owner],prop.cost/2)
		prop.owner = -prop.owner

def unmortgage(prop):
	if prop.owner > 0:
		print('property is not mortgaged')
	elif prop.owner == 0:
		print('no one owns this property')
	else:
		prop.owner = -prop.owner
		payToBank(pi[prop.owner],prop.cost/2)

def increaseValue(prop):
	if prop.owner in range(1,len(pi)):
		prop.changeVal(1)
	else:
		print("you don't own this property")

def increaseValueBy(prop,n):
	if prop.owner in range(1,len(pi)):
		prop.changeVal(n)
	else:
		print("you don't own this property")

def decreaseValue(prop):
	if prop.owner in range(1,len(pi)):
		prop.changeVal(-1)
	else:
		print("you don't own this property")

def decreaseValueBy(prop,n):
	if prop.owner in range(1,len(pi)):
		prop.changeVal(-n)
	else:
		print("you don't own this property")

def resetValue(prop):
	if prop.owner in range(1,len(pi)):
		prop.setVal(0)
	else:
		print("you don't own this property")

def calcHouseCost(prop,n):
    cost = 0
    if prop.num in range(1,6):
        cost = n*prop.houseCost[0]
    elif prop.num in range(6,12):
        cost = n*prop.houseCost[1]
    elif prop.num in range(12,18):
        cost = n*prop.houseCost[2]
    elif prop.num in range(18,23):
        cost = n*prop.houseCost[3]
    else:
        #throw property number exception
        print('invalid property')
    return cost
		
def buyHouses(prop,n):
    if prop.owner in range(1,len(pi)):
        increaseValueBy(prop,n)
        cost = calcHouseCost(prop,n)
        payToBank(pi[prop.owner],cost)
        print(pi[prop.owner].name +' bought '+ str(n) +' house(s) on '+ prop.name +' for $'+ str(cost))
    else:
        print("you don't own this property")

def buyHouse(prop):
	buyHouses(prop,1)

def sellHouses(prop,n):
    if prop.owner in range(1,len(pi)):
        decreaseValueBy(prop,n)
        value = int(calcHouseCost(prop,n)/2)
        receiveFromBank(pi[prop.owner],value)
        print(pi[prop.owner].name +' sold '+ str(n) +' house(s) on '+ prop.name +' for $'+ str(value))
    else:
        print("you don't own this property")

def sellHouse(prop):
	sellHouses(prop,1)
	
def passGO(p1):
    receiveFromBank(p1,200)
	
#MAIN
def test():
    initGame()
    
    addPlayer('Gilly')
    addPlayer('Zander')
    addPlayer('Tristan')
    
    buyProperty(pi[1],prop[1])
    buyProperty(pi[1],prop[5])
    buyProperty(pi[1],prop[6])
    
    print(prop[1].getInfo())
    buyHouse(prop[1])
    print(prop[1].getInfo())
    resetValue(prop[1])
    print(prop[1].getInfo())
	

test()