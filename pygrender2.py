import pygame as pg
from pygame.locals import *
import pygame.math
import math
from bomb import Bomb
import time
from Calculation import XDisToSpringDis
import sys



def rendder(anglr,veloc,veloc2,timec,dista,high,sppull,kspr):
    pg.init()
    Reso_x = 1100  # Screen SIZE
    Reso_y = 500
    screen = pg.display.set_mode((Reso_x, Reso_y))
    pg.display.set_caption("FRA163 x FRA142 Catapult Simulator. | Graphic Render by pygame.")
    icon1 = pg.image.load('./image/object_2.ico')
    pg.display.set_icon(icon1)
    screen.fill((153, 204, 255))  # bg

    catapult1 = pg.image.load('./image/Asset 1.png')
    bucket1 = pg.image.load('./image/Asset 2.png')
    bg1 = pg.image.load('./image/Asset 22.png')
    txtbox1 = pg.image.load('./image/whbox.png')
    quitbx = pg.image.load('./image/b_quit.png')

    rx = Reso_x / 6.47 # 170
    ry = Reso_x / 6.47
    bg1 = pg.transform.scale(bg1, (Reso_x, Reso_y))
    catapult1 = pg.transform.scale(catapult1, (int(1.0 * rx), int(0.5 * rx)))
    bucket1 = pg.transform.scale(bucket1, (int(1.0 * ry), int(0.8 * ry)))
    txtbox1 = pg.transform.scale(txtbox1,(300,270))
    qbx = 0.7
    quitbx = pg.transform.scale(quitbx, (int(148*qbx), int(70*qbx)))
    velocc = float(veloc) * 4.97
    bb4 = Bomb(0, 0, velocc , anglr, 0.003, "./image/object_8.png")

    def dccf(x, a):  # config decimal for answer
        aa = str(int(a))
        dm = "{:." + aa + "f}"
        ff = float(dm.format(x))
        return str(ff)

    screen.blit(bg1, (0, 0))  # Background

    # White text box
    pos_tbx_x = Reso_x * 0.74
    pos_tbx_y = Reso_y * 0.016
    screen.blit(txtbox1, (pos_tbx_x, pos_tbx_y))  # (positZ + S_bucket_Py - 0.0785 * py, positA)

    def txtdraw(txt,siz,col,pratx,praty):
        pg.font.init()
        myfont = pg.font.SysFont('calibri', siz,bold=True)
        text_dist = myfont.render(txt, False, col)
        pos_distx_x = Reso_x * pratx    # Position in ratio 0-1
        pos_distx_y = Reso_y * praty
        screen.blit(text_dist, (pos_distx_x, pos_distx_y))

    txt_x = 0.76
    dista_txt = "Distance (m) : " + str(dista)
    high_txt = "    High (m) : " + str(high)
    ang_txt ="   Angle (deg) : " + str(anglr)
    ks_txt ="K spring (N/m) : " + str(kspr)
    tme_txt = "    Time (Sec) : "+ str(timec)
    vel_txt = "Velocity (m/s) : "+ str(veloc2)
    spp_txt ="Spring_pull (m) : "+ str(sppull)
    txtdraw(dista_txt, 21, (255, 0, 0), txt_x, 0.04)
    txtdraw(high_txt, 21, (255, 0, 0), txt_x, 0.10)
    txtdraw(ang_txt, 21, (255, 0, 0), txt_x, 0.17)
    txtdraw(ks_txt, 21, (255, 0, 0), txt_x, 0.24)
    txtdraw(tme_txt, 21, (255, 150, 0), txt_x, 0.34)
    txtdraw(vel_txt, 21, (255, 150, 0), txt_x, 0.41)
    txtdraw(spp_txt, 21, (255, 150, 0), txt_x, 0.48)

    pos_ctp_x = Reso_x * 0.036
    pos_ctp_y = Reso_y * 0.814
    screen.blit(catapult1, (pos_ctp_x, pos_ctp_y))  # (positX + S_bucket_Px - 0.0785 * px , positY)
    pos_bck_x = Reso_x * 0.83
    pos_bck_y = Reso_y * 0.7
    screen.blit(bucket1, (pos_bck_x, pos_bck_y))  # (positZ + S_bucket_Py - 0.0785 * py, positA)
    pos_qbx_x = Reso_x * 0.9
    pos_qbx_y = Reso_y * 0.9
    screen.blit(quitbx, (pos_qbx_x, pos_qbx_y))  # (positZ + S_bucket_Py - 0.0785 * py, positA)
    pg.draw.rect(screen, (40, 40, 40), (640, 420, 250, 120), 5)

    # Quit_command_Area
    rect_q_x = 1000
    rect_q_y = 455
    rect_q_sx = 85
    rect_q_sy = 40


    done = False
    while not done:

        mouse = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == QUIT:
                done = True
            pressed = pg.key.get_pressed()
            # Quit BUTTON
            if event.type == pg.MOUSEBUTTONDOWN:
                if rect_q_x <= mouse[0] <= rect_q_x + rect_q_sx \
                        and rect_q_y <= mouse[1] <=rect_q_y + rect_q_sy:
                   pg.quit()

        bb4.update()
        bb4.draw(screen, 190, -2, 8, 8)

        #print Real time position xy--------------------------------------------------------------
        pg.draw.rect(screen, (220, 220, 220), (640, 420, 250, 120))

        rtx_txt = "X : " + dccf(( bb4.sentxy(190, -2, 8, 8)[0])/931.20 *dista,5 ) + "  m."
        txtdraw(rtx_txt, 21, (0, 0, 255), 0.6, 0.87)
        rty_txt = "Y : " + dccf(((398.09-bb4.sentxy(190, -2, 8, 8)[1])/931.20 *dista ),5) + "  m."
        txtdraw(rty_txt, 21, (0, 0, 255), 0.6, 0.94)
        # print Real time position xy--------------------------------------------------------------

        pg.display.update()

    pg.quit()

#rendder(20,23.5,5,2,5,5,5,5)
