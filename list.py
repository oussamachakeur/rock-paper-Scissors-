'''
lst = ['orang','banana','kiwi','apple']

#print(fruits[1]) printing anything we want

#fruits[3]='changed' #replace apple with changed 
#print(fruits)

#print(fruits[-1]) #here counting is from the last item , mean -1 is apple and -2 is kiwi

#fruits.append('date') #add a new item at the end of the list 
#print(fruits)
//
# List Methods

# Adds an item x to the end of the list.
lst.append('x')

# Extends the list by appending elements from the iterable.
lst.extend('iterable' , 'saass')

# Inserts an item x at a given position i.
lst.insert(3, 'x')

# Removes the first item from the list whose value is x.
lst.remove('x')

# Removes and returns the item at the given position i. If no index is specified, it removes and returns the last item in the list.
lst.pop([1])

# Removes all items from the list.
lst.clear()

# Returns the index of the first item whose value is x. The optional arguments start and end limit the search to a particular subsequence of the list.
#lst.index('x'[, start[, end]])

# Returns the number of times x appears in the list.
lst.count('x')

# Sorts the items of the list in place. The arguments can be used for sort customization.
lst.sort(key=None, reverse=False)

# Reverses the elements of the list in place.
lst.reverse()

# Returns a shallow copy of the list.
lst.copy()

# Built-in Functions

# Returns the number of items in the list.
len(lst)

# Creates a new list from an iterable.
list(['iterable'])

# Returns the largest item in the list.
max(lst)

# Returns the smallest item in the list.
min(lst)

# Returns the sum of the items in the list.
sum(lst, start=0)

# Returns a new sorted list from the elements of any iterable.
sorted('iterable', key=None, reverse=False)

# Returns a reverse iterator over the values of the list.
reversed(lst)

# Returns an enumerate object. It contains pairs of index and items from the iterable.
enumerate('iterable', start=0)

# Returns True if any element of the iterable is true. If the iterable is empty, returns False.
any('iterable')

# Returns True if all elements of the iterable are true. If the iterable is empty, returns True.
all('iterable')
'''
#import random 

#names = str(input('please enter all the name of the list '))
#name_list= names.split(",")
#selected = random.randint(0,(len(name_list)-1))
 
#print(name_list[selected] + 'is going to pay today') 

'''

import random

row1=['🤗','🤗','🤗']
row2=['🤗','🤗','🤗']
row3=['🤗','🤗','🤗']

matrix = [row1 , row2 , row3]

print(f'{row1}\n{row2}\n{row3}')

for i in range(1, 6):
 #######################################################################################################################

    # Human turn
    position = input("Please enter the position (e.g., 11 for top-left): ")
    pos_list = [int(digit) for digit in position]
    horizontal = pos_list[0]
    vertical = pos_list[1]
    matrix[vertical-1][horizontal-1] = "X"
    print(f'{row1}\n{row2}\n{row3}')
 
 ######################################################################################################################
    # Computer turn
    while True:
        computer_choice = [random.randint(1, 3), random.randint(1, 3)]
        if matrix[computer_choice[1]-1][computer_choice[0]-1] == '🤗':
            matrix[computer_choice[1]-1][computer_choice[0]-1] = "O"
            break
    
    print("Computer choice:", computer_choice)
    print(f'{row1}\n{row2}\n{row3}')
 #######################################################################################################################
    # Check win condition again after the computer move
    if (matrix[0][0]=="X") and (matrix[1][1]=="X") and (matrix[2][2]=="X") or \
       (matrix[0][0]=="X") and (matrix[0][1]=="X") and (matrix[0][2]=="X") or \
       (matrix[0][0]=="X") and (matrix[1][0]=="X") and (matrix[2][0]=="X") or \
       (matrix[0][1]=="X") and (matrix[1][1]=="X") and (matrix[2][1]=="X") or \
       (matrix[0][2]=="X") and (matrix[1][2]=="X") and (matrix[2][2]=="X") or \
       (matrix[1][0]=="X") and (matrix[1][1]=="X") and (matrix[1][2]=="X") or \
       (matrix[2][0]=="X") and (matrix[2][1]=="X") and (matrix[2][2]=="X"):  
       print("HUMAN WIN")
       break
    ##########      
    elif (matrix[0][0]=="O") and (matrix[1][1]=="O") and (matrix[2][2]=="O") or \
         (matrix[0][0]=="O") and (matrix[0][1]=="O") and (matrix[0][2]=="O") or \
         (matrix[0][0]=="O") and (matrix[1][0]=="O") and (matrix[2][0]=="O") or \
         (matrix[0][1]=="O") and (matrix[1][1]=="O") and (matrix[2][1]=="O") or \
         (matrix[0][2]=="O") and (matrix[1][2]=="O") and (matrix[2][2]=="O") or \
         (matrix[1][0]=="O") and (matrix[1][1]=="O") and (matrix[1][2]=="O") or \
         (matrix[2][0]=="O") and (matrix[2][1]=="O") and (matrix[2][2]=="O") :    
         print("COMPUTER WIN") 
         break
    elif all(cell != '🤗' for row in matrix for cell in row):
         print("IT'S A DRAW ")
         break
    '''
import random 

print ("hello to the game rock paper ciser with me , the great computer \n are u ready")
answer0=str(input("press Y for yes and N for no (Y/N): "))
answer= answer0.upper()

if answer == "Y":
    pick0 = str(input("choose rock or paper or cesar (R/P/C): "))
    pick = pick0.upper()
    cm_choices =['R','P','C']
    cm_pick= random.randint(0,2)
    cm = cm_choices[cm_pick]
    print('computer choosed '+cm)
    if (pick == 'R') and (cm == 'C') or (pick == 'P') and (cm == 'R') or (pick=='C') and (cm == 'P'):
        print(' i admit it , you HUMAN  win .')
    elif (pick == 'R') and (cm == 'P') or (pick == 'P') and (cm == 'C') or (pick=='C') and (cm == 'R'): 
        print("AS I SAID THE GREAT COMPUTER ALWAYS WIN HAHAHAHAH")
    elif (cm==pick):
        print('its a DRAW ' )
    else :
        print('wrong input')    
else:
    print('okey byby')            
        

