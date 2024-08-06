import sys
from storytell.storytell import storytell 

print("Hello")
ans = input("Are we starting?(Yes/No)")

if ans == "Yes":
    storytell()
else:
    sys.exit()

    