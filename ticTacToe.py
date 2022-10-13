###our game code
#pseudocode:
#1. provide user with instructions
#2. ask user if they would like to go first. store in variable 'first'
#3. ask user what character they wouod like to play as. store in variable 'letter'


import random

print('''Welcome to Tic-Tac-Toe! 
To play, you will enter a number on the grid in
accordance to which position you wish to make your mark: 

0|1|2
-----
3|4|5
-----
6|7|8

''')
#I don't like the way my instructions are worded..........

first=input('Would you like to go first? (y/n) ')
letter=input('What letter do you want to play as? (x/o) ')

if first=='y' and letter=='x':
    game=int(input('Please enter a number between 0 and 8:'))
    if game==0:
        print('''
X| | 
-----
 | | 
-----
 | | 
''')
    elif game==1:
        print('''
 |X| 
-----
 | | 
-----
 | | 
''')
    elif game==2:
        print('''
 | |X 
-----
 | | 
-----
 | | 
''')
    elif game==3:
        print('''
 | | 
-----
X| | 
-----
 | | 
''')
    elif game==4:
        print('''
 | | 
-----
 |X| 
-----
 | | 
''')
    elif game==5:
        print('''
 | | 
-----
 | |X 
-----
 | | 
''')
    elif game==6:
        print('''
 | | 
-----
 | | 
-----
X| | 
''')
    elif game==7:
        print('''
 | | 
-----
 | | 
-----
 |X| 
''')
    elif game==8:
        print('''
 | | 
-----
 | | 
-----
 | |X 
''')
    else:
        print('You entered an incorrect value, please try again.') ###How do do they start again? loop?





    
elif first=='y' and letter=='o':
    game=int(input('Please enter a number between 0 and 8:'))
    if game==0:
        print('''
O| | 
-----
 | | 
-----
 | | 
''')
    elif game==1:
        print('''
 |O| 
-----
 | | 
-----
 | | 
''')
    elif game==2:
        print('''
 | |O 
-----
 | | 
-----
 | | 
''')
    elif game==3:
        print('''
 | | 
-----
O| | 
-----
 | | 
''')
    elif game==4:
        print('''
 | | 
-----
 |O| 
-----
 | | 
''')
    elif game==5:
        print('''
 | | 
-----
 | |O 
-----
 | | 
''')
    elif game==6:
        print('''
 | | 
-----
 | | 
-----
O| | 
''')
    elif game==7:
        print('''
 | | 
-----
 | | 
-----
 |O| 
''')
    elif game==8:
        print('''
 | | 
-----
 | | 
-----
 | |O 
''')
    else:
        print('You entered an incorrect value, please try again.') ###How do do they start again? loop?









elif first=='n' and letter=='x':
    point=random.randint(0,8)
    if point==1:
        print

elif first=='n' and letter=='o':
    point2=random.randint(0,8)
    print('''Please enter a number
 | | 
-----
 | | 
-----
 | | 
''')


    
