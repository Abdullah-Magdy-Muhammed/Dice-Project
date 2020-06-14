import random
Dice_1 = [1,2,3,4,5,6]
Dice_2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
m = int(input("Which dice do you want !"))
if m == 1:
        n = input("Do You Want To Throw The Dice ?").lower()
        if n == "no" or "n":
                print(random.randrange(1,7))
        else:
                pass



             
elif m == 2:
        l = input("Do You Want To Throw The Dice ?").lower()
        if l== "yes" or "y":
                print(random.randrange(1,25))
        else:
                pass      

               
else:
        print("Sorry,This is invalid value")             




    



