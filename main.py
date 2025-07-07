from Tile import *
from constants import *
import pygame as pg

def init_game_board():
    grid = []
    for row in range(TILE_ROW):
        grid_row = []
        for col in range(TILE_COL):
            x = TILE_GAP + col * (TILE_SIZE + TILE_GAP)
            y = TILE_GAP + row * (TILE_SIZE + TILE_GAP)
            grid_col = Tile(x,y,TILE_SIZE,GRID_NOTPLAYED)
            grid_row.append(grid_col)
        grid.append(grid_row)
    return(grid)

def draw_game_board(board):
    for row in board:
        for col in row:
            player1_x1 = col.get_coordinate()
            y = col.get_coordinate()
            pg.draw.rect(screen, TILE_COLORS[col.get_tile_state()], col.get_location())
            get_player_symbol(col.get_tile_state(),col.get_coordinate())
    pg.display.flip()
def get_player_symbol(player,coord):
    match player:
        case 1:
            line1_x1 = coord[0] + TILE_GAP
            line1_y1 = coord[1] + TILE_GAP
            line1_x2 = coord[0] + (TILE_SIZE - TILE_GAP)
            line1_y2 = coord[1] + (TILE_SIZE - TILE_GAP)

            line2_x1 = coord[0] + (TILE_SIZE - TILE_GAP)
            line2_y1 = coord[1] + TILE_GAP
            line2_x2 = coord[0] + TILE_GAP
            line2_y2 = coord[1] + (TILE_SIZE - TILE_GAP)
            pg.draw.line(screen, (0,0,0),(line1_x1,line1_y1),(line1_x2,line1_y2),5)
            pg.draw.line(screen, (0,0,0),(line2_x1,line2_y1),(line2_x2,line2_y2),5)

        case 2:
            x = coord[0] + (TILE_SIZE / 2)
            y = coord[1] + (TILE_SIZE / 2)
            center = (x,y)
            radius = (TILE_SIZE / 2) - TILE_GAP
            pg.draw.circle(screen, (0,0,0), center, radius,5)
            print(center,radius)

def toggle_next_turn(current_turn):
    match current_turn:
        case 1:
            return 2
        case 2:
            return 1

def get_player_move(tile):
    match tile:
        case 0:
            return None
        case 1:
            return 1
        case 2:
            return 2


def check_win_conditions(game_board):
    winner = None
    played_moves = []
    for row in game_board:
        played_row = []
        for col in row:
            tile_state = get_player_move(col.get_tile_state())
            played_row.append(tile_state)
        played_moves.append(played_row)
    for row in range(3):
        if played_moves[row][0] is not None and played_moves[row][0] == played_moves[row][1] == played_moves[row][2]:
            print(f"Winner: Player {played_moves[row][0]}")
            return False
    for col in range(3):
        if played_moves[0][col] is not None and played_moves[0][col] == played_moves[1][col] == played_moves[2][col]:
            print(f"Winner: Player {played_moves[0][col]}")
            return False
    if played_moves[0][0] is not None and played_moves[0][0] == played_moves[1][1] == played_moves[2][2]:
            print(f"Winner: Player {played_moves[0][0]}")
            return False
    if played_moves[0][2] is not None and played_moves[0][2] == played_moves[1][1] == played_moves[2][0]:
            print(f"Winner: Player {played_moves[0][2]}")
            return False
    return True

pg.init()

current_turn = 1
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
running = True
grid = init_game_board()


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 
        elif event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            column = pos[0] // (TILE_SIZE + TILE_GAP)
            row = pos[1] // (TILE_SIZE + TILE_GAP)
            if grid[row][column].get_tile_state() == 0:
                grid[row][column].set_tile_state(current_turn)
                current_turn = toggle_next_turn(current_turn)
    draw_game_board(grid)
    running = check_win_conditions(grid)
    
                