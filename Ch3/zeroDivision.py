
def divide(n):
    try:
        return 42/n
    except ZeroDivisionError:
        print('Error: Invalid argument')

print(divide(53))
print(divide(1))
print(divide(5))
print(divide(0))

