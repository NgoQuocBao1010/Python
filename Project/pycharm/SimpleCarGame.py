Start = input('Do you want to start a simple car game?: ')

if Start.lower() == 'yes' or Start.lower() == 'absolutely':
    print('''
    >type 'Start' to trigger the car engine.
    >type 'Accelerate' to speed up the car
    >type 'Stop' to stop the car
    >type 'Quit' to stop the game
    ''')
    users_command = ''
    started = False
    accelerated = False
    maxspeed = False
    while True:
        users_command = input('> ').lower()
        if users_command == 'start':
            if started:
                print('The car is already started.')
            else:
                print('The engine is starting!!!!!!!')
                started = True
                accelerated = False
        elif users_command == 'accelerate':
            if accelerated :
                print('It is even going faster!!')
                #maxspeed = True
            elif not accelerated and started :
                print('The car is going too fast!')
                accelerated = True
            elif not started:
                print('The car has not started yet!')
        elif users_command == 'stop':
            if not started:
                print('This car is already stopped!')
            else:
                started = False
                accelerated = False
                print('The car stopped.')
        elif users_command == 'quit':
            print('Thanks for playing this game!')
            break
        elif users_command == 'help':
            print('''
    >type 'Start' to trigger the car engine.
    >type 'Accelerate' to speed up the car
    >type 'Stop' to stop the car
    >type 'Quit' to stop the game
                ''')
        else:
            print('Invalid Input. Please stick to the rule, this is just a SIMPLE car game.')
else:
    print('Plese come back again!')