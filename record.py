import pygame as pg
import copy
from board import boards
from board import bc

# ver code
ver = '0.1'

# pygame initial

pg.init()

## properties
# const

WIDTH = 760
HEIGHT = 800
FPS = 60
W = 'white'
B = 'black'

# files

screen = pg.display.set_mode((WIDTH, HEIGHT))
timer = pg.time.Clock()
font40 = pg.font.Font('font.ttc', 40)
font20 = pg.font.Font('font.ttc', 20)
font10 = pg.font.Font('font.ttc', 10)
table = copy.deepcopy(boards)
ts = copy.deepcopy(bc) # table situation

# images
b_piece = pg.transform.scale(pg.image.load(f'textures/black_piece.png'), (32, 32))
w_piece = pg.transform.scale(pg.image.load(f'textures/white_piece.png'), (32, 32))
table_image = pg.transform.scale(pg.image.load(f'textures/table.png'), (WIDTH, WIDTH))
cover_image = pg.transform.scale(pg.image.load(f'textures/cover.png'), (WIDTH, HEIGHT))
icon = pg.image.load(f'textures/go_piece.ico')

# decorations

pg.display.set_caption(f"囲碁紀錄 Ver {ver}")
pg.display.set_icon(icon)

## functions
# draw board
def draw_board(tabs):
    K = 40
    for i in range(len(boards)):
        for j in range(len(boards[i])):
            if boards[i][j] == 0: # normal point
                pg.draw.line(screen, B, (K * j + K / 2 , K * i), (K * j + K / 2, K * (i +1)), 2)
                pg.draw.line(screen, B, (K * j, K * i + K / 2), (K * (j + 1), K * i + K / 2), 2)
            if boards[i][j] == 1: # star point 
                pg.draw.line(screen, B, (K * j + K / 2 , K * i), (K * j + K / 2, K * (i +1)), 2)
                pg.draw.line(screen, B, (K * j, K * i + K / 2), (K * (j + 1), K * i + K / 2), 2)
                pg.draw.circle(screen, B, (K * j + K / 2 + 1, K * i + K / 2 + 1), 6, 0) # +1 to make slight fix
            if boards[i][j] == 2: # top
                pg.draw.line(screen, B, (K * j, K * i + K / 2), (K * (j + 1), K * i + K / 2), 2)
                pg.draw.line(screen, B, ((K * j + K / 2, K * i + K / 2)), ((K * j + K / 2, K * i + K)), 2)
            if boards[i][j] == 3: # bottom
                pg.draw.line(screen, B, (K * j, K * i + K / 2), (K * (j + 1), K * i + K / 2), 2)
                pg.draw.line(screen, B, ((K * j + K / 2, K * i + K / 2)), ((K * j + K / 2, K * i)), 2)
            if boards[i][j] == 4: # left
                pg.draw.line(screen, B, (K * j + K / 2, K * i + K / 2), (K * (j + 1), K * i + K / 2), 2)
                pg.draw.line(screen, B, ((K * j + K / 2, K * i)), ((K * j + K / 2, K * (i + 1))), 2)
            if boards[i][j] == 5: # right
                pg.draw.line(screen, B, (K * j + K / 2, K * i + K / 2), (K * j, K * i + K / 2), 2)
                pg.draw.line(screen, B, ((K * j + K / 2, K * i)), ((K * j + K / 2, K * (i + 1))), 2)
            if boards[i][j] == 6: # top left
                pg.draw.line(screen, B, (K * j + K / 2, K * i + K / 2), (K * j + K, K * i + K / 2), 2)
                pg.draw.line(screen, B, (K * j + K / 2, K * i + K / 2), (K * j + K / 2, K * i + K), 2)
            if boards[i][j] == 7: # top right
                pg.draw.line(screen, B, (K * j + K / 2, K * i + K / 2), (K * j, K * i + K / 2), 2)
                pg.draw.line(screen, B, (K * j + K / 2, K * i + K / 2), (K * j + K / 2, K * i + K), 2)
            if boards[i][j] == 8: # down left
                pg.draw.line(screen, B, (K * j + K / 2, K * i + K / 2), (K * j + K, K * i + K / 2), 2)
                pg.draw.line(screen, B, (K * j + K / 2, K * i + K / 2), (K * j + K / 2, K * i), 2)
            if boards[i][j] == 9: # down right
                pg.draw.line(screen, B, (K * j + K / 2, K * i + K / 2), (K * j, K * i + K / 2), 2)
                pg.draw.line(screen, B, (K * j + K / 2, K * i + K / 2), (K * j + K / 2, K * i), 2)

    for i in range(len(tabs)):
            for j in range(len(tabs)):
                if tabs[i][j] == 'B':
                    screen.blit(b_piece, (K * j + 4 , K * i + 4))
                if tabs[i][j] == 'W':
                    screen.blit(w_piece, (K * j + 4 , K * i + 4))        

