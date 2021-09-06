import random

from turtle import TK, TurtleScreen, Turtle, Shape, _Screen, ScrolledCanvas, _Root, Screen

import os

import math 

 

nrows = 4  # number of rows in grid

ncols = 4  # number of cols in grid

grid_width = 140  # grid element width/height

imgsPath = "/Users/ycxel/Desktop/NEU Fall 2020/5001/proj/gif"  # path containing gifs

 

grid_selection_1 = None  # first selection (row,col)  (0 relative)

grid_selection_2 = None  # second selection (row,col)  (0 relative)

 

show_images = list()  # list of images to show as { (row,col) } 

 

grid = None  # grid matrix to which matching grid id pairs are assigned

image_cnt = None  # number of gif images read from folder

 

t = None  # general turtle

t_fill = None # turtle for filling

 

#—————————————————————————————-

 

def on_click(x,y):

    # process mouse click

    # if in the score row, the mouse click is ignored

    # displays image of selected grid element

    # if 2nd selection, update according to whether match or not

    

    global score, show_images, grid_selection_1, grid_selection_2

    print ('x: ', x)

    print ('y: ', y)

    if y > nrows:

        # in score row

        return

    

    # convert logical units to grid (row,col)

    grid_x = int(math.floor(x))

    grid_y = int(math.floor(y))

 

    # display image in selected grid element

    display_image(grid_x,grid_y)

    drawGrid()

    

    # game behavior after selection

    if grid_selection_1 == None:  # if first selection

        grid_selection_1 = (grid_x, grid_y)

        return

    else:  # second selection

        grid_selection_2 = (grid_x, grid_y)

        if selections_match():

            score += score_inc

            show_images.append( grid_selection_1 )

            show_images.append( grid_selection_2 )

            redraw()

        else:

            redraw()

        grid_selection_1 = None


        
#—————————————————————————————-

 

def display_image(row,col):

    # displays image at grid elment (row,col) 

    t.penup()

    t.setpos(row+0.5,col+0.5)  # position at centre of grid element

    image_id = str(grid[row][col]) # get id of image

    t.shape(image_id)

    t.stamp()  # draw image

 

#—————————————————————————————-

 

def selections_match():

    # returns true if the selected images match

    return grid[grid_selection_1[0]][grid_selection_1[1]] == grid[grid_selection_2[0]][grid_selection_2[1]] 

 

#—————————————————————————————-

 

def restart_game():

    # restart the game

    # init vars, recompute image assignments and redraws window

    # only called once. could be called again at the end of each game.

    global score, show_images

    

    score = 0

    show_images = list()

    grid_selection_1 = None

    init_grid_image_assignments() 

    redraw()

    

#—————————————————————————————-

 

def redraw():

    # clears window and displays: background, visible images, grid, and score

    fill()

    for xy in show_images:

        display_image(xy[0],xy[1])

    drawGrid() 

    updateScore()

    

#—————————————————————————————-

 

class MyScreen(_Screen):

    # override _Screen to create a window with desired attributes:

    #    * window size as per globals canvas_size_x and canvas_size_y

    #    * canvas size the same as window size (no scroll bars)

    #    * logical coordinate system based on grid size rather than pixels

    # MyScreen -> _Screen -> TurtleScreen

    # _Screen contains functions for setting up the window => contains root, canvas, title. handles closing.

    

    _title = "Alex's Memory Game"

    # _root

    # _canvas

    

    def __init__(self):

        if _Screen._root is None:

            _Screen._root = self._root = _Root()

            self._root.title(MyScreen._title)

            self._root.ondestroy(self._destroy)

        if _Screen._canvas is None:

            self._root._canvas = ScrolledCanvas(self._root, canvas_size_x, canvas_size_y, canvas_size_x, canvas_size_y)

            self._root._canvas.pack(expand=1, fill="both")

            _Screen._canvas = self._root._getcanvas()

            TurtleScreen.__init__(self, _Screen._canvas)

            self.setworldcoordinates(0, 0, ncols, nrows+1)     # nrows+1 for score header

            self.onclick(on_click)

            

