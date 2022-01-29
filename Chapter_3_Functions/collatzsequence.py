def collatz(number):
    if number%2 == 0:
        return int(number/2)
    else:
        return int(number*3+1)
try:
    while True:
        try:
            print('\nInsert a integer:')
            number = int(input())
        except ValueError:
            print('Sorry, try input again')
        else:
            while number != 1:
                collatz(number)
                number = collatz(number)
            print('Number reached to: 1')
except KeyboardInterrupt:
    if SystemExit():
        print('Exiting...')