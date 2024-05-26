import sys
from locations.NY import story as NYs
from locations.Asgard import story as Asgards
from locations.Planet import story as Planets

def background():
    print()

def storytell():
    locats = [NYs, Asgards, Planets]
    

    background()
    save = background()
    
    for loc in locats:
        loc()
storytell()