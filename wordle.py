


import random 

board = ['_', '_', '_', '_']

words = [
    'grab',
    'slap',
    'tram',
    'slam',
    'harm',
    
]

choice = random.choice(words)

choice = 'harm'

check = True

while check:
    
    word = input('Input word: ')
    
    if len(word) > 4 or len(word) < 4:
        print('Please input a 4-letter word.')
        continue
        
    for i in range(4):
        if choice[i] == word[i]:
            board[i] = word[i]
            
    if '_' not in board:
        check = False
        continue
            
    for i in range(4):
        if word[i] in choice:
            print(f'{word[i]} is in the word.')
    
    for i in range(4):
        print(board[i], end=' ')
        
    print('\n')
    
    

else:
    print('You guessed the word.')
    

            
    
