import os
import sys
import random
import pygame as pg
import time


WIDTH, HEIGHT = 1600, 900
delta = {
    pg.K_UP:(0, -5),
    pg.K_DOWN:(0, +5),
    pg.K_LEFT:(-5, 0),
    pg.K_RIGHT:(+5, 0),
}
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def bombom():
    for i in range(1,11):
        bd_img = pg.Surface((20+i, 20+i))
        bd_img.set_colorkey((0, 0, 0))
        pg.draw.circle(bd_img, (255, 0, 0), (10, 10), 10)

def gameover():                             #演習のための関数
    fonto = pg.font.Font(None, 80)          #爆破された後にデスログが出る
    pienton = pg.image.load("fig/8.png")
    txt = fonto.render("Game over",
    True, (255,255,255))
    return txt
    
def check_bound(obj_rct:pg.Rect) -> tuple[bool, bool]:
    yoko, tate = True, True
    if obj_rct.left < 0 or WIDTH < obj_rct.right: 
        yoko = False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom:
        tate = False
    return yoko, tate

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    clock = pg.time.Clock()
    for i in range(1,11):
        bd_img = pg.Surface((20+i, 20+i))
        bd_img.set_colorkey((0, 0, 0))
        pg.draw.circle(bd_img, (255, 0, 0), (10, 10), 10)
    pienton = pg.image.load("fig/8.png")
    bd_rct = bd_img.get_rect()
    bd_rct.center = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    vx, vy = +5, +5
    txt = gameover()

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        if kk_rct.colliderect(bd_rct):
            print("Game Over")
            bout = pg.Surface((1600,900))                 #スクリーンをブラックアウトさせる
            pg.draw.rect(bout,(0,0,0),(0,0,1600,900))
            bout.set_alpha(200)
            screen.blit(bout, [0,0])
            screen.blit(txt, [650, 450])
            screen.blit(pienton, [600,450])               #泣いてるこうかとん（ぴえんとん）を出す
            screen.blit(pienton, [950,450])
            pg.display.update()
            time.sleep(5)

            return
        screen.blit(bg_img, [0, 0]) 

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k,v in delta.items():
            if key_lst[k]:
                sum_mv[0] += v[0]
                sum_mv[1] += v[1]
        kk_rct.move_ip(sum_mv)
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        screen.blit(kk_img, kk_rct)
        screen.blit(kk_img, kk_rct)
        bd_rct.move_ip(vx, vy)       
        screen.blit(bd_img, bd_rct)
        yoko, tate = check_bound(bd_rct)
        if not yoko: 
            vx *= -1
        if not tate: 
            vy *= -1
        tmr += 1
        clock.tick(50)
        pg.display.update()

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
