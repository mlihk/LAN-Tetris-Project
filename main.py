import pygame
import sys
import random
from pygame.locals import *
from _thread import *
import time
import numpy
import socket
from Network import Network

pygame.font.init()
pygame.mixer.init()

# defining the pixel (set as 1920 x 1080 cause of my resolution, adjustable by changing the values below, screen_width is the horizontal pixels and screen_height is vertical pixels
screen_width = 1920
screen_height = 1080

clientNumber = 0


play_width = 300  # excatly half as height to get perfect squares
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30

# menu back ground image
background_image = pygame.image.load(r"D:\Tetris\venv\bg8.jpg")
background_image_2 = pygame.image.load(r"D:\Tetris\venv\bg7withtitle.jpg")

mainmenu_backgroundimage =  pygame.image.load(r"D:\Tetris\venv\bg10.jpg")

#Game play back ground image
gameplay_background_image = pygame.image.load(r"D:\Tetris\venv\bg6.jpg")


top_left_x = (screen_width - play_width) // 2
top_left_y = screen_height - play_height

# 7 types of shape, using a "gird" with 5 by 5 to create a shape within, where 0 means a block is occupying within
# Each shape has included their alternative appearnace, "90,180,270 differences"
# starting with their standard appeareance then turned with 90 degrees

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T] #Ease of indexing certain shape using list/numbers

# same idea of ease of indexing.
shape_colors = [(102, 204, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (0, 0, 204), (255, 128, 0), (128, 0, 128)]


# index 0 - 6 represent shape

class Piece(object):
    pass


def create_grid(locked_positions={}):
    pass


def convert_shape_format(shape):
    pass


def valid_space(shape, grid):
    pass


def check_lost(positions):
    pass

def check_win(score):
    pass

def get_shape():
    pass


def draw_text_middle(text, size, color, surface):
    pass


def draw_grid(surface, row, col):
    pass


def clear_rows(grid, locked):
    pass

def draw_next_shape(shape, surface):
    pass

def draw_window(surface):
    pass

def draw_windowmultiplayer(surface):
    pass

def main():
    pass


def main_menu():
    pass

def play_menu():
    pass

class user():
    def details(self, username, password):
        self.username = username


class Piece(object):
    rows = 20  # y
    columns = 10  # x

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)] #as used in the list mention above
        self.rotation = 0  # number from 0-3, when turning blocks using arrow keys, we add 1 to this value to get a different block shape


def create_grid(locked_positions={}): #creating a dictionary called locked_positions
    grid = [[(0,0,0) for i in range(10)] for i in range(20)] # we are creating a list for every single row in the "grid", hence 20! and a list for the colors as we have 10 "small boxes" in each row

    for i in range(len(grid)): #loops 20 times as we have 20 rows in a grid
        for j in range(len(grid[i])):
            if (j,i) in locked_positions: #rows are i and each row has 10 column (i)
                c = locked_positions[(j,i)]
                grid[i][j] = c
    return grid


def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)] #using modulus and some maths getting the different shape rotations of a shape

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions


def valid_space(shape, grid):
    accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
    accepted_positions = [j for sub in accepted_positions for j in sub]
    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False

    return True


def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False

def check_win(score):
    if score >= int(300):
        return True
    else:
        return False

def get_shape():
    global shapes, shape_colors

    return Piece(5, 0, random.choice(shapes)) # picking a random peice in the shape list set above and return it, 5 is located at the middle of the grid


def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont('bitstreamverasans', size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (top_left_x + play_width/2 - (label.get_width() / 2), top_left_y + play_height/2 - label.get_height()/2)) #You will get the middle of the screen

def draw_text(text, size, color, surface, x, y):
    font = pygame.font.SysFont('bitstreamverasans', size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (x, y))



def draw_grid(surface, row, col): #drawing the grid for the gameplay
    sx = top_left_x
    sy = top_left_y
    for i in range(row): #there are 20 rows as y number
        pygame.draw.line(surface, (128,128,128), (sx, sy+ i*30), (sx + play_width, sy + i * 30))  # horizontal lines, starting from the top left of the grid to the top
        for j in range(col): #there are 10 column in each row
            pygame.draw.line(surface, (128,128,128), (sx + j * 30, sy), (sx + j * 30, sy + play_height))  # vertical lines




def clear_rows(grid, locked):
    inc = 0
    for i in range(len(grid)-1,-1,-1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            # add positions to remove from locked
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)
    return inc



