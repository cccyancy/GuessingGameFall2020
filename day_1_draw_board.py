import turtle
from time import sleep
import random


ms = turtle.Screen()
ms.setup(800, 800)
t1 = turtle.Turtle()
t1.ht()
t1.pu()
t1.speed(2)
t1.width('2')
index_1 = None
index_2 = None
card_1 = None
card_2 = None

deck = []
card_num = 0
user_name = None
t_write = turtle.Turtle()


ms.addshape('card_warning.gif')

moves = 0
matches = 0


    
#-- turle input

def user_input():
    user_inp = turtle.textinput('CS 5001 Memory', 'Your Name:')
    user_number = turtle.numinput('CS 5001 Memory', '# of Cards to Play:(8, 10, or 12)', minval = 8, maxval = 12)

    if user_number == 9:
        user_number = random.choice([8, 10])#Constant
        t1.goto(0, 100)
        t1.shape('card_warning.gif')
        t1.st()
        warning = t1.stamp()
        sleep(3)
        t1.ht()
        t1.clearstamp(warning)
    elif user_number == 11:
        user_number = random.choice([10, 12])#Constant
        t1.goto(0, 100)
        t1.shape('card_warning.gif')
        t1.st()
        warning = t1.stamp()
        sleep(3)
        t1.ht()
        t1.clearstamp(warning)


        
    return user_inp, user_number

#--- get cards info
def get_cards(x):
    x = x // 2
    cards_list = []
    cards_list_chosen = []
    with open('cardsname.txt', 'r') as cards:
        for i in cards:
            cards_list.append(i.strip())
    for i in range(int(x)):
        cards_list_chosen.append(cards_list[i])

    cards_list_chosen *= 2
    random.shuffle(cards_list_chosen)
        
    return cards_list_chosen


#-- leader board file
def get_leader():
    leader_all = []
    with open('leaderboards.txt', 'r') as leader:
        for i in leader:
            leader_all.append(i.strip().split(' '))

        
            
    return(sorted(leader_all, key = lambda x: int(x[0])))





#---draw board

def draw_board():
    t1.penup()
    t1.goto(-370, 340)
    t1.pendown()
    for i in range(4):
        if i % 2 == 0:
            t1.forward(450)
            t1.right(90)
        else:
            t1.forward(500)
            t1.right(90)

    t1.penup()

    t1.goto(-370, -180)
    t1.pendown()

    for i in range(4):
        if i % 2 == 0:
            t1.forward(450)
            t1.right(90)
        else:
            t1.forward(70)
            t1.right(90)
    
    t1.penup()
    t1.pencolor('blue')
    t1.goto(100, 340)
    t1.pendown()

    for i in range(4):
        if i % 2 == 0:
            t1.forward(250)
            t1.right(90)
        else:
            t1.forward(500)
            t1.right(90)
    t1.pu()
    t1.goto(120, 280)
    t1.write('Leaders:', font=("Verdana", 20, "normal"))
    t1.goto(150, 240)
    for i in range(len(get_leader())):
        t1.write(get_leader()[i][0] + ' : ' + get_leader()[i][1], font=("Verdana", 10, "normal"))
        
        t1.goto(150, 200 - 40 * i)


    t1.penup()
    t1.goto(200, -200)
    ms.addshape('quitbutton.gif')
    t1.shape('quitbutton.gif')
    t1.st()
    t1.stamp()
    t1.ht()


#--- display cards
def display_cards(cards):

    
    ms.addshape('card_back.gif')
    t1.shape('card_back.gif')

    if cards == 8:
        
        t1.goto(-295, 260)
        t1.st()
        t1.stamp()
        for i in range(3):
            t1.forward(100)
            t1.stamp()
        t1.ht()
        t1.goto(-295, 110)
        t1.st()
        t1.stamp()
        for i in range(3):
            t1.forward(100)
            t1.stamp()

            
    elif cards == 10:
        t1.goto(-295, 260)
        t1.st()
        t1.stamp()
        for i in range(3):
            t1.forward(100)
            t1.stamp()
        t1.ht()
        t1.goto(-295, 110)
        t1.st()
        t1.stamp()
        
        for i in range(3):
            t1.forward(100)
            t1.stamp()
            
        t1.ht()
        t1.goto(-295, -40)
        t1.st()
        t1.stamp()
    
        t1.forward(100)
        t1.stamp()
        t1.ht()
            
    elif cards == 12:
        t1.goto(-295, 260)
        t1.st()
        t1.stamp()
        for i in range(3):
            t1.forward(100)
            t1.stamp()
        t1.ht()
        t1.goto(-295, 110)
        t1.st()
        t1.stamp()
        
        for i in range(3):
            t1.forward(100)
            t1.stamp()
            
        t1.ht()
        t1.goto(-295, -40)
        t1.st()
        t1.stamp()
        for i in range(3):
            t1.forward(100)
            t1.stamp()
            t1.ht()
    


