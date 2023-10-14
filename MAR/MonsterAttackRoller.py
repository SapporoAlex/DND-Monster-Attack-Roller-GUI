import pygame
import buttons
import random as rd


# Initialize Pygame
pygame.init()

# create display window
WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 500
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
BG = pygame.image.load("MAR Assets/Other/MARBGvertical - Copy.jpg")
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("MAR")

# constants
font = pygame.font.Font('freesansbold.ttf', 14)

# TEXTBOX
white = (255, 255, 255)
black = (0, 0, 0)

melee_sound_effects = ["MAR Assets/SFX/m1.mp3", "MAR Assets/SFX/m2.mp3",
                       "MAR Assets/SFX/m3.mp3", "MAR Assets/SFX/m4.mp3"]
ranged_sound_effects = ["MAR Assets/SFX/r1.mp3", "MAR Assets/SFX/r2.mp3",
                        "MAR Assets/SFX/r3.mp3", "MAR Assets/SFX/r4.mp3"]
bite_sound_effect = pygame.mixer.Sound("MAR Assets/SFX/b1.mp3")
claw_sound_effect = pygame.mixer.Sound("MAR Assets/SFX/claw.mp3")
crush_sound_effect = pygame.mixer.Sound("MAR Assets/SFX/cr.mp3")

for m_sound in melee_sound_effects:
    pygame.mixer.Sound(m_sound)

for r_sound in ranged_sound_effects:
    pygame.mixer.Sound(r_sound)


# load button images
m_img = pygame.image.load("MAR Assets/Buttons/m.png").convert_alpha()
r_img = pygame.image.load("MAR Assets/Buttons/r.png").convert_alpha()
b_img = pygame.image.load("MAR Assets/Buttons/b.png").convert_alpha()
c_img = pygame.image.load("MAR Assets/Buttons/c.png").convert_alpha()
th_img = pygame.image.load("MAR Assets/Buttons/th.png").convert_alpha()
cr_img = pygame.image.load("MAR Assets/Buttons/cr.png").convert_alpha()

# create button instances
AT_button = buttons.Button(200, 50, r_img, scale=0.5)
BM_button = buttons.Button(200, 100, m_img, scale=0.5)
BR_button = buttons.Button(250, 100, r_img, scale=0.5)
BA_button = buttons.Button(200, 150, b_img, scale=0.5)
DMC_button = buttons.Button(200, 200, cr_img, scale=0.5)
DWM_button = buttons.Button(200, 250, b_img, scale=0.5)
GHB_button = buttons.Button(200, 300, b_img, scale=0.5)
GHC_button = buttons.Button(250, 300, c_img, scale=0.5)
GUM_button = buttons.Button(200, 400, m_img, scale=0.5)
GM_button = buttons.Button(200, 350, m_img, scale=0.5)
GR_button = buttons.Button(250, 350, r_img, scale=0.5)
KM_button = buttons.Button(200, 450, m_img, scale=0.5)
KR_button = buttons.Button(250, 450, r_img, scale=0.5)
OM_button = buttons.Button(200, 500, m_img, scale=0.5)
OR_button = buttons.Button(250, 500, r_img, scale=0.5)
OB_button = buttons.Button(200, 550, m_img, scale=0.5)
SB_button = buttons.Button(200, 600, b_img, scale=0.5)
SC_button = buttons.Button(250, 600, c_img, scale=0.5)
SohS_button = buttons.Button(300, 600, m_img, scale=0.5)
SthS_button = buttons.Button(350, 600, th_img, scale=0.5)
SM_button = buttons.Button(200, 650, m_img, scale=0.5)
SR_button = buttons.Button(250, 650, r_img, scale=0.5)
SNM_button = buttons.Button(200, 700, b_img, scale=0.5)
ZM_button = buttons.Button(200, 800, m_img, scale=0.5)
SPM_button = buttons.Button(200, 750, b_img, scale=0.5)


