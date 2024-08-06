import time
import sys

def slp():
    time.sleep(1)

def act():
    return input("Who are you acting? Thor or Rocket?")

def arrive():
    print("Thor and Rocket traveled to Asgard in 2013 for the \"Reality Stone\"")
    slp()
    print("Now the queen of Asgard, Thor\'s mother, walked towards where you are.")

def rocket():
    print("You ran away, and found the Reality Stone with your nose. It\'s in the guard\'s hand!")
    slp()
    print("You jumped up, got the Reality Stone, then you ran away with twenty guards chasing you!")
    slp()
    print("You found Thor and his mother then went back to the headquarters wtih Thor.")

def thor():
    print("You saw your mother, but you\'re so nevious that you stay at there like a wood")
    slp()
    print("Your mother saw you and send away the maid, she said, \"Hey Thor!\"")
    slp()
    print("You and your mother spent a little time on chating. You saw Rocket ran over here with the Reality Stone!")
    slp()
    return input("Your mother said, \"Now is the time to make a decision, stay or leave?\"")

def stay():
    print("You said, \"Mom, I want to stay here to protect the Asgard forever!\"")
    slp()
    print("So, you and Rocket stay here and lived peaceful!")
    slp()
    print("What a beautiful end!!!")
    slp()
    print("Thanks for playing!")
    slp()
    print("Hope to see you next time!")
    sys.exit()

def leave():
    print("You decided to leave and said, \"Wait! Let me try to find my hammer! \"")
    slp()
    print("ZOOOOOOOOOOOOOOOOOOM! The hammer flew back into your hand!")
    slp()
    print("\"Haha! Haha! It\'s here! I\'m still allow to have it! My hammer!\" You said.")
    slp()
    print("After it , you and Rocket went straight back to the headquarters.")