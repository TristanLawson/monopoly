# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 10:19:23 2020

@author: trist
"""
'''
NEW
_ bankrupcy booleans
_ chance deck
_ drawChance()
_ start display cleaned up
_ allToPlayer() - just passGO

IN PROCESS

TODO
_ allToProp (for interaction)
_ !bankrupcy!
_ create modules to import (ie clean up this mess)
_ booleans for all invalids
_ throw exceptions
_ printing at all transactions
'''
import random as r

#GLOBAL VARS
pi = []
prop = [0]*23
chance = [0]*32
special = [0]*3
chanceIndex = 0

#CLASSES
class Player(object):
    
    def __init__(self,playerNum,playerName):
        self.num = playerNum
        self.name = playerName
        self.properties = [0]*23
        self.savings = 1500
    
    def isPlayer(self):
        return True
    
    def pay(self,n):
        if n<0:
            print('invalid number')
            return False
        elif self.savings-n < 0:
            print('cannot make payment')
            return False
        else:
            self.savings -= n
            return True
            
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

class Chance(object):
    
    def __init__(self,num,phrase):
        self.num = num
        self.phrase = phrase
    
    def printArt(self):
        print(
' ______________________\n'+
'|         ____         |\n'+
'|        /    \        |\n'+
'|           __/        |\n'+
'|          |           |\n'+
'|          o           |\n'+
'|----------------------|')
        lines = formatString(self.phrase)
        for l in range(len(lines)):
            print(lines[l])
        print(
'|______________________|')

def stringToLines(string):
    word = string.split()
    lines = []
    w = 0
    l = 0
    lines.append('')
    while w < len(word):
        if len(lines[l])+len(word[w])+1 <= 22:
            lines[l] = lines[l] + ' ' + word[w]
            w += 1
        else:
            lines.append('')
            l += 1
    return lines

def formatLine(line):
    while len(line) < 22:
        if len(line) == 21:
            line = line + ' '
        else:
            line = ' ' + line + ' '
    line = '|' + line + '|'
    return line

def formatString(string):
    lines = stringToLines(string)
    for l in range(len(lines)):
        lines[l] = formatLine(lines[l])
    return lines
   
#METHODS
def nameToPlayer(name):
    for i in range(1,len(pi)):
        if name == str(pi[i].name):
            return pi[i]
    return False

def numToPlayer(num):
    if num in range(1,len(pi)):
        return pi[num]
    return False

def allToPlayer(anyForm):
    if type(anyForm) == int:
        return numToPlayer(anyForm)
    elif type(anyForm) == str:
        return nameToPlayer(anyForm)
    elif isinstance(anyForm,Player):
        return anyForm
    return False

def initChance():
    global chanceIndex
    initChanceCards()
    shuffleChanceCards()
    chanceIndex = 0

def initChanceCards():
    chance[0] = Chance(0,'Advance to GO.')
    chance[1] = Chance(1,'Advance to Illinois Avenue. If you pass GO, collect $200.')
    chance[2] = Chance(2,'Advance to St.Charles Place. If you pass GO, collect $200.')
    chance[3] = Chance(3,'Bank pays you a dividend of $50.')
    chance[4] = Chance(4,'Get out of jail free. This card may be kept until needed, or sold/traded.')
    chance[5] = Chance(5,'Go back three spaces.')
    chance[6] = Chance(6,'Go to jail. Do not pass GO, do not collect $200.')
    chance[7] = Chance(7,'Make general repairs on your properties: for each house pay $25.')
    chance[8] = Chance(8,'Speeding fine $15.')
    chance[9] = Chance(9,'Take a stroll on the Boardwalk. Advance to Boardwalk.')
    chance[10]= Chance(10,'You have been elected chairman of the board. Pay each player $50.')
    chance[11]= Chance(11,'Your building loan matures. Receive $150.')
    chance[12]= Chance(12,'You won a crossword competition! Collect $100.')
    chance[13]= Chance(13,'Advance to Marvin Gardens. If you pass GO, collect $200.')
    chance[14]= Chance(14,'Wrong train! Roll one die and move backwards.')
    chance[15]= Chance(15,'Advance to GO.')
    chance[16]= Chance(16,'Bank error in your favor! Collect $200.')
    chance[17]= Chance(17,'Attempt tax fraud. If you roll 1 or 2, collect $50. Otherwise, go to jail.')
    chance[18]= Chance(18,'Renovation. Pay $50.')
    chance[19]= Chance(19,'You bought another house. Pay $100 in extra maintenance.')
    chance[20]= Chance(20,'Go to jail. Do not pass GO, do not collect $200.')
    chance[21]= Chance(21,'Get out of jail free. This card may be kept until needed, or sold/traded.')
    chance[22]= Chance(22,'Grand Opera Night. Collect $50 from every player for opening night seats.')
    chance[23]= Chance(23,'Your cat scratched all your furniture! Pay $75.')
    chance[24]= Chance(24,'Xmas gift! Receive $100.')
    chance[25]= Chance(25,'Income tax refund. Collect $20.')
    chance[26]= Chance(26,'Your cat died. Collect life insurance of 20 kibbles and $5.')
    chance[27]= Chance(27,'Featured on Home Renovation. Upgrade one of your properties for free.')
    chance[28]= Chance(28,'You won a participation award in a beauty contest. Collect $10.')
    chance[29]= Chance(29,'You inherited $100.')
    chance[30]= Chance(30,'Buy a dog on the internet. Pay $40.')
    chance[31]= Chance(31,'FIRE! Your nearest building burns down. Remove all houses. Receive $25 in insurance for each house.')
    
    special[0]= Chance(32,'-----<YOU DIED>----- Return your properties to the bank and write a will. Your savings will be divided amongst the remaining players accordingly.')
    special[1]= Chance(33,'---<TORNADO HITS>--- Remove one house from every property on the street. All players on the street lose a turn.')
    special[2]= Chance(34,'---<HIRED HITMAN>--- Pay $200. Pick a player: if you roll 6, that player dies. All valuables go to the bank. If you roll a 1,2 or 3, go to jail.')

def shuffleChanceCards():
    #shuffle decks
    shuffle(chance,100)
    shuffle(special,5)
    #place specials in last 3 spots
    chance.append(special[0])
    chance.append(special[1])
    chance.append(special[2])
    #shuffle specials into deck, spread out
    spot = r.randint(10,13)
    swap(chance,spot,32)
    spot = r.randint(16,19)
    swap(chance,spot,33)
    spot = r.randint(22,25)
    swap(chance,spot,34)
    
def shuffle(cards,n):
    MAX = len(cards)-1
    for i in range(n):
        a = r.randint(0,MAX)
        b = r.randint(0,MAX)
        cards = swap(cards,a,b)
    return cards

def swap(cards,a,b):
    temp = cards[a]
    cards[a] = cards[b]
    cards[b] = temp
    return cards

def drawChance():
    global chance,chanceIndex
    chance[chanceIndex].printArt()
    chanceIndex += 1
    if chanceIndex >= 35:
        chance = [0]*32
        initChance()
    
    

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

def startGame():
    initProperties()
    initChance()
    addPlayer('the Bank')
    print(
'                               __\n'+
' //\/\\\   // \\\  |\||  // \\\  ||_|  // \\\  ||    \\\//  \n'+
'//    \\\  \\\ //  ||\|  \\\ //  ||    \\\ //  ||__   ||   ')
    print('\n> use addPlayer("name") to add each person')

def addPlayer(name):
    k = len(pi)
    pi.append(Player(k,name))
    if k != 0:
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
    if p1.pay(n):
        p2.receive(n)
        return True
    else:
        print('payment failed')
    return False

def receiveFromBank(p1,n):
    p1.receive(n)

def payToBank(p1,n):
    if p1.pay(n):
        return True
    return False


def buyProperty(p1,prop):
    if prop.owner == 0:
        if payToBank(p1,prop.cost):
            prop.owner = p1.num
            p1.addProperty(prop.num)
            print(p1.name + ' bought ' + prop.name)
        return True
    else:
        print('someone already owns that!')
    return False

def payRent(p1,prop):
    if prop.owner == 0:
        print('no one owns this property')
    else:
        if payPlayer(p1,prop.getRent(),pi[prop.owner]):
            print(p1.name + ' paid $' + str(prop.getRent()) + ' to ' + pi[prop.owner].name)
            return True
    return False

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
        if payToBank(pi[-prop.owner],prop.cost/2):
            prop.owner = -prop.owner
            return True
    return False

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
        cost = calcHouseCost(prop,n)
        if payToBank(pi[prop.owner],cost):
            increaseValueBy(prop,n)
            print(pi[prop.owner].name +' bought '+ str(n) +' house(s) on '+ prop.name +' for $'+ str(cost))
            return True
    else:
        print("you don't own this property")
    return False

def buyHouse(prop):
    if buyHouses(prop,1):
        return True
    return False

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
	
def passGO(anyForm):
    p1 = allToPlayer(anyForm)
    if isinstance(p1,Player):
        receiveFromBank(p1,200)
        print(p1.name +' passed GO')
        return True
    print('invalid player')
    return False
    
    
    
	
#MAIN
def test():
    startGame()
    addPlayer('Gilly')
    addPlayer('Zander')
    addPlayer('Tristan')
    displayPlayers()
    
    passGO(1)
    passGO(4)
    passGO('Gilly')
    passGO('tristan')
    passGO(pi[0])
    passGO(pi[2])
test()
    