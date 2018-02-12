import random
correct=random.randint(10,16)
print(str(correct))
print('Guess a number AL')
for i in range(1,7):
    guess=int(input())
    if guess>15:
        print('Too high bro!')
    elif guess<10:
        print('Too low bro!!')
    else:
        print('You were somewhat nearer!')
        if(guess==correct):
            print('Bro perfect shot man!')
            break;
print('You done with ur chances man!')
