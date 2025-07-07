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