def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, (255,255,255))

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j*30, sy + i*30, 30, 30), 0)

    surface.blit(label, (sx + 10, sy- 30))

def draw_window(surface, grid, score=0):
    surface.fill((0,0,0))
    win.fill((0, 0, 0))
    win.blit(gameplay_background_image, (0, 0))  # Background image for actualy gameplay

    font = pygame.font.SysFont('comicsans', 100)
    label = font.render('your Score: '+ str(score), 1, (255,255,255))

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100

    surface.blit(label, (sx - 1000, sy - 30))

    for i in range(len(grid)): #There are 20 rows in a grid so the len will be 20
        for j in range(len(grid[i])): #10 colum in each rows
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j* 30, top_left_y + i * 30, 30, 30), 0) # drawing a grid onto the "surface" window now, which will be poisition in the middle bottom, and 30 is the block size in pixels

    draw_grid(surface, 20, 10) # calling the draw_grid function to draw 20 rows and 10 columns each555555555555555555555
    pygame.draw.rect(surface, (255, 255, 255), (top_left_x, top_left_y, play_width, play_height), 2) #white frame around the border, border size of 2, cause it looks nicer

def draw_timedwindow(surface, grid, seconds, score=0):
    surface.fill((0,0,0))
    win.fill((0, 0, 0))
    win.blit(gameplay_background_image, (0, 0))  # Background image for actualy gameplay

    font = pygame.font.SysFont('comicsans', 100)
    font2 = pygame.font.SysFont('comicsans', 100)
    label = font.render('your Score: '+ str(score), 1, (255,255,255))
    label2 = font2.render('Time Used: '+ str(seconds), 1, (0,0,0))

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100

    surface.blit(label, (sx - 1000, sy - 30))
    surface.blit(label2, (sx - 100, sy - 350))

    for i in range(len(grid)): #There are 20 rows in a grid so the len will be 20
        for j in range(len(grid[i])): #10 colum in each rows
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j* 30, top_left_y + i * 30, 30, 30), 0) # drawing a grid onto the "surface" window now, which will be poisition in the middle bottom, and 30 is the block size in pixels

    draw_grid(surface, 20, 10) # calling the draw_grid function to draw 20 rows and 10 columns each555555555555555555555
    pygame.draw.rect(surface, (255, 255, 255), (top_left_x, top_left_y, play_width, play_height), 2) #white frame around the border, border size of 2, cause it looks nicer

def draw_windowmultiplayer(surface, grid, score=0, score2=0):
    surface.fill((0,0,0))
    win.fill((0, 0, 0))
    win.blit(gameplay_background_image, (0, 0))  # Background image for actualy gameplay

    font = pygame.font.SysFont('comicsans', 100)
    label = font.render('your Score: '+ str(score), 1, (255,255,255))
    label2 = font.render('Opponent Score: '+ str(score2), 1, (255,255,255))

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100

    surface.blit(label, (sx - 1000, sy - 30))
    surface.blit(label2, (sx - 1000, sy - 400))

    for i in range(len(grid)): #There are 20 rows in a grid so the len will be 20
        for j in range(len(grid[i])): #10 colum in each rows
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j* 30, top_left_y + i * 30, 30, 30), 0) # drawing a grid onto the "surface" window now, which will be poisition in the middle bottom, and 30 is the block size in pixels

    draw_grid(surface, 20, 10) # calling the draw_grid function to draw 20 rows and 10 columns each555555555555555555555
    pygame.draw.rect(surface, (255, 255, 255), (top_left_x, top_left_y, play_width, play_height), 2) #white frame around the border, border size of 2, cause it looks nicer