def dark_mantle_crush():
    double_damage = False
    attack = rd.randrange(1, 21)
    if attack == 20:
        double_damage = True
    attack += 5
    damage = rd.randrange(1, 7)
    if double_damage is True:
        damage *= 2
    damage += 3
    print()
    text = font.render(f"Dark mantle attacks with crush for {attack}, dealing {damage} damage.",
                       True, white, black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)


def arrow_trap():
    double_damage = False
    arrow_attack = rd.randrange(1, 21)
    if arrow_attack == 20:
        double_damage = True
    total_a_d = 0
    for i in range(2):
        arrow_damage = rd.randrange(1, 11)
        if double_damage is True:
            arrow_damage *= 2
        total_a_d += arrow_damage
    text = font.render(f"Arrow trap attacks for {arrow_attack}, and does {total_a_d} damage",
                       True, white, black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)


def bandit_melee():
    double_damage = False
    attack = rd.randrange(1, 21)
    if attack == 20:
        double_damage = True
    attack += 3
    damage = rd.randrange(1, 7)
    if double_damage is True:
        damage *= 2
    damage += 1
    text = font.render(f"Bandit attacks with scimitar for {attack}, dealing {damage} damage.",
                       True, white, black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)


def bandit_ranged():
    double_damage = False
    attack = rd.randrange(1, 21)
    if attack == 20:
        double_damage = True
    attack += 3
    damage = rd.randrange(1, 9)
    if double_damage is True:
        damage *= 2
    damage += 1
    text = font.render(f"Bandit attacks with crossbow for {attack}, dealing {damage} damage.",
                       True, white, black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)


def basilisk():
    double_damage = False
    attack = rd.randrange(1, 21)
    if attack == 20:
        double_damage = True
    attack += 5
    total_d = 0
    for i in range(2):
        damage = rd.randrange(1, 7)
        if double_damage is True:
            damage *= 2
        total_d += damage
    total_d += 3
    total_pd = 0
    for i in range(2):
        poison_damage = rd.randrange(1, 7)
        if double_damage is True:
            poison_damage *= 2
        total_pd += poison_damage
    text = font.render(f"Basilisk bites for {attack}, dealing {total_d} damage, and {total_pd}poison damage.",
                       True, white, black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)

def owlbear():
    double_damage = False
    attack1 = rd.randrange(1,21)
    if attack1 == 20:
        double_damage = True
    attack1 += 7
    damage1 = rd.randrange(1, 11)
    if double_damage is True:
        damage1 *= 2
    damage1 += 5
    double_damage = False
    attack2 = rd.randrange(1,21)
    if attack2 == 20:
        double_damage = True
    attack2 += 7
    total_d = 0
    for i in range(2):
        second_damage = rd.randrange(1, 9)
        if double_damage is True:
            second_damage *= 2
        total_d += second_damage
    text = font.render(f"Owlbear attacks twice, first {attack1} for {damage1}, 2nd {attack2} for {total_d}",
                       True, white, black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)


def dire_wolf_melee():
    double_damage = False
    attack = rd.randrange(1, 21)
    if attack == 20:
        double_damage = True
    attack += 5
    total_a_d = 3
    for i in range(2):
        bite_damage = rd.randrange(1, 7)
        if double_damage is True:
            bite_damage *= 2
        total_a_d += bite_damage
    text = font.render(f"Dire Wolf attacks for {attack}, and does {total_a_d} damage",
                       True, white, black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)


def ghast_claws():
    double_damage = False
    claw_attack = rd.randrange(1, 21)
    if claw_attack == 20:
        double_damage = True
    claw_attack += 5
    claw_damage_total = 3
    for i in range(2):
        claw_damage = rd.randrange(1, 7)
        if double_damage is True:
            claw_damage *= 2
        claw_damage_total += claw_damage
    text = font.render(f"Ghast claws {claw_attack}, for {claw_damage_total} damage.DC10 Con save or paralysed 1 min.",
                       True, white, black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)


def ghast_bite():
    double_damage = False
    bite_attack = rd.randrange(1, 21)
    if bite_attack == 20:
        double_damage = True
    bite_attack += 3
    bite_damage_total = 3
    for i in range(2):
        bite_damage = rd.randrange(1, 9)
        if double_damage is True:
            bite_damage *= 2
        bite_damage_total += bite_damage
    text = font.render(f"Ghast attacks with bite for {bite_attack}, dealing {bite_damage_total} damage.",
                       True, white, black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)


