import random
numberOfStreaks = 0
counter = 0
checker = None #Records previously checked index of list
current = None #Checking current index of list
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coin = []
    # HeadStreaks = 0
    # TailStreaks = 0
    for numflips in range(100):
        flip = random.randint(0,1)
        if flip == 0:
            coin.append('H')
        else:
            coin.append('T')
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for c in range(len(coin)):
        current = checker
        checker = coin[c]
        if current == checker:
            counter += 1
        elif current != checker:
            counter = 0
        if counter == 6:
            numberOfStreaks += 1
            counter = 0
# MY FKIN SHIT OF CODE THAT DOESN'T WORKS AND IDK WHY (NOW I KNOW HOW IT WORKS, BAD)
#         if numflips >= 5:
#             if coin[(numflips-5):(numflips+1)] == ['H','H','H','H','H','H']:
#                 HeadStreaks += 1
#             elif coin[(numflips-5):(numflips+1)] == ['T','T','T','T','T','T']:
#                 TailStreaks += 1
#     numberOfStreaks += HeadStreaks + TailStreaks
#print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))