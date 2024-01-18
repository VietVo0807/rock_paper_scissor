import random
print('Welcome to Rock, Paper, Scissor!')
computer_score = 0
player_score = 0
turns = 0

while turns < 3:
    archive = ['rock','scissor','paper']
    your_choice = input(
'''Press 1 if you want to pick rock
Press 2 if you want to pick paper
Press 3 if you want to pick scissor
Press q if you want to quit!
\n''') 
    
    if your_choice == 'q':
        print('Thank you for playing!')
        break
    
    if your_choice not in ['1','2','3']:
        print('Invalid choice! Please re-enter your command')
        continue
    
    player = archive[int(your_choice)-1]
    computer = random.choice(archive)
    
    if your_choice == '1':
        print('You choose rock')
    elif your_choice == '2':
        print('You choose scissor')
    elif your_choice == '3':
        print('You choose paper')
    print(f'Your opponent choose {computer}!')
    
    if player == computer :
            print('It\' s a draw!')
    elif (player == 'rock' and computer == 'scissor') or (player == 'scissor' and computer =='paper') or (player == 'paper' and computer =='rock'):
            print('You have won!')
            player_score += 1
    else:
        print('You have lost!')
        computer_score += 1 
    turns +=1
    print(f'You have {3 - turns} turn left!')

    if turns == 3:
        if player_score > computer_score:
            print('You won! That\'s some great skills.')
        elif player_score == computer_score:
            print('You have tied!')
        else:
            print('You have lost! Try again.')
            

        
    
