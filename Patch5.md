5.5
Gameplay test remarks
- fix net worth calculation
- consider writing functions that apply to multiple players at once
- write help() function with list of commands
- add displayPlayer(pin) to display a single player's attributes
  (likely in patch-6)
Code remarks
- remove owner, value from Property.__init__()
- isolate Player.getProperties() from prop[]
Patch notes
- added methods helpme(), trade(), payAll(), receiveFromAll()
- fixed net worth calculation
- repaired exception messages
- remove owner,value from Property.__init__()
- Player.getProperties() returns properties list (1's and 0's)
- displayPropertiesOf(player)
- rename .unMortgage() to .unmortgage()
- rename printArt() to printChance() 
5.4
- use appropriate Property.getOwner() or .getOwnerName() or .getOwnerNum()
- print() needs space = '' for printing multiple objects
- set max name size
- displayPlayers() should print spaces after each name to hit the right size
NEXT STEPS
- thoroughly test
5.3
- organize & write user output
- thoroughly commented code
- .getOwner() now returns Player
- added .getOwnerNum() and .getOwnerName()
- added some exceptions to .set and .get for Property and Player classes
NEXT STEPS
- implement .getOwner(), .getOwnerName(), .getOwnerNum()
- print() needs space = '' for printing multiple objects
- set max name size
- displayPlayers() should print spaces after each name to hit the right size
5.2
- added displayProperty() as easily-accessible way to see property info
- fully implemented allToProp, allToPlayer (in response to displayPropertiesOf() issue)
- payRent() is repaired and tested
- changed many payToBank() and receiveFromBank() to .pay() and .receive()
NEXT STEPS
- organizing and writing user output
- thoroughly commenting code
5.1
This file was tested in the cmd window.
open cmd, type 'python', type 'import monopoly as m', type commands
Remarks:
- need user-friendly method that calls .getInfo() with allToProp()
- buying a property prints 2 lines... thoroughly plan and write the user output
- payRent(pin,propin) should call .isMortgaged() on line 516. Check other methods and use .getInfo instead of directly accessing classes
- add allToPlayer() to displayPropertiesOf(pin) (and others)
- code needs better comments
