import pygame
import sys

# Inicializa Pygame
pygame.init()

# Dimensiones de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('PyGoal')

# Colores
green = (0, 128, 0)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Fuentes
font = pygame.font.SysFont(None, 55)

# Elementos del juego
score = 0
time_left = 60  # 1 minuto
ball_pos = [width // 2, height - 50]
goalie_pos = [width // 2, 50]
goalie_speed = 5
ball_speed = 10
ball_in_play = False

# Funciones del juego
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def draw_game_elements():
    screen.fill(green)
    draw_text(f'Score: {score}', font, white, screen, 20, 20)
    draw_text(f'Time: {int(time_left)}', font, white, screen, width - 150, 20)
    pygame.draw.circle(screen, black, ball_pos, 15)
    pygame.draw.rect(screen, red, (goalie_pos[0] - 25, goalie_pos[1] - 25, 50, 50))
    pygame.draw.rect(screen, white, (width//2 - 50, 0, 100, 10))  # Marcar el arco
    pygame.display.flip()

# Bucle principal del juego
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not ball_in_play:
                ball_in_play = True

    # Mueve al arquero
    goalie_pos[0] += goalie_speed
    if goalie_pos[0] >= width - 25 or goalie_pos[0] <= 25:
        goalie_speed = -goalie_speed

    # Mueve la pelota si está en juego
    if ball_in_play:
        ball_pos[1] -= ball_speed

    # Detectar colisiones
    if ball_pos[1] <= 10 and (width // 2 - 50 <= ball_pos[0] <= width // 2 + 50):
        score += 1
        ball_pos = [width // 2, height - 50]
        ball_in_play = False
    elif ball_pos[1] <= 10 or (goalie_pos[0] - 25 <= ball_pos[0] <= goalie_pos[0] + 25 and 25 <= ball_pos[1] <= 75):
        ball_pos = [width // 2, height - 50]
        ball_in_play = False

    # Dibujar los elementos del juego
    draw_game_elements()

    # Control de tiempo
    time_left -= clock.tick(60) / 1000  # Decrementa el tiempo en segundos
    if time_left <= 0:
        running = False

pygame.quit()
sys.exit()