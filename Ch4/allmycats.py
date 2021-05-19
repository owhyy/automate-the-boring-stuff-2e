cat_names = []
while True:
    print('Enter the name of cat ' + str(len(cat_names) + 1) + ' (or enter nothing to stop)') 
    name = input()
    if name == '':
        break
    cat_names += [name] # list concatination
print('The cat names are:')
for name in cat_names: # loop integration with lists
    print(' ' + name)
