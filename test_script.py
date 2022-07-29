"""
Test file for the new patches

Created by @fkS124 - 07/29/22 18:06:36

This file should be deleted at the end of the development phase.
"""


import src as scoreunlocked
import pygame as pg
import random


# connect the client
client = scoreunlocked.Client()
client.connect("fks124-dev", "test")

# initialize pygame stuff
pg.init()
screen = pg.display.set_mode((300, 300))
clock = pg.time.Clock()

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit

        if event.type == pg.KEYDOWN:
            # post a new random score
            if event.key == pg.K_p:
                # this one works without pausing the program
                client.post_score(name="dev", score=random.randint(0, 100))

                # this one does pause the program
                # client.post_score(name="dev", score=random.randint(0, 100), use_thread=False)

            # get the current leaderboard
            elif event.key == pg.K_s:
                print(client.get_leaderboard())

    screen.fill((random.randint(0, 255), 0, 0))
    pg.display.update()
    clock.tick(60)
    pg.display.set_caption(str(clock.get_fps()))
