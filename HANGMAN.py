import random

def update ():
    for i in right:
        print (i, end =" ")
    print ()

def checkWinning(right):
    for r in right:
        if r == "_":
            return False
    return True

word= ['python','program']
picked = random.choice(word)
right = ['_'] * len(picked) 
life =len(picked)+3
print ("you have " ,life, "trys" )
update()

while True:
    if checkWinning(right):
        print("Winner Winner ")
        break
    guess = input("Enter a word ")
    life=life-len(guess)
    if life>0:
        for p in range(len(picked)):
            for g in range(len(guess)):
                if picked[p] == guess[g]:
                    right[p]= picked[p]        
        update()
    else:
        print("Loser, You can try again") 
        break

            
   
