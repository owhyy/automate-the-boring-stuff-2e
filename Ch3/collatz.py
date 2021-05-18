
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    print(3 * number + 1)
    return 3 * number + 1

def read():
    try:
        number = int(input())
        while(number != 1):
            number = collatz(number)
    except ValueError:
        print('Error: Invalid paramter (expected int)')

read()
