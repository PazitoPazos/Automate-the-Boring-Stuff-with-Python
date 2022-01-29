"""
1. What are the two values of the Boolean data type? How do you write them?
True/False

2. What are the three Boolean operators?
And/Or/Not

3. Write out the truth tables of each Boolean operator
(that is, every possible combination of Boolean values for the operator and what they evaluate to).
And                             Or                              Not
True and True = True            True or True = True             not True = False                   
True and False = False          True or False = True            ----------------
False and True = False          False or True = True            not False = True
False and False = False         False or False = False          ----------------

4. What do the following expressions evaluate to?
--------------------------------------------------
(5 > 4) and (3 == 5) #= (True) and (False) = False
not (5 > 4) #= not (True) = False
(5 > 4) or (3 == 5) #= (True) or (False) = True
not ((5 > 4) or (3 == 5)) #= not ((True) or (False)) = not (True) = False
(True and True) and (True == False) #= (True) and (False) = False
(not False) or (not True) #= (True) or (False) = True
--------------------------------------------------

5. What are the six comparison operators?
== Equal to
!= Not Equal to
< Less than
> Greater than
<= Less than or equal to
>= Greater than or equal to

6. What is the difference between the equal to operator and the assignment operator?
== is used for compare if two values are equal
= assigns the value on the right into the variable on the left

7. Explain what a condition is and where you would use one.

8. Identify the three blocks in this code:

spam = 0
if spam == 10:
    print('eggs') #First block
    if spam > 5:
        print('bacon') #Second Block
    else:
        print('ham') #Third Block
    print('spam')
print('spam')

9. Write code that prints Hello if 1 is stored in spam,
prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

spam = 3
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')

10. What keys can you press if your program is stuck in an infinite loop?
Ctrl^C

11. What is the difference between break and continue?
Break exits the loop and continue go to the loop's start.

12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
range(10) will be a range of 10 numbers (0 to 9 for example)
range(0,10) is a range that gonna start at 0 (first argument is where starts)
and finish at 10 (second argument is where finishes)
range(0,10,1) will be start at 0 and finish at 10 and will go in steps of 1 (third argument)

13. Write a short program that prints the numbers 1 to 10 using a for loop.
Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

print('***FOR LOOP***')
for i in range (1,11):
    print(i)

j = 0
print('***WHILE LOOP***')
while j < 11:
    print(j)
    j = j + 1

14. If you had a function named bacon() inside a module named spam,
how would you call it after importing spam?
spam.bacon()
"""