def goblin_melee():
    double_damage = False
    attack = rd.randrange(1, 21)
    if attack == 20:
        double_damage = True
    attack += 4
    damage = rd.randrange(1, 7)
    if double_damage is True:
        damage *= 2
    damage += 2
    text = font.render(f"Goblin attacks with scimitar for {attack}, dealing {damage} damage.",
                       True, white, black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)


def goblin_ranged():
    double_damage = False
    attack = rd.randrange(1, 21)
    if attack == 20:
        double_damage = True
    attack += 4
    damage = rd.randrange(1, 7)
    if double_damage is True:
        damage *= 2
    damage += 2
    text = font.render(f"Goblin attacks with short bow for {attack}, dealing {damage} damage.",
                       True, white, black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)

def guard_melee():
    double_damage = False
    attack = rd.randrange(1, 21)
    if attack == 20:
        double_damage = True
    attack += 3
    damage = rd.randrange(1, 9)
    if double_damage is True:
        damage *= 2
    damage += 1
    text = font.render(f"Guard attacks with spear for {attack}, dealing {damage} damage.",
                       True, white, black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)


def knight_melee():
    double_damage = False
    attack = rd.randrange(1, 21)
    if attack == 20:
        double_damage = True
    attack += 5
    total_d_first = 3
    for i in range(2):
        damage = rd.randrange(1, 7)
        if double_damage is True:
            damage *= 2
        total_d_first += damage
    double_damage = False
    total_d_second = 3
    second_attack = rd.randrange(1, 21)
    if second_attack == 20:
        double_damage = True
    second_attack += 5
    for i in range(2):
        second_damage = rd.randrange(1, 7)
        if double_damage is True:
            second_damage *= 2
        total_d_second += second_damage
    text = font.render(f"Knight attacks twice, 1st {attack}, for {total_d_first}. 2nd {second_attack}, for {total_d_second}.", True, white,
                       black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)


def knight_ranged():
    double_damage = False
    attack = rd.randrange(1, 21)
    if attack == 20:
        double_damage = True
    attack += 2
    damage = rd.randrange(1, 11)
    if double_damage is True:
        damage *= 2
    text = font.render(f"Knight attacks with heavy crossbow for {attack}, dealing {damage} damage.", True, white,
                       black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)


def orc_melee():
    double_damage = False
    attack = rd.randrange(1, 21)
    if attack == 20:
        double_damage = True
    attack += 5
    damage = rd.randrange(1, 13)
    if double_damage is True:
        damage *= 2
    damage += 3
    text = font.render(f"Orc attacks with great axe for {attack}, dealing {damage} damage.", True, white,
                       black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)


def orc_ranged():
    double_damage = False
    attack = rd.randrange(1, 21)
    if attack == 20:
        double_damage = True
    attack += 5
    damage = rd.randrange(1, 7)
    if double_damage is True:
        damage *= 2
    damage += 3
    text = font.render(f"Orc attacks with javelin for {attack}, dealing {damage} damage.", True, white,
                       black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)


def sahuagin_bite():
    double_damage = False
    bite_attack = rd.randrange(1, 21)
    if bite_attack == 20:
        double_damage = True
    bite_attack += 3
    bite_damage = rd.randrange(1, 5)
    if double_damage is True:
        bite_damage *= 2
    bite_damage += 1
    text = font.render(f"Sahuagin bites for {bite_attack}, for {bite_damage}. It can do one more attack.", True, white,
                       black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)


def sahuagin_claws():
    double_damage = False
    claw_attack = rd.randrange(1, 21)
    if claw_attack == 20:
        double_damage = True
    claw_attack += 3
    claw_damage = rd.randrange(1, 5)
    if double_damage is True:
        claw_damage *= 2
    claw_damage += 1
    text = font.render(f"Sahuagin's 2nd attack with claws for {claw_attack}, dealing {claw_damage}.",
                       True, white, black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)


