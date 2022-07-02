
import turtle
import random
import PySimpleGUI as sg

def game(amount = None):
    from get_number_of_r import get_number_of_racers
    from init import init_turtle

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

    racers, bet_turtle, amount, bet_amount = get_number_of_racers[0], get_number_of_racers[1], get_number_of_racers[2], get_number_of_racers[3]
    
    init_turtle()

    random.shuffle(COLORS)
    colors = COLORS[:racers]

    if race(bet_turtle):
        amount = bet_amount + (amount)
        output = 'Current amount: $' + str(amount)
        sg.popup('Your turtle won!', output)
        turtle.Screen().clear()
        game(amount)
    else:
        amount = -bet_amount + (amount)
        if amount == 0:
            output = 'Current amount: $' + str(amount)
            sg.popup('Your turtle lost :(', output, 'You do not have sufficient money to continue')
            turtle.Screen().clear()
        else:
            output = 'Current amount: $' + str(amount)
            sg.popup('Your turtle lost :(', output)
            turtle.Screen().clear()
            game(amount)

game()
