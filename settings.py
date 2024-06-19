WIDTH = 540
HEIGHT = 720
RES = [WIDTH, HEIGHT]

CENTER = [WIDTH//2, HEIGHT//2]

BLUE = (135, 206, 235)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WALL_GREY = (34, 43, 47)
FLOOR_GREY = (58, 68, 72)

# (90, 100, 105)

PLAYER_CENTER = [WIDTH//2, 600]
PLAYER_COLORKEY = (48, 104, 80)

# constants = {
#     'player': {
#         'init_scale': 0.7
#     },
#     'coin':{
#         'dimension': 16,
#         'init_scale': 1.5
#     },
#     'torch':{
#         'dimension': 64,
#         'init_scale': 1
#     }
# }

class Constants:
    class Player:
        init_scale = 0.8
        x_pos = [int((1530 - PLAYER_CENTER[1]) / 7), 
                 WIDTH//2, 
                 WIDTH-int((1530 - PLAYER_CENTER[1]) / 7)]
    class Coin:
        dimension = 16
        init_scale = 1.5
    class Torch:
        dimension = 64