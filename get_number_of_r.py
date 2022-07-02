import PySimpleGUI as sg

# get user input
def get_number_of_racers(amount = None):

    if not amount:
        amount = 1000
    init_output = 'Inital amonut: $' + str(amount)
    layout = [  [sg.Text('Input amount of racers (2 - 10):'), sg.InputText()], 
                [sg.Button('Ok'), sg.Button('Cancel')] ]
    bet = [ [sg.Text(init_output)],
            [sg.Text('Which number turtle would you like to bet on:'), sg.InputText()],
            [sg.Text('Bet amount:'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Setup your derby.', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, racers = window.read()
        racers = racers[0]
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break

        if racers.isdigit():
            racers = int(racers)
        else:
            sg.popup('Invalid intput... submit a numerical value')
            continue

        if not (2 <= racers <= 10):
            sg.popup('For the number of racers, please input a number between 2 and 10')
            continue
        break

    window.close()


    new_window = sg.Window('Bet on your turtle.', bet)

    while True:
        event, bet_turtle = new_window.read()
        bet_turtle, bet_amount = bet_turtle[0], bet_turtle[1]
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break

        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
        else:
            sg.popup('Invalid intput... submit a numerical value')
            continue    

        if bet_amount > amount:
            output = 'You do not have enough money to bet $' + str(amount)
            sg.popup(output)
            continue 

        if bet_turtle.isdigit():
            bet_turtle = int(bet_turtle)
        else:
            sg.popup('Invalid intput... submit a numerical value')
            continue

        if  not (1 <= bet_turtle <= racers):
            sg.popup('Bet on a turtle up to the range you choose')
            continue

        new_window.close()

        return racers, bet_turtle - 1, amount, bet_amount