def sahuagin_one_hand_spear():
    double_damage = False
    one_hand_spear_attack = rd.randrange(1, 21)
    if one_hand_spear_attack == 20:
        double_damage = True
    one_hand_spear_attack += 3
    one_hand_spear_damage = rd.randrange(1, 7)
    if double_damage is True:
        one_hand_spear_damage *= 2
    one_hand_spear_damage += 1
    text = font.render(f"Sahuagin's 2nd attack with single hand spear for {one_hand_spear_attack}, dealing {one_hand_spear_damage}.",
        True, white, black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)


def sahuagin_two_hand_spear():
    double_damage = False
    two_hand_spear_attack = rd.randrange(1, 21)
    if two_hand_spear_attack == 20:
        double_damage = True
    two_hand_spear_attack += 3
    two_hand_spear_damage = rd.randrange(1, 9)
    if double_damage is True:
        two_hand_spear_damage *= 2
    two_hand_spear_damage += 1
    text = font.render(
        f"Sahuagin's 2nd attack with two hand spear for {two_hand_spear_attack}, dealing {two_hand_spear_damage}.",
        True, white, black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)


def skeleton_melee():
    double_damage = False
    attack = rd.randrange(1, 21)
    if attack == 20:
        double_damage = True
    attack += 4
    damage = rd.randrange(1, 7)
    if double_damage is True:
        damage *= 2
    damage += 2
    text = font.render(f"Skeleton attacks with short sword for {attack}, dealing {damage} damage.",
                       True, white, black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)


def skeleton_ranged():
    double_damage = False
    attack = rd.randrange(1, 21)
    if attack == 20:
        double_damage = True
    attack += 5
    damage = rd.randrange(1, 7)
    if double_damage is True:
        damage *= 2
    damage += 2
    text = font.render(f"Skeleton attacks with short bow for {attack}, dealing {damage} damage.",
                       True, white, black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)


def spider_melee():
    double_damage = False
    attack = rd.randrange(1, 21)
    if attack == 20:
        double_damage = True
    attack += 4
    poison_damage = rd.randrange(1, 5)
    damage = 0
    if double_damage is True:
        damage += 1
    damage += 1
    text = font.render(f"Spider bites for {attack}, for {damage} damage. DC9 Con save: {poison_damage} poison damage.",
                       True, white, black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)


def snake_melee():
    double_damage = False
    attack = rd.randrange(1, 21)
    damage = 0
    total_damage = 0
    if attack == 20:
        double_damage = True
    attack += 4
    if double_damage is True:
        damage += 1
    damage += 1
    for i in range(2):
        poison_damage = rd.randrange(1, 5)
        total_damage += poison_damage
    text = font.render(f"Snake attacks with bite for {attack}, dealing {damage} damage,and if fails DC10 Con save, does {total_damage} poison damage.",
                       True, white, black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)


def zombie():
    double_damage = False
    attack = rd.randrange(1, 21)
    if attack == 20:
        double_damage = True
    attack += 3
    damage = rd.randrange(1, 7)
    if double_damage is True:
        damage *= 2
    damage += 1
    text = font.render(f"Zombie attacks with slam for {attack}, dealing {damage} damage.",
                       True, white, black)
    textRect = text.get_rect()
    textRect.center = (250, 930)
    screen.blit(text, textRect)

def draw_buttons():
    AT_button.draw(screen)
    BM_button.draw(screen)
    BR_button.draw(screen)
    BA_button.draw(screen)
    DMC_button.draw(screen)
    DWM_button.draw(screen)
    GUM_button.draw(screen)
    GHB_button.draw(screen)
    GHC_button.draw(screen)
    GM_button.draw(screen)
    GR_button.draw(screen)
    KM_button.draw(screen)
    KR_button.draw(screen)
    OR_button.draw(screen)
    OM_button.draw(screen)
    OB_button.draw(screen)
    SB_button.draw(screen)
    SC_button.draw(screen)
    SohS_button.draw(screen)
    SthS_button.draw(screen)
    SM_button.draw(screen)
    SR_button.draw(screen)
    SPM_button.draw(screen)
    SNM_button.draw(screen)
    ZM_button.draw(screen)


