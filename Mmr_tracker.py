#ekran
#kolory
#czcionki
#mmr
#ekrany
#pisanie
#przyciski menu
#wstecz
#pętla gry

#from pygame.examples.sprite_texture import renderer
import pygame

pygame.init()

#===Historia===
historia = [None,None,None,None,None,None,None,None,None,None]
#===Ekran===
SZEROKOSC = 1000
WYSOKOSC = 800
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
zegar = pygame.time.Clock()
pygame.display.set_caption('MMR tracker 2.0')
#===Kolory===
CZARNY = (0,0,0)
BIALY = (255,255,255)
CZERWONY = (255,0,0)
ZIELONY = (0,255,0)
NIEBIESKI = (0,0,255)
ZOLTY = (255,250,0)
SZARY = (107, 107, 107)
CIEMNOSZARY = (56, 56, 56)
CIEMNOCZERWONY=(36, 0, 0)


#===Mmr===
mmr={
    'mmr':100,
    'peak':100,
    'lower':100,
}


#===ekrany===
MENU = 1
TRACKER = 2
OAPL = 3
STATY = 4
HISTORIA = 5
aktualny = MENU


#===Pisanie===
czcionka_mala = pygame.font.Font(None, 30)
czcionka_mid = pygame.font.Font(None, 60)
czcionka_big = pygame.font.Font(None, 90)
wpisywanie = ''
input_actiwe = True


#===przyciski menu===
buttons = [
    pygame.Rect(375,400,250,75),
    pygame.Rect(375,500,250,75),
    pygame.Rect(375,600,250,75),
    pygame.Rect(375,700,250,75),
]


#===Przycisk wstecz===
back = pygame.Rect(50,700,100,50)