def main():
    global grid

    locked_positions = {}  #dicitionary set above
    grid = create_grid(locked_positions)

    change_piece = False
    run = True # works with the while loop
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27
    score = 0

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()


        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get(): #Control quitting the game
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN: # Control the movements when a key is being pressed
                if event.key == pygame.K_LEFT: # when the left key is being pressed
                    current_piece.x -= 1 #from getshape function, which returns a random shape chosen form the list of shapes, then move it's x value which is the x coords by 1, because it's negative it moves it to the left
                    if not valid_space(current_piece, grid): #to prevent the block from moving outside the grid, we check using valid space function, when it is not reaching the requirement( eg no space) then it will counter the action
                        current_piece.x += 1
                elif event.key == pygame.K_RIGHT: # when the right key is being pressed
                    current_piece.x += 1 # same idea but adding value to x coords makes it goes right by 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_UP: # when the up key is being pressed
                    current_piece.rotation += 1 #as set early above, rotation is default 0, which corresponds the index of the list of shapes and now we add it by 1 it rotates it towards the next index within the list of a shape
                    if not valid_space(current_piece, grid):
                        current_piece.rotation -= 1
                if event.key == pygame.K_DOWN: #when the down key is being pressed
                    current_piece.y += 1 # adds the y coords by 1, kinda did it in the inverse way which we start from 0 at the top and higher y value at the bottom
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1

                #Terminates the program in game with ESC
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

                if event.key == pygame.K_SPACE: #drop instantly
                    while valid_space(current_piece, grid):
                        current_piece.y +=1
                    current_piece.y -=1

        shape_pos = convert_shape_format(current_piece)

        # add piece to the grid for drawing
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        # Function when the piece hits the bottom level it can reach and therefore locking it into the "gird" frame
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False

            # call four times to check for multiple clear rows
            score += clear_rows(grid, locked_positions) * 10

        draw_window(win, grid, score)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        # Check if user lost
        if check_lost(locked_positions):
            run = False
            draw_text_middle("You Lost", 40, (255, 255, 255), win)
            pygame.display.update()
            pygame.time.delay(2000)

        if check_win(score):
            run = False
            draw_text_middle("You've won!", 40, (255, 255, 255), win)
            pygame.display.update()
            pygame.time.delay(2000)


def timedmain():
    global grid

    locked_positions = {}  #dicitionary set above
    grid = create_grid(locked_positions)

    change_piece = False
    run = True # works with the while loop
    countdownloop = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27
    score = 0
    count_down = pygame.time.get_ticks()
    t = 0


    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()
        t = t + 1
        print(t)
        seconds = numpy.trunc(t / 71.2)

        if t == 12816:
            run = False
            draw_text_middle("Your Score:" + str(score), 40, (255, 255, 255), win)
            pygame.display.update()
            pygame.time.delay(2000)


        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get(): #Control quitting the game
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN: # Control the movements when a key is being pressed
                if event.key == pygame.K_LEFT: # when the left key is being pressed
                    current_piece.x -= 1 #from getshape function, which returns a random shape chosen form the list of shapes, then move it's x value which is the x coords by 1, because it's negative it moves it to the left
                    if not valid_space(current_piece, grid): #to prevent the block from moving outside the grid, we check using valid space function, when it is not reaching the requirement( eg no space) then it will counter the action
                        current_piece.x += 1
                elif event.key == pygame.K_RIGHT: # when the right key is being pressed
                    current_piece.x += 1 # same idea but adding value to x coords makes it goes right by 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_UP: # when the up key is being pressed
                    current_piece.rotation += 1 #as set early above, rotation is default 0, which corresponds the index of the list of shapes and now we add it by 1 it rotates it towards the next index within the list of a shape
                    if not valid_space(current_piece, grid):
                        current_piece.rotation -= 1
                if event.key == pygame.K_DOWN: #when the down key is being pressed
                    current_piece.y += 1 # adds the y coords by 1, kinda did it in the inverse way which we start from 0 at the top and higher y value at the bottom
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1

                #Terminates the program in game with ESC
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

                if event.key == pygame.K_SPACE: #drop instantly
                    while valid_space(current_piece, grid):
                        current_piece.y +=1
                    current_piece.y -=1

        shape_pos = convert_shape_format(current_piece)

        # add piece to the grid for drawing
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        # Function when the piece hits the bottom level it can reach and therefore locking it into the "gird" frame
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False

            # call four times to check for multiple clear rows
            score += clear_rows(grid, locked_positions) * 10
            data = str(score)


        draw_timedwindow(win, grid, seconds, score)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        if check_lost(locked_positions):
            run = False
            draw_text_middle("You Lost", 40, (255, 255, 255), win)
            pygame.display.update()
            pygame.time.delay(2000)


