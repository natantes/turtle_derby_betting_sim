
from codecs import replace_errors
import turtle
import time
import random
import PySimpleGUI as sg
from venv import create

def game(amount = None):
    WIDTH, HEIGHT = 500, 500
    START_Y = -(HEIGHT // 2) + 20

    COLORS = ['red', 
    'green', 
    'blue', 
    'yellow', 
    'orange', 
    'black', 
    'purple', 
    'cyan', 
    'aquamarine', 
    'bisque', 
    'coral', 
    'DarkBlue', 
    'brown']



    # get user input
    def get_number_of_racers(amount = None):

        if not amount:
            amount = 1000
        init_output = 'Inital amonut: $' + str(amount)
        layout = [  [sg.Text('Input amount of racers (2 - 10)'), sg.InputText()], 
                    [sg.Button('Ok'), sg.Button('Cancel')] ]
        bet = [ [sg.Text(init_output)],
                [sg.Text('Which number turtle would you like to bet on'), sg.InputText()],
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
            bet_turtle = bet_turtle[0]
            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break

            if bet_turtle.isdigit():
                bet_turtle = int(bet_turtle)
            else:
                sg.popup('Invalid intput... submit a numerical value')
                continue

            if  not (1 <= bet_turtle <= racers):
                sg.popup('Bet on a turtle up to the range you choose')
                continue

            new_window.close()

            return racers, bet_turtle - 1, amount



    def init_turtle():
        screen = turtle.Screen()
        screen.setup(WIDTH, HEIGHT)
        screen.title('TURTLE DERBY')


    def race(bet_turtle):
        turtles = create_turtles(colors)

        while True:
            for racer in turtles:
                distance = random.randrange(2, 20)
                racer.forward(distance)

                x, y = racer.pos()
                if y >= HEIGHT // 2 - 20:
                    if bet_turtle == turtles.index(racer):
                        return True
                    else:
                        return False
        


    def create_turtles(colors):
        turtles = []
        spacing_x = WIDTH // (len(colors) + 1)
        for i, color in enumerate(colors):
            racer = turtle.Turtle()
            racer.color(color)
            racer.shape('turtle')
            racer.left(90)
            racer.penup()
            racer.setpos(-WIDTH//2 + (i + 1) * spacing_x, START_Y)
            racer.pendown()
            turtles.append(racer)
        return turtles

    get_number_of_racers = get_number_of_racers(amount)

    racers, bet_turtle, amount = get_number_of_racers[0], get_number_of_racers[1], get_number_of_racers[2]
    init_turtle()

    random.shuffle(COLORS)
    colors = COLORS[:racers]

    if race(bet_turtle):
        amount *= 2
        output = 'Current amount: $' + str(amount)
        sg.popup('Your turtle won!', output)
        turtle.Screen().clear()
        game(amount)
    else:
        amount //= 2
        output = 'Current amount: $' + str(amount)
        sg.popup('Your turtle lost :(', output)
        turtle.Screen().clear()
        game(amount)

game()
