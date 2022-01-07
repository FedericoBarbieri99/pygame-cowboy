import sys
from player import *
from bullet import *
from enemy import *

pygame.init()

background = pygame.image.load("assets/background.png")
screen_size = background.get_rect().size
screen = pygame.display.set_mode(screen_size, vsync=1)
background = background.convert()
font = pygame.font.Font(None, 60)


enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
player = Player(screen)
player_group.add(player)

clock = pygame.time.Clock()
gameover = False


def update_screen():

    screen.blit(background, [0, 0])
    player_group.update()
    enemy_group.update()
    bullet_group.update()
    pygame.sprite.groupcollide(enemy_group, bullet_group, True, True)
    if pygame.sprite.spritecollideany(player, enemy_group):
        enemy_group.empty()
        bullet_group.empty()
        player.kill()
        return True
    print('b')
    player_group.draw(screen)
    enemy_group.draw(screen)
    bullet_group.draw(screen)

    pygame.display.flip()
    return False


def event_handler(gameover):
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.orientation = 'Left'
            if event.key == pygame.K_RIGHT:
                player.orientation = 'Right'
            if event.key == pygame.K_SPACE and not gameover:
                bullet_group.add(Bullet(screen, player))
                enemy_group.add(Enemy(screen))
            if event.key == pygame.K_r and gameover:
                return False

        if event.type == pygame.QUIT:
            sys.exit()


def new_game():
    screen.fill((0, 0, 0))
    respawn_text = font.render("Press R to Respawn", False, (255, 255, 255))
    rect = respawn_text.get_rect()
    rect.center = screen.get_rect().center
    screen.blit(respawn_text, rect)


def main():

    while True:

        clock.tick(60)
        global gameover
        if not gameover:
            event_handler(gameover)
            gameover = update_screen()
        else:
            new_game()
            gameover = event_handler(gameover)



main()
