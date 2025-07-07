import pygame as pg
pg.init()
TILE_SIZE = 200
TILE_ROW = 3
TILE_COL = 3
TILE_GAP = 10
SCREEN_HEIGHT = ((TILE_SIZE*TILE_ROW)+((TILE_GAP*TILE_ROW)+TILE_GAP))
SCREEN_WIDTH = ((TILE_SIZE*TILE_COL)+((TILE_GAP*TILE_COL)+TILE_GAP))

tile_pos = []

for row in range(TILE_ROW):
    for col in range(TILE_COL):
        x1 = TILE_GAP + col * (TILE_SIZE + TILE_GAP)
        y1 = TILE_GAP + row * (TILE_SIZE + TILE_GAP)
        x2 = TILE_SIZE
        y2 = TILE_SIZE
        tile_pos.append((x1,y1,x2,y2))

print(tile_pos)
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

running = True

for tile in tile_pos:
    pg.draw.rect(screen, (230, 230, 230), tile)
    pg.display.flip()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 
        elif event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            column = pos[0] // (TILE_SIZE + TILE_GAP)
            row = pos[1] // (TILE_SIZE + TILE_GAP)
            pg.draw.rect(screen, (30, 30, 230), tile)
            print("Click ", pos, "Grid coordinates: ", row, column)