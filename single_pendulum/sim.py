import pygame
import numpy as np
import time

pygame.init()

WIDTH, HEIGHT = 300, 300
window = pygame.display.set_mode((WIDTH,HEIGHT))
originan_x,originan_y =  WIDTH/2,HEIGHT/2

# data
m = 1
length = 120
g = 981
theta_0inr= np.pi/10
w0 = np.sqrt((5*g)/(2*length))
gamma = 0.01
patience = 1
w = np.sqrt(abs(w0**2-(gamma/2)**2))

def blip(window,x,y):
    image = pygame.image.load("bitmap.png")
    window.blit(image, (x,y))
def movement(t):
    global x
    global y
    if gamma/2<w0:
        theta =theta_0inr*np.exp(-gamma*t*0.5)*np.cos(w*t)

    elif gamma/2>w0:
        theta = theta_0inr*np.exp(-gamma*t*0.5)*(2*np.sinh(w*t))
    else:
        theta = theta_0inr*np.exp(-gamma*t*0.5)
    x= originan_y-10+length*np.sin(theta)
    y= originan_x-10+length*np.cos(theta)

    return x,y
t = 0
a = time.perf_counter()
def mainloop(window):
    global t
    run = True
    clock = pygame.time.Clock()
    fps = 120
    c = 0
    while run:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run= False
                break
        clock.tick(fps)
        window.fill("#ffffff")
        if c<1*120:
            x,y = movement(0)
            t = time.perf_counter()
            
        else:
            x,y = movement((time.perf_counter()-t)*patience)
        blip(window,x,y)
        pygame.draw.line(window,color="#222222",start_pos=(originan_x,originan_y),end_pos=(x+10,y+10))
        c+=1
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    mainloop(window)
