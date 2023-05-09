import string
import random
#print(string.ascii_letters)
"""
printing all the alphabet starting form small letter that 
is small a to the the capital letter that is z """

symbol=[]
symbol=list(string.ascii_letters)
"""symbol has assign all the alphabet from small letter to capital letter as a list"""
#print(symbol)

card1=[0]*5
card2=[0]*5
"""we have intialize the five symbol in the card1 and card2 that all the symbol is intialize to zero"""

pos1=random.randint(0,4)
pos2=random.randint(0,4)
"""random.randint give the any random number betwwn 0 and 5 including o as well as 5"""
"""
pos1 and pos2 are the same symbol positon in card 1 and card 2 respectively
"""

samesymbol=random.choice(symbol)
"""if we want to choce from the list 
we can chose randomly from the random.choice
"""
symbol.remove(samesymbol)

if(pos1==pos2):
    card2[pos2]=samesymbol
    card1[pos1]=samesymbol
else:
    card1[pos1]=samesymbol
    card2[pos2]=samesymbol
    card1[pos2]=random.choice(symbol)
    symbol.remove(card1[pos2])
    card2[pos1]=random.choice(symbol)
    symbol.remove(card2[pos1])

i=0
while(i<5):
    if(i!=pos1 and i!=pos2):
        alphabet1=random.choice(symbol)
        symbol.remove(alphabet1)
        alphabet2=random.choice(symbol)
        symbol.remove(alphabet2)
        card1[i]=alphabet1
        card2[i]=alphabet2
    i=i+1

print(card1)
print(card2)

chinput=input("ask the similar symbol ")
if(chinput==samesymbol):
    print("wright")
else:
    print("wrong")
