import random 

mydeck = [r+s for r in "23456789TJQKA" for s in "ACDS"]

def deal(numhands, n=5, deck=mydeck):
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]
   

print deal(5, n=5, deck=mydeck)
