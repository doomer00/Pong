import math
import pygame as pyg
import random as rnd
import sys

#Globals
w, h = 858, 525
pad_w, pad_l = 15, 75
pad_speed = 0.5

def game_bot(paddle, ball, diff):
    
    speed = 0

    if paddle.y + pad_l / 2 < ball.y:
        speed = pad_speed * diff
    elif paddle.y + pad_l / 2 > ball.y:
        speed = -pad_speed * diff
    
    return speed

def main():

    #Setup    
    pyg.init()
    screen = pyg.display.set_mode((w, h))

    clock = pyg.time.Clock()
    run = 1
    scores = [0, 0]

    ball_pos = pyg.Vector2(w/2, rnd.uniform(h/4, 3*h/4))
    ball_speed = 1/2
    ball_w = 20

    pad1_pos = pyg.Vector2(20, h/2 - pad_l/2)
    pad2_pos = pyg.Vector2(w - 20 - pad_w, h/2 -  pad_l/2)
    pad_speed = 0.5

    dx, dy = rnd.uniform(-1, 1), rnd.uniform(1,-1)
    previous = ball_pos

    #run all function here
    while run:

        if scores[0] == 10 or scores[1] == 10:
            run = 0
            break

        keys = pyg.key.get_pressed()

        #Game control
        if keys[pyg.K_UP]:

            if pad2_pos.y - pad_speed <= 0:
                pad2_pos.y  += 0
            else:
                pad2_pos.y -= pad_speed
        
        elif keys[pyg.K_DOWN]:
        
            if pad2_pos.y + pad_speed + pad_l >= h:
                pad_speed += 0
            else:
                pad2_pos.y += pad_speed
                
        
        if keys[pyg.K_w]:
            
            if pad1_pos.y - pad_speed <= 0:
                pad1_pos.y += 0
            else:        
                pad1_pos.y -= pad_speed
        
        elif keys[pyg.K_s]:
            
            if pad1_pos.y + pad_speed + pad_l >= h:
                pad1_pos.y += 0
            else:
                pad1_pos.y += pad_speed 


        for event in pyg.event.get():
           
            if event.type == pyg.QUIT:
                run = 0
            elif event.type == pyg.KEYDOWN:
                if event.key == pyg.K_q:
                    pyg.quit()
                    sys.exit()
                elif event.key == pyg.K_r:
                    scores = [0, 0]
                    ball_pos.x, ball_pos.y = w/2, rnd.uniform(h/4, 3*h/4)
                    dx, dy = rnd.uniform(-1, 1), rnd.uniform(-1, 1)
                    pad1_pos.y, pad2_pos.y = h/2, h/2
                    continue
                
        screen.fill("black")

        for x in range(0, w, 30):
            pyg.draw.line(screen, "white", (w/2, x), (w/2, x + 25), 5)

        #Font 
        pyg.font.init()
        font = pyg.font.Font(size = 50)
    
        left_dp, right_dp= font.render(str(scores[0]), 0, "white"), font.render(str(scores[1]), 0, "white")
    
        text_w = max(left_dp.get_width(), right_dp.get_width())
        screen.blit(left_dp, (w/2 - text_w - 50, 30))
        screen.blit(right_dp, (w/2 + 50, 30))

        #draw ball
        pyg.draw.rect(screen, "white", (ball_pos.x - ball_w/2, ball_pos.y - ball_w/2, ball_w, ball_w)) 
        
        #draw pads
        pyg.draw.rect(screen, "white", (pad1_pos.x, pad1_pos.y, pad_w, pad_l)) 
        pyg.draw.rect(screen, "white", (pad2_pos.x, pad2_pos.y, pad_w, pad_l)) 
            
        #Game logic
        if ball_pos.x >= w:
            scores[0] += 1
            ball_pos.x, ball_pos.y = w/2, rnd.uniform(h/4, 3*h/4)
            dx, dy = rnd.uniform(-1, 1), rnd.uniform(-1, 1)
            ball_speed = 1/2
            continue
        
        elif ball_pos.x <= 0:
            scores[1] += 1
            ball_pos.x, ball_pos.y = w/2, rnd.uniform(h/4, 3*h/4)
            dx, dy = rnd.uniform(-1, 1), rnd.uniform(-1, 1)
            ball_speed = 1/2
            continue 
        
        #pad1_pos.y = simple_ai(pad1_pos, ball_pos, 1)
        if pad2_pos.y +     
        pad2_pos.y += game_bot(pad2_pos, ball_pos, 1/2)

        #When the ball hits the pads
        if ball_pos.x <= pad1_pos.x + pad_w:
            if pad1_pos.y <= ball_pos.y <= pad1_pos.y + pad_l:
                dx = 1
        elif ball_pos.x >= pad2_pos.x:
            if pad2_pos.y <= ball_pos.y <= pad2_pos.y + pad_l:
                dx = -1

        #When the ball hits the floor/ ceiling
        if ball_pos.y <= 0:
            dy = 1
        elif ball_pos.y + ball_w >= h:
            dy = -1

        ball_pos.x += dx * ball_speed
        ball_pos.y += dy * ball_speed

        pyg.display.flip() 
    
    pyg.quit()

if __name__ == "__main__":
    main()
