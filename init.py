#import Snake
#import World
import GeneticAlgorythm
class Snake:
    size = 1
    tail = []
    starting_location = (3,0)
    alive = True
    direction = 0

    def __init__(self):
        self.tail = []
        self.size = 0
        self.tail.append(self.starting_location)
        self.alive = True



    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for _ in keys:
                if keys[pygame.K_LEFT]:
                    self.direction = 2

                elif keys[pygame.K_RIGHT]:
                    self.direction = 0

                elif keys[pygame.K_UP]:
                    self.direction = 1

                elif keys[pygame.K_DOWN]:
                    self.direction = 3


        if self.direction == 0:
            self.tail.insert(0, (self.tail[0][0], self.tail[0][1]+1))
        elif self.direction == 1:
            self.tail.insert(0, (self.tail[0][0] - 1, self.tail[0][1]))
        elif self.direction == 2:
            self.tail.insert(0, (self.tail[0][0], self.tail[0][1] - 1))
        elif self.direction == 3:
            self.tail.insert(0, (self.tail[0][0] + 1, self.tail[0][1]))
        self.tail.pop()


    def endgame_check(self, size, moves):

        head = self.tail[0]
        rest_tail = self.tail[1:]

        if head in rest_tail or head[0] == -1 or head[0] == size or\
                head[1] == -1 or head[1] == size or moves < 1:
            print("DED")
            self.alive = False


    def check_if_apple_eaten(self, apple):
        head = self.tail[0]
        if head[0] == apple[0] and head[1] == apple[1]:
            return True
        else:
            return False
    def add_tail(self):
        self.tail.append(self.tail[-1])

    def draw(self, surface, world):
        global width

        rows = world.size

        for i, c in enumerate(self.tail):
            if i == 0:
                self.draw_part(c, surface, width, rows, True)
            else:
                self.draw_part(c, surface, width, rows, False)

    def draw_part(self, place, surface, w, r, something=False):
        dis = w//r
        i = place[1]
        j = place[0]
        color = (0, 255, 0)
        if something:
            color = (255, 255, 0)
        pygame.draw.rect(surface, color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))



import random

class World:
    size = 0
    width = 0
    area = []
    score = 0
    apple = (3, 3)

    def __init__(self, size, width):
        self.size = size
        self.width = width
        self.area = []
        self.score = 0

        for _ in range(self.size):
            self.area.append([0 for _ in range(self.size)])
        '''for i in range(world.size):
            world.area[0][i] = 2
            world.area[i][0] = 2
            world.area[-1][i] = 2
            world.area[i][-1] = 2
        '''





    def spawn_apple(self, snake):
        found_place = False
        while not found_place:
            x,y = random.randrange(1, self.size-1), random.randrange(1, self.size-1)
            if (x,y) not in snake.tail:
                found_place = True
                self.apple = (x, y)

    def draw_snack(self, surface):
        global rows, width
        w = width
        r = rows
        dis = w // r
        i = self.apple[1]
        j = self.apple[0]
        color = (0, 0, 255)

        pygame.draw.rect(surface, color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))


def print_snake(world, snake):
    for tail_part in snake.tail:
        world.area[tail_part[0]][tail_part[1]] = 1
    world.area[world.apple[0]][world.apple[1]] = 3
    for i in range(len(world.area)):
        print(world.area[i])
    print("")
    print("_______________________________")
    print("_______________________________")
    print("")


def draw_snake(world, snake, win):
    redrawWindow(win, snake, world)


import pygame


def drawGrid(surface):
    global width, rows
    print(rows)
    sizeBtwn = width // rows
    w = width
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redrawWindow(surface, snake, world):
    global rows, width
    width = width

    drawGrid(surface)
    surface.fill((0, 0, 0))
    world.draw_snack(surface)
    snake.draw(surface, world)
    pygame.display.update()


# import pygame
# import time

def play(size, dim, child, player='Bot',):
    print("Starting snake")
    world = None
    world = World(size, dim)
    snake = Snake()
    print("WORLD:")
    print(world.size)
    print(world.width)
    print(world.apple)
    print("snake.len = ", snake.size)
    global rows, width
    width = dim
    rows = size

    print_snake(world, snake)
    score = 0
    moves = 0
    avilable_moves = 5
    win = pygame.display.set_mode((width, width))
    clock = pygame.time.Clock()
    if player == 'Bot':
        print("_____________________-----------------------------------")
        print("_____________________")
        print("________", child.batch, "\\", child.id, "________")
        print("_____________________")
        while snake.alive:
            avilable_moves -= 1

            print_snake(world, snake)
            snake.endgame_check(world.size, avilable_moves)

            if snake.check_if_apple_eaten(world.apple):
                snake.add_tail()
                world.spawn_apple(snake)
                score += 100
                avilable_moves += 100
            score += 1
            moves += 1

    if player == 'Human':
        print("????????????????????????????????????????????????????????????????")
        if player == 'Human':
            while snake.alive:
                # print_snake(world, snake)
                draw_snake(world, snake, win)
                pygame.time.delay(100)
                clock.tick(150)
                snake.move()
                snake.endgame_check(world.size, avilable_moves)

                if snake.check_if_apple_eaten(world.apple):
                    snake.add_tail()
                    world.spawn_apple(snake)
                    score += 100
                    avilable_moves += 100
                score += 1


        # DO MAGIC


        # snake.endgame_check(world)
    print("Snake died after ", moves, "moves.")
    print("Total score was ", score, "points.")
    print("Number of aviable movements is ", avilable_moves, ".")


if __name__ == '__main__':
    play(20,800,None, player='Human')



