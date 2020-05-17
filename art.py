# -*- coding: utf-8 -*-
"""
Created on Sat May 16 19:42:48 2020
art.py
monopoly_6 module
patch 6.0
@author: trist
"""

#FORMATTING

def formatString(string):       #format string to fit on card
    lines = stringToLines(string)   #break into lines
    for l in range(len(lines)):     #format each line
        lines[l] = formatLine(lines[l])
    return lines

def stringToLines(string):      #return string as list of lines
    word = string.split()           #split string into list of words
    lines = []
    w = 0
    l = 0
    lines.append('')
    while w < len(word):                        #parse through words
        if len(lines[l])+len(word[w])+1 <= 22:  #each line <= 22 chars long
            lines[l] = lines[l] + ' ' + word[w] #space btw each word
            w += 1
        else:
            lines.append('')
            l += 1
    return lines

def formatLine(line):           #center text and add | on each side
    while len(line) < 22:           #add spaces until line is 22 chars long
        if len(line) == 21:         #while keeping words centered
            line = line + ' '
        else:
            line = ' ' + line + ' '
    line = '|' + line + '|'         #add | to either side
    return line


#ART

def printStartScreen():     #print art for start screen
    print(
'                               __\n'+
' //\/\\\   // \\\  |\||  // \\\  ||_|  // \\\  ||    \\\//  \n'+
'//    \\\  \\\ //  ||\|  \\\ //  ||    \\\ //  ||__   ||   ')

def printHelpScreen():
    print(
'\nEnter the player number or property number to use these methods    \n\n'+
'<PAYMENT>                          <PROPERTIES>                    \n'+
'payToBank(player,amount)           changeOwner(new owner,property) \n'+
'receiveFromBank(player,amount)     buyProperty(player,property)    \n'+
'payPlayer(payer,amount,receiver)   mortgage(property)              \n'+
'payAll(payer,amount_per_person)    unmortgage(property)            \n'+
'receiveFromAll(receiver,amount_pp) buyHouse(property)              \n'+
'                                   buyHouses(property,number)      \n'+
'<ACTIONS>                          sellHouse(property)             \n'+
'passGO(player)                     sellHouses(property,number)     \n'+
'payRent(player)                    \n'+
'drawChance()                       \n'+
'trade(player1,portfolio1,amount1,player2,portfolio2,amount2)       \n'+
'   portfolios are list of property numbers, amount is an integer   \n'+
'   portfolio1 & amount1 are received by player1, port2 & n2 by p2  \n'+
'                                   \n'+
'<INFO>                             <GAMEPLAY>                         \n'+
'displayPlayers()                   startGame()                     \n'+
'displayProperty(property)          addPlayer()                     \n'+
'displayProperties()                helpme()                        \n'+
'displayPropertiesOf(player)')
    
def printChance(phrase):
    lines = formatString(phrase)    #format phrase to fit on card
    print(                          #print card
' ______________________\n'+
'|         ____         |\n'+
'|        /    \        |\n'+
'|           __/        |\n'+
'|          |           |\n'+
'|          o           |\n'+
'|----------------------|')
    for l in range(len(lines)):
        print(lines[l])
    print(
'|______________________|')