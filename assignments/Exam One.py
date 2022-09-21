#IFSC 1202 - Exam 1
#By: Christian Johnston

from random import randint
print("Winners and Losers - Human is Even, Computer is Odd")

hGuess = 0
cGuess = 0
hScore = 0
cScore = 0

for i in range(1, 6):
    print("Round: " + str(i))

    hGuess = int(input("Enter your guess: "))
    cGuess = randint(1,5)

    print("Human Guess: " + str(hGuess) + " - " + "Computer Guess: " + str(cGuess))
    
    sum = hGuess + cGuess
    
    if sum % 2 == 0:
        print("Sum is Even")
        hScore += 1
    else:
        print("Sum is Odd")
        cScore += 1
    print("Human Score: " + str(hScore) + " - " + "Computer Score: " + str(cScore))

if hScore > cScore:
    print("Human Wins!")
else:
    print("Computer Wins!")