def multigame():
    n = Network()
    score = 0

    global grid

    locked_positions = {}  #dicitionary set above
    grid = create_grid(locked_positions)

    change_piece = False
    run = True # works with the while loop
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27

    while run:
        score2 = str(n.send(str(score)))
        print(score2)

        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()


        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get(): #Control quitting the game
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN: # Control the movements when a key is being pressed
                if event.key == pygame.K_LEFT: # when the left key is being pressed
                    current_piece.x -= 1 #from getshape function, which returns a random shape chosen form the list of shapes, then move it's x value which is the x coords by 1, because it's negative it moves it to the left
                    if not valid_space(current_piece, grid): #to prevent the block from moving outside the grid, we check using valid space function, when it is not reaching the requirement( eg no space) then it will counter the action
                        current_piece.x += 1
                elif event.key == pygame.K_RIGHT: # when the right key is being pressed
                    current_piece.x += 1 # same idea but adding value to x coords makes it goes right by 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_UP: # when the up key is being pressed
                    current_piece.rotation += 1 #as set early above, rotation is default 0, which corresponds the index of the list of shapes and now we add it by 1 it rotates it towards the next index within the list of a shape
                    if not valid_space(current_piece, grid):
                        current_piece.rotation -= 1
                if event.key == pygame.K_DOWN: #when the down key is being pressed
                    current_piece.y += 1 # adds the y coords by 1, kinda did it in the inverse way which we start from 0 at the top and higher y value at the bottom
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1

                #Terminates the program in game with ESC
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

                if event.key == pygame.K_SPACE: #drop instantly
                    while valid_space(current_piece, grid):
                        current_piece.y +=1
                    current_piece.y -=1

        shape_pos = convert_shape_format(current_piece)

        # add piece to the grid for drawing
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        # Function when the piece hits the bottom level it can reach and therefore locking it into the "gird" frame
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False

            # call four times to check for multiple clear rows
            score += clear_rows(grid, locked_positions) * 10
            n.send(str(score))


        draw_windowmultiplayer(win, grid, score, score2)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        if check_lost(locked_positions):
            run = False
            draw_text_middle("You Lost", 40, (255, 255, 255), win)
            pygame.display.update()
            pygame.time.delay(2000)

def multigame2():
    n = Network()
    score = 0

    global grid

    locked_positions = {}  #dicitionary set above
    grid = create_grid(locked_positions)

    change_piece = False
    run = True # works with the while loop
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27

    while run:
        score2 = str(n.send(str(score)))
        print(score2)

        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()


        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get(): #Control quitting the game
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN: # Control the movements when a key is being pressed
                if event.key == pygame.K_LEFT: # when the left key is being pressed
                    current_piece.x -= 1 #from getshape function, which returns a random shape chosen form the list of shapes, then move it's x value which is the x coords by 1, because it's negative it moves it to the left
                    if not valid_space(current_piece, grid): #to prevent the block from moving outside the grid, we check using valid space function, when it is not reaching the requirement( eg no space) then it will counter the action
                        current_piece.x += 1
                elif event.key == pygame.K_RIGHT: # when the right key is being pressed
                    current_piece.x += 1 # same idea but adding value to x coords makes it goes right by 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_UP: # when the up key is being pressed
                    current_piece.rotation += 1 #as set early above, rotation is default 0, which corresponds the index of the list of shapes and now we add it by 1 it rotates it towards the next index within the list of a shape
                    if not valid_space(current_piece, grid):
                        current_piece.rotation -= 1
                if event.key == pygame.K_DOWN: #when the down key is being pressed
                    current_piece.y += 1 # adds the y coords by 1, kinda did it in the inverse way which we start from 0 at the top and higher y value at the bottom
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1

                #Terminates the program in game with ESC
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

                if event.key == pygame.K_SPACE: #drop instantly
                    while valid_space(current_piece, grid):
                        current_piece.y +=1
                    current_piece.y -=1

        shape_pos = convert_shape_format(current_piece)

        # add piece to the grid for drawing
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        # Function when the piece hits the bottom level it can reach and therefore locking it into the "gird" frame
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False

            # call four times to check for multiple clear rows
            score += clear_rows(grid, locked_positions) * 10
            n.send(str(score))


        draw_windowmultiplayer(win, grid, score, score2)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        if check_lost(locked_positions):
            run = False
            draw_text_middle("You Lost", 40, (255, 255, 255), win)
            pygame.display.update()
            pygame.time.delay(2000)

        if score2 == "None":
            score2 = 0

        if int(score2) >= 300 and int(score) < 300:
            run = False
            draw_text_middle("You Lost", 40, (255, 255, 255), win)
            pygame.display.update()
            pygame.time.delay(2000)
        if int(score2) < 300 and int(score) >= 300:
            run = False
            draw_text_middle("You Win", 40, (255, 255, 255), win)
            pygame.display.update()
            pygame.time.delay(2000)


