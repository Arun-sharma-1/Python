"""
*
* *
* * *
* * * *
* * * * *
"""
for row in range(1, 6):
    for col in range(1, row+1):
        print('*', end=' ')
    print()

""" 
* * * * *
* * * *
* * *
* *
*
"""
print()
for row in range(6, 1, -1):
    for col in range(1, row):
        print('*', end=" ")

    print()

"""
    *
   **
  ***
 ****
*****
"""
print()

for row in range(1,6):
    for space in range(1,6-row):
        print(' ',end='')
    for col in range(1,row+1):
        print('*', end='')
    print()


"""
*****
 ****
  ***
   **
    *
"""
print()

for row in range(6,0,-1):
    for space in range(1,6-row+1):
        print(' ',end='')
    for col in range(1,row):
        print('*', end='')
    print()


"""
    *
   * *
  * * *
 * * * *
* * * * *
"""
print()

for row in range(1,6):
    for space in range(1,6-row):
        print(' ',end='')
    for col in range(1,row+1):
        print('*', end=' ')
    print()