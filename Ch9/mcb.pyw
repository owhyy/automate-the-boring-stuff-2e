import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb') # creates shelf

if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save': # if you pass 3 comandline args and 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste() # paste into shelf (word is key, value is definition)
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.pop(sys.argv[2])
elif len(sys.argv) == 2: 
    
    if sys.argv[1].lower() == 'list': # if word is list:
        # try clause in case you want to use the book copy version (not actually doing anything in this scenario)
        try:
            # pyperclip.copy(str(list(mcbShelf.keys()))) # copy all words that have definitions to keyboard
            print(str(list(mcbShelf.keys()))) # don't think there's any need to copy this to clipboard
        except ImportError:
            print("No words. Please run python3 mcb.pyw save <word> with the definition in your buffer\n")
    elif sys.argv[1] in mcbShelf: # if the argument passed is a word that has a definition
        print(f"{mcbShelf[sys.argv[1]]} copied to clipboard!")
        pyperclip.copy(mcbShelf[sys.argv[1]]) # copy the word and definition to keyboard
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()

# delete <word> and delete all keywords
# merzbow    

mcbShelf.close() #close shelf
