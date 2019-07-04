import pygame
import random

pygame.init()

win = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Tree Planting Simulator")
clock = pygame.time.Clock()
rannum = random.randint(0, 160)


class Seed(object):
    def __init__(self, x, y, size, colour):
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour
        self.timer = random.randint(0, 80)

    def draw(self, win):
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.size)


class Sprout(object):
    def __init__(self, x, y, size, colour):
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour
        self.timer = random.randint(0, 120)

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.size * 2, self.size * 4))


class Sapling(object):
    def __init__(self, x, y, size, colour):
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour
        self.timer = rannum

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.size * 3, self.size * 12))


class Tree(object):
    def __init__(self, x, y, size, colour):
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.size * 6, self.size * 30))


class Leaf(object):
    def __init__(self, x, y, size, colour, timer, tt):
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour
        self.timer = timer
        self.tt = tt

    def draw(self, win):
        # pygame.draw.rect(win, self.colour, (self.x, self.y, self.size * 5 + self.size * 6 + self.size * 5, self.size * 12))
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.size * 5)


class Ground(object):
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height))


def redraw_game_window():
    win.fill((135, 206, 235))
    for seed in seeds:
        if seed.y < base.y:
            seed.y += 5
        seed.draw(win)

    for sprout in sprouts:
        sprout.draw(win)

    for sapling in saplings:
        sapling.draw(win)

    for tree in trees:
        tree.draw(win)

    for leaf in leaves:
        leaf.draw(win)

    base.draw(win)
    pygame.display.update()


def tree_grow_check():
    for seed in seeds:
        seed.timer += 1
        if seed.timer >= 300:
            sprouts.append(Sprout(seed.x, base.y - seed.size * 4, seed.size, (0, 128, 0)))
            seeds.pop(seeds.index(seed))
    for sprout in sprouts:
        sprout.timer += 1
        if sprout.timer >= 600:
            saplings.append(Sapling(sprout.x, base.y - sprout.size * 12, sprout.size, (0, 100, 0)))
            sprouts.pop(sprouts.index(sprout))
            leaves.append(Leaf(sprout.x + round(sprout.size * 1.5), base.y - sprout.size * 12 - sprout.size * 3, sprout.size, (0, 140, 0), rannum, 1))
    for sapling in saplings:
        sapling.timer += 1
        if sapling.timer >= 800:
            randnums.append(random.randint(30, 70))
            trees.append(Tree(sapling.x, base.y - sapling.size * 30, sapling.size, (0, randnums[-1], 0)))
            saplings.pop(saplings.index(sapling))
            randnums.append(random.randint(85, 120))
            leaves.append(Leaf(sapling.x + sapling.size * 3, base.y - sapling.size * 30 - sapling.size * 8, round(sapling.size * 1.5), (0, randnums[-1], 0), sapling.timer, 2))
            leaves.append(Leaf(sapling.x + sapling.size * 8, base.y - sapling.size * 30 - sapling.size * 6 + sapling.size * 8, round(sapling.size * 1.5), (0, randnums[-1], 0), sapling.timer, 2))
            leaves.append(Leaf(sapling.x - sapling.size * 3, base.y - sapling.size * 30 - sapling.size * 6 + sapling.size * 8, round(sapling.size * 1.5), (0, randnums[-1], 0), sapling.timer, 2))
    for leaf in leaves:
        leaf.timer += 1
        if leaf.tt == 1:
            if leaf.timer >= 800:
                leaves.pop(leaves.index(leaf))


randnums = []
seeds = []
sprouts = []
saplings = []
trees = []
leaves = []

sizes = [2, 4, 6]

base = Ground(0, 400, 1000, 100, (86, 176, 0))

run = True
while run:
    clock.tick(50)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            seeds.append(Seed(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], random.randint(3, 6), (78, 46, 40)))

    if keys[pygame.K_r]:
        for seed in seeds:
            seeds.pop(seeds.index(seed))
        for sprout in sprouts:
            sprouts.pop(sprouts.index(sprout))
        for sapling in saplings:
            saplings.pop(saplings.index(sapling))
        for tree in trees:
            trees.pop(trees.index(tree))
        for leaf in leaves:
            leaves.pop(leaves.index(leaf))

    tree_grow_check()
    redraw_game_window()

pygame.quit()
