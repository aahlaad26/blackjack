import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
j="y"
def card(d,b):
  
  a=random.choice(cards)
  b.append(a)
  if j=="y":
    x=random.choice(cards)
    d.append(x)
    
    y=True


def blackjack():
  d=[]
  c=0
  b=[]
  y=True
  sum2=0
  
  sum1=0
  while y:
  
    while c<2:
      card(d,b)
     
      c+=1
    for i in d:
      sum1+=i
    if sum1<=17:
      j="y"
    if 11 in b and sum(b)>21:
        b.remove(11)
        b.append(1)
    for k in b:
      sum2+=k
    print(f"Your cards are {b}",f"dealer's first card is [{d[1]}]")
    z=input("y or n:")
    if z=="y":
      sum1=0
      sum2=0
      card(d,b)
    elif z=="n":
      if sum2<21 and sum2>sum1:
        print(f"you win, your score is {sum2} and dealer hand was{d}")
      elif sum2==sum1:
          print(f"draw,you and the dealer have same score that is {sum2}")
      elif sum2==21:
          print(f"You got blackjack,the dealer hand was {d}")
      elif sum2>21:
        print(f"Busted it is over 21,your score is {sum2} and the cards the dealer had was{d}")
      else:
        print(f"you lose,your score is {sum2} and the dealers hand was {d}")
      y=False
g= True     

while g:
    
    if input("Do you want to play blackjack y or n:")=="y":
      blackjack()
      
    else:
        g=False
