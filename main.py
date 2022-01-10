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
start_ticks = 0
SPAWNENEMY = pygame.USEREVENT + 1
clock = pygame.time.Clock()
pygame.time.set_timer(SPAWNENEMY, 500)
score = 0


def update_entities():
    global score
    player_group.update()
    enemy_group.update()
    bullet_group.update()
    score += len(pygame.sprite.groupcollide(enemy_group, bullet_group, True, True))
    if pygame.sprite.spritecollideany(player, enemy_group):
        enemy_group.empty()
        bullet_group.empty()
        player.alive = False
        player.kill()


def draw_screen():
    global score
    screen.blit(background, [0, 0])
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, score_text.get_rect())
    player_group.draw(screen)
    enemy_group.draw(screen)
    bullet_group.draw(screen)
    pygame.display.flip()


def event_handler():
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.orientation = 'Left'
            if event.key == pygame.K_RIGHT:
                player.orientation = 'Right'
            if event.key == pygame.K_SPACE and player.alive:
                bullet_group.add(Bullet(screen, player))
            if event.key == pygame.K_r and not player.alive:
                main()

        if event.type == SPAWNENEMY:
            spawn_enemy()

        if event.type == pygame.QUIT:
            sys.exit()


def new_game():
    global score
    player.die()
    score_text = font.render(f"Last score: {score}", True, (255, 255, 255))
    respawn_text = font.render("Press R to Respawn", True, (255, 255, 255))
    respawn_rect = respawn_text.get_rect()
    respawn_rect.centerx = screen.get_rect().centerx
    respawn_rect.centery = screen.get_rect().centery - (screen.get_rect().centery / 6)
    score_rect = score_text.get_rect()
    score_rect.centerx = screen.get_rect().centerx
    score_rect.centery = screen.get_rect().centery + (screen.get_rect().centery / 6)
    screen.blit(respawn_text, respawn_rect)
    screen.blit(score_text, score_rect)
    pygame.display.flip()


def reset():
    global score, start_ticks
    player.__init__(screen)
    enemy_group.empty()
    bullet_group.empty()
    player.alive = True
    player_group.add(player)
    score = 0
    start_ticks = pygame.time.get_ticks()


def spawn_enemy():
    speed = random.uniform(0.1, (pygame.time.get_ticks() - start_ticks) / 1000)
    enemy_group.add(Enemy(screen, speed))


def main():
    pass
    reset()
    while True:
        clock.tick(60)
        event_handler()
        update_entities()
        if player.alive:
            draw_screen()
        else:
            new_game()


main()
