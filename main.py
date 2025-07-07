import pygame as pg
TILE_SIZE = 200
TILE_ROW = 3
TILE_COL = 3
TILE_GAP = 10
SCREEN_HEIGHT = ((TILE_SIZE*TILE_ROW)+((TILE_GAP*TILE_ROW)+TILE_GAP))
SCREEN_WIDTH = ((TILE_SIZE*TILE_COL)+((TILE_GAP*TILE_COL)+TILE_GAP))
GRID_NOTPLAYED = 0
GRID_PLAYED_X = 1
GRID_PLAYED_Y = 2
TILE_COLORS = [
    (230,230,230),
    (0,255,0),
    (0,0,255)
]

class Tile:
    def __init__(self,x,y,size,state):
        self.x = x
        self.y = y
        self.size = size
        self.state = state
    
    def get_location(self):
        return (
            self.x,
            self.y,
            self.size,
            self.size,
        )
    
    def get_tile_state(self):
        return (self.state)
    
    def set_tile_state(self,player):
        self.state = player

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
            pg.draw.rect(screen, TILE_COLORS[col.get_tile_state()], col.get_location())
            pg.display.flip()


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
    played_moves = []
    for row in game_board:
        played_row = []
        for col in row:
            tile_state = check_win_conditions(col.get_tile_state()) 
            played_row.append(tile_state)
        played_moves.append(played_row)
    return played_moves


pg.init()

current_turn = 1
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
running = True
grid = init_game_board()

while running:
    draw_game_board(grid)
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
            