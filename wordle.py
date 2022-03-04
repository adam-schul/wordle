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
    
    word = input('Input 4-letter word (or q to quit): ')
    
    if word == 'q':
        break
    
    letters = []
    
    if len(word) > 4 or len(word) < 4:
        print('Please input a 4-letter word.')
        continue
        
    for i in range(4):
        if choice[i] == word[i]:
            board[i] = word[i]
            letters.append(word[i])
            
    if '_' not in board:
        check = False
        continue
            
    for i in range(4):
        if word[i] in choice and word[i] not in letters:
            print(f'{word[i]} is in the word.')
            letters.append(word[i])
    
    for i in range(4):
        print(board[i], end=' ')
        
    print('\n')
    
    

else:
    print('You guessed the word.')
    
