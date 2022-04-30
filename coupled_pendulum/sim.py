import pygame
import numpy as np
import time
# pygame initialization
pygame.init()
WIDTH, HEIGHT = 500, 600
window = pygame.display.set_mode((WIDTH,HEIGHT))

# constants
originan_x,originan_y =  WIDTH/2,1000                                           # setting up origin
length = np.sqrt(originan_x**2+originan_y**2)                                   # 1030.7764064044
m, g, k, spring_len, gamma = 10, 10, 0.01, 50, 0.0005                   

# boundry conditions
x0 = 50                        # initial displacement at t=0

# i took here patience in 10**something. it's origianal freqency because it's too slow to see pendulum's behaviour
patience = 10
# at_eq = []
w1 = np.sqrt(abs((gamma/2)**2-g/length))
w2 = np.sqrt(abs((gamma/2)**2-(g/length+(2*k/m))))

Dw = (w2-w1)/2                  # differetiating term 
Mw = (w1+w2)/2                  # mean term

class ball:
    def __init__(self,window,image):
        self.window = window
        self.image = pygame.image.load(image)
    def draw(self,x,y):
        self.window.blit(self.image, (x,y))

ball_a = ball(window,"bitmap.png")
ball_b = ball(window, "bitmap2.png")

def positions(t):
    global x1, x2    
    x1= originan_x + (x0*np.exp(-gamma*t)*(np.sin(Mw*t)*np.sin(Dw*t)))
    x2= originan_x+spring_len + (x0*np.exp(-gamma*t)*(np.cos(Mw*t)*np.cos(Dw*t)))
    return x1,x2
def velocities(t):
    global v1, v2
    v1 = (x1-originan_x)*(-gamma+(Mw/np.tan(Mw*t))+(Dw/np.tan(Dw*t)))
    v2 = (x2-originan_x-spring_len)*(-gamma+(Mw*np.tan(Mw*t))+(Dw*np.tan(Dw*t)))
    return v1,v2

t = 0                          
a = time.perf_counter()                 # getting time
def mainloop(window):
    run = True
    global t
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
        pygame.draw.line(window,color="#000000",start_pos=(originan_x,HEIGHT/2-50),end_pos=(originan_x,HEIGHT/2+50))
        
        if c<1*120:             # Lag before starting simulation
            x1,x2 = positions(0)
            t = time.perf_counter()
        else:
            x1,x2 = positions((time.perf_counter()-t)*patience)
            v1,v2 = velocities((time.perf_counter()-t)*patience)
            # if v2< 0.5 and v2 > -0.5 and x2<(originan_x+spring_len+5) and x2>(originan_x+spring_len-5):
                # at_eq.append((np.pi*0.5)/(time.time()-t))
        pygame.draw.aaline(window,color="#6D398B",start_pos=(originan_x-spring_len-10,-originan_y),end_pos=(x1-spring_len-10,HEIGHT/2+10))
        pygame.draw.aaline(window,color="#6D398B",start_pos=(originan_x+spring_len+10,-originan_y),end_pos=(x2+10,HEIGHT/2+10))
        pygame.draw.line(window,color="#F19001",start_pos=(x1-spring_len-10,HEIGHT/2+10),end_pos=(x2+10,HEIGHT/2+10),width=5)
        ball_a.draw(x1-spring_len-20,HEIGHT/2)
        ball_b.draw(x2,HEIGHT/2)
        c+=1
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    mainloop(window)
