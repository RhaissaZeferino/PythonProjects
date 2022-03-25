'''
A simple project where the user guess the right number 
'''
import random

try:
    right=random.sample(range(1, 100), 3)
    n=random.sample(range(0, 3), 3) 
    #Uncomment to know the answer:
    #print(n)
    #print(right)
    print(right[n[0]],right[n[1]],right[n[2]])
    chosed = int(input('Please input your chosed number: '))
    if right[0]==chosed:
        print('You got it! Nice guess')
    else:
        print('Maybe next time! The answer was {}'.format(right[0]))
except Exception as msg:
    print('Error: {}'.format(msg))
    

