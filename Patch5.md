5.1
This file was tested in the cmd window.
open cmd, type 'python', type 'import monopoly as m', type commands
Remarks:
- need user-friendly method that calls .getInfo() with allToProp()
- buying a property prints 2 lines... thoroughly plan and write the user output
- payRent(pin,propin) should call .isMortgaged() on line 516. Check other methods and use .getInfo instead of directly accessing classes
- add allToPlayer() to displayPropertiesOf(pin) (and others)
- code needs better comments
5.2
- added displayProperty() as easily-accessible way to see property info
- fully implemented allToProp, allToPlayer (in response to displayPropertiesOf() issue)
- payRent() is repaired and tested
- changed many payToBank() and receiveFromBank() to .pay() and .receive()
NEXT STEPS
- organizing and writing user output
- thoroughly commenting code
