# monopoly
automated version of monopoly to be used with a board (in-person game, computerized rules)

HOW TO USE
- open python in the command window in the same folder as monopoly_#.py
- execute 'import monopoly_# as m'
- a start screen should appear. Follow the prompts and use helpme() if needed
- remember to type m.____ before each method

NEXT STEPS

    PATCH 6
- modulate
- fix chance initiation
- add bool isPlayer(),isProperty(),sufficientFunds() for efficiency
- add method removePlayer()

    PLAYABILITY
> beautification
- property card display (num houses, ownership, rent/cost/mortgaged)
- player profile (property list, savings, net worth)
> what happens to bankrupt players?
- bankrupcy calculation... if networth is too low for a transaction
- display BANKRUPT in player's savings and net worth
> write/repair functions
- removePlayer() <- adjust index for all players
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
- create separate module chance
