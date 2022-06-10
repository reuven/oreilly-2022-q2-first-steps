def menu(choices):
    while True:

        s = input('Enter a choice: ').strip()

        if s in choices:
            return s
        
        print(f'{s} is not a valid choice.')