# game loop
run = True
while run:

    # display BG
    screen.blit(BG, (0, 0))

    if AT_button.draw(screen):
        AT_rolled = True
        arrow_trap()
        random_sound = rd.choice(ranged_sound_effects)
        pygame.mixer.Sound(random_sound).play()
        draw_buttons()
        pygame.display.update()
        while AT_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    AT_rolled = False
                if event.type == pygame.QUIT:
                    pygame.quit()

    if DMC_button.draw(screen):
        DMC_rolled = True
        dark_mantle_crush()
        crush_sound_effect.play()
        draw_buttons()
        pygame.display.update()
        while DMC_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    DMC_rolled = False
                if event.type == pygame.QUIT:
                    pygame.quit()

    if GHB_button.draw(screen):
        GHB_rolled = True
        ghast_bite()
        bite_sound_effect.play()
        draw_buttons()
        pygame.display.update()
        while GHB_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    GHB_rolled = False
                if event.type == pygame.QUIT:
                    pygame.quit()

    if GHC_button.draw(screen):
        GHC_rolled = True
        ghast_claws()
        claw_sound_effect.play()
        draw_buttons()
        pygame.display.update()
        while GHC_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    GHC_rolled = False
                if event.type == pygame.QUIT:
                    pygame.quit()

    if GUM_button.draw(screen):
        GUM_rolled = True
        guard_melee()
        random_sound = rd.choice(melee_sound_effects)
        pygame.mixer.Sound(random_sound).play()
        draw_buttons()
        pygame.display.update()
        while GUM_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    GUM_rolled = False
                if event.type == pygame.QUIT:
                    pygame.quit()

    if SPM_button.draw(screen):
        SPM_rolled = True
        spider_melee()
        bite_sound_effect.play()
        draw_buttons()
        pygame.display.update()
        while SPM_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    SPM_rolled = False
                if event.type == pygame.QUIT:
                    pygame.quit()

    if SNM_button.draw(screen):
        SNM_rolled = True
        snake_melee()
        bite_sound_effect.play()
        draw_buttons()
        pygame.display.update()
        while SNM_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    SNM_rolled = False
                if event.type == pygame.QUIT:
                    pygame.quit()

    if DWM_button.draw(screen):
        DWM_rolled = True
        dire_wolf_melee()
        bite_sound_effect.play()
        draw_buttons()
        pygame.display.update()
        while DWM_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    DWM_rolled = False
                if event.type == pygame.QUIT:
                    pygame.quit()

    if BM_button.draw(screen):
        BM_rolled = True
        bandit_melee()
        random_sound = rd.choice(melee_sound_effects)
        pygame.mixer.Sound(random_sound).play()
        draw_buttons()
        pygame.display.update()
        while BM_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    BM_rolled = False
                if event.type == pygame.QUIT:
                    pygame.quit()

    if BA_button.draw(screen):
        BA_rolled = True
        basilisk()
        bite_sound_effect.play()
        draw_buttons()
        pygame.display.update()
        while BA_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    BA_rolled = False
                if event.type == pygame.QUIT:
                    pygame.quit()

    if OB_button.draw(screen):
        OB_rolled = True
        owlbear()
        random_sound = rd.choice(melee_sound_effects)
        pygame.mixer.Sound(random_sound).play()
        draw_buttons()
        pygame.display.update()
        while OB_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    OB_rolled = False
                if event.type == pygame.QUIT:
                    pygame.quit()

    if BR_button.draw(screen):
        BR_rolled = True
        bandit_ranged()
        random_sound = rd.choice(ranged_sound_effects)
        pygame.mixer.Sound(random_sound).play()
        draw_buttons()
        pygame.display.update()
        while BR_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    BR_rolled = False
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

    if GM_button.draw(screen):
        GM_rolled = True
        goblin_melee()
        random_sound = rd.choice(melee_sound_effects)
        pygame.mixer.Sound(random_sound).play()
        draw_buttons()
        pygame.display.update()
        while GM_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    GM_rolled = False
                if event.type == pygame.QUIT:
                    pygame.quit()

    if GR_button.draw(screen):
        GR_rolled = True
        goblin_ranged()
        random_sound = rd.choice(ranged_sound_effects)
        pygame.mixer.Sound(random_sound).play()
        draw_buttons()
        pygame.display.update()
        while GR_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    GR_rolled = False
                if event.type == pygame.QUIT:
                    pygame.quit()


    if KM_button.draw(screen):
        KM_rolled = True
        knight_melee()
        random_sound = rd.choice(melee_sound_effects)
        pygame.mixer.Sound(random_sound).play()
        draw_buttons()
        pygame.display.update()
        while KM_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    KM_rolled = False
                if event.type == pygame.QUIT:
                    pygame.quit()

    if KR_button.draw(screen):
        KR_rolled = True
        knight_ranged()
        random_sound = rd.choice(ranged_sound_effects)
        pygame.mixer.Sound(random_sound).play()
        draw_buttons()
        pygame.display.update()
        while KR_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    KR_rolled = False
                if event.type == pygame.QUIT:
                    pygame.quit()

    if OM_button.draw(screen):
        OM_rolled = True
        orc_melee()
        random_sound = rd.choice(melee_sound_effects)
        pygame.mixer.Sound(random_sound).play()
        draw_buttons()
        pygame.display.update()
        while OM_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    OM_rolled = False
                if event.type == pygame.QUIT:
                    pygame.quit()

    if OR_button.draw(screen):
        OR_rolled = True
        orc_ranged()
        random_sound = rd.choice(ranged_sound_effects)
        pygame.mixer.Sound(random_sound).play()
        draw_buttons()
        pygame.display.update()
        while OR_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    OR_rolled = False
                if event.type == pygame.QUIT:
                    pygame.quit()

    if SB_button.draw(screen):
        SB_rolled = True
        sahuagin_bite()
        bite_sound_effect.play()
        draw_buttons()
        pygame.display.update()
        while SB_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    SB_rolled = False
                if event.type == pygame.QUIT:
                    pygame.quit()

    if SC_button.draw(screen):
        SC_rolled = True
        sahuagin_claws()
        claw_sound_effect.play()
        draw_buttons()
        pygame.display.update()
        while SC_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    SC_rolled = False
                if event.type == pygame.QUIT:
                    pygame.quit()

    if SohS_button.draw(screen):
        SohS_rolled = True
        sahuagin_one_hand_spear()
        random_sound = rd.choice(melee_sound_effects)
        pygame.mixer.Sound(random_sound).play()
        draw_buttons()
        pygame.display.update()
        while SohS_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    SohS_rolled = False
                if event.type == pygame.QUIT:
                    pygame.quit()

    if SthS_button.draw(screen):
        SthS_rolled = True
        sahuagin_two_hand_spear()
        random_sound = rd.choice(melee_sound_effects)
        pygame.mixer.Sound(random_sound).play()
        draw_buttons()
        pygame.display.update()
        while SthS_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    SthS_rolled = False
                if event.type == pygame.QUIT:
                    pygame.quit()

    if SM_button.draw(screen):
        SM_rolled = True
        skeleton_melee()
        random_sound = rd.choice(melee_sound_effects)
        pygame.mixer.Sound(random_sound).play()
        draw_buttons()
        pygame.display.update()
        while SM_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    SM_rolled = False
                if event.type == pygame.QUIT:
                    pygame.quit()

    if ZM_button.draw(screen):
        ZM_rolled = True
        zombie()
        random_sound = rd.choice(melee_sound_effects)
        pygame.mixer.Sound(random_sound).play()
        draw_buttons()
        pygame.display.update()
        while ZM_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ZM_rolled = False
                if event.type == pygame.QUIT:
                    pygame.quit()

    if SR_button.draw(screen):
        SR_rolled = True
        skeleton_ranged()
        random_sound = rd.choice(ranged_sound_effects)
        pygame.mixer.Sound(random_sound).play()
        draw_buttons()
        pygame.display.update()
        while SR_rolled:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    SR_rolled = False
                if event.type == pygame.QUIT:
                    pygame.quit()



    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
