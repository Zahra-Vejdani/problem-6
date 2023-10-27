import random
dice=random.randint(1,6)
dice1=random.randint(1,6)
while True:
    while dice==6:
        print("you`re lucky,you got", dice, ",your 2nd number is: ", + dice1)
        
        if dice1==6:
            print("yay! you got 6, you can toss again!", dice)

        break
        
    if dice==1 or dice==2 or dice==3 or dice==4 or dice==5:
        print("Better luck next time, your number is: ", dice)
    
    break
