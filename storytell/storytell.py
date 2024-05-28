import time 
import sys

from locations.NY import story as NYs
from locations.Asgard import story as Asgards
from locations.Planet import story as Planets
from locations.Headquarters import story as Headquarters


def background():
    print("Thanos just snaps away a half of the creature in the universe!!!")
    time.sleep(1)
    print("You, will act as an Avenger and save thw universe!!!")
    time.sleep(1)
    input("But hold on, are we saving the universe???(Yes or No)")

def end():
    print()

def storytell():
    locats = [NYs, Asgards, Planets, Headquarters]
    
    save = background()
    print(save)

    if save == "Yes":
        print("Hello")
        pass
    else:
        print("Bye")
        sys.exit()

    for loc in locats:
        loc()
    
    end()
    
