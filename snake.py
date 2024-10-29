import pygame as pg
import random

WIDTH, HEIGHT = 1280, 1280
WINDOW = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Snake")
ACTION = pg.event.custom_type()

#Sound Effects
pg.mixer.init()
chomp_sound = pg.mixer.Sound("chomp.mp3")
lose_sound = pg.mixer.Sound("lose.mp3")

FPS = 60


class Snake():

    def __init__(self):
        self.restart()
    
    def draw(self):
        head = True
        for tail_unit in self.tail_ls:
            if head:
                pg.draw.rect(WINDOW,"purple",([tail_unit[0]+1,tail_unit[1]+1],(62,62)))
                head = False
            else:
                pg.draw.rect(WINDOW,"green",([tail_unit[0]+1,tail_unit[1]+1],(62,62)))

    def move(self, vec):
        self.head_pos[0] +=vec[0]
        self.head_pos[1] +=vec[1]
        self.head_cords = change_px(self.head_pos)
        self.tail_ls.insert(0,self.head_cords)
        self.tail_ls.pop()

    def restart(self):
        self.head_pos = [10,10]
        self.head_cords = change_px(self.head_pos)
        self.tail_ls = [self.head_cords,add_vec2(self.head_cords,[0,1])]
        self.move_vec = [0,-1]

        

        

    def create_new_head(self,fruit_pos):
        self.head_pos = fruit_pos
        self.head_cords = change_px(self.head_pos)
        self.tail_ls.insert(0,self.head_cords)

        


class Fruit():
    fruit_pos = None
    fruit_cords = None
    score_list = []
    score = 0

    def __init__(self) -> None:
        self.add_fruit()
    def draw(self):
        pg.draw.rect(WINDOW,"red", (self.fruit_cords,(64,64)) )
    def add_fruit(self):
        while True:
            x = random.randint(0,19)
            y = random.randint(0,19)
            if change_px([x,y]) not in snake.tail_ls:
                self.fruit_pos = [x,y]
                self.fruit_cords = change_px(self.fruit_pos)
                break

                




    


def change_px(vec):
    return [vec[0]*64,vec[1]*64]

def add_vec2(vec1,vec2):
    return [vec1[0]+vec2[0],vec1[1]+vec2[1]]


def main():
    running = True
    time_elapsed = 0
    clock = pg.time.Clock()
    while running:
        
        dt = clock.tick(30)
        time_elapsed += dt
             
        if time_elapsed > 120:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_w and snake.move_vec[1] != 1:
                        snake.move_vec = [0,-1]
                        
                    elif event.key == pg.K_s and snake.move_vec[1] != -1:
                        snake.move_vec = [0, 1]
                    elif event.key == pg.K_a and snake.move_vec[0] != 1:
                        snake.move_vec = [-1,0]
                    elif event.key == pg.K_d and snake.move_vec[0] != -1:
                        snake.move_vec = [1,0]
                    elif event.key == pg.K_SPACE:
                        snake.add_tail_unit()
            
            next_pos = add_vec2(snake.head_pos,snake.move_vec)
            if change_px(next_pos) in snake.tail_ls or 20 in next_pos or -1 in next_pos:
                snake.move_vec = [0,0]
                pg.mixer.Sound.play(lose_sound)
                
                
                fruit.score_list.append(fruit.score)
                snake.restart()
                
                
                
            if next_pos == fruit.fruit_pos:
                fruit.score += 1
                snake.create_new_head(fruit.fruit_pos)
                fruit.add_fruit()
                pg.mixer.Sound.play(chomp_sound)
            
                
                

            snake.move(snake.move_vec)
        
                
            time_elapsed = 0
        
            


        draw()
    

def draw():
    dark_green = False
    
    for i in range(0,1280,64):
        dark_green = not dark_green
        for j in range(0,1280,64):
            dark_green= not dark_green
            if dark_green:
                pg.draw.rect(WINDOW,(0,70,0),((i,j),(64,64)))
            else:
                pg.draw.rect(WINDOW,(0,100,0),((i,j),(64,64)))
            

    snake.draw()
    fruit.draw()
    
    
    pg.display.update()

if __name__ == "__main__":
    snake = Snake()
    fruit = Fruit()

    main()