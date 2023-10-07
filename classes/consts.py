import pygame

# GAME
WINDOW_SIZE = (640, 640)
FPS = 30

# FPS INTERFACE
FPS_TEXT_FONT = 'Lucida Sans Typewriter'
FPS_TEXT_SIZE = 20
FPS_TEXT_COLOR = (0, 0, 0)
FPS_LEFT_MARGIN = 5
FPS_TOP_MARGIN = 640

# TIME INTERFACE
TIME_TEXT_FONT = 'Lucida Sans Typewriter'
TIME_TEXT_SIZE = 20
TIME_TEXT_COLOR = (0, 0, 0)
TIME_LEFT_MARGIN = 5
TIME_TOP_MARGIN = 620

# PLAYER INFO INTERFACE
PLAYER_TEXT_FONT = 'Lucida Sans Typewriter'
PLAYER_TEXT_SIZE = 20
PLAYER_TEXT_COLOR = (0, 0, 0)
PLAYER_TOP_MARGIN = 5
PLAYER_1_LEFT_MARGIN = 5
PLAYER_2_LEFT_MARGIN = 450

# MENU
MENU_MUSIC = './assets/sounds/menu.mp3'
GAME_TITLE = 'PIRACY RUSH'
MENU_BACKGROUND = './assets/images/menu.png'
MENU_TEXT_FONT = 'Lucida Sans Typewriter'
MENU_SELECTED_TEXT_COLOR = (255, 255, 0)
MENU_TEXT_COLOR = (255, 255, 255)
MENU_OPTION_FONT_SIZE = 40
MENU_OPTION_SPACE_BETWEEN = 40
MENU_OPTIONS = ('NEW GAME 1P',
                'NEW GAME 2P - VERSUS',
                'NEW GAME 2P - COOPERATIVE',
                'HIGH SCORE',
                'EXIT')
MENU_OPTION_OFFSET = 100
MENU_TITLE_FONT_SIZE = 60
MENU_TITLE_OFFSET = 50

# FINAL SCORE
FINAL_SCORE_MUSIC = './assets/sounds/menu.mp3'
FINAL_BACKGROUND = './assets/images/menu.png'
FINAL_SCORE_TEXT_FONT = 'Lucida Sans Typewriter'
FINAL_SCORE_FONT_SIZE = 40
FINAL_SCORE_TEXT_COLOR = (255, 255, 255)
FINAL_SCORE_SELECTED_TEXT_COLOR = (255, 255, 0)
FINAL_SCORE_OFFSET = 140
FINAL_SCORE_SPACE_BETWEEN = 40
GAME_OVER_TEXT_COLOR = (255, 0, 0)
GAME_OVER_OFFSET = 60
GAME_OVER_FONT_SIZE = 60
FINAL_SCORE_OPTION_SPACE_BETWEEN = 40
FINAL_SCORE_OPTIONS = ('PLAY AGAIN',
                       'MENU',
                       'EXIT')
FINAL_SCORE_OPTION_OFFSET = 200

# LEVELS
LEVELS = {
    '1': {
        'CLASS': 'Level',
        'NAME': 'Level 1',
        'BACKGROUND_FILENAME': './assets/images/levels/1.png',
        'BACKGROUND_FPS': 30,
        'BACKGROUND_TOTAL_FRAMES': 64,
        'MUSIC': './assets/sounds/levels/1.mp3',
        'ENEMY_SPAWN_DELAY': 3000
    }
}

# PLAYERS
PLAYER_1 = {
    'CLASS': 'Player',
    'FILENAME': './assets/images/player_1.png',
    'POSITION': (5, WINDOW_SIZE[1]/2 + 150),
    'MOVEMENT_KEYS': [pygame.K_UP,
                      pygame.K_RIGHT,
                      pygame.K_DOWN,
                      pygame.K_LEFT
                      ],
    'SHOOT': {
        'CLASS': 'PlayerShoot',
        'FILENAME': './assets/images/cannon_shoot.png',
        'SPEED': 8.0,
        'DELAY': 1000,
        'KEY': pygame.K_RCTRL
    }
}

PLAYER_2 = {
    'CLASS': 'Player',
    'FILENAME': './assets/images/player_2.png',
    'POSITION': (5, WINDOW_SIZE[1]/2 + 250),
    'MOVEMENT_KEYS': [pygame.K_w,
                      pygame.K_d,
                      pygame.K_s,
                      pygame.K_a
                      ],
    'SHOOT': {
        'CLASS': 'PlayerShoot',
        'FILENAME': './assets/images/cannon_shoot.png',
        'SPEED': 8.0,
        'DELAY': 1000,
        'KEY': pygame.K_SPACE
    }
}

# PLAYER GENERAL
PLAYER_MAX_POSITIONS = (310, 630, 635, 0)
PLAYER_SPEED = 10
PLAYER_SHOOT_OFFSET = (20, 10)

# ENEMIES
ENEMY_1 = {
    'CLASS': 'Enemy',
    'FILENAME': './assets/images/enemy_1.png',
    'SPEED': 5.0,
    'SIZE': (64, 64),
    'SHOOT':   {
        'CLASS': 'EnemyShoot',
        'FILENAME': './assets/images/cannon_shoot.png',
        'SPEED': 8.0,
        'DELAY': 1000
    }
}

ENEMY_2 = {
    'CLASS': 'Enemy',
    'FILENAME': './assets/images/enemy_2.png',
    'SPEED': 5.0,
    'SIZE': (64, 58),
    'SHOOT':   {
        'CLASS': 'EnemyShoot',
        'FILENAME': './assets/images/cannon_shoot.png',
        'SPEED': 8.0,
        'DELAY': 2000
    }
}

# ENEMY GENERAL
ENEMY_SHOOT_OFFSET = (20, 10)

# EVENTS
NEW_NEMEY_EVENT = pygame.USEREVENT + 1
BACKGROUND_MOVE_EVENT = pygame.USEREVENT + 2
PLAYER_SHOOT_EVENT = pygame.USEREVENT + 3
ENEMY_SHOOT_EVENT = pygame.USEREVENT + 4
