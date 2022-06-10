def menu(choices):
    while True:

        choice_string = '/'.join(choices)
        s = input(f'Enter a choice ({choice_string}): ').strip()

        if s in choices:
            return s
        
        print(f'{s} is not a valid choice.')
