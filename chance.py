# -*- coding: utf-8 -*-
"""
Created on Sat May 16 19:33:31 2020
chance.py
monopoly_6 module
patch 6.0
@author: trist
"""
#IMPORTS
import random as r

#GLOBAL VARS
normal = [0]*32
special = [0]*3
chance = []
chanceIndex = 0

class Chance(object):                       #each chance card is a Chance object
    
    def __init__(self,num,phrase):
        self.num = num          #number for indexing purposes
        self.phrase = phrase    #statement on card
    
    def getPhrase(self):
        return self.phrase      #return phrase as string

def initChance():           #create chance cards and shuffle
    global chanceIndex
    initChanceCards()
    shuffleChanceCards()
    chanceIndex = 0

def initChanceCards():      #properties of all normal and special chance cards
    normal[0] = Chance(0,'Advance to GO.')
    normal[1] = Chance(1,'Advance to Illinois Avenue. If you pass GO, collect $200.')
    normal[2] = Chance(2,'Advance to St.Charles Place. If you pass GO, collect $200.')
    normal[3] = Chance(3,'Bank pays you a dividend of $50.')
    normal[4] = Chance(4,'Get out of jail free. This card may be kept until needed, or sold/traded.')
    normal[5] = Chance(5,'Go back three spaces.')
    normal[6] = Chance(6,'Go to jail. Do not pass GO, do not collect $200.')
    normal[7] = Chance(7,'Make general repairs on your properties: for each house pay $25.')
    normal[8] = Chance(8,'Speeding fine $15.')
    normal[9] = Chance(9,'Take a stroll on the Boardwalk. Advance to Boardwalk.')
    normal[10]= Chance(10,'You have been elected chairman of the board. Pay each player $50.')
    normal[11]= Chance(11,'Your building loan matures. Receive $150.')
    normal[12]= Chance(12,'You won a crossword competition! Collect $100.')
    normal[13]= Chance(13,'Advance to Marvin Gardens. If you pass GO, collect $200.')
    normal[14]= Chance(14,'Wrong train! Roll one die and move backwards.')
    normal[15]= Chance(15,'Advance to GO.')
    normal[16]= Chance(16,'Bank error in your favor! Collect $200.')
    normal[17]= Chance(17,'Attempt tax fraud. If you roll 1 or 2, collect $50. Otherwise, go to jail.')
    normal[18]= Chance(18,'Renovation. Pay $50.')
    normal[19]= Chance(19,'You bought another house. Pay $100 in extra maintenance.')
    normal[20]= Chance(20,'Go to jail. Do not pass GO, do not collect $200.')
    normal[21]= Chance(21,'Get out of jail free. This card may be kept until needed, or sold/traded.')
    normal[22]= Chance(22,'Grand Opera Night. Collect $50 from every player for opening night seats.')
    normal[23]= Chance(23,'Your cat scratched all your furniture! Pay $75.')
    normal[24]= Chance(24,'Xmas gift! Receive $100.')
    normal[25]= Chance(25,'Income tax refund. Collect $20.')
    normal[26]= Chance(26,'Your cat died. Collect life insurance of 20 kibbles and $5.')
    normal[27]= Chance(27,'Featured on Home Renovation. Upgrade one of your properties for free.')
    normal[28]= Chance(28,'You won a participation award in a beauty contest. Collect $10.')
    normal[29]= Chance(29,'You inherited $100.')
    normal[30]= Chance(30,'Buy a dog on the internet. Pay $40.')
    normal[31]= Chance(31,'FIRE! Your nearest building burns down. Remove all houses. Receive $25 in insurance for each house.')
    
    special[0]= Chance(32,'-----<YOU DIED>----- Return your properties to the bank and write a will. Your savings will be divided amongst the remaining players accordingly.')
    special[1]= Chance(33,'---<TORNADO HITS>--- Remove one house from every property on the street. All players on the street lose a turn.')
    special[2]= Chance(34,'---<HIRED HITMAN>--- Pay $200. Pick a player: if you roll 6, that player dies. All valuables go to the bank. If you roll a 1,2 or 3, go to jail.')

    #private
def shuffleChanceCards():
    shuffle(normal,100)         #shuffle decks
    shuffle(special,5)
    for i in range(len(normal)):    #add into chance deck
        chance.append(normal[i])
    for i in range(len(special)):
        chance.append(special[i])
    spot = r.randint(10,13)     #precisely place specials into the deck, at increment in mid-to-late
    swap(chance,spot,32)
    spot = r.randint(19,25)
    swap(chance,spot,33)
    spot = r.randint(29,34)
    swap(chance,spot,34)
    
    #private
def shuffle(cards,n):           #swap random cards n times
    MAX = len(cards)-1
    for i in range(n):
        a = r.randint(0,MAX)
        b = r.randint(0,MAX)
        cards = swap(cards,a,b)
    return cards
    
    #private
def swap(cards,a,b):            #swap objects in cards[] at index a,b
    temp = cards[a]
    cards[a] = cards[b]
    cards[b] = temp
    return cards

def drawChance():               #return phrase for next card as str
    global chance,chanceIndex
    phrase = chance[chanceIndex].getPhrase()  #get phrase
    chanceIndex += 1                #increment index
    if chanceIndex >= len(chance):           #if end of deck, re-initiate
        initChance()
    return phrase