import pygame
import math
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pure Pursuit")
clock = pygame.time.Clock()
path = [(100, 300), (200, 200), (350, 250), (500, 150), (650, 200), (750, 300)]
running = True
car_x,car_y=100.0,300.0
speed=2.0
current_target=1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255)) 
    for p in path:
        pygame.draw.circle(screen,color="black",center=p,radius=5.0)
    for i in range(len(path)-1):
        pygame.draw.line(screen,color="black",start_pos=path[i],end_pos=path[i+1],width=2)
    
    pygame.draw.circle(screen,color="red",center=(car_x,car_y),radius=15.0)
    
    if current_target < len(path):
        hedef_x, hedef_y = path[current_target]
        angle = math.atan2(hedef_y - car_y, hedef_x - car_x)
        car_x += speed * math.cos(angle)
        car_y += speed * math.sin(angle)
        distance = math.sqrt((hedef_x - car_x)**2 + (hedef_y - car_y)**2)
        if distance < 10:
            current_target += 1
    pygame.display.flip()
    clock.tick(60)

pygame.quit()