def check_board(tabs, f, bp, wp, tp, x, y):
    K = 40
    done = 0

    if done != 1:
        for i in range(len(tabs)):
                if done != 1:
                    for j in range(len(tabs[i])):
                            if tabs[i][j] == 'N' and (K * j + 5 <= x <= K * (j + 1) - 5) and (K * i + 5 <= y <= K * (i + 1) - 5) and done != 1:
                                if f == 0:
                                    bp += 1
                                    tp += 1
                                    f = 1
                                    tabs[i][j] = 'B'
                                    num = font10.render(f'{tp}', True, W)
                                    m = j
                                    n = i
                                    return bp, wp, tp, f, num, m, n

                                elif f == 1:
                                    wp += 1
                                    tp += 1
                                    f = 0
                                    tabs[i][j] = 'W'
                                    num = font10.render(f'{tp}', True, B)
                                    m = j
                                    n = i
                                    return bp, wp, tp, f, num, m, n
                                done = 1
                                break
                            else: # if not on the point then return null
                                num = -1
                                m = -1
                                n = -1
                                
    return bp, wp, tp, f, num, m, n

def get_mouse_posi():
    mx = pg.mouse.get_pos()[0]
    my = pg.mouse.get_pos()[1]
    return mx, my
## pages
# setting room
setting_room = True

# main running functions
running = False

def setting(table, set, run):
    op = 0
    first = 0

    title = font40.render(f"囲碁紀錄 Ver {ver}", True, B)
    ptr = font20.render(">>>", True, 'red')
    op0 = font20.render("開始記錄", True, B)
    op1 = font20.render("先手:黑", True, B)
        

    while set:
        timer.tick(FPS)
        screen.fill(B)
        screen.blit(cover_image, (0, 0))
        # option limit
        if op > 1:
            op = 1
        if op < 0:
            op = 0
        # first draw limit
        if first > 1:
            first = 1
        if first < 0:
            first = 0
        # first draw setting
        
        if first == 0:
            op1 = font20.render("先手:黑", True, B)
            pg.draw.circle(screen, B, (450, 460), 15)
        elif first == 1:
            op1 = font20.render("先手:白", True, B)
            pg.draw.circle(screen, W, (450, 460), 15)
        # setting room display
        screen.blit(title, title.get_rect(center = (WIDTH / 2, 380)))
        screen.blit(op0, op0.get_rect(center = (WIDTH / 2, 420)))
        screen.blit(op1, op1.get_rect(center = (WIDTH / 2, 460)))
        # option choose
        if op == 0:
            screen.blit(ptr, ptr.get_rect(center = ((WIDTH - 130) / 2, 420)))
        if op == 1:
            screen.blit(ptr, ptr.get_rect(center = ((WIDTH - 130) / 2, 460)))
        # KEY EVENTS
        for event in pg.event.get():
            if event.type == pg.QUIT:
                set = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    op -= 1 
                if event.key == pg.K_DOWN:
                    op += 1
                if event.key == pg.K_RETURN and op == 0:
                    set = False
                    run = True
                    main(table, set, run, first)
                if event.key == pg.K_LEFT and op == 1:
                    first -= 1
                if event.key == pg.K_RIGHT and op == 1:
                    first += 1
        
        pg.display.update()

def main(table, set, run, f):
    K = 40
    # black
    b_eaten = 0
    b_placed = 0
    # white
    w_eaten = 0
    w_placed = 0
    # total
    total_placed = 0
    tp_num = [[], [], []] # order num, x, y (use append to joint the elements)
    while run:
        timer.tick(FPS)

        total = font20.render(f"總下子數 = {total_placed}", True, B)
        
        screen.fill(W)
        screen.blit(table_image, (0, 0))
        screen.blit(total, (10, 770))

        draw_board(table)

        for i in range(len(tp_num[0])):
            screen.blit(tp_num[0][i], tp_num[0][i].get_rect(center = (K * tp_num[1][i] + K / 2, K * tp_num[2][i] + K / 2)))
            

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False
                    set = True
                    table = copy.deepcopy(bc)
                    setting(table, set, run)
                if total_placed >= 1:
                    if event.key == pg.K_BACKSPACE:
                        table[tp_num[2][total_placed - 1]][tp_num[1][total_placed - 1]] = 'N' # bug is here = = # possible solution: print the num m n when placing, and print the tp_num before removing it 
                        tp_num[0].pop(-1)
                        tp_num[1].pop(-1)
                        tp_num[2].pop(-1)
                        total_placed -= 1
                        if f == 0:
                            f = 1
                        elif f == 1:
                            f = 0

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                m_x, m_y = get_mouse_posi()
                b_placed, w_placed, total_placed, f, num, m, n = check_board(table, f, b_placed, w_placed, total_placed, m_x, m_y) # check click and make move
                if not(num == -1 and m == -1 and n == -1): # check if out put from checking is NULL
                    tp_num[0].append(num)
                    tp_num[1].append(m)
                    tp_num[2].append(n)
        
        pg.display.update()
                    
# main      
setting(ts, setting_room, running)

pg.quit()

## 20230123
# made the start and running page
# made them two funcitons and local variables

## 20230124
# made the first draw option
# made draw board function
# made pieces able to be placed sequently

## 20230125
# made the backspace function to redraw (NOT DONE YET HAS Bug WITH MANY PIECES ) problem(print tp_num arrays to check)

## TO DO LIST
# choose which is the first one to draw (v)
# board function (v)
# made pieces able to be placed sequently(v)
# put number order on it (v)
# if get eaten, eaten point++ ()
# able to print out the picture ()