run = True
while run:
    ekran.fill(CZARNY)
    mysz_klik = pygame.mouse.get_pressed()[0]
    mysz_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # -----------------------------------------jeśli kliknięto przycisk tracker-----------------------------------------
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if buttons[0].collidepoint(event.pos):
                    aktualny = TRACKER
        # -----------------------------------------jeśli kliknięto przycisk o aplikacji-----------------------------------------
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if buttons[1].collidepoint(event.pos):
                    aktualny = OAPL
        # -----------------------------------------jeśli kliknięto przycisk staty-----------------------------------------
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if buttons[2].collidepoint(event.pos):
                    aktualny = STATY

        #-----------------------------------------jeśli kliknięto przycisk back-----------------------------------------
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if back.collidepoint(event.pos):
                    aktualny = MENU
        #========================================jeśli kliknięto historia================================================
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if buttons[3].collidepoint(event.pos):
                    aktualny = HISTORIA


            #--------------------------------------------mmr w trackerze-----------------------------------------------------
        if input_actiwe == True:
            if aktualny == TRACKER:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        try:
                            zmiana = int(wpisywanie)
                            mmr['mmr'] += zmiana
                            if None in historia:
                                historia.append(zmiana)
                                historia.remove(None)
                                print(historia)
                            elif None is not historia:
                                historia.pop(0)
                                historia.append(zmiana)
                                print(historia)
                            if mmr['mmr'] > mmr['peak']:
                                mmr['peak'] = mmr['mmr']
                            elif mmr['mmr'] < mmr['lower']:
                                mmr['lower'] = mmr['mmr']
                            wpisywanie = ''
                        except ValueError:
                            continue
                    elif event.key == pygame.K_BACKSPACE:
                        wpisywanie = wpisywanie[:-1]
                    else:
                        wpisywanie += event.unicode
    mmr['mmr']= max(0,mmr['mmr'])
    mmr['lower']=max(0,mmr['lower'])

    #-----rysowanie-----

    #-------------------------------------------------menu--------------------------------------------------------------
    if aktualny == MENU:
        input_actiwe =False
        for i, rect in enumerate(buttons):
            text = ('tracker', 'o aplikacji', 'statystyki', 'historia')
            kolor = CIEMNOSZARY if rect.collidepoint(mysz_pos) else SZARY
            pygame.draw.rect(ekran,kolor,buttons[i],border_radius=20)
            pygame.draw.rect(ekran,BIALY,buttons[i],5,border_radius=20)
            ekran.blit(czcionka_mala.render(text[i],True,BIALY),(rect.x + 50,rect.y + 27))
            ekran.blit(czcionka_big.render('MENU',True,BIALY),(400,50))

    #--------------------------------------------------tracker------------------------------------------------------------
    elif aktualny == TRACKER:
        input_actiwe = True

        ekran.blit(czcionka_big.render('TRACKER',True,BIALY),(100,100))
        text = [f'mmr: {mmr['mmr']}',f'peak {mmr['peak']}',f'lower {mmr['lower']}']
        kolor = [BIALY,ZIELONY,CZERWONY]
        y = 200
        i=0
        for tekst in text:
            ekran.blit(czcionka_mid.render(tekst,True,kolor[i]),(100,y))
            i+=1
            y += 80
        kolor = CIEMNOCZERWONY if back.collidepoint(mysz_pos) else CZERWONY
        pygame.draw.rect(ekran,kolor,back,border_radius=20)
        pygame.draw.rect(ekran,BIALY,back,5,border_radius=20)
        ekran.blit(czcionka_mala.render('wyjdź',True,BIALY),(64,716))
        if input_actiwe == True:
            ekran.blit(czcionka_mid.render("Wpisz zmianę (+/-) i ENTER:", True, BIALY), (50, 400))
            ekran.blit(czcionka_mid.render(wpisywanie if wpisywanie else "Wpisz liczbę", True, BIALY), (50, 460))

    #------------------------------------------o aplikacji------------------------------------------------
    elif aktualny == OAPL:
        input_actiwe = False
        ekran.blit(czcionka_big.render('O Aplikacji', True, BIALY), (100, 100))
        ekran.blit(czcionka_mid.render('Twórca:krystian', True, BIALY), (100, 200))
        kolor = CIEMNOCZERWONY if back.collidepoint(mysz_pos) else CZERWONY
        pygame.draw.rect(ekran, kolor, back, border_radius=20)
        pygame.draw.rect(ekran, BIALY, back, 5, border_radius=20)
        ekran.blit(czcionka_mala.render('wyjdź', True, BIALY), (64, 716))

    #------------------------------------------staty--------------------------------------------------------------------
    elif aktualny == STATY:
        input_actiwe = False
        ekran.blit(czcionka_big.render('STATY', True, BIALY), (100, 100))
        ekran.blit(czcionka_mid.render('Na razie nie ma ', True, BIALY), (100, 200))
        ekran.blit(czcionka_mala.render('wyjdź', True, BIALY), (64, 716))
        kolor = CIEMNOCZERWONY if back.collidepoint(mysz_pos) else CZERWONY
        pygame.draw.rect(ekran, kolor, back, border_radius=20)
        pygame.draw.rect(ekran, BIALY, back, 5, border_radius=20)
        ekran.blit(czcionka_mala.render('wyjdź', True, BIALY), (64, 716))

    #----------------------------------------------historia-------------------------------------------------------------
    elif aktualny == HISTORIA:
        input_actiwe = False
        ekran.blit(czcionka_big.render('HISTORIA', True, BIALY), (100, 100))
        ekran.blit(czcionka_mid.render('MMR: ', True, BIALY), (100, 200))
        ekran.blit(czcionka_mala.render(f'mmr:{historia}', True, BIALY), (100, 300))
        kolor = CIEMNOCZERWONY if back.collidepoint(mysz_pos) else CZERWONY
        pygame.draw.rect(ekran, kolor, back, border_radius=20)
        pygame.draw.rect(ekran, BIALY, back, 5, border_radius=20)
        ekran.blit(czcionka_mala.render('wyjdź', True, BIALY), (64, 716))

    pygame.display.flip()
    zegar.tick(60)
pygame.quit()