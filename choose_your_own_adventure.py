#Basic adventure game

name = input('Type your name: ')
print('Welcome to the game, ', name + '!')

answer = input('You are on a dirt road that has come to an end. You can go left or right. Which way do you want to go? ')

if answer.lower() == 'left':
    q2 = input('You turn left and come to a river. Do you want to walk around it or swim across? Type walk to walk around it and swim to swim around it: ')
    
    if q2.lower() == 'walk':
        q2_1 = input('You walk for miles to get around the river. You need food now. Do you want to hunt or fish at the lake? Type hunt to hunt or fish to fish: ')
        
        if q2_1.lower() == 'hunt':
            print('You ran into a predator. The hunter has become the hunted. Game Over!')
            
        elif q2_1.lower() == 'fish':
            print('You caught a fish for dinner! You win!')
            
        else: print('Not a valid input. Game Over!')
        
                
    elif q2.lower() == 'swim':
        print('You got eaten by an aligator. Game Over!')
        
    else: print('Not a valid option. Game Over!')
elif answer.lower() == 'right':
    q3 = input('You turn right and come to a mountain. Do you want to climb the mountain or walk around it? Type climb to climb and walk to walk around: ')
    
    if q3.lower() == 'climb':
        q3_1 = input('You successfully climb the mountian, but you need get down. There is a path down to the left and to the right. Which way would you like to go? ')
        
        if q3_1.lower() == 'left':
            print('You fell off a cliff. Game Over!')
            
        elif q3_1.lower() == 'right':
            print('You made it down the mountain and made it home! You win!')
            
        else: print('Not a valid input. Game Over!')
        
    elif q3.lower() == 'walk':
        q3_2 = input('As you walk around the mountain, you are attached by tigers. Game Over!')
        
    else: print('Not a valid answer. Game Over!')
            
else: print('Not a valid option. Game Over!')