import pygame
import sys
pygame.init()
window=pygame.display.set_mode([640,480])
pygame.display.set_caption("Team JhaneVhiel")
font=pygame.font.Font("freesansbold.ttf",20)
#font2=pygame.font.Font("ITCKRIST.ttf",32)
while True:
    events=pygame.event.get()
    def TitleScreen(window,font):
        textColor=pygame.Color(216,137,184)
        text1=font.render("Team JhaneVhiel:",False,textColor)
        textColor2=pygame.Color(216,137,184)
        text2=font.render("Jane Claudette Alambra",False,textColor2)
        textColor3=pygame.Color(216,137,184)
        text3=font.render("Ma.Elvira Oco",False,textColor3)
        window.blit(text1,[0,0])
        window.blit(text2,[20,20])
        window.blit(text3,[20,40])
    for event in events :
        if(event.type==pygame.QUIT):
            pygame.quit()
            sys.exit()
    TitleScreen(window,font)
    pygame.display.update()
