print('Welcome to my computer quiz!')

playing = input('Would you like to play? ')
if playing.lower() != 'yes':
    quit()

print('Okay lets play!')

name = input('What is your name? ')
score = 0

answer = input('What does CPU stand for? ')
if answer.lower() == 'central processing unit':
    print('Correct!')
    score += 1
else: print('Incorrect')


answer_1 = input('What does GPU stand for? ')
if answer_1.lower() == 'graphics processing unit':
    print('Correct!')
    score += 1
else: print('Incorrect')

answer_2 = input('What does PSU stand for? ')
if answer_2.lower() == 'power supply':
    print('Correct!')
    score += 1
else: print('Incorrect')

if score == 0:
    print('You scored ' + str(score) + ' points ' + name + '. You may want to do some more studying.')
elif score == 1:
    print('You scored ' + str(score) + ' points ' + name + '. Not too bad.')
elif score == 2:
    print('You scored ' + str(score) + ' points ' + name + '. Great job!')
else: print('Perfect score ' + name + '!!!')

print('We are testing git stuff!')