def main_menu():
    run = True
    while run:
        click = False

        mousex, mousey = pygame.mouse.get_pos() #set coord to the point where your mouse is at

        win.fill((0,0,0))
        win.blit(mainmenu_backgroundimage, (0, 0))

        button_1 = pygame.Rect(730, 700, 400, 100)
        button_2 = pygame.Rect(830, 900, 200, 50)
        pygame.draw.rect(win, (255, 255, 255), button_1)
        draw_text('Play', 100, (0, 0, 0), win, 850, 685)
        pygame.draw.rect(win, (255, 255, 255), button_2)
        draw_text('Quit', 50, (0, 0, 0), win, 880, 895)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_1.collidepoint((mousex, mousey)):
            if click:
                play_menu()
        if button_2.collidepoint((mousex, mousey)):
            if click:
                pygame.quit()

        pygame.display.update()
    pygame.quit()

def multi_menu():
    run = True
    while run:
        click = False

        mousex, mousey = pygame.mouse.get_pos() #set coord to the point where your mouse is at

        win.fill((0,0,0))
        win.blit(mainmenu_backgroundimage, (0, 0))

        button_1 = pygame.Rect(730, 400, 400, 100)
        button_2 = pygame.Rect(730, 650, 400, 100)
        pygame.draw.rect(win, (255, 255, 255), button_1)
        draw_text('Race to 300', 75, (0, 0, 0), win, 750, 405)
        pygame.draw.rect(win, (255, 255, 255), button_2)
        draw_text('Infinite', 75, (0, 0, 0), win, 830, 655)
        button_3 = pygame.Rect(830, 900, 200, 50)
        pygame.draw.rect(win, (255, 255, 255), button_3)
        draw_text('Quit', 50, (0, 0, 0), win, 880, 895)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_1.collidepoint((mousex, mousey)):
            if click:
                multigame2()
        if button_2.collidepoint((mousex, mousey)):
            if click:
                multigame()
        if button_3.collidepoint((mousex, mousey)):
            if click:
                quit()

        pygame.display.update()
    pygame.quit()


def play_menu():
    run = True
    while run:
        click = False

        mousex, mousey = pygame.mouse.get_pos() #set coord to the point where your mouse is at

        win.fill((0,0,0))
        win.blit(mainmenu_backgroundimage, (0, 0))

        button_1 = pygame.Rect(730, 400, 400, 100)
        button_2 = pygame.Rect(730, 650, 400, 100)
        pygame.draw.rect(win, (255, 255, 255), button_1)
        draw_text('SinglePlayer', 75, (0, 0, 0), win, 750, 405)
        pygame.draw.rect(win, (255, 255, 255), button_2)
        draw_text('Multiplayer', 75, (0, 0, 0), win, 750, 655)
        button_3 = pygame.Rect(830, 900, 200, 50)
        pygame.draw.rect(win, (255, 255, 255), button_3)
        draw_text('Quit', 50, (0, 0, 0), win, 880, 895)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_1.collidepoint((mousex, mousey)):
            if click:
                playsolo_menu()
        if button_2.collidepoint((mousex, mousey)):
            if click:
                multi_menu()
        if button_3.collidepoint((mousex, mousey)):
            if click:
                quit()

        pygame.display.update()
    pygame.quit()

def playsolo_menu():
    run = True
    while run:
        click = False

        mousex, mousey = pygame.mouse.get_pos() #set coord to the point where your mouse is at

        win.fill((0,0,0))
        win.blit(mainmenu_backgroundimage, (0, 0))

        button_1 = pygame.Rect(730, 400, 400, 100)
        button_2 = pygame.Rect(730, 650, 400, 100)
        pygame.draw.rect(win, (255, 255, 255), button_1)
        draw_text('Race to 300', 75, (0, 0, 0), win, 750, 405)
        pygame.draw.rect(win, (255, 255, 255), button_2)
        draw_text('Timed 3 Min', 75, (0, 0, 0), win, 750, 655)
        button_3 = pygame.Rect(830, 900, 200, 50)
        pygame.draw.rect(win, (255, 255, 255), button_3)
        draw_text('Quit', 50, (0, 0, 0), win, 880, 895)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_1.collidepoint((mousex, mousey)):
            if click:
                main()
        if button_2.collidepoint((mousex, mousey)):
            if click:
                timedmain()
        if button_3.collidepoint((mousex, mousey)):
            if click:
                quit()

        pygame.display.update()
    pygame.quit()


win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tetris')


main_menu()  # start the GAME!
