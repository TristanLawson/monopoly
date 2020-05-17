# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 10:19:23 2020
monopoly_6_0.py
patch 6.0
@author: trist
"""
'''
NEW
    TESTED
- created art and chance modules
- fix chance initiation
- add method removePlayer()

    UNTESTED

IN PROCESS

NEXT STEPS
    PATCH 6
- add bool isPlayer(),isProperty(),sufficientFunds() for efficiency
- add endgame() that declares winner, displays final standings, and resets
- add railroads


    PLAYABILITY
> beautification
- property card display (num houses, ownership, rent/cost/mortgaged)
- player profile (property list, savings, net worth)
> what happens to bankrupt players?
- bankrupcy calculation... if networth is too low for a transaction
- display BANKRUPT in player's savings and net worth
> write/repair functions
- smart chance drawer
> long-term
- landOn(pin,space) displays actions (draws chance,displays property cost, pays rent, indicates not enough money)
    and automatically collects GO money

    CODE
- add bool isPlayer() to further modulate code (remove error handling from downstream methods)
- add bool sufficientFunds() to check savings without making a payment yet
- add bool isProperty() to modulate code
- cast int() at bottlenecks (instead of everywhere else)
- init normal chance cards into normal[],
    then shuffle into chance[]
    to prevent re-initializing all cards

    ORGANIZATION
'''

#IMPORTS
import chance as c
import art as a

#GLOBAL VARS
pi = []
prop = [0]*23

#CLASSES
class InsufficientFunds(Exception): #raised when Player.savings is not large enough for a payment
    def __init__(self,msg):
        super().__init__(msg)

class InputError(Exception):        #raised when user input does not match a valid case
    def __init__(self,msg):
        super().__init__(msg)

class PropertyIssue(Exception):     #raised for illegal attempts to mortgage, change value, or change ownership
    def __init__(self,msg):
        super().__init__(msg)

class Player(object):               #each player has their own Player object
    
    def __init__(self,playerNum,playerName):
        self.num = playerNum        #dnc        Player.num is the index for pi[]
        self.name = playerName      #dnc        Player.name is set by the user
        self.savings = 1500         #changes    Player.savings starts at 1500
        self.properties = [0]*23    #changes    Player.properties is 0 for unowned properties, 1 for owned
    
    #CHANGE ATTRIBUTES
    def pay(self,n):                            #remove n from savings
        if n<0:                                     #only positive integers
            raise InputError('payment of n < 0')
        elif self.savings-n < 0:                    #check if sufficient savings
            raise InsufficientFunds(self.getName()+' cannot make payment')
        else:                                       #adjust savings
            self.savings -= n
    
    def receive(self,n):                        #add n to savings
        if n<0:                                     #only positive integers
            raise InputError('receipt of n < 0')
        else:                                       #adjust savings
            self.savings += n
    
    def addProperty(self,p):                    #add property to list (when purchased or traded for)
        if p in range(1,23):                        #check if valid property
            self.properties[p] = 1                  #change status in Player.properties
        else:
            raise InputError('invalid property number')
    
    def removeProperty(self,p):                 #remove from list (when sold or traded away)
        if p in range(1,23):                        #check if valid property
            self.properties[p] = 0                  #change status in Player.properties
        else:
            raise InputError('invalid property number')
    
    def setNum(self,n):
        if n not in range(len(pi)+1):
            raise InputError('invalid player number')
        if isinstance(pi[n],Player):
            raise InputError('this number is already taken')
        self.num = n
    
    #INFO
    def getName(self):                          #return Player.name as str
        return self.name
    
    def getNum(self):                           #return Player.num as int
        return int(self.num)
    
    def getSavings(self):                       #return Player.savings as int
        return int(self.savings)
    
    def getProperties(self):
        return self.properties
    
    def getNetWorth(self):                      #calculate and return net worth as int
        worth = self.savings
        for p in range(1,22):
            if self.properties[p] == 1:
                if prop[p].isMortgaged():
                    worth += prop[p].getCost()/2
                else:
                    worth += prop[p].getCost()
                    worth += prop[p].getValue()*prop[p].getHouseCost()
        return int(worth)

class Property(object):                     #all 22 properties are Property objects
    
    def __init__(self,num,name,cost,houseCost,rent):
        self.num = num              #dnc        Property.num is the index for prop[]
        self.name = name            #dnc        Property.name is defined in __init__
        self.owner = 0              #change     Property.owner is the Player.num, or 0 if owned by the bank
        self.cost = cost            #dnc        Property.cost is the purchase price (int)
        self.houseCost = houseCost  #dnc        Property.houseCost is the purchase price of a house (increase of value)
        self.val = 0                #change     Property.val is 1,2,3,4,5 and determines the rent
        self.rent = rent            #dnc        Property.rent is a list of rent at each val
        self.mortgaged = False      #change     Property.mortgaged is True if mortgaged, False if not
    
    #CHANGE ATTRIBUTES
    def setOwner(self,pn):                  #change owner to an int
        if pn in range(len(pi)):                #if valid pn, change ownership to pn
            self.owner = pn
            if pn == 0:                         #if bank takes ownership, unmortgage
                    self.mortgaged = False
        else:
            raise InputError('not a valid player input')
            
    def setVal(self,n):                     #set Property.val to an int
        if n in range(5):                       #if valid value, set
            self.val = n
        else:
            raise InputError('invalid property value')
            
    def changeVal(self,n):                  #add n (pos or neg int) to Property.val
        if self.val+n in range(5):              #if val + n is valid, change
            self.val += n
        else:
            raise InputError('invalid property value')
    
    def mortgage(self):                     #change mortgaged to True
        if self.isMortgaged():                      #raise exception if already mortgaged
            raise PropertyIssue('property is already mortgaged')
        else:
            self.mortgaged = True
            
    def unmortgage(self):                   #change mortgaged to False
        if self.mortgaged:
            self.mortgaged = False
        else:                                   #raise exception if .mortgaged is already False
            raise PropertyIssue('property was not mortgaged')
    
    #INFO
    def getNum(self):                       #return Property.num as int
        return int(self.num)
    
    def getName(self):                      #return Property.name as str
        return self.name        
    
    def getOwnerNum(self):                  #return owner's number as int
        if self.owner in range(len(pi)):
            return int(self.owner)                  #0 if Bank, pos int if player
        else:
            raise PropertyIssue('Property #'+str(self.num)+' has invalid owner')
    
    def getOwner(self):                     #return Player that owns property
        if self.owner == 0:                     #raise exception if owned by bank
            raise PropertyIssue('Property is owned by the bank')
        else:                                   #otherwise return Player
            return pi[self.getOwnerNum()]       #by calling getOwnerNum()
    
    def getOwnerName(self):                 #return owner's name as str
        if self.getOwnerNum() == 0:             #call .getOwnerNum()
            return 'the Bank'
        else:
            return self.getOwner().getName()    #call .getOwner().getName()
    
    def getCost(self):                      #return Property.cost as int
        return int(self.cost)
    
    def getHouseCost(self):                 #return houseCost as int
        return int(self.houseCost)
    
    def getValue(self):                     #return property value as int
        return int(self.val)
    
    def getRentCost(self):                  #determine and return rent cost as int
        if self.mortgaged:                      #if mortgaged, rent is 0
            return 0
        else:
            return int(self.rent[self.val])     #return correct index of rent[] according to self.val
	
    def isMortgaged(self):                  #return True if mortgaged, False if not
        return self.mortgaged
    
    def getInfo(self):                      #return str describing property
        info = self.name +' is owned by '+ pi[self.owner].name  #Player owns Property
        if self.owner == 0:                                 #if owned by Bank
            return info + '\nBuy for $'+ str(self.cost)     #write cost
        elif self.mortgaged:                                #if owned by player and mortgaged
            return info + '\nCurrently mortgaged'           #write mortgaged
        else:                                               #else write rent cost
            return info + '\nRent is $'+ str(self.getRentCost())
   
#METHODS

##INPUT PARSING
    #private
def nameToPlayer(name):     #given name, return associated Player
    for i in range(1,len(pi)):  #check through pi to see if name matches
        if name == str(pi[i].getName()):
            return pi[i]
    raise InputError(str(name)+' is not a valid player')

    #private
def numToPlayer(num):       #given number, return associated Player
    if num in range(1,len(pi)):
        return pi[num]
    else:
        raise InputError(str(num)+' is not a valid player')

    #private
def allToPlayer(anyForm):   #given str/int/Player, return associated Player (if able)
    if type(anyForm) == int:
        return numToPlayer(anyForm)
    elif type(anyForm) == str:
        return nameToPlayer(anyForm)
    elif isinstance(anyForm,Player):
        return anyForm
    else:
        raise InputError(str(anyForm)+' is not a valid player')

    #private
def numToProp(num):         #given number, return associated Property
    if num in range(1,23):
        return prop[num]
    else:
        raise InputError(str(num)+' is not a valid property')

    #private
def allToProp(anyForm):     #given int/Property, return associated Property
    if type(anyForm) == int:
        return numToProp(anyForm)
    elif isinstance(anyForm,Property):
        return anyForm
    else:
        raise InputError(str(anyForm)+' is not a valid property')

##INITIALIZATION

    #private            init all 22 properties with their attributes
def initProperties(): #num  name                    cost  hc  rent
    prop[1] = Property( 1, 'Mediterranean Avenue',   60,  50, [ 70,130,220,370, 750])
    prop[2] = Property( 2, 'Baltic Avenue',          60,  50, [ 70,130,220,370, 750])
    prop[3] = Property( 3, 'Oriental Avenue',       100,  50, [ 80,140,240,410, 800])
    prop[4] = Property( 4, 'Vermont Avenue',        100,  50, [ 80,140,240,410, 800])
    prop[5] = Property( 5, 'Connecticut Avenue',    120,  50, [100,160,260,440, 860])
    prop[6] = Property( 6, 'St. Charles Place',     140, 100, [110,180,290,460, 900])
    prop[7] = Property( 7, 'States Avenue',         140, 100, [110,180,290,460, 900])
    prop[8] = Property( 8, 'Virginia Avenue',       160, 100, [130,200,310,490, 980])
    prop[9] = Property( 9, 'St. James Place',       180, 100, [140,210,330,520,1000])
    prop[10]= Property(10, 'Tennessee Avenue',      180, 100, [140,210,330,520,1000])
    prop[11]= Property(11, 'New York Avenue',       200, 100, [160,230,350,550,1100])
    prop[12]= Property(12, 'Kentucky Avenue',       220, 150, [170,250,380,580,1160])
    prop[13]= Property(13, 'Indiana Avenue',        220, 150, [170,250,380,580,1160])
    prop[14]= Property(14, 'Illinois Avenue',       240, 150, [190,270,400,610,1200])
    prop[15]= Property(15, 'Atlantic Avenue',       260, 150, [200,280,420,640,1300])
    prop[16]= Property(16, 'Ventnor Avenue',        260, 150, [200,280,420,640,1300])
    prop[17]= Property(17, 'Marvin Gardens',        280, 150, [220,300,440,670,1340])
    prop[18]= Property(18, 'Pacific Avenue',        300, 200, [230,320,460,700,1400])
    prop[19]= Property(19, 'North Carolina Avenue', 300, 200, [230,320,460,700,1400])
    prop[20]= Property(20, 'Pennsylvania Avenue',   320, 200, [250,340,480,730,1440])
    prop[21]= Property(21, 'Park Place',            350, 200, [270,360,510,740,1500])
    prop[22]= Property(22, 'Boardwalk',             400, 200, [300,400,560,810,1600])

##PAYMENT

    #public
def payToBank(pin,n):           #remove $n from p1
    p1 = allToPlayer(pin)
    p1.pay(n)
    print(p1.getName(),' paid $',n,sep ='')

    #public
def receiveFromBank(pin,n):     #give $n to p1
    p1 = allToPlayer(pin)
    p1.receive(n)
    print(p1.getName(),' received $',n,sep ='')

    #public
def payPlayer(p1in,n,p2in):     #move $n from p1 to p2
    p1 = allToPlayer(p1in)
    p2 = allToPlayer(p2in)
    p1.pay(n)
    p2.receive(n)
    print(p1.getName(),' paid $',n,' to ',p2.getName(),sep ='')
    
    #public
def payAll(pin,n):
    p1 = allToPlayer(pin)
    for p in range(1,len(pi)):
        if pi[p].getNum() != p1.getNum():
            p1.pay(n)
            pi[p].receive(n)
    print(p1.getName(),' paid $',n,' to all other players',sep ='')
    
    #public
def receiveFromAll(pin,n):
    p1 = allToPlayer(pin)
    for p in range(1,len(pi)):
        if pi[p].getNum() != p1.getNum():
            pi[p].pay(n)
            p1.receive(n)
    print(p1.getName(),' received $',n,' from all other players',sep ='')

##PROPERTIES

    #public              (use try catch)
def changeOwner(pin,propin):    #change all ownership attributes (in Player and Property)
    p1 = allToPlayer(pin)
    prop = allToProp(propin)
    prevOwnerNum = prop.getOwnerNum()  #remove ownership from previous owner (if Player)
    if prevOwnerNum in range(1,len(pi)):
        pi[prevOwnerNum].removeProperty(prop.getNum())
    p1.addProperty(prop.getNum())   #add ownership for new owner
    prop.setOwner(p1.getNum())      #set Property.owner
    print(p1.getName(),'now owns',prop.getName())
    
    #public
def buyProperty(pin,propin):    #pin pays and takes ownership of propin
    p1 = allToPlayer(pin)
    prop = allToProp(propin)
    if prop.getOwnerNum() == 0:     #if owned by bank
        p1.pay(prop.getCost())          #pay
        prop.setOwner(p1.getNum())      #assign property ownership
        p1.addProperty(prop.getNum())   #player takes ownership
        print(p1.getName(),' bought ',prop.getName(),' for $',prop.getCost(),sep ='')
    else:                           #otherwise tell user it is already owned
        raise PropertyIssue(prop.getOwnerName()+' already owns that')

    #public
def mortgage(propin):               #owner mortgages a property and receives money
    prop = allToProp(propin)
    if prop.getOwnerNum() == 0:          #if owned by bank, raise exception
        raise PropertyIssue('no one owns this property')
    else:
        cost = int(prop.getCost()/2)    #player receives half of property cost
        prop.mortgage()                 #mortgage
        prop.getOwner().receive(cost)   #owner receives money
        print(prop.getOwnerName(),' mortgaged ',prop.getName(),' for $',cost,sep ='')

    #public
def unmortgage(propin):             #owner pays to unmortgage a property
    prop = allToProp(propin)
    if prop.getOwnerNum() == 0:         #if owned by bank, raise exception
        raise PropertyIssue('no one owns this property')
    else:
        cost = int(prop.getCost()/2)
        prop.unmortgage()               #unmortgage property
        prop.getOwner().pay(cost)       #owner pays bank
        print(prop.getOwnerName(),' unmortgaged ',prop.getName(),' for $',cost,sep ='')        

    #public         (use try catch so all conditions are checked)
def buyHouses(propin,n):                #owner pays to increase property value by n
    prop = allToProp(propin)
    if prop.getOwnerNum() == 0:
        raise PropertyIssue('no one owns this property')
    else:
        prop.changeVal(n)                   #update house value
        cost = prop.getHouseCost()*n        #get cost of n houses
        prop.getOwner().pay(cost)           #owner pays cost
        print(prop.getOwnerName(),' bought ',n,' house(s) on ',prop.getName(),' for $',cost,sep ='')

    #public
def buyHouse(propin):       #owner pays to increase property value by 1
    buyHouses(propin,1)

    #public
def sellHouses(propin,n):   #owner receives money to decrease property value by n
    prop = allToProp(propin)
    if prop.getOwnerNum() in range(1,len(pi)):  #if owned by a player
        prop.changeVal(-n)                      #reduce .val by n
        cost = int(n*prop.getHouseCost()/2)    #receive half the house cost
        prop.getOwner().receive(cost)          #owner receives money
        print(prop.getOwnerName(),' sold ',n,' house(s) on ',prop.getName(),' for $',cost,sep ='')
    else:
        raise PropertyIssue('no one owns this property')

    #public
def sellHouse(propin):      #owner receives money to decrease property value by 1
	sellHouses(propin,1)

##ACTIONS
    
    #public
def passGO(pin):                #pin receives $200 for passing GO
    p1 = allToPlayer(pin)
    p1.receive(200)
    print(p1.getName(),'passed GO')

    #public
def payRent(pin,propin):        #pin pays rent to owner of propin
    p1 = allToPlayer(pin)
    prop = allToProp(propin)
    if prop.isMortgaged():          #unless it is mortgaged
        raise PropertyIssue('Property is mortgaged by '+prop.getOwnerName())
    elif prop.getOwnerNum() == 0:   #or owned by the bank
        raise PropertyIssue('No one owns this property')
    else:
        payPlayer(p1,prop.getRentCost(),prop.getOwner())     #pay owner

    #public
def drawChance():           #print next card in chance deck
    card = c.drawChance()
    a.printChance(card)
        
    #public
def trade(p1,port1,n1,p2,port2,n2):     #p1 receives properties in list port1, money n1
                                        #p2 receives properties in list port2, money n2
    try:
        print('TRADE')
        if n1 > 0:                  #transfer money
            payPlayer(p2,n1,p1)
        if n2 > 0:
            payPlayer(p1,n2,p2)
        for p in range(len(port1)):     #call changeOwner() for properties
            changeOwner(p1,port1[p])
        for p in range(len(port2)):
            changeOwner(p2,port2[p])
    except TypeError:                   #instruct user to reset trade if it fails
        print('*trade failed*\nInput should be:\n'+
              '\t(Player1,[property,list,1],integer1,P2,[prop,list,2],int2)\n'+
              'Please reset all transactions')

##INFO

    #public
def displayPlayers():           #display all players and their savings and net worth
    print('---------------------------------')  #with formatting so it looks nice
    print('_________________________________')
    print('Name      Number  Savings  Net Worth')
    for i in range(1,len(pi)):
        name = pi[i].getName()
        while len(name) < 10:
            name = name + ' '
        print(name,'  ',pi[i].getNum(),
              '\t  $',pi[i].getSavings(),
              '\t   $',pi[i].getNetWorth(),sep ='')
    print('---------------------------------')

    #public
def displayProperty(propin):    #display info for a property
    prop = allToProp(propin)
    print(prop.getInfo())       #calls Property.getInfo()

    #public
def displayProperties():        #displays .getInfo() for all properties
    print('---------------------------------')
    for i in range(1,23):
        print(prop[i].getInfo())
    print('---------------------------------')

    #public
def displayPropertiesOf(pin):   #displays list of properties owned by pin
    p1 = allToPlayer(pin)
    plist = p1.getProperties()      #call Player.getProperties()
    print(p1.getName(),'owns:')
    for i in range(1,len(plist)):   #print name of all properties owned by player
        if i == 1:
            print(prop[i].getName())

##GAMEPLAY
    
    #public
def startGame():        #sets up game
    initProperties()
    c.initChance()
    addPlayer('the Bank')   #to occupy the Player 0 spot (with other convenient uses)
    a.printStartScreen()
    print('\n> use addPlayer("name") to add each person')
    print('> type helpme() for assistance')

    #public
def addPlayer(name):    #add Player to game with user-defined name
    if type(name) == str:
        if len(name) > 10:
            raise InputError('name is too long, please use 10 or fewer characters')
        k = len(pi)
        for i in range(k):      #name must be unique
            if pi[i].getName() == name:
                raise InputError('name already taken')
        pi.append(Player(k,name))
        if k != 0:              #print an acknowledgement (except for the Bank)
            print(name,'is player',k)
    else:
        raise InputError('name was not a string')

    #public
def removePlayer(pin):          #remove player from game
    p1 = allToPlayer(pin)
    num = p1.getNum()
    if num == 0:
        raise InputError('you cannot remove the Bank from the game')
    pi[num] = 0                     #set to 0 in pi
    for i in range(num+1,len(pi)):    #decrement all higher player numbers
        pi[i].setNum(i-1)
        pi[i-1] = pi[i]
        pi[i] = 0
    pi.remove(0)                    #remove 0 from pi
    print(p1.getName(),'has been removed from the game')
    
    #public
def helpme():
    a.printHelpScreen()

#MAIN
startGame()