#—————————————————————————————-

 

def drawGrid():

    # draw grid lines

    

    # vert lines

    for i in range(0,ncols+1):

        t.penup()

        t.setpos(i,0)

        t.pendown()

        t.setpos(i,nrows)

    

    # horz lines

    for i in range(0,nrows+1):

        t.penup()

        t.setpos(0,i)

        t.pendown()

        t.setpos(ncols,i)

 

#—————————————————————————————-

 

def fill():

    # draw background colour

    t_fill.stamp()

 

#—————————————————————————————-

 

def loadImages():

    # loads images from the specified folder.

    # the images are added as shapes to the screen, identified by number in order loaded.

    # shapes are also available through any turtle.

    

    global image_cnt

    # reads all gifs in path and adds them to screen, named by number

    # img_count contains number of loaded images

    listing = os.listdir(imgsPath)

    image_counter = 0

    for fname in listing: 

        fullfname = os.path.join(imgsPath, fname)

        if os.path.isfile(os.path.join(imgsPath, fname)):

            ls=fname.rsplit(".", 1)

            if ls[1]=="gif":

                s=Shape("image", fullfname)

                screen.addshape(str(image_counter),s)

                image_counter += 1

    image_cnt = image_counter

 

#—————————————————————————————-

 

def updateScore():

    # print score in top row

    t.penup()

    t.setpos(0, 4.5)

    t.write("Score: " + str(score), font=("Arial", 20, "normal"))

 

#—————————————————————————————-

 

def init_grid_image_assignments():

    # As part of game initialisation, this function assigns images to grid squares.

    # Image id is assigned rather than actual image. 

    

    global grid, image_cnt

    # note: images are taken in sequence and added to boxes randomly.

    # ie, only (nrows*ncols / 2) images will be ever be used

    # To source images from a larger set, image selection could be random as well.

    remaining_boxes = range(0,nrows * ncols)

    box_to_grid_coords = list()

 

    # init grid

    grid = list()

    for row in range(0,nrows):

        grid.append(list(range(0,ncols)))

 

    # init box number to grid coords map

    for row in range(0,nrows):

        for col in range(0, ncols):

            box_to_grid_coords.append( (row,col) )

    

    # assign image ids to grid

    image_num = 0

    while len(remaining_boxes) > 0:

        # choose two grid squares at random

        box_image_1 = random.choice(remaining_boxes)

        remaining_boxes.remove(box_image_1)

        box_image_2 = random.choice(remaining_boxes)

        remaining_boxes.remove(box_image_2)

        

        # assign to the two grid squares the next image (image_num)

        for xy in [ box_to_grid_coords[box_image_1], box_to_grid_coords[box_image_2]  ]:

            x = xy[0]  # xy is a tuple (x, y)

            y = xy[1]

            grid[x][y] = image_num

        image_num += 1

        if image_num >= image_cnt:

            image_num = 0  # reset image num, meaning there may be more than one image pair

        

 


    

#—————————————————————————————- 

 

def debug_show_all_images():

    # only for debugging

    # draws all images in grid

    for row in range(0, nrows):

        for col in range(0, ncols):

            display_image(row, col)

 

# intialise globals

grid_size_x = grid_width * ncols

grid_size_y = grid_width * nrows

canvas_size_x = grid_size_x

canvas_size_y = grid_size_y + grid_width

score = 0

score_inc = 10

 

# create window

screen=MyScreen()

Turtle._screen = screen

loadImages()

 

# create general turtle

t = Turtle()

t.speed(0)

t.hideturtle()

t.penup()

 

# create fill turtle

t_fill = Turtle()

t_fill.speed(0)

t.hideturtle()

t_fill.fillcolor( 0.8, 0.8, 0.8 )  # background colour

t_fill.shape("square")

t_fill.shapesize(100,100)

 

# draw window

restart_game() 

 

TK.mainloop()
