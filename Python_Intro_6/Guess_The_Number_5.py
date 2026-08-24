import random
the_number = random.randint(1, 20)
attempts=5
print('Guess the number:')
while attempts>0:
    attempts-=1
    guess = int(input())
    if guess > the_number:
        print('Too high!')
    elif guess < the_number:
        print('Too low!')
    else:
        print('Correct!')
        break
else:
    print('Out of attempts!')
