import states
import huis
import zolder
import tuin
import gang

while True:
    if states.locatie == "HUIS" :
        huis.begin()
    elif states.locatie == "GANG" :
        gang.begin()
    elif states.locatie == "ZOLDER" :
        zolder.begin()
    elif states.locatie == "GANG" :
        gang.begin()
        