import pygame
import random
import sys

pygame.init()

direccion_actual = "DERECHA"

snake = [
    (100, 100), 
    (80, 100),
    (60, 100),
]

# Tamaño de la ventana
WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake_IA")

# Colores
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Tamaño de cada bloque
BLOCK = 20

# Velocidad inicial
speed_x = BLOCK
speed_y = 0

clock = pygame.time.Clock()

food_x = random.randint(0, (WIDTH - BLOCK) // BLOCK) * BLOCK
food_y = random.randint(0, (HEIGHT - BLOCK) // BLOCK) * BLOCK


while True:

    # Eventos
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT and direccion_actual != "IZQUIERDA":
                direccion_actual = "DERECHA"
                speed_x = BLOCK
                speed_y = 0
            elif event.key == pygame.K_LEFT and direccion_actual != "DERECHA":
                direccion_actual = "IZQUIERDA"
                speed_x = -BLOCK
                speed_y = 0
            elif event.key == pygame.K_UP and direccion_actual != "ABAJO":
                direccion_actual = "ARRIBA"
                speed_x = 0 
                speed_y = -BLOCK
            elif event.key == pygame.K_DOWN and direccion_actual != "ARRIBA":
                direccion_actual = "ABAJO"
                speed_x = 0 
                speed_y = BLOCK
                
    # Mover la serpiente
    head_x, head_y = snake[0]
    
    new_head =(head_x + speed_x, head_y + speed_y) 
    snake.insert(0, new_head)
    
    if new_head[0] == food_x and new_head[1] == food_y:
        
        while True: 
           food_x = random.randint(1, (WIDTH - BLOCK)// BLOCK - 2) * BLOCK
           food_y = random.randint(1, (HEIGHT - BLOCK)// BLOCK - 2) * BLOCK
           
           if (food_x, food_y) not in snake: 
            break
    
    else:
        snake.pop()
        
    if new_head in snake[1:]:
        pygame.quit()
        sys.exit()
        
    # Si toca un borde termina el juego
    if (
        new_head[0] < 0 or
        new_head[0] >= WIDTH or
        new_head[1] < 0 or
        new_head[1] >= HEIGHT
    ):
        pygame.quit()
        sys.exit()

    # Dibujar
    screen.fill(BLACK)

    # Marco verde
    pygame.draw.rect(screen, GREEN, (0, 0, WIDTH, HEIGHT), 5)
    
    pygame.draw.rect(screen, (255, 0, 0), (food_x, food_y, BLOCK, BLOCK))

    # Cabeza de la serpiente
    for segmento in snake:
        pygame.draw.rect(screen, GREEN, (segmento[0], segmento[1], BLOCK, BLOCK))

    pygame.display.update()

    # Controlar FPS
    clock.tick(10)