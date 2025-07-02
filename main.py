from random import randint

import pygame as pg



# ЗАДАНИЯ ПРОСТО, НЕ КОД
# def move(starship_rect, events):
#     for event in events:
#         if event.type == pg.KEYDOWN:
#             if event.key == pg.K_a:
#                 starship_rect.x -= 1
#             if event.key == pg.K_d:
#                 starship_rect.x += 1
#             if event.key == pg.K_q:
#                 starship_rect.x -= 10
#
#             if event.key == pg.K_e:
#                 starship_rect.x += 10

# def laser_shoot(events):
#     for event in events:
#         if event.type == pg.MOUSEBUTTONDOWN:
#             if event.button == 1:
#                 rect = pg.Rect(0,0, 20, 20)
#                 rect.center = event.pos
#                 return rect




pg.mixer.init()

size = (1000, 1000)
screen = pg.display.set_mode(size)

fps = 60
clock = pg.time.Clock()


rect_1 = pg.Rect(100,400, 50,80)

dante = pg.image.load("dante.png")
dante = pg.transform.scale(dante, (600, 500))
dante_rect = dante.get_rect(center=(size[0] // 2, size[1] // 2))
vergil = pg.image.load("vergil.png")
vergil = pg.transform.scale(vergil, (400, 300))
vergil_rect = vergil.get_rect(center=(size[0] // 2, size[1] // 2))

background = pg.image.load("maxresdefault.jpg")
background = pg.transform.scale(background, size)
pg.mixer.music.load("I AM THE STORM THAT IS APPROACHING (mp3cut.net).mp3")

pg.mixer.music.set_volume(0.6)

# pg.mixer.music.play()
sound = pg.mixer.Sound("pder.mp3")
sound.play()



while True:
    # move(guts_rect, pg.event.get())
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
        if event.type == pg.KEYDOWN:
        #     if event.key == pg.K_LEFT:
        #         guts_rect.x -= 10
        #     if event.key == pg.K_RIGHT:
        #         guts_rect.x += 10
            if event.key == pg.K_SPACE:
                pg.mixer.music.play()




    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        dante_rect.x -= 3
    if keys[pg.K_RIGHT]:
        dante_rect.x += 3
    mouse_pos = pg.mouse.get_pos()
    mouse_keys = pg.mouse.get_pressed()
    if mouse_keys[0]:
        dante_rect.center = mouse_pos
    if mouse_keys[2]:
        vergil_rect.center = mouse_pos




    screen.fill(pg.Color("white"))
    screen.blit(background, (0,0))

    screen.blit(dante, dante_rect )
    # pg.draw.rect(screen,pg.Color('black'),small_rect)
    screen.blit(vergil, vergil_rect)



    pg.display.flip()
    clock.tick(fps)
