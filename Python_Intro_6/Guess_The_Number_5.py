import random
TheNumber = random.randint(1, 20)
attempts=5
print('Guess the number:')
while attempts>0:
    attempts-=1
    guess = int(input())
    if guess > TheNumber:
        print('Too high!')
    elif guess < TheNumber:
        print('Too low!')
    else:
        print('Correct!')
        break