def status_msg():
    global moves, matches
    t_write.pu()
    t_write.ht()
    t_write.pencolor('black')
    t_write.goto(-355, -220)
    t_write.write('Status: {} moves, {} matches'.format(str(moves), str(matches)), font=("Verdana", 10, "normal"))


def get_click_display_image(x, y):
    global index_1, index_2, card_1, card_2, moves, matches, card_num, user_name, deck

    t1.speed(1)


    if int(x) in range(171, 225) and int(y) in range(-218, -185):
        t2 = turtle.Turtle()
        t2.ht()
        t2.pu()
        t2.goto(0, 100)
        ms.addshape('quitmsg.gif')
        t2.shape('quitmsg.gif')
        t2.st()
        t2.stamp()
        sleep(3)
        turtle.bye()
    
    if index_1 == None:
        if int(y) in range(190,330):
            index = round((int(x) + 295) / 100)
            index_1 = index         
        
        elif int(y) in range(40, 190):
            index = round(((int(x) + 295) / 100) + 4)
            index_1 = index

        elif int(y) in range(-110, 30):
            index = round(((int(x) + 295) /100) + 8)
            index_1 = index
      
        if index_1 in range(0, 4):
            t1.speed(0)
            t1.goto((index_1 * 100) - 295, 260)
            t1.shape(deck[index_1])
            t1.st()
            card_1 = t1.stamp()
            t1.ht()

        elif index_1 in range(4, 8):
            t1.speed(0)
            t1.goto(((index_1 - 4) * 100) - 295, 110)
            t1.shape(deck[index_1])
            t1.st()
            card_1 = t1.stamp()
            t1.ht()
        
        elif index_1 in range(8, 12):
        
            t1.speed(0)
            t1.goto(((index_1 - 8) * 100) - 295, -40)
            t1.shape(deck[index_1])
            t1.st()
            card_1 = t1.stamp()
            t1.ht()

    elif index_2 == None:
        if int(y) in range(190,330):
            index = round((int(x) + 295) / 100)
            index_2 = index
            
        
        elif int(y) in range(40, 190):
            index = round(((int(x) + 295) / 100) + 4)
            index_2 = index
            

        elif int(y) in range(-110, 30):
            index = round(((int(x) + 295) /100) + 8)
            index_2 = index
        
        if index_2 in range(0, 4):
            t1.speed(0)
            t1.goto((index_2 * 100) - 295, 260)
            t1.shape(deck[index_2])
            t1.st()
            card_2 = t1.stamp()
            t1.ht()
            print('card_2', card_2)

        elif index_2 in range(4, 8):
            t1.speed(0)
            t1.goto(((index_2 - 4) * 100) - 295, 110)
            t1.shape(deck[index_2])
            t1.st()
            card_2 = t1.stamp()
            t1.ht()
            print('card_2', card_2)

        elif index_2 in range(8, 12):
            t1.speed(0)
            t1.goto(((index_2 - 8) * 100) - 295, -40)
            t1.shape(deck[index_2])
            t1.st()
            card_2 = t1.stamp()
            t1.ht()
            print('card_2', card_2)

    if index_1 == index_2:
        print('do not click on same card twice, try again.')
        t1.clearstamp(card_1)
        t1.clearstamp(card_2)

        index_1 = None
        index_2 = None


    elif index_1 != None and index_2 != None:
        if deck[index_1] == deck[index_2]:
            print('match')
            print(index_1)
            print(index_2)
            matches += 1
            moves += 1
            t_write.clear()
            t_write.ht()
            t_write.pencolor('black')
            t_write.goto(-355, -220)
            t_write.write('Status: {} moves, {} matches'.format(str(moves), str(matches)),
                     font=("Verdana", 10, "normal"))
            print(card_num)

            if matches == (card_num//2):
                t3 = turtle.Turtle()
                t3.ht()
                t3.pu()
                t3.goto(0, 100)
                ms.addshape('winner.gif')
                t3.shape('winner.gif')
                t3.st()
                t3.stamp()
                sleep(3)

                

                with open('leaderboards.txt', 'a') as leader:
                    leader.write('\n')
                    leader.write('{} {}'.format(str(moves), user_name))
                
                turtle.bye()
                
            index_1 = None
            index_2 = None
           

        else:
            print('not match')
            print(index_1)
            print(index_2)
            print(card_1)
            print(card_2)

            sleep(2)

            t1.clearstamp(card_1)
            t1.clearstamp(card_2)
            
            moves += 1
            t_write.clear()
            t_write.ht()
            t_write.pencolor('black')
            t_write.goto(-355, -220)
            t_write.write('Status: {} moves, {} matches'.format(str(moves), str(matches)),
                     font=("Verdana", 10, "normal"))

            index_1 = None
            index_2 = None





def main():
    global deck, card_num, user_name
    
    user_name, card_num = user_input()
    deck = get_cards(card_num)
    for i in deck:
        ms.addshape(i)

    draw_board()
    display_cards(card_num)
    get_cards(card_num)

    status_msg()
    ms.onscreenclick(get_click_display_image)


    
    
  
    

if __name__=='